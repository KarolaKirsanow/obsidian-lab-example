
# Meeting Log

💡 [[00 Bullet Journal Log | Bullet Journal]] |  📚 [[00 Media Log | Media Log]] | 🤝  [[00 Meeting Log|Meeting Log]] | 📊  [[00 Project Log|Project Log]] | 🧪 [[00 Experiment Log | Experiment Log]]

## Meeting Log
---
```datacorejsx
const FIELD = "🤝MeetingLog";
const ALT = "MeetingLog";
const COLUMNS = [
  { id: "File", value: p => p.$link },
  {
    id: "Log",
    value: p =>
      p.value(FIELD)
      || p.value(ALT)
  }
];

return function View() {
  const pages = dc.useQuery(
    '@page and path("Daily Notes")'
  );
  const rows = dc.useMemo(
    () => pages
      .filter(p => {
        const v = p.value(FIELD)
          || p.value(ALT);
        return v
          && String(v).trim() !== "";
      })
      .sort((a, b) =>
        String(b.$name)
          .localeCompare(
            String(a.$name)
          )
      ),
    [pages]
  );
  return (
    <dc.Table
      columns={COLUMNS}
      rows={rows}
    />
  );
}
```
