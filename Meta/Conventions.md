## Experiments

Should have a target question or hypothesis
Are complete when at least one clear result is produced that permits an answer to the target question or hypothesis
## Claims and Results / Evidence

Claims are `Supported By` Evidence or Results if:
- condition1
- condition2

Otherwise they are `Consistent With` Result / Evidence

## Candidate tagging

Use `#iss-candidate` or `#res-candidate` on any line to flag an observation as a candidate for promotion to a full ISS or RES discourse node.

**Scoping rule:** The `# Candidates` query on Experiment, Issue, and Project pages picks up tagged lines automatically from within those files. When tagging from *outside* the node's own file (e.g. a daily note, a source note, or another experiment), include a wikilink to the target node on the same line so the query can find it:

```
- noticed Y behaves oddly at low temps #iss-candidate [[EXP - My Experiment]]
- this finding strongly supports X #res-candidate [[PRJ - My Project]]
```

This wikilink can ride along on an existing `#🧪ExperimentLog::` line — no extra syntax needed:

```
- #🧪ExperimentLog:: [[EXP - My Experiment]] result looks publishable #res-candidate
```

**Project page scope:** The project candidates view automatically includes all files where `project:` frontmatter names the project, so experiment and issue notes don't need an explicit project link.

## Tasks

We use the tasks plugin to manage tasks