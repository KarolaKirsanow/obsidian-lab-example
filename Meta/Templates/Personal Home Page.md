```datacorejsx
return function NewItemButtons() {
  const [status, setStatus] = dc.useState("");

  const createFrom = async (templatePath, namePrefix, folder, promptLabel) => {
    const name = window.prompt(promptLabel);
    if (!name) return;
    const path = `${folder}/${namePrefix}${name}.md`;
    if (app.vault.getAbstractFileByPath(path)) {
      setStatus(`"${namePrefix}${name}" already exists`);
      return;
    }
    const tpl = app.vault.getAbstractFileByPath(templatePath);
    const content = await app.vault.read(tpl);
    const file = await app.vault.create(path, content);
    const leaf = app.workspace.getLeaf("tab");
    await leaf.openFile(file);
    setStatus("");
  };

  return (
    <span style={{ display: "flex", gap: "0.5em", alignItems: "center", flexWrap: "wrap" }}>
      <button onClick={() => createFrom("Meta/Templates/Project.md", "PRJ - ", "Projects", "Project name:")}>
        + New Project
      </button>
      <button onClick={() => createFrom("Meta/Templates/Experiment.md", "EXP - ", "DiscourseGraph", "Experiment name:")}>
        + New Experiment
      </button>
      {status && <span style={{ opacity: 0.6, fontSize: "0.9em" }}>{status}</span>}
    </span>
  );
}
```

## Misc/links

## Top of mind

### My projects

![[Projects.base#My Projects]]

## Todos

```datacorejsx
return function Todos() {
  const tasks = dc.useQuery("@task and !$completed");

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const parseDue = (text) => {
    const m = String(text).match(/📅\s*(\d{4}-\d{2}-\d{2})/);
    if (!m) return null;
    const d = new Date(m[1]);
    d.setHours(0, 0, 0, 0);
    return d;
  };

  const important = tasks.filter(t => String(t.$text || "").trimStart().startsWith("#"));

  const overdue = [], dueToday = [], upcoming = [], noDue = [];
  important.forEach(t => {
    const due = parseDue(t.$text);
    if (!due) { noDue.push(t); return; }
    if (due < today) overdue.push(t);
    else if (due.getTime() === today.getTime()) dueToday.push(t);
    else upcoming.push(t);
  });

  const renderTask = (t, i) => {
    const href = String(t.$path).replace(/\.md$/, "");
    const label = String(t.$text || "")
      .replace(/^#/, "")
      .replace(/📅\s*\d{4}-\d{2}-\d{2}/, "")
      .trim();
    const file = href.split("/").pop();
    return (
      <li key={i} style={{ marginBottom: "0.2em" }}>
        {label}{" "}
        <a href={href} className="internal-link" data-href={href}
           style={{ opacity: 0.5, fontSize: "0.85em" }}>
          {file}
        </a>
      </li>
    );
  };

  if (important.length === 0)
    return <p><em>No open tasks. Mark tasks with <code>#</code> to show them here.</em></p>;

  return (
    <div>
      {overdue.length > 0 && (
        <div>
          <strong style={{ color: "var(--color-red)" }}>Overdue</strong>
          <ul>{overdue.map(renderTask)}</ul>
        </div>
      )}
      {dueToday.length > 0 && (
        <div>
          <strong style={{ color: "var(--color-orange)" }}>Due Today</strong>
          <ul>{dueToday.map(renderTask)}</ul>
        </div>
      )}
      {upcoming.length > 0 && (
        <div>
          <strong>Upcoming</strong>
          <ul>{upcoming.map(renderTask)}</ul>
        </div>
      )}
      {noDue.length > 0 && (
        <div>
          <strong style={{ opacity: 0.6 }}>No Due Date</strong>
          <ul>{noDue.map(renderTask)}</ul>
        </div>
      )}
    </div>
  );
}
```

## Daily Log

```datacorejsx
return function DailyLog() {
  const DAYS = 7;
  const pages = dc.useQuery('@page and path("Daily Notes")');

  const recent = dc.useMemo(() =>
    [...pages]
      .sort((a, b) => String(b.$name).localeCompare(String(a.$name)))
      .slice(0, DAYS),
    [pages]
  );

  if (recent.length === 0)
    return <p><em>No daily notes found.</em></p>;

  const LOGS = [
    { field: "📊ProjectLog",    alt: "ProjectLog",    label: "📊 Project" },
    { field: "🧪ExperimentLog", alt: "ExperimentLog", label: "🧪 Experiment" },
    { field: "📝BulletJournal", alt: "BulletJournal", label: "📝 Bullet" },
    { field: "🤝MeetingLog",    alt: "MeetingLog",    label: "🤝 Meeting" },
    { field: "📚MediaLog",      alt: "MediaLog",      label: "📚 Media" },
  ];

  return (
    <div>
      {recent.map((p, i) => {
        const entries = LOGS.flatMap(({ field, alt, label }) => {
          const raw = p.value(field) || p.value(alt);
          if (!raw) return [];
          return String(raw).split(",").map(v => v.trim()).filter(Boolean).map(v => ({ label, v }));
        });
        if (entries.length === 0) return null;
        const href = String(p.$path).replace(/\.md$/, "");
        return (
          <div key={i} style={{ marginBottom: "1em" }}>
            <strong>
              <a href={href} className="internal-link" data-href={href}>{p.$name}</a>
            </strong>
            <ul style={{ marginTop: "0.25em" }}>
              {entries.map((e, j) => (
                <li key={j}>
                  <span style={{ opacity: 0.6, fontSize: "0.85em" }}>{e.label}</span>{" — "}{e.v}
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

## Notes
