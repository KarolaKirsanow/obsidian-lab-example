---
nodeTypeId: node_Qbdr-LbBCb_WjPFNTnjTX
targetQuestionOrHyp: "[[QUE - How do inert IDRs affect binding affinity?]]"
rel_5nnUOb6wBzlAwAF2Wk-ts: "[[RES - repeated association and dissociation events between (rU)25 and the (GS)25-RBD constructs.md]]"
project: "[[PRJ - Molecular determinants of evolutionary conservation in disordered protein regions]]"
status: Completed
lead: "[[Esther Lederberg]]"
contributors:
  - "[[Rosalind Franklin]]"
  - "[[Joshua Lederberg]]"
nodeInstanceId: 019d7372-cb57-780e-b858-a9b4f03fc7d9
---
# Resources

Protocol: [[Molecular determinant simulation experiments]]
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

## 9/22/22

New result! Discussed with team, looks like [[RES - (GS)25-RBD suppressed RNA binding compared to the RBD alone]]
- [ ] [[RES - maybe later we can follow up on this with another chimera variant]]

![[CleanShot 2025-09-11 at 16.55.46.png]]

## 9/18/22

Discussed plots with team. Think we can say that there's [[RES - repeated association and dissociation events between (rU)25 and the (GS)25-RBD constructs]]

## 9/17/22

(GS)25 simulation completed! 

Plotted distances between (GS)25-RBD and (rU)25 COM over simulation time course.

To make distance threshold, fitted the COM distributions with dual Gaussians.
Then define threshold based on intersection that minimizes overlap of the distributions
NOTE: cutoff distance varies based on the size of the protein and RNA

Then plotted distance threshold to delineate the bound and unbound frames

![[CleanShot 2025-09-11 at 16.14.05.png]]
## 9/8/22

Successfully replaced NTDSCO2 with a length-matched GS repeat – (GS)25. (GS)25-RBDSCO2 chimera ready for simulation experiment!

![[CleanShot 2025-09-11 at 16.12.52.png]]