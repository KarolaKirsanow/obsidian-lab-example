---
status:
targetQuestionOrHyp:
lead:
contributors:
template: "[[Project]]"
---
# Resources
> [!info] Add links to datasets, analysis files, manuscript files, etc. The button below will create a Project Canvas
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


# Aims

# Experiments, Issues, & Results

```datacorejsx
return function ProjectDashboard() {
  const current = dc.useCurrentFile();
  const name = current.$name;

  const nodes = dc.useQuery('@page and path("DiscourseGraph")');

  const EXP_ID = "node_Qbdr-LbBCb_WjPFNTnjTX";
  const ISS_ID = "node_2unblKFUVJkOdOnT8MstZ";
  const RES_ID = "node_i7PzyKw2NfkA8asBfxeey";
  const CON_ID = "node_J9JyrRTQj6nuJs6IY83Mo";

  const exps = dc.useMemo(() =>
    nodes.filter(p =>
      p.value("nodeTypeId") === EXP_ID &&
      String(p.value("project") || "") === name
    ), [nodes, name]);

  const issues = dc.useMemo(() =>
    nodes.filter(p =>
      p.value("nodeTypeId") === ISS_ID &&
      String(p.value("project") || "") === name
    ), [nodes, name]);

  const rescons = dc.useMemo(() =>
    nodes.filter(p =>
      [RES_ID, CON_ID].includes(p.value("nodeTypeId")) &&
      (p.$links || []).some(l => String(l.path || l).includes(name))
    ), [nodes, name]);

  const NodeLink = ({ page }) => {
    const href = page.$path.replace(/\.md$/, "");
    return (
      <li style={{ marginBottom: "0.25em" }}>
        <a href={href} className="internal-link" data-href={href}>
          {page.$name}
        </a>
      </li>
    );
  };

  const Column = ({ title, items, isLast }) => (
    <div style={{
      flex: 1,
      minWidth: 0,
      paddingRight: isLast ? 0 : "1em",
      marginRight: isLast ? 0 : "1em",
      borderRight: isLast ? "none" : "1px solid var(--background-modifier-border)"
    }}>
      <div style={{
        fontWeight: "bold",
        marginBottom: "0.5em",
        paddingBottom: "0.25em",
        borderBottom: "1px solid var(--background-modifier-border)"
      }}>
        {title}{" "}
        <span style={{ opacity: 0.45, fontWeight: "normal", fontSize: "0.85em" }}>
          ({items.length})
        </span>
      </div>
      {items.length === 0
        ? <span style={{ opacity: 0.4, fontStyle: "italic", fontSize: "0.9em" }}>None</span>
        : <ul style={{ margin: 0, paddingLeft: "1.2em" }}>
            {items.map((p, i) => <NodeLink key={i} page={p} />)}
          </ul>
      }
    </div>
  );

  return (
    <div style={{ display: "flex", alignItems: "flex-start", padding: "0.25em 0" }}>
      <Column title="Experiments" items={exps} />
      <Column title="Issues" items={issues} />
      <Column title="Results & Conclusions" items={rescons} isLast />
    </div>
  );
}
```

# Experiments in this Project

![[Experiments.base#Experiments in this Project]]

# Issues in this Project
> [!info] Issues are problems or questions that arise during the course of a Project that may require a new  Experiment to solve

![[Issues.base#Issues in this Project]]


# Results and Conclusions

![[Results.base#Results and Conclusions in this Project]]


# Todos
> [!info] This space collates ToDos  related to this Project
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
