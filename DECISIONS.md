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
