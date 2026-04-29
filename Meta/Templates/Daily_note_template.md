
tags:: [[+Daily Notes]]

# <% tp.file.title %>

<< [[<% tp.date.yesterday() %>]] | [[<% tp.date.tomorrow() %>]] >>
---
💡 [[00 Bullet Journal Log | Bullet Journal]] |  📚 [[00 Media Log | Media Log]] | 🤝  [[00 Meeting Log|Meeting Log]] | 📊  [[00 Project Log|Project Log]] |🧪 [[00 Experiment Log | Experiment Log]]

----
## Tasks
#### Over Due
```tasks
not done
description regex matches /^#/
due before <% tp.date.now("YYYY-MM-DD") %>
```
----
#### On Deck 
```tasks
not done
description regex matches /^#/
due after <% tp.date.now("YYYY-MM-DD", 1) %>
```
```tasks
not done
description regex matches /^#/
no due date
```
----
#### Due Today
```tasks
not done
description regex matches /^#/
due on <% tp.date.now("YYYY-MM-DD") %>
```
----
#### New Today
- [ ] add tasks here — use a #tag prefix to track them 📅 
----
## Daily Log
💡 [[00 Bullet Journal Log | Bullet Journal]] |  📚 [[00 Media Log | Media Log]] | 🤝  [[00 Meeting Log|Meeting Log]] | 📊  [[00 Project Log|Project Log]] | 🧪 [[00 Experiment Log | Experiment Log]]
----
### 📝 Bullet Journal
- #📝BulletJournal:: 
----
### 📚 Media Log
- #📚MediaLog:: 
----
### 🤝 Meeting Log
- #🤝MeetingLog:: 
----
### Project Log
- #📊ProjectLog:: 
----
### 🧪 Experiment Log
- #🧪ExperimentLog::
----
## Projects

![[Projects.base]]

## Experiments

![[Experiments.base]]

# Research questions

![[Questions.base]]

----
### ✔️ Done Today
```tasks
done
description regex matches /^#/
done on <% tp.date.now("YYYY-MM-DD") %>
```
---
### Notes created today

```datacorejsx
return function View() {
  // Use dc.useCurrentFile() to get
  // the daily note's own metadata,
  // then parse the date from its name
  // instead of using new Date()
  const current = dc.useCurrentFile();
  const noteDate = current
    ? String(current.$name) : "";

  const pages = dc.useQuery('@page');
  const created = [];

  for (let i = 0; i < pages.length; i++) {
    const p = pages[i];
    const path = String(p.$path);

    // Skip the daily note itself
    if (current
      && path === String(current.$path))
      continue;

    // Prefer frontmatter "created" field
    // as file.stat.ctime is unreliable
    // in Obsidian (changes on modify).
    // Fall back to file.stat.ctime.
    let dateStr = "";
    const fm = p.$frontmatter;
    if (fm && fm.created) {
      // Handle both "YYYY-MM-DD" and
      // "YYYY-MM-DD HH:mm:ss" formats
      dateStr = String(fm.created)
        .substring(0, 10);
    } else {
      const file = dc.app.vault
        .getAbstractFileByPath(path);
      if (!file || !file.stat) continue;
      const ct = new Date(file.stat.ctime);
      dateStr = ct.getFullYear()
        + "-"
        + String(ct.getMonth() + 1)
            .padStart(2, "0")
        + "-"
        + String(ct.getDate())
            .padStart(2, "0");
    }

    if (dateStr === noteDate)
      created.push({
        path,
        name: path
          .replace(/\.md$/, "")
          .split("/").pop()
      });
  }

  if (created.length === 0)
    return (
      <p>
        <em>
          No notes created on {noteDate}
        </em>
      </p>
    );
  return (
    <ul>
      {created.map((c, i) => {
        const href = c.path
          .replace(/\.md$/, "");
        return (
          <li key={i}>
            <a
              href={href}
              className="internal-link"
              data-href={href}
            >{c.name}</a>
          </li>
        );
      })}
    </ul>
  );
}
```

### Notes modified today

```datacorejsx
return function View() {
  // Same approach: derive the target
  // date from the daily note's name
  const current = dc.useCurrentFile();
  const noteDate = current
    ? String(current.$name) : "";

  const pages = dc.useQuery('@page');
  const modified = [];

  for (let i = 0; i < pages.length; i++) {
    const p = pages[i];
    const path = String(p.$path);

    // Skip the daily note itself
    if (current
      && path === String(current.$path))
      continue;

    const file = dc.app.vault
      .getAbstractFileByPath(path);
    if (!file || !file.stat) continue;
    const mt = new Date(file.stat.mtime);
    const dateStr = mt.getFullYear()
      + "-"
      + String(mt.getMonth() + 1)
          .padStart(2, "0")
      + "-"
      + String(mt.getDate())
          .padStart(2, "0");

    if (dateStr === noteDate)
      modified.push({
        path,
        name: path
          .replace(/\.md$/, "")
          .split("/").pop()
      });
  }

  if (modified.length === 0)
    return (
      <p>
        <em>
          No notes modified on {noteDate}
        </em>
      </p>
    );
  return (
    <ul>
      {modified.map((c, i) => {
        const href = c.path
          .replace(/\.md$/, "");
        return (
          <li key={i}>
            <a
              href={href}
              className="internal-link"
              data-href={href}
            >{c.name}</a>
          </li>
        );
      })}
    </ul>
  );
}
```