---
nodeTypeId: node_4SqRl5RIkaUMb9fLOpdhq
tags:
aliases:
  - QUE - Can a 5 ounce bird can carry a one-pound coconut?
template: "[[Question]]"
---

# Summary

## Related QUE/CLM/EVD

## Testable Hypotheses

The loadbearing capacity of a 5 ounce bird can be estimated mathematically

The loadbearing capacity of a 5 ounce bird can be determined empirically

# WorkBench

## Papers

### Screenshots & Direct Quotes

## Notes

> [!log] Log

### YYYY-MM-DD

### 2026-04-28 

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
