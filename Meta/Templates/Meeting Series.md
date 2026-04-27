---
project:
attendees:
---

**Zoom link:**

**Frequency:**

# Standing Agenda


# Instances

```datacorejsx
return function MeetingInstances() {
  const current = dc.useCurrentFile();
  const name = current.$name;

  const pages = dc.useQuery('@page');

  const instances = dc.useMemo(() =>
    pages
      .filter(p => {
        const s = p.value("series");
        if (!s) return false;
        return String(s).includes(name);
      })
      .sort((a, b) => {
        const da = String(a.value("date") || a.$name);
        const db = String(b.value("date") || b.$name);
        return db.localeCompare(da);
      }),
    [pages, name]
  );

  if (instances.length === 0)
    return (
      <p>
        <em>
          No instances yet. Create a meeting note with{" "}
          <code>{"series: [[" + name + "]]"}</code> in its frontmatter.
        </em>
      </p>
    );

  return (
    <ul>
      {instances.map((p, i) => {
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
