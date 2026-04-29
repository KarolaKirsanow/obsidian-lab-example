# Design decisions

Append-only log. Newest entries at the bottom.
See CLAUDE.md for format and conventions.

---

## 2026-04-13 — Convert Dataview syntax to Datacore in Daily Note Template

**[[QUE - Should the daily note template use datacore or dataview syntax?]]**

**[[CLM - Datacore should replace dataview syntax while preserving all functionality. The Tasks blocks stay unchanged; only the two dataview blocks at the bottom (Notes created today and Notes modified today) need replacement with datacore equivalents.]]**

**[[RES - Rewrote Daily_note_template.md to use datacore syntax instead of dataview. The template now uses datacore JSX query blocks for fetching notes created and modified on today's date, while maintaining compatibility with Templater and Tasks plugins.]]**

---

## 2026-04-13 — Link-based routing for experiment log entries to specific EXP notes

**[[QUE - How can entries written in the daily note's experiment log be automatically routed to the correct Experiment note's # Log section?]]**

**[[CLM - Use a wikilink from the daily note log entry to the target EXP note as the routing key. The daily log entry format should be: `- #🧪ExperimentLog:: [[EXP - protocol with cell line xyz]] - your note here`. A Datacore query in the EXP note's # Log section can then filter for entries that link to that specific file.]]**

**[[RES - Implemented link-aware Datacore query in EXP note templates to dynamically display log entries from daily notes that reference the specific experiment. The daily note's inline tagging system (`#🧪ExperimentLog::`) now feeds into both the aggregate 00 Experiment Log view and individual EXP note logs.]]**

---

## 2026-04-14 — Interleaving dynamic queries with manual text in logs

**[[QUE - How can entries from daily notes (dynamic) and direct manual entries be kept together by date in the # Log section?]]**

**[[CLM - Two options exist: Option A uses parallel sections with manual entries organized under date headings (## YYYY-MM-DD) separate from the Datacore query section; Option B makes the daily note the single source of truth for all entries, eliminating manual duplication.]]**

**[[RES - Chose Option A. Restructured the # Log section in EXP templates and notes to have separate subsections: "From daily notes" (Datacore query) and "Direct entries" (manual date-organized sections). This provides ergonomic flexibility for users already in an EXP note while maintaining date organization.]]**

---

## 2026-04-14 — Tasks plugin filtering for hashtag-prefixed entries

**[[QUE - How can the Tasks plugin queries be filtered to show only entries that start with a hashtag (#)?]]**

**[[CLM - Add the filter `description regex matches /^#/` to all tasks query blocks. This regex ensures only tasks whose text begins with # are displayed, excluding placeholder tasks like `- [ ] task 📅`.]]**

**[[RES - Updated all tasks query blocks in Daily_note_template.md and existing daily notes with the regex filter. This allows users to write placeholder tasks without them appearing in filtered query results, while tagged tasks (`- [ ] #call lab 📅`) are properly captured.]]**

---

## 2026-04-14 — Template path migration to Meta/Templates folder

**[[QUE - Will moving templates to a new Meta/Templates folder break plugin references?]]**

**[[CLM - Yes, hardcoded paths in two plugins will break. The Daily Notes plugin and Templater plugin both reference the old Templates folder location. The core Templates plugin (templates.json) handles this correctly via file references.]]**

**[[RES - Updated .obsidian/daily-notes.json to point to `Meta/Templates/Daily_note_template`. Updated .obsidian/plugins/templater-obsidian/data.json to reference `Meta/Templates/` folder. Verified discourse-graphs plugin does not use hardcoded paths (safe to move).]]**

---

## 2026-04-14 — Query for Results and Conclusions in Project notes

**[[QUE - How can Project notes automatically collect RES (Result) and CON (Conclusion) discourse graph nodes that are related to them?]]**

**[[CLM - Create a Datacore-based `.base` view that queries for nodes with specific `nodeTypeId` values (RES: `node_i7PzyKw2NfkA8asBfxeey`, CON: `node_J9JyrRTQj6nuJs6IY83Mo`) that have backlinks to the project note via the convention `[[PRJ - Project name]]`.]]**

**[[RES - Created Results.base as an embedded query in Project.md template. The query filters discourse graph nodes by nodeTypeId and checks for file links back to the current project file. This automatically populates without duplicating RES/CON content in the project note itself.]]**

---

## 2026-04-14 — Convention for linking Results and Conclusions to Projects

**[[QUE - Should RES and CON nodes link to projects via backlinks or forward links, and what's the ergonomic convention?]]**

**[[CLM - RES and CON notes should contain `[[PRJ - project name]]` wikilinks in their body. The query in the project note uses `file.hasLink(this.file.name)` to find these references. This is more ergonomic because it allows RES/CON notes to reference multiple related projects without cluttering the project note itself.]]**

**[[RES - Established the convention: any RES or CON note that mentions a project via wikilink will automatically appear in that project's Results & Conclusions section when the query-based base is embedded.]]**

---

## 2026-04-20 — NodeTypeIds are vault-scoped and inherited by downloaders

**[[QUE - Are the Discourse Graph NodeTypeIds unique to this vault or globally shared? Will downloaders inherit these IDs?]]**

**[[CLM - NodeTypeIds are vault-scoped (stored in .obsidian/plugins/discourse-graphs/data.json) and are NOT globally registered. They are random nanoid-style strings generated locally when node types are created. Downloaders WILL inherit these exact IDs when they clone the vault, which is desirable for schema consistency.]]**

**[[RES - Confirmed NodeTypeIds are vault-portable and intentionally inherited. New node types added by downloaders will generate fresh random IDs without collision risk. The vault's discourse graph schema is fully distributed with vault downloads.]]**

---

## 2026-04-20 — Create Discourse Canvas for Projects via button

**[[QUE - Is there a way to automatically create and open a Discourse Canvas for each Project, and can it be added to the template?]]**

**[[CLM - Use a Datacore JSX button in the Project template. The button checks if `Discourse Canvas/<ProjectName>.canvas` exists; if not, it creates an empty canvas file and opens it; if yes, it just opens it (idempotent). No additional plugins needed since Datacore is already installed.]]**

**[[RES - Added a Datacore JSX button to Project.md template that creates and manages project-specific Discourse Canvases. The button is idempotent and automatically creates the Discourse Canvas folder if it doesn't exist. Existing project notes require manual paste of the button block since they won't inherit template changes.]]**

---

## 2026-04-21 — Entry point for Discourse Graph example vault

**[[HYP - The vault should have a guided onboarding flow analogous to Obsidian's sandbox vault, starting from a "Start Here" page that links into a "Discourse Graph Sandbox" folder.]]**

**[[CLM - Adding an entry to the Discourse Graph plugin menu or Help sidebar requires plugin code changes. Without touching plugin code, the two available hooks are: workspace.json (controls which file opens on vault launch) and bookmarks.json (pins a note in the Bookmarks panel, already visible in the left sidebar).]]**

**[[RES - Start Here.md placed at vault root, set as the active leaf in workspace.json (preview mode), and pinned in bookmarks.json. The Sandbox folder will be renamed to "Discourse Graph Sandbox" and contain the branching flow content linked from Start Here.md.]]**

---

## 2026-04-22 — Filename sanitization and alias strategy for discourse nodes

**[[HYP - Adding frontmatter properties for "full title" and "short title" will allow node content to be stored without illegal character and path length issues.]]**

**[[CLM - Obsidian prevents illegal filenames with an error rather than sanitizing; Templater fires post-creation and can rename for length but cannot rescue a failed Windows file creation.]]**
**[[CLM - File Regex Templates in Templater allow per-node-type template routing from a flat folder, which folder templates cannot do.]]**
**[[EVD - All discourse nodes land in DiscourseGraph/ with a type prefix (RES, CLM, QUE, etc.), making prefix-based regex matching reliable.]]**

**[[RES - Illegal chars are a user-convention concern (don't use ? : * etc. in node titles); length truncation is handled by a Templater block in each node template. The full pre-truncation title is written to aliases for autocomplete. Templater file regex templates route each node type prefix to the correct template file; a catch-all template covers types without custom body structure.]]**

**[[CLM - DG uses vault.create(fullPath) directly, bypassing Obsidian's default new note location entirely; core Templates is only used to resolve the template folder path.]]**
**[[CLM - Intermittent duplicate at vault root is caused by tp.file.rename() emitting a create event that races with DG's concurrent vault.append, not by Obsidian's default note location.]]**
**[[EVD - Duplicate only appeared when filename exceeded 60 chars, confirming the rename code path as the trigger.]]**

**[[RES - Removed tp.file.rename() from all node templates. Aliases alone solve the autocomplete problem; filename length is addressed by user convention rather than automation.]]**

**[[RES - Switched to a Datacore button in each node template for alias writing and filename truncation. Button is user-triggered (no creation race), self-hiding once aliases are populated, uses app.fileManager.processFrontMatter and app.fileManager.renameFile. Templater file regex templates disabled; DG plugin continues applying body structure via core Templates.]]**

---

## 2026-04-23 — RES nodes link to SRC via frontmatter

**[[QUE - Should RES nodes reference their supporting SRC (EXP or @ publication) in frontmatter or in the note body?]]**

**[[CLM - Frontmatter is preferable: it is queryable in Bases/Datacore, consistent with how EXP nodes store structured relationships (targetQuestionOrHyp, rel_* keys), and keeps the epistemic link machine-readable.]]**
**[[EVD - EXP nodes already use named frontmatter fields for their structured links to RES and QUE nodes; body wikilinks are reserved for prose annotation.]]**

**[[CLM - The field should be named supported_by rather than source, because "source" is ambiguous (data provenance vs. citation), while supported_by expresses the epistemic relationship explicitly.]]**

**[[RES - Added supported_by: list field to RES node template frontmatter. Values are wikilinks to EXP or @ nodes. Prose context about those sources continues to live in ## Grounding Context in the note body.]]**

---

## 2026-04-24 — Move aliasing button to bottom of node templates

**[[HYP - The NodeSetup aliasing button at the top of node templates confronts users with a code block immediately on node creation.]]**

**[[CLM - Moving the button to the bottom of each template means the cursor lands on the first content section instead, and the button remains accessible by scrolling down.]]**
**[[EVD - The button is self-hiding once aliases are set, so it adds no lasting clutter at the bottom.]]**

**[[RES - Moved NodeSetup datacorejsx button to the bottom of Result.md, Experiment.md, and the RES instance template. _Discourse Node.md is a bare button snippet with no sections and was left unchanged.]]**

---

## 2026-04-27 — Horizontal 3-column project dashboard via DatacoreJSX

**[[QUE - How best to replicate the Roam project page layout (metadata + canvas link + horizontal 3-column query dashboard) in Obsidian?]]**

**[[CLM - DatacoreJSX flex layout is the right approach for the horizontal columns.]]**
**[[EVD - Base transclusion always stacks vertically; CSS multi-column is fragile across theme updates; DatacoreJSX is already in use for the canvas button so the infrastructure is present.]]**
**[[CLM - The three columns map to existing query logic: EXP nodes filtered by project property, ISS nodes filtered by backlink, RES+CON nodes filtered by backlink (already in Results.base).]]**

**[[RES - Build the dashboard as a single DatacoreJSX block rendering three flex columns (EXP | ISS | RES+CON), each running dc.useQuery() filtered to the current project file.]]**

---

## 2026-04-27 — Test horizontal dashboard on a new page before touching the shared template

**[[HYP - The horizontal dashboard should be prototyped on a dedicated test project page rather than modifying the existing Project.md template directly.]]**

**[[RES - Build and validate the layout on "Horizontal Dashboard Test" first; only promote to Project.md template once the design is confirmed. ISS node schema must be inspected before the JSX query can be written.]]**

---

## 2026-04-27 — Protocol/Git repo/Benchling as properties vs. body text in Project notes

**[[QUE - Is there a benefit to making Protocol, Git repo, and Benchling structured frontmatter properties rather than plain body text? Tradeoffs?]]**

**[[CLM - Properties enable cross-project Bases/Datacore queries (e.g. a table of all projects with their protocol and repo) and URL-typed properties render as clickable links in the Properties panel; body text only supports full-text search, which both approaches share.]]**
**[[CLM - Protocol is the strongest candidate for a property if it uses a wikilink to a Protocol note, since Obsidian then tracks it as a backlink and enables "all projects using this protocol" queries for free.]]**
**[[CLM - Git repo and Benchling are worth making URL-typed properties primarily for the clickable link rendering in the Properties panel; their cross-project query value is low.]]**

**[[RES - Decision deferred to user. Recommendation: make Protocol a wikilink property and Git repo/Benchling URL-typed properties if cross-project rollup views are wanted; leave as body text if these are reference-only fields accessed from within individual project notes.]]**

---

## 2026-04-27 — Todo flow architecture across PRJ / EXP / ISS / daily notes

**[[HYP - There is no need for a todo query on a PRJ page that collects tasks written on that same PRJ page. All PRJ todos should aggregate from related EXP and ISS nodes; daily note todos should flow into whichever EXP/ISS node they tag.]]**

**[[CLM - This gives a clean three-level flow: daily note todo with [[EXP-X]] wikilink → EXP-X todo section; EXP/ISS todos → PRJ aggregated todo section. PRJ pages are display-only for todos, not authoring surfaces.]]**

**[[RES - PRJ todo section: DatacoreJSX aggregator only (no Tasks plugin block). EXP/ISS todo section: Tasks query with OR clause — tasks in the note itself OR tasks in Daily Notes whose description includes the note filename. Template updated in Experiment.md and Issue.md.]]**

---

## 2026-04-27 — Hover Reveal plugin for inline tooltips; ℹ glyph for info buttons

**[[QUE - Is there a way to do hover-over info buttons in Obsidian?]]**

**[[CLM - Hover Reveal plugin (community, by Asrieal, added to registry early 2025) is the best option: syntax [visibleText]{tooltip}, works in both Live Preview and Reading View, no raw HTML in notes.]]**
**[[EVD - Alternatives (abbr tag, CSS span data-tooltip) are reading-view-only and require raw HTML or a CSS snippet to look reasonable.]]**

**[[RES - Use Hover Reveal plugin for inline tooltips with ℹ (U+2139, the standard Unicode information symbol) as the visible trigger glyph: [ℹ]{tooltip text here}.]]**

---

## 2026-04-27 — Meeting-to-project affiliation via frontmatter vs. daily note inline field

**[[HYP - Adding project: frontmatter to meeting notes is the right way to affiliate a meeting with a project.]]**

**[[CLM - Meetings either belong to one project (use project: frontmatter on the meeting note) or to no project (captured by #🤝MeetingLog:: on the daily note alone). The two cases are not in conflict: all meetings flow through the daily note log; only project-affiliated ones additionally carry project: metadata.]]**

**[[RES - Meeting.md template gets a project: frontmatter field. The # Project Meetings section in Project.md gets a Datacore query filtering meeting notes where project == current page name. The global 00 Meeting Log continues to aggregate from daily note MeetingLog:: entries.]]**

---

## 2026-04-27 — Recurring meetings: index note + per-instance notes

**[[QUE - What is the best strategy for recurring meetings — one note with a log, or multiple notes?]]**

**[[CLM - An index note per series plus one note per instance gives the best of both: the index is the stable face of the series (linkable, carries project: frontmatter, holds standing agenda and zoom link); instance notes are individually linkable for citation in RES/EXP nodes.]]**

**[[RES - Two templates: Meeting Series.md (index, has project: frontmatter, Datacore query collecting instances via series: field) and Meeting.md (instance, has series: and date: instead of project:). Project Meetings query on Project.md picks up series index notes only. Global Meeting Log picks up instance notes via daily note MeetingLog:: entries.]]**

---

## 2026-04-27 — ISS-to-EXP upgrade flow: rename not generate

**[[HYP - A "claim issue" button on the Issue template should generate a new EXP note with data carried over from the ISS note.]]**

**[[CLM - The correct user flow is to rename the ISS node as an EXP note directly, rather than generate a new note from it.]]**
**[[CLM - A dedicated upgrade button is premature until multiplayer graphs exist; single-user flow does not need the extra ceremony.]]**

**[[RES - No claim-issue button. To upgrade an ISS to an EXP, the user renames the file (ISS prefix → EXP prefix); all backlinks and log entries follow the rename automatically.]]**

---

## 2026-04-27 — Project Template: Todos, Issues query, and Project Log promoted from test page

**[[HYP - The Todos aggregator, Issues in this Project query, and Project Log with entry button are ready to move from the test page into the shared Project.md template.]]**

**[[CLM - The horizontal dashboard (3-column DatacoreJSX) is not yet promoted — it remains on the test page pending further validation.]]**

**[[RES - Project.md template updated with: (1) # Todos section — a manual entry placeholder followed by the DatacoreJSX aggregator pulling open tasks from related EXP/ISS/RES nodes; (2) # Issues in this Project — Base transclusion via ![[Issues.base#Issues in this Project]]; (3) # Project Log — DatacoreJSX "+ New log entry" button that inserts dated ## headings above the --- separator, followed by the daily-notes aggregator below the separator. Old Tasks plugin block and static ## YYYY-MM-DD placeholder removed.]]

---

## 2026-04-27 — Datacore vs. Dataview: verbosity audit of existing queries

**[[QUE - Which existing Datacore queries could be meaningfully shortened by switching to Dataview DQL?]]**

**[[CLM - Eight query blocks across six templates are straightforward Dataview replacements with no functionality loss: the five "00 Log" aggregate views and the three "from daily notes" inline views (plus two meeting/series list queries).]]**

**[[EVD - The five aggregate log views (00 Project Log, 00 Meeting Log, 00 Media Log, 00 Bullet Journal Log, 00 Experiment Log) each use ~30 lines of DatacoreJSX to produce a two-column table (date | log entry) from Daily Notes pages. The equivalent Dataview DQL is 4 lines: `TABLE ExperimentLog AS "Log" / FROM "Daily Notes" / WHERE ExperimentLog / SORT file.name DESC`. Emoji field names (e.g. 🧪ExperimentLog) require backtick quoting in DQL or can use the ALT name variants already present in each block.]]**

**[[EVD - The three "From daily notes" inline views in Experiment.md, Issue.md, and Project.md each use ~40 lines of DatacoreJSX to filter daily notes whose inline field value contains the current file's name, then render a linked list. The equivalent Dataview DQL is 4 lines: `LIST ExperimentLog / FROM "Daily Notes" / WHERE contains(string(ExperimentLog), this.file.name) / SORT file.name DESC`.]]**

**[[EVD - The ProjectMeetings block in Project.md (~50 lines) lists meeting notes with a project: frontmatter field referencing the current file. Dataview DQL equivalent: `LIST date / FROM "" / WHERE contains(string(project), this.file.name) / SORT date DESC` (4 lines).]]**

**[[EVD - The MeetingInstances block in Meeting Series.md (~40 lines) lists notes with a series: frontmatter field referencing the current file. Same 4-line DQL pattern with `series` field.]]**

**[[CLM - Six other Datacore blocks cannot meaningfully be replaced by Dataview and should remain as DatacoreJSX.]]**

**[[EVD - NodeSetup (alias button), CanvasButton, AddLogEntry button, and NewItemButtons are imperative UI: they write frontmatter, rename files, create vault files, and open editor leaves. Dataview is read-only and has no equivalent capability.]]**

**[[EVD - The ProjectTodos aggregator in Project.md computes a related-path set in two passes (first collecting EXP/ISS nodes by nodeTypeId, then RES/CON nodes by backlink), then filters the task index against that computed set. There is no DQL mechanism for multi-step computed sets or task filtering against a derived path list.]]**

**[[EVD - The Todos view on the Personal Home Page applies custom bucketing (overdue / due today / upcoming / no due date) to tasks filtered by a non-standard `#`-prefix importance marker. Dataview has no bucketed task rendering and cannot filter on task text prefix.]]**

**[[EVD - The DailyLog view on the Personal Home Page joins five distinct inline fields per daily note into a single grouped display, limiting to the most recent 7 entries. Dataview GROUP BY cannot join multiple fields per row in this way without significant complexity.]]**

**[[RES - Decision pending discussion with eng team. Candidates for Dataview replacement: (1) the five 00 Log aggregate views; (2) the three "from daily notes" views in EXP, ISS, and PRJ templates; (3) ProjectMeetings in Project.md; (4) MeetingInstances in Meeting Series.md. All other DatacoreJSX blocks should remain. Net effect if all candidates are switched: ~8 blocks shrink from ~30–50 lines each to ~4 lines each, with identical rendered output.]]**

---

## 2026-04-28 — Template auto-apply for notes created via Bases "New" button

**[[QUE - Why doesn't creating a new note from a Base use the correct template?]]**

**[[CLM - Obsidian Bases has no native support for specifying a template per base; the "New +" button creates a blank note.]]**
**[[EVD - Multiple open feature requests on the Obsidian forum confirm this is unimplemented in core Bases.]]**
**[[CLM - The community plugin "Bases New with Template" (theol0403) fills this gap: it watches for new notes with a `template: [[TemplateName]]` frontmatter property and auto-applies the named template.]]**
**[[CLM - Obsidian Bases pre-fills frontmatter properties from AND-level equality filters as "implied properties" on new notes; adding `template == "[[TemplateName]]"` to a base's filter causes new notes to receive the property automatically.]]**
**[[EVD - Backfilling `template:` into all existing nodes is required so they continue to appear in filtered views; existing notes without the property would otherwise be hidden by the new filter.]]**

**[[RES - Installed "Bases New with Template" plugin. Added `template == "[[TemplateName]]"` filter to all views in all node-type bases (EXP, ISS, RES, QUE, HYP, CON, PRJ). Backfilled `template: [[TemplateName]]` into all existing notes of each type. Added `template:` to each node template so notes created via Discourse Graphs plugin also carry the property from creation.]]**

---

## 2026-04-28 — Hashtags for log entry differentiation in node templates

**[[QUE - How can log entries in QUE (and other node) templates be made searchable and differentiated from each other?]]**

**[[CLM - Inline hashtags (e.g. #reading, #finding) appended to each log line are searchable vault-wide via Obsidian's tag pane and `tag:` search syntax, and are queryable in Datacore via `$tags`.]]**

**[[RES - Use inline hashtags at the end of each log line for entry typing. Tag vocabulary is left to user convention; no prescribed set is baked into templates.]]**

---

## 2026-04-28 — QUE creation during EXP authoring

**[[QUE - What is the fastest way to create a properly-templated QUE node and link it in EXP frontmatter without leaving the EXP page?]]**

**[[HYP - A "Create linked QUE" Datacore button on the EXP template could prompt for question text, create the QUE file, and write the wikilink into targetQuestionOrHyp: in one action.]]**

**[[CLM - Less busy templates are better; adding more buttons increases cognitive load on every EXP creation.]]**

**[[RES - No button added. Current flow: type the wikilink directly in targetQuestionOrHyp: frontmatter, ctrl+click to create the blank file, then apply the Question template via Templater. Button remains a candidate if the two-step friction proves significant in practice.]]**

---

## 2026-04-29 — Add log entry button on EXP, ISS, QUE templates

**[[HYP - The static `### YYYY-MM-DD` placeholder in the Log section of EXP, ISS, and QUE templates should be replaced with an interactive button that inserts a dated heading and starter bullet.]]**

**[[CLM - A DatacoreJSX AddLogEntry button (matching the one already on PRJ) inserts `### yyyy-mm-dd` + `- ` above the `---` separator, is idempotent, and makes the expected format self-documenting.]]**
**[[EVD - PRJ already had this button using `## ${today}`; EXP/ISS/QUE use h3 to match the existing placeholder convention within their callout sections.]]**
**[[CLM - QUE had no `---` separator (no "From daily notes" section), so one was added before the NodeSetup block to give the button a consistent insertion anchor.]]**
**[[HYP - Obsidian users prefer human-readable, low-code notes for easy export and cognitive ownership; automation should be opt-in, not default structure.]]**
**[[CLM - Guidance will be added explaining how to delete the DatacoreJSX button block for users who prefer a clean, manually-maintained log.]]**
**[[CLM - The example QUE note in the vault will demonstrate a manually-ordered log (no button), showing that the `### yyyy-mm-dd` / bullet format works equally well without the automation.]]**

**[[RES - Replaced the static `### YYYY-MM-DD` placeholder in Experiment.md, Issue.md, and Question.md with a DatacoreJSX AddLogEntry button. QUE received a `---` separator before NodeSetup. HYP, RES, and CON were left unchanged as they have no log sections. Onboarding guidance and the example QUE will communicate that the button is removable for users who prefer plain markdown logs.]]**

---

## 2026-04-29 — Dummy placeholder in daily note task list

**[[HYP - The "New Today" task list needs a placeholder that signals to the user that the space is for a checkoff list, without polluting the task queries.]]**

**[[CLM - All Tasks plugin query blocks in the template already filter with `description regex matches /^#/`, so any placeholder whose text does not begin with `#` is invisible to every query (Over Due, On Deck, Due Today, Done Today).]]**

**[[RES - Changed the placeholder from `- [ ] task 📅` to `- [ ] add tasks here — use a #tag prefix to track them 📅`. The text is instructive and, because it does not start with `#`, remains excluded from all task queries.]]**
