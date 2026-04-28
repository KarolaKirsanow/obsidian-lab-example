---
status: Ongoing
targetQuestionOrHyp: "[[QUE - Can a 5 ounce bird carry a one-pound coconut|QUE - Can a 5 ounce bird carry a one-pound coconut?]]"
lead:
contributors:
template: "[[Project]]"
---
## Resources

```datacorejsx
return function CanvasButton() {
  const current = dc.useCurrentFile();
  const [status, setStatus] = dc.useState("");

  const handleClick = async () => {
    const name = current.$name;
    const folder = "Discourse Canvas";
    const path = `${folder}/${name}.canvas`;

    let file = app.vault.getAbstractFileByPath(path);
    if (file) {
      setStatus("Already exists — opening…");
    } else {
      try {
        if (!app.vault.getAbstractFileByPath(folder)) {
          await app.vault.createFolder(folder);
        }
        file = await app.vault.create(path, JSON.stringify({ nodes: [], edges: [] }));
        setStatus("Canvas created!");
      } catch (e) {
        setStatus("Error: " + e.message);
        return;
      }
    }
    const leaf = app.workspace.getLeaf("tab");
    await leaf.openFile(file);
  };

  return (
    <span>
      <button onClick={handleClick}>
        🗺 Open / Create Discourse Canvas
      </button>
      {status && <span style={{ marginLeft: "0.5em", opacity: 0.7 }}>{status}</span>}
    </span>
  );
}
```

## Aims


[[QUE - Can a 5 ounce bird carry a one-pound coconut]]


# Experiments in this Project

![[Experiments.base#Experiments in this Project]]

# Issues in this Project
![[Issues.base#Issues in this Project]]
# Results and Conclusions

![[Results.base#Results and Conclusions in this Project]]


# Todos

- [ ] #task 📅 

```datacorejsx
return function ProjectTodos() {
  const current = dc.useCurrentFile();
  const name = current.$name;

  const nodes = dc.useQuery('@page and path("DiscourseGraph")');
  const allTasks = dc.useQuery('@task and path("DiscourseGraph")');

  const EXP_ID = "node_Qbdr-LbBCb_WjPFNTnjTX";
  const ISS_ID = "node_2unblKFUVJkOdOnT8MstZ";
  const RES_ID = "node_i7PzyKw2NfkA8asBfxeey";
  const CON_ID = "node_J9JyrRTQj6nuJs6IY83Mo";

  const relatedPaths = dc.useMemo(() => {
    const byProject = nodes.filter(p =>
      [EXP_ID, ISS_ID].includes(p.value("nodeTypeId")) &&
      String(p.value("project") || "") === name
    );
    const byLink = nodes.filter(p =>
      [RES_ID, CON_ID].includes(p.value("nodeTypeId")) &&
      (p.$links || []).some(l => String(l.path || l).includes(name))
    );
    return new Set([...byProject, ...byLink].map(p => p.$path));
  }, [nodes, name]);

  const todos = dc.useMemo(() =>
    allTasks.filter(t => {
      const fp = t.$file?.path ?? t.$file ?? t.$path ?? "";
      return relatedPaths.has(fp) && !t.$completed;
    }),
    [allTasks, relatedPaths]
  );

  if (todos.length === 0)
    return (
      <p style={{ opacity: 0.5, fontStyle: "italic", fontSize: "0.9em" }}>
        No open todos in related nodes.
      </p>
    );

  const grouped = dc.useMemo(() => {
    const map = new Map();
    for (const t of todos) {
      const fp = t.$file?.path ?? t.$file ?? t.$path ?? "unknown";
      if (!map.has(fp)) map.set(fp, []);
      map.get(fp).push(t);
    }
    return map;
  }, [todos]);

  return (
    <div>
      {[...grouped.entries()].map(([fp, tasks], i) => {
        const href = fp.replace(/\.md$/, "");
        const label = fp.replace(/^.*\//, "").replace(/\.md$/, "");
        return (
          <div key={i} style={{ marginBottom: "0.75em" }}>
            <div style={{ fontSize: "0.85em", opacity: 0.55, marginBottom: "0.2em" }}>
              <a href={href} className="internal-link" data-href={href}>{label}</a>
            </div>
            <ul style={{ margin: 0, paddingLeft: "1.2em" }}>
              {tasks.map((t, j) => (
                <li key={j} style={{ marginBottom: "0.15em" }}>
                  {t.$text ?? t.text ?? String(t)}
                </li>
              ))}
            </ul>
          </div>
        );
      })}
    </div>
  );
}
```

# Notes

> [!log] Project Log

```datacorejsx
return function AddLogEntry() {
  const current = dc.useCurrentFile();
  const [msg, setMsg] = dc.useState("");

  const handleClick = async () => {
    const file = app.vault.getAbstractFileByPath(current.$path);
    if (!file) return;

    const today = new Date().toISOString().slice(0, 10);
    const content = await app.vault.read(file);

    if (content.includes(`## ${today}`)) {
      setMsg(`${today} already exists`);
      return;
    }

    const sep = "\n---\n";
    const sepIdx = content.indexOf(sep);
    const insertAt = sepIdx !== -1 ? sepIdx : content.length;
    const newEntry = `\n\n## ${today}\n\n`;
    await app.vault.modify(file, content.slice(0, insertAt) + newEntry + content.slice(insertAt));
    setMsg(`Added ${today}`);
  };

  return (
    <span>
      <button onClick={handleClick}>+ New log entry</button>
      {msg && <span style={{ marginLeft: "0.7em", opacity: 0.55, fontSize: "0.85em" }}>{msg}</span>}
    </span>
  );
}
```

---
> [!log] From daily notes

```datacorejsx
return function View() {
  const current = dc.useCurrentFile();
  const FIELD = "📊ProjectLog";
  const ALT = "ProjectLog";

  const pages = dc.useQuery('@page and path("Daily Notes")');

  const rows = dc.useMemo(() =>
    pages
      .filter(p => {
        const v = p.value(FIELD) || p.value(ALT);
        if (!v) return false;
        return String(v).includes(current.$name);
      })
      .sort((a, b) =>
        String(b.$name).localeCompare(String(a.$name))
      ),
    [pages, current]
  );

  if (rows.length === 0)
    return (
      <p>
        <em>
          No entries yet. In your daily note write:
          {" "}<code>{"#📊ProjectLog:: [[" + current.$name + "]] your note here"}</code>
        </em>
      </p>
    );

  return (
    <ul>
      {rows.map((p, i) => {
        const v = String(p.value(FIELD) || p.value(ALT));
        const href = String(p.$path).replace(/\.md$/, "");
        return (
          <li key={i}>
            <strong>
              <a href={href} className="internal-link" data-href={href}>
                {p.$name}
              </a>
            </strong>
            {" — "}
            {v.replace("[[" + current.$name + "]]", "").trim()}
          </li>
        );
      })}
    </ul>
  );
}
```
> [!log] Project Meetings

```datacorejsx
return function ProjectMeetings() {
  const current = dc.useCurrentFile();
  const name = current.$name;

  const pages = dc.useQuery('@page');

  const meetings = dc.useMemo(() =>
    pages
      .filter(p => {
        const path = String(p.$path);
        if (path.includes("DiscourseGraph")) return false;
        if (path.includes("Daily Notes")) return false;
        if (path.includes("Meta")) return false;
        const proj = p.value("project");
        if (!proj) return false;
        return String(proj).includes(name);
      })
      .sort((a, b) => {
        const da = String(a.value("date") || a.$name);
        const db = String(b.value("date") || b.$name);
        return db.localeCompare(da);
      }),
    [pages, name]
  );

  if (meetings.length === 0)
    return (
      <p>
        <em>
          No meetings yet. Create a meeting note with{" "}
          <code>{"project: [[" + name + "]]"}</code> in its frontmatter.
        </em>
      </p>
    );

  return (
    <ul>
      {meetings.map((p, i) => {
        const href = String(p.$path).replace(/\.md$/, "");
        const date = p.value("date");
        return (
          <li key={i}>
            <a href={href} className="internal-link" data-href={href}>
              {p.$name}
            </a>
            {date && (
              <span style={{ opacity: 0.55, fontSize: "0.85em", marginLeft: "0.5em" }}>
                {String(date).substring(0, 10)}
              </span>
            )}
          </li>
        );
      })}
    </ul>
  );
}
```