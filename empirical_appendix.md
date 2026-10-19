# Separate prospective empirical module, R1

**Not an executed or registered field study.** The main paper is a completed theoretical article. This module is conditional on an authorized partner, independent truth evidence, and a feasible number of independent service pools. No trial outcomes are supplied. The executable estimator's fixture is synthetic software validation only.

## E1. Setting and treatment regimes

Begin with a bounded shadow-workflow pilot: retrospective internal-reporting discrepancies, frozen records, no customer-facing action or live financial posting. A task requires an amount, period, definition, evidence citation, and resolve/escalate disposition. All assigned tasks enter the frame before treatment. Unfinished tasks require measured fallback work, rather than disappearing from the denominator. No partner, access, participants, or approval has been secured.

The randomization unit must include the entire independent reference pool and all tasks competing for it. A pool includes the reference analysts, correction service, and any source-validation team drawing on that same time budget. Two departments cannot be treated as independent clusters merely because they have different managers. Before assignment, map cross-pool staff sharing, source sharing, escalation, and emergency coverage. Merge connected units or use a prespecified interference design if separation is impossible. A time switchback alone does not remove learning about corrected sources; use disjoint historical source bundles and account for time effects before considering it.

Two scientifically different designs are available. The primary proposed design for this article is a cross-department two-by-two: source repair for a prespecified source-consuming class, crossed with offered AI access for a different recipient class that shares the pool but does not consume that source. Both classes' tasks, plus any other pool workload, are outcomes. This tests the total cross-department policy interaction. A conventional whole-corpus repair-by-AI-access design is still possible but estimates a broader bundle and cannot isolate the cross-department mechanism.

Across the four arms, hold task frame, deadlines, ordinary incentives, user orientation duration, model snapshot, prompt scaffold, retrieval code, tool permissions, and compute budgets comparable. AI remains optional. AI-specific orientation is an unavoidable part of offered access, with equal-duration ordinary-tool orientation in controls. Source repair changes the authorized corpus and documented definitions/timestamps, not the interface, additional computation, or user coaching. Freeze and hash all versions. No deliberate misinformation is introduced into live production.

## E2. Interference-aware estimand

Let Z_g=(A_g,D_g) be assignment of independent service pool g, and Y_g the sum of operational net values for every task in its fixed frame, including source consumers, recipient classes, and unfinished-task fallback. Under partial interference restricted within pools, define the task-weighted mean

mu_ad=(1/N) sum_g Y_g(ad), where N=sum_g N_g is the fixed total assigned task count.

The access ITT interaction is delta=mu11-mu10-mu01+mu00. It concerns optional access and source repair under the pool's actual allocation policy. Usage, review intensity, and staffing reallocations are mediators, not substitutes for assignment. Do not estimate a committed-workflow interaction by comparing users and nonusers. The theoretical global optimizer provides a policy benchmark, not an assumption that real pools reoptimize perfectly.

If external pool exposures matter, potential outcomes are Y_g(Z_g,E_g). Prespecify E_g from a pre-assignment sharing graph. An own-assignment two-by-two coefficient then does not identify a universal no-interference effect. A larger-pool randomization, randomized saturation, or a factorial assignment that holds neighboring exposure constant is needed. The supplied estimator rejects no interference automatically: it requires the study designer to justify pool independence. A computed p-value cannot establish that assumption.

Primary estimate is the design-based Horvitz-Thompson contrast of total pool outcomes with known assignment probability 1/4 within balanced blocks. Report all four cell means, conditional access/data effects, pool sizes, completion/fallback and uncertainty. Do not normalize by a post-treatment count of submitted tasks or AI-generated outputs.

## E3. Cost and independent audit manual

Primary operational Y is negative total resource-adjusted decision loss. Use a frozen price schedule in euros; no particular schedule is empirically validated here. Record production labor, independent examination labor, actual correction labor, ordinary review, source validation, recurring maintenance, compute, delay/fallback, and final undetected material loss. An hour belongs to one activity ledger only. Source validation done by the reference pool consumes its budget and is priced once as labor; an estimated shadow price is not added as a second actual cost. Setup can be a one-time outlay in NPV or per-task amortization, never both. Research-only audit expense is separate; a deployment-equivalent audit enters sensitivity accounting.

Illustrative, not confirmatory, loss schedule: correct answer or justified escalation 0; minor non-disposition defect EUR 10; material amount/period/definition/disposition error EUR 250; severe explicitly defined downstream-risk error EUR 2500. Assign the highest applicable final-output severity once. These are scored decision losses, not realized harm. Record actual downstream costs separately if authorized. The partner's blinded pilot must establish materially defensible thresholds before any confirmatory assignment.

A truth team creates an independent gold ledger from authoritative information outside the experimental corpus. A separate data team repairs sources; a separate blinded audit team grades outputs. Verification can use a common authorized escalation/reference channel across arms, but its workload and elapsed times count. If no independent reference exists, that source class cannot satisfy the model and must be labeled unverifiable. A second LLM's agreement is not independent truth.

Freeze the final output after ordinary controls and before research audit. Double-grade every sampled output for: amount/arithmetic; effective period; semantic definition/units; evidence relevance/traceability; disposition. A material error is one that changes disposition under the frozen ledger. Retain independent scores and disagreements; a third specialist adjudicates. Measure blinding guesses. Log and apply any reference-ledger correction to every affected arm equally before unmasking.

Audit all tasks in the small pilot. A larger confirmatory study may use known-probability random audit sampling, never sampling only confident outputs. To use the supplied estimator, create complete pool totals from a prespecified sampling estimator and supply its extra sampling variance separately; the current executable variance assumes complete audited totals. Missing nonrandom audit outcomes require bounds, not an assertion that weighting solves them. For the most feasible first pilot, insist on complete audit and fallback measurement.

## E4. Mechanism tests and falsification

The pool-level two-by-two interaction does not identify source reliability and document structure separately. Nor does it distinguish a resource spillover from increased managerial attention without further variation. Diagnose but do not causally equate them.

Preclassify baseline task defects as retrieval difficulty, ambiguous meaning, stale date, missing record, and correct clean reference. Log the source-consumer class and recipient class before assignment. Mechanism predictions: repair reduces source-defect rates; it can reduce source-consumer demand and increase recipient service allocation; recipient residual error can decline without a change in its raw error probability or retrieved source. If analysts simply transfer work upstream or ordinary reviewers absorb extra cleanup, the all-cost primary outcome captures it.

Prespecified checks: identical model/prompt/retrieval hashes across D, no extra D-specific training, unchanged task assignment, source correctness audited independently before outcomes, no recipient source contamination, reviewer/staff cross-pool exposure, differential missingness and grader blinding. A null interaction must not be reframed as positive evidence of complementarity. A negative interaction may reflect reversed service demand, repair's own reference workload, or other bundle effects; it is not by itself a falsification of every theoretical regime.

For causal channel separation, a separate safe design could randomize factual repair versus structure-only reformatting with identical facts, and/or independent service budgets. It would need additional independent assignment units and a new precision assessment. Diagnostic confidence scores do not identify the shadow price or detection technology. Estimate marginal value of service using randomized service increments only if a separately authorized design is feasible.

## E5. Runnable estimator, inference, and honest precision

`code/field_estimator.py` accepts one JSON record per complete independent pool. Fields: pool_id, block, A, D, task_count, total_Y, frame_frozen. It requires fixed-frame complete totals, balanced four-cell blocks, and at least two pools per cell per block. It computes HT means, the factorial interaction, and a conservative Neyman variance on pool totals. The t interval is an approximation, not an exact weak-null confidence interval. It accounts for assignment at the pool level and unequal fixed pool task counts; it does not cure unmodeled cross-pool interference.

The same program enumerates the exact blocked assignment space when small and otherwise uses a seeded Monte Carlo test with plus-one correction. **That Fisher test is for the global sharp null of no treatment effects on any pool. It is not an exact test of a zero interaction allowing arbitrary main effects.** A confirmatory interaction claim needs the registered weak-null estimator/uncertainty assessment, not reinterpretation of that sharp-null p-value. There is one primary interaction; secondary defect-class and conditional-effect families use prespecified Holm adjustment. Loss-price and opportunity-cost sensitivity are reported as such, without selecting a favorable schedule after results.

`code/test_field_estimator.py` executes an eight-pool synthetic fixture, checks the analytic interaction and enumerates all 2520 assignments. It also checks invalid inputs. This software test is not a demonstration that a real eight-pool study is adequate. No incomplete R scaffold is presented as confirmatory code. Python is used because R was unavailable; the numerical theory and estimator both execute in the delivered environment.

The earlier EUR 2 interaction calculation is retained only as a feasibility warning: with task SD EUR 20, 20 tasks per independent pool, ICC .05, and equal allocation, normal approximation gives about 1225 pools for 80% power at 5% two-sided. These assumptions were invented. Correctly defining a larger shared pool is likely to reduce independent sample size further. A small authorized pilot should estimate reference workload, spillover feasibility, error frequencies, and dispersion, not claim a precise interaction null. No confirmatory sample size is fixed without blinded pilot estimates, a realistic loss distribution, and interference mapping.

## E6. Data dictionary and accounting checks

| Object | Required fields | Provenance |
|:--|:--|:--|
| Fixed task frame | task_id, pool_id, department, source_id, class, deadline, N_g | Pretreatment task register |
| Assignment | block, A, D, probability, seed, corpus/model/prompt hashes | Concealed randomization manifest |
| Independent service | analyst_id, start/end, examination, correction, source validation, transfer | Disjoint time ledger |
| Source repair | source_id, old/new version, authority, setup and maintenance, service reserve | Independent source team |
| Work output | first and ordinary-final answer, citations, fallback, escalation | Workflow records |
| Outcome audit | blinded scores, severity, adjudication, audit inclusion probability | Independent gold reference |
| Costs | production, service wage, upstream, compute, fallback, scored loss | One-entry cost ledger |
| Pool outcome | fixed task_count, complete total_Y, frame_frozen | Reconciled total over entire pool |

Use pseudonymous identifiers and partner-approved access and retention. No personal or firm data are included in this package. The ledger reconciliation must show that total labor by person equals the sum of disjoint activities, source maintenance is counted once, and all assigned tasks are represented by completion or fallback. An NPV uses incremental expected net value, actual volumes, startup outlay, maintenance, and discounting without subtracting amortized startup again. No illustrative business case here is a forecast.


## R2 adaptive-information amendment (prospective only)

The completed two-exposure benchmark in manuscript Section 8 is theoretical and synthetic, not a pilot result. A future authorized shadow study should additionally timestamp first independent evidence, the source-version change, correction propagation, each exposure's release and any recipient workflow change after the finding. Record certification service, propagation service and recipient review separately, with shared-pool totals. The full pool remains the assignment unit: adaptive information and endogenous review both transmit interference. A bundled source/structure intervention still cannot identify its components. Learning should be an explicitly randomized timing or propagation option in a separate mechanism study, not controlled away using post-treatment discovery indicators. Audit discarded or unchecked outputs through a separately budgeted outcome-measurement channel. Budget that measurement channel without treating it as free production verification. Access ITT remains the offered-access contrast, while committed workflow contrasts require an assigned workflow or justified separate estimand. No recruitment, data collection, or field intervention has occurred.

## R3 pathwise-capacity amendment (prospective only)

The pathwise results in manuscript Section 9 are exact synthetic/theoretical results, not staffed-service observations. A future authorized design must distinguish an expected pooled budget from a non-borrowable per-batch limit. Record available service before each finding, realized source validation, first checking, conditional propagation and recipient audit, and verify service feasibility for every realized workflow lottery. A realized history cannot borrow unused service from an unrealized one. This is separate from independent outcome measurement, whose audit budget must also be reported. Source finding should not be treated as evidence about independent recipient quality. Pool assignment, source/structure nonidentification, access ITT and the separate committed-workflow estimand remain as specified above. No new study or recruitment is undertaken.


## R5 granularity amendment (prospective only)

A future authorized study would record recipient task sizes, audit indivisibilities and whether workflows/audits can be allocated taskwise while aggregate work is held fixed. A positive timing effect with one indivisible audit must not be interpreted as a fluid capacity effect. Offered-access ITT remains distinct from committed-workflow effects. Measure access-alone gains rather than assume they vanish; Section10 predicts positive access-alone value in its fluid strip. No participants, data collection or new enterprise evidence exist.


## Prospective R6 measurement distinction
No new study was run. Any future protocol must record root capacity procurement as a separate real input from realized reference-service cost and internal scarcity transfers. Observed fixed quotas do not identify endogenous capacity responses. Theoretical procurement choices in Section11 and synthetic validation are not enterprise evidence. Shared-pool interference and the access-ITT versus committed-workflow distinction above remain.


## Prospective R7 supply measurement
No new field work was performed. Any future study must distinguish procurement-tier thresholds/prices from a hard stock ceiling, service wages and internal transfers. Fixed-stock, flat-price and tiered-supply interactions are different estimands. Offered-access ITT, committed-workflow contrasts and shared-pool interference remain distinct. Synthetic witnesses and smoothing diagnostics are not firm evidence.
