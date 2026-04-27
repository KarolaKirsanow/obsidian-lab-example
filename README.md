This is an example vault that illustrates potential usage of the [discourse graph plugin](https://discoursegraphs.com/docs/obsidian/getting-started) to structure project/experiment management, and synthesis and reflection of results in conversation with prior literature towards new directions and contributions.
# Plugins in the vault (and why)

## Core

**Bases**: enables queries over discourse nodes, etc. - examples are in the vault

**Backlinks** (optional): nice to have references to a given note easily accessible at the bottom of the page

## Community

### Required

- **[BRAT](https://github.com/TfTHacker/obsidian42-brat)**: this is how we load our plugin at the moment
- **[Datacore](https://github.com/blacksmithgu/datacore)** : this is the query engine that underlies our plugin
- **[Discourse Graph](https://discoursegraphs.com/docs/obsidian/getting-started)** (required): this is our plugin :)

### Recommended
- **[Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks)** (recommended): makes it easier to create/query/manage todos
- **[Outliner](https://github.com/vslinko/obsidian-outliner)** (optional): 
- [Calendar](https://obsidian.md/plugins?id=calendar): supports a Daily Notes workflow
- [Style Settings](https://obsidian.md/plugins?id=obsidian-style-settings): adjust themes & CSS snippets
- [Templater](https://obsidian.md/plugins?id=templater-obsidian): create more advanced templates (including the Daily Note Template)
- [Zotsidian](https://github.com/obsidian-community/obsidian-zotero-integration): connect your Zotero library to Obsidian

# Overall structure of the vault (and why)

The current structure of this vault parallels lab discourse graphs workflows we've developed in Roam, modified for the affordances provided by Obsidian/git yet. But little of this structure is written in stone -- we follow the Obsidian convention that your vault is your own. We've tried to support reasoning about the folder structure with some rationales and marking where the existence of certain folders is important.

- `Bases/` Your `.base` files could also inside their respective content folders (e.g., a `Projects.base` in the Project folder). Putting them in one place allows you to see which bases you've created, which is #clm-candidate more valuable as you set up your vault and less important later.
- `DiscourseGraph/` not a bad idea to set a default location for new discourse nodes #hyp-candidate this separation-of-concerns is especially useful for users grafting the discourse graph protocol onto an mature vault.
- `Meta/`
	- `Attachments/` usually it's good set a folder for attachments to go to, but it can be anywhere
	- `Templates/` the discourse nodes can be created based on a template. the plugin needs to be pointed to a folder that contains templates to use. Templates in these folder can also be used for other notes, not just discourse nodes
	- `Conventions.md` this might be a good place to write down the conventions/workflows for your lab
- `Projects/` pretty self-explanatory, and probably something you want to do to track projects. 
- `Protocols/` optional, if you want to create and track specific protocols and link to them in your experiments, and what questions they can address

## Functional Modules

### Experiment pages

Annotated example

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdiscourse-graphs%2FYvAlbf0Gk8.png?alt=media&token=d81e673e-b65f-4d70-b5dc-95fde17c8a48)

The structure of these pages enables you to
- Keep target question or hypothesis close by, to define the purpose of the experiment
- Keep an experiment log where you can reflect on observations, and (if appropriate) formalize these into hypotheses or results you want to share with others by creating discourse nodes
- Reflect on progress of the experiment by comparing tabulated results from the experiment against the target question

Key actions
- Set/change the target question by changing it in the `targetQuestionOrHyp` property for the page
- Review progress by comparing the target question to the tabulated results so far. The `.base` query will auto-update

There is a template in the example vault that you can modify (in `Meta/Templates/Experiment.md`)

### Project pages

Annotated example

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdiscourse-graphs%2FrNriAK2fdI.png?alt=media&token=ee7e1ebc-2bc1-48fd-b7d6-6ec65d2f078f)

The structure of these pages enables you to
- Keep the broad target question(s) close by, provide space for reflecting on what has been learned from the experiments
- Consolidate key links/resources for the project
- Keep a log of project notes

Key actions
- Review progress by pulling in results from each experiment alongside the literature and your questions by placing them on the project canvas
- There is a template in the example vault that you can modify (in `Meta/Templates/Project.md`)

### Creating Discourse Nodes

Currently this can be done in three ways (see [docs](https://discoursegraphs.com/docs/obsidian/creating-discourse-nodes) for more details)
- Using the command palette
- Convert existing text to node
	- Suspect to start with, if you're migrating over a small project, you'll mostly be doing this
		- List out all the questions/claims/evidence/etc., maybe in an outline
		- And convert individual ones to nodes, put figures/other info inside as needed
- Convert existing page to node

You can also set/create/edit templates to use for creating specific nodes (see [docs](https://discoursegraphs.com/docs/obsidian/node-types-templates#working-with-templates) for more details). For instance, you might want to ensure that a result page has a key figure and some details about the experimental method.

### Exploring "Discourse Context" for Nodes

You can toggle a sidebar "discourse context" component that shows you any discourse relations you've created between a given node to other nodes (e.g., what claims inform this question, which evidence supports/opposes this claim)

See [docs](https://discoursegraphs.com/docs/obsidian/discourse-context) for more details

### Linking Discourse Nodes

Currently this is done using the buttons in the discourse context component (see [docs](https://discoursegraphs.com/docs/obsidian/creating-discourse-relationships) for more details)

### Bases

This is new in Obsidian as of the last ~month or so. It enables you to create "databases" for your notes, which you can use to view/rank/sort projects, experiments, or other things you want to track in a live updated query. We find these queries to be quite useful in our labs so it will probably be useful here too. I've included some examples in the vault.

# Notes

Please feel free to organize the vault's folders however you like! It sounds like Graham has very substantial Obsidian experience, + there may be organizational structure patterns that work well for your lab.

## Suggestions for how to explore discourse graphs using this example vault

1. Download this example vault (all plugin "batteries" are included already)
2. Choose 1-2 projects that already have some questions/claims/evidence around them, maybe some sub-experiments too
3. For each project
	1. Create the project and its container experiments
	2. Map out the key questions/claims/evidence for the project
	3. Maybe tabulate some logs for ongoing experiments in those projects

Here's a quick Loom on how this might go: https://www.loom.com/share/f80799f5d0f44a51b1951bc835e4fef7
## Some additional open questions that can be up to you and we can discuss more

### Tracking different types/shades of (claims/hypotheses/conclusion, evidence/results). 

Conceptually claims/hypotheses/conclusions are basically the same (generalized assertions about a phenomenon) and evidence/results are the same (contextualized descriptions of observations from a specific experiment). 

If you'd like to iterate on this, we can discuss more, and/or you can explore the docs for how to define [new types of nodes](https://discoursegraphs.com/docs/obsidian/node-types-templates#adding-a-node-type) and [new types of relations](https://discoursegraphs.com/docs/obsidian/relationship-types#adding-relationship-types).

### Templates/workflows

At the moment a lot of our lab processes are encoded in "smartblock" workflows and templates. For instance, we have meeting templates that focus attention on research questions, and workflows for creating new projects/experiments that encourage specification of target questions/hypotheses. You may want to start working in similar things to support sufficient (minimal) standardization and shared processes as you collaborate.

Our discourse plugin supports the use of templates when creating discourse nodes, but for more advanced workflow structuring, you might experiment with the Templater plugin: 

Docs: https://silentvoid13.github.io/Templater/

Examples: https://github.com/SilentVoid13/Templater/discussions/categories/templates-showcase

### Personal home page notes

In Roam in a collaborative setting, we often have personal home pages and sidebars where people can bookmark certain important pages for them and write any other unsorted notes they like. Like this:

![](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Fdiscourse-graphs%2F2MC50YqgoG.png?alt=media&token=20fb476b-f534-4f6a-8d5c-25a6d303a2ab)

This is a bit different from a usual single-player Obsidian pattern where you might just work in daily note pages, but might end up being useful in a lab/collaborative setting. So this isn't in the example vault in a formal way, though there is a small example in [[Rosalind Franklin]] page that could be a starting point for exploration of this pattern. 

### Literature notes

The example vault currently lacks an example of literature notes (e.g., a source page with associated claims or evidence).

If you're interested in this use case and would like to learn more, please [reach out](https://join.slack.com/t/discoursegraphs/shared_invite/zt-37xklatti-cpEjgPQC0YyKYQWPNgAkEg) to talk more about this, especially once you've selected a couple starter projects and what the related literature is and what a useful workflow would be.

### Meeting notes

In a lab setting it can be useful to host meeting notes in the same vault: this allows you to structure your meetings around sharing/developing discourse nodes (e.g., hypotheses/results). The vault includes a simple example note ([[Lab Meeting Notes 2025]]) with links to experiments/results. Feel free to modify!

