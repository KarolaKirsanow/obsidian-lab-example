---
nodeTypeId: node_Qbdr-LbBCb_WjPFNTnjTX
project: PRJ - Passarine Songbird Cargo Capacity
template: "[[Experiment]]"
status: seed
targetQuestionOrHyp: "[[QUE - Can a 5 ounce bird carry a one-pound coconut|QUE - Can a 5 ounce bird can carry a one-pound coconut?]]"
tags:
  - dg/source
cssclasses: dg-exp
lead:
contributors:
aliases:
  - "@analysis - Conduct air speed measurements under laden & unladen conditions"
dg_type: Source
keywords: ""
rating: 3
citekey: analysis - Conduct air speed measurements under laden & unl
---
> [!Note]-
> This is a Source describing an experimental observation. This example graph uses the same naming convention ("@Source") for both literature and experimental Sources. You might choose to differentiate the two, for ex. by using "EXP" as the prefix for your own experiments, for searchability.
 
# Resources
> [!info]-
> This space can be used to include any materials or context necessary to carry out or understand this experiment. 
> You can customize the template to include fields relevevant to your research.

Benchling: ==link to a cloud platform or electronic lab notebook==
Protocol: ==attached protocol file==
Github: ==link to relevant repos==

#  Results

>[!info]-
>This section collects Results from this Experiment in a Base. To find issue 7 result candidates, use the built-in search function on the top left menu to search for e.g. "tag:#iss-candidate @analysis - Conduct air speed measurements" to find issue candidates  linked to this  Experiment page throughout your graph

![[Results.base#Results from this Experiment]]

![[Issues.base#Issues from this Experiment]]
# Todos

```tasks
not done
(path includes {{query.file.path}}) OR (path includes Daily Notes AND description includes {{query.file.filenameWithoutExtension}})
```

> [!log] Log

>[!info]-
>For experiments taking place over several days/weeks, moths, you can log your observations here. 
### 2026-04-24
-  
- [ ] #task when you add ToDos to your Experimental log they show up in this query 📅 2026-05-05 
### 2026-02-06
- [[ISS - better weather measurements needed]]
- weather disproportionately affects laden condition #iss-candidate 
### 2026-02-05
- coconut shape highly variable #iss-candidate 
- European swallows are more  homogeneous in size & speed #res-candidate 
- African swallows seem a bit faster #res-candidate 
- 



---
> [!log] From daily notes

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

```datacorejsx
return function NodeSetup() {
  const current = dc.useCurrentFile();
  const aliases = current.value("aliases");
  if (aliases && aliases.length > 0) return null;

  const handleClick = async () => {
    const full = current.$name;
    const MAX = 60;
    const slug = full.replace(/[?:*"<>|\\]/g, '').slice(0, MAX).trimEnd();
    const file = app.vault.getAbstractFileByPath(current.$path);
    if (!file) return;

    await app.fileManager.processFrontMatter(file, fm => {
      fm.aliases = [full];
    });

    if (slug !== full) {
      const newPath = `${file.parent.path}/${slug}.md`;
      await app.fileManager.renameFile(file, newPath);
    }
  };

  return <button onClick={handleClick}>Save full title as alias</button>;
}
```
> [!info]-
> This space will collect ToDos related to this experiment from elsewhere in your graph, as long as they are tagged with [[@analysis - Conduct air speed measurements under laden & unl]]