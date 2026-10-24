# Paper archive

- This repository is the user's durable paper archive. For vague recall requests, read `catalog.json` and match the topic, Korean and English keywords, summary, and retrieval hint. Do not rely on a paper title alone.
- `catalog.json` is the source of truth. Preserve user notes and reading status. Adding an unread paper does not mean the user has read it.
- Classify papers by a broad primary topic and optional additional topics. Keep paper type (survey, method, etc.) and reading status separate from topic.
- Verify new metadata and summaries against the original abstract or official project page. Clearly distinguish preliminary classification from a full reading.
- After changes, run `python3 scripts/archive.py build` and `python3 scripts/archive.py check`. README, topic pages, and paper cards are generated from the catalog.
- `paper_archive.xlsx` is the initial dated snapshot. The README and catalog hold the current archive. Do not silently overwrite user edits in Excel.
- Before editing a remote-backed checkout, inspect git status and fetch remote updates when available. Preserve concurrent user changes. Commit or push only the archive files covered by the user's request. Never force-push.
- Do not claim a remote save until the commit can be read back from GitHub. Do not upload unrelated lab files, credentials, or temporary authoring files.
