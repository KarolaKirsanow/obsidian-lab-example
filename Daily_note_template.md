---
created: 2026-04-20 16:25
---
tags:: [[+Daily Notes]]

# Daily_note_template

<< [[2026-04-19]] | [[2026-04-21]] >>
---
💡 [[00 Bullet Journal Log | Bullet Journal]] | 📼 [[00 Media Log | Media Log]] | 🤝  [[00 Meeting Log|Meeting Log]] | 💬 [[00 Comms Log | Comms Log]]  |✒️ [[00 writing_plan | Writing Plan]] | 🎒 [[ 00 Learning_Plan | Learning Plan ]] | 💾 [[ 00 Tech Log | Tech Log ]]
----
## Tasks
#### Over Due
```tasks
not done
due before 2026-04-20
```
----
#### On Deck 
```tasks
not done
due after 2026-04-21
```
```tasks
not done
no due date
```
----
#### Due Today
```tasks
not done
due on 2026-04-20
```
----
#### New Today
- [ ] task 📅 
----
## Daily Log
💡 [[00 Bullet Journal Log | Bullet Journal]] | 📼 [[00 Media Log | Media Log]] | 🤝  [[00 Meeting Log|Meeting Log]] | 
----
----
### 📝 Bullet Journal
- #📝BulletJournal:: 
----

### 📓 Meeting Log
- #🗒️MeetingLog:: 
----
### 📼 Media Log
- #📼MediaLog:: 

----
### ✔️ Done Today
```tasks
done
done on 2026-04-20
```
---
### Notes created today

```datacorejsx
const today = DateTime.now();
const pages = dc.useQuery('@page')
  .where(p => p.$ctime && p.$ctime.hasSame(today, 'day'))
  .sort(p => p.$ctime.toMillis());

return (
  <ul>
    {pages.map(p => <li key={p.$path}><dc.NoteLink note={p} /></li>)}
  </ul>
);
```
### Notes modified today

```datacorejsx
const today = DateTime.now();
const pages = dc.useQuery('@page')
  .where(p => p.$mtime && p.$mtime.hasSame(today, 'day'))
  .sort(p => p.$mtime.toMillis());

return (
  <ul>
    {pages.map(p => <li key={p.$path}><dc.NoteLink note={p} /></li>)}
  </ul>
);
```