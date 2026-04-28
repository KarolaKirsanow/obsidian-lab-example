---
nodeTypeId: node_Qbdr-LbBCb_WjPFNTnjTX
status:
lead:
contributors:
targetQuestionOrHyp: "[[CLM - the barrier helps cells regulate breathing by injecting fun]]"
project: "[[PRJ - my awesome new project]]"
nodeInstanceId: 019d7372-cb0c-7dda-b9c9-7392a4fee39f
template: "[[Experiment]]"
---
# Resources

Protocol:
Git repo:
Benchling: 
# Results

![[Results.base#Results from this Experiment]]
# Todos
```tasks
not done
path includes {{query.file.path}}
```
# Log

## 2024-09-16
formalized result [[RES - cells died after 15 days in the lab]]
- protocol was xyz

---
## From daily notes

```datacorejsx
return function View() {
  const current = dc.useCurrentFile();
  const FIELD = "🧪ExperimentLog";
  const ALT = "ExperimentLog";

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
          {" "}<code>{"#🧪ExperimentLog:: [[" + current.$name + "]] your note here"}</code>
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