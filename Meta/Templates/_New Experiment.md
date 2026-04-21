<%*
const name = await tp.system.prompt("Experiment name:");
if (name) {
  const template = tp.file.find_tfile("Meta/Templates/Experiment.md");
  const folder = app.vault.getAbstractFileByPath("DiscourseGraph");
  await tp.file.create_new(template, `EXP - ${name}`, true, folder);
}
-%>