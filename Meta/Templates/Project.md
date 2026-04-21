---
status:
targetQuestionOrHyp:
lead:
contributors:
---
# Resources

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


# Experiments in this Project

![[Experiments.base#Experiments in this Project]]

# Results and Conclusions

![[Results.base#Results and Conclusions in this Project]]


# Todos
```tasks
not done
path includes {{query.file.path}}
```
# Notes

# Log

## YYYY-MM-DD


---
## From daily notes

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
