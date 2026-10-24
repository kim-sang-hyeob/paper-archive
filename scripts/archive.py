#!/usr/bin/env python3
"""Render and search a paper archive using only the Python standard library."""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


def load_catalog():
    data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    ids = set()
    topics = {t["id"] for t in data["topics"]}
    for record in data["records"]:
        paper_id = record["arxiv_id"]
        if not re.fullmatch(r"\d{4}\.\d{4,5}", paper_id) or paper_id in ids:
            raise ValueError(f"Invalid or duplicate arXiv ID: {paper_id}")
        ids.add(paper_id)
        if record["reading_status"] not in data["status_options"]:
            raise ValueError(f"Invalid reading status: {paper_id}")
        if record["primary_topic"] not in record["topics"]:
            raise ValueError(f"Primary topic missing from topics: {paper_id}")
        if set(record["topics"]) - topics:
            raise ValueError(f"Unknown topic: {paper_id}")
        for source in record["sources"]:
            if not source.startswith("https://"):
                raise ValueError(f"Invalid source URL: {paper_id}")
    return data


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def paper_table(records, topic_names, prefix=""):
    lines = [
        "| 상태 | 논문 | 유형 | 주분류 | 기억할 단서 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        paper_id = record["arxiv_id"]
        title = record["title"]
        if record.get("method_name"):
            title += f" ({record['method_name']})"
        link = f"[{cell(title)}]({prefix}papers/{paper_id}.md)"
        lines.append("| " + " | ".join([
            cell(record["reading_status"]), link, cell(record["paper_type"]),
            cell(topic_names[record["primary_topic"]]), cell(record["retrieval_hint"]),
        ]) + " |")
    return "\n".join(lines)


def documents(data):
    records = data["records"]
    topic_names = {t["id"]: t["name"] for t in data["topics"]}
    unread = sum(r["reading_status"] == "미독" for r in records)
    lines = [
        "# 논문 보관함", "",
        "나중에 제목이 기억나지 않아도 내용과 키워드로 다시 찾기 위한 개인 논문 목록입니다.", "",
        f"현재 {len(records)}편, 미독 {unread}편. 최근 수정일 {data['updated_on']}.", "",
        "## 전체 목록", "", paper_table(records, topic_names), "",
        "초록과 공식 프로젝트 페이지를 바탕으로 초벌 분류했습니다. 읽기 상태는 사용자의 상태입니다.", "",
        "## 주제별 보기", "",
        "한 논문이 여러 주제에 속할 수 있습니다. 서베이와 방법론은 유형으로, 미독과 완독은 읽기 상태로 따로 관리합니다.", "",
    ]
    for topic in data["topics"]:
        count = sum(topic["id"] in r["topics"] for r in records)
        lines.append(f"- [{topic['name']}](topics/{topic['id']}.md): {count}편. {topic['description']}.")
    lines += [
        "", "## 내용으로 다시 찾기", "",
        "이 프로젝트의 채팅에서는 ‘보관한 논문 중 마인크래프트에서 영상으로 행동을 배우는 거 찾아줘’처럼 말하면 됩니다. 다른 채팅에서는 이 저장소 링크를 함께 주고 검색을 요청하세요. 비공개 저장소를 읽을 수 있는 GitHub 연결이나 로컬 파일 접근이 필요합니다.", "",
        "로컬에서 키워드로 찾으려면:", "", "```bash",
        'python3 scripts/archive.py search "마인크래프트 행동"',
        'python3 scripts/archive.py search "월드모델 서베이"', "```", "",
        "## 기록과 수정", "",
        "`catalog.json`에 제목, 저자, 원문 링크, 한글 요약, 분류, 검색 키워드, 읽기 상태, 사용자 메모를 저장합니다. 새 논문을 등록할 때 arXiv ID가 같은 항목은 중복 생성하지 않고 갱신합니다. 원문은 arXiv 및 PDF 링크로 보관합니다.", "",
        "분류표와 논문별 메모는 아래 명령으로 갱신합니다:", "", "```bash",
        "python3 scripts/archive.py build", "python3 scripts/archive.py check", "```", "",
        f"[엑셀 내려받기]({data['workbook']})는 {data['workbook_snapshot_on']}에 만든 초기 스냅샷입니다. 최신 목록은 이 페이지와 `catalog.json`에서 확인합니다.", "",
    ]
    result = {Path("README.md"): "\n".join(lines)}

    for topic in data["topics"]:
        members = [r for r in records if topic["id"] in r["topics"]]
        result[Path("topics") / f"{topic['id']}.md"] = "\n".join([
            f"# {topic['name']}", "", topic["description"] + ".", "",
            "[전체 목록](../README.md)", "", paper_table(members, topic_names, "../"), "",
        ])

    for record in records:
        paper_id = record["arxiv_id"]
        info = [
            f"# {record['title']}", "", "[전체 목록](../README.md)", "",
            f"- 읽기 상태: {record['reading_status']}",
            f"- 유형: {record['paper_type']}",
            f"- 주분류: {topic_names[record['primary_topic']]}",
            "- 관련 주제: " + ", ".join(topic_names[t] for t in record["topics"]),
            f"- 저자: {', '.join(record['authors'])}",
            f"- 최초 제출일: {record['submitted_on']}",
            f"- 보관일: {record['added_on']}",
            f"- 확인한 버전: {paper_id}{record['version_checked']}",
            f"- [arXiv 원문]({record['arxiv_url']})",
            f"- [PDF]({record['pdf_url']})",
        ]
        if record.get("project_url"):
            info.append(f"- [공식 프로젝트]({record['project_url']})")
        if record["original_url"] != record["arxiv_url"]:
            info.append(f"- [처음 보낸 링크]({record['original_url']})")
        info += [
            "", "## 대략 어떤 논문인가", "", record["summary_ko"], "",
            "## 다시 찾을 단서", "", record["retrieval_hint"], "",
            ", ".join(record["retrieval_keywords"]), "",
            "## 사용자 메모", "", record["user_note"] or "아직 메모 없음.", "",
            "## 분류 근거", "", data["classification_basis"], "",
            f"확인일: {record['source_checked_on']}.", "",
        ]
        info += [f"- [출처 {i}]({url})" for i, url in enumerate(record["sources"], 1)]
        info.append("")
        result[Path("papers") / f"{paper_id}.md"] = "\n".join(info)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("build")
    sub.add_parser("check")
    search = sub.add_parser("search")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()
    data = load_catalog()
    if args.command == "search":
        terms = re.findall(r"[\w]+", args.query.casefold())
        ranked = []
        for record in data["records"]:
            text = " ".join([
                record["title"], record.get("method_name", ""), record["summary_ko"],
                record["retrieval_hint"], " ".join(record["retrieval_keywords"]),
            ]).casefold()
            score = sum(term in text for term in terms)
            if score:
                ranked.append((score, record))
        ranked.sort(key=lambda row: -row[0])
        for _, record in ranked[:args.limit]:
            print(f"{record['arxiv_id']}  {record['title']}  [{record['reading_status']}]")
            print(record["retrieval_hint"])
            print(record["arxiv_url"] + "\n")
        if not ranked:
            print("일치하는 키워드가 없습니다. 다른 단어나 catalog.json 전체 내용으로 찾아보세요.")
        return
    generated = documents(data)
    if args.command == "build":
        for relative, content in generated.items():
            target = ROOT / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        print(f"Built {len(generated)} pages from {len(data['records'])} records.")
        return
    stale = [str(p) for p, content in generated.items()
             if not (ROOT / p).exists() or (ROOT / p).read_text(encoding="utf-8") != content]
    if stale:
        print("Out-of-date pages: " + ", ".join(stale), file=sys.stderr)
        sys.exit(1)
    print(f"OK: {len(data['records'])} unique papers, {len(data['topics'])} topics, {len(generated)} pages in sync.")


if __name__ == "__main__":
    main()
