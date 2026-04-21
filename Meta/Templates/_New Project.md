<%*
const name = await tp.system.prompt("Project name:");
if (name) {
  const template = tp.file.find_tfile("Meta/Templates/Project.md");
  const folder = app.vault.getAbstractFileByPath("Projects");
  await tp.file.create_new(template, `PRJ - ${name}`, true, folder);
}
-%>