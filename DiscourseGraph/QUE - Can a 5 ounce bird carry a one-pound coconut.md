---
nodeTypeId: node_4SqRl5RIkaUMb9fLOpdhq
tags:
aliases:
  - QUE - Can a 5 ounce bird can carry a one-pound coconut?
template: "[[Question]]"
---
>[!tip] The "save full title as alias" button at the bottom of each newly-created Question node edits the filename to shorten it and remove unsafe characters. The full title is preserved as an alias and will surface in searches and autocomplete. Press it once and it disappears
# Summary
> [!info]- 
> This should include everything needed to quickly grok the Question

## Related QUE/CLM/EVD
>[!info]- 
>Here you can log related Claims, Questions, & Evidence as they accumulate. A Base is a good way of organizing these nodes.

## Testable Hypotheses
>[!info]- 
>Alex Trebek voice: "Please restate your Question as a statement you can test"

[[HYP- The loadbearing capacity of a 5 ounce bird can be estimated mathematically]]

[[HYP- The loadbearing capacity of a 5 ounce bird can be determined empirically]]

# WorkBench
> [!info]- 
> This area can be used to collate the resources you used to  formulate your Question
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
