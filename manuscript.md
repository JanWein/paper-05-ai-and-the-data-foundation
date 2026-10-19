---
abstract: |
  Knowing that an output is wrong need not identify its reusable source. We solve joint source repair, provenance and optional AI investment under matched error states, physical costs and slack resources. Late attribution improves correction targeting but cannot promote prior repair in the stated region. Early lineage also avoids checks on an already repaired source. These opposing margins yield exact conditions for complementarity and an open region in which lineage activates AI while retaining repair. Dividing exposure into arbitrarily fine tasks leaves the result unchanged, whereas equally cheap prior repair of both sources eliminates strictly optimal lineage-plus-single-repair investment. Marginal accuracy alone does not identify the timing channel. All examples are synthetic.
author:
- Dr. Jan-Hendrik Weinert
date: 19 October 2026
title: AI and the Data Foundation
---

# 1. Introduction {#why-the-timing-of-provenance-matters}

A verifier can establish that a report is wrong without knowing which upstream dataset, spreadsheet or template generated it. That distinction matters when the organization can correct named sources and those sources feed many outputs. A provenance record answers an origin question. It does not certify that the origin is correct. Conversely, a correct/incorrect verdict does not necessarily provide either a source identifier or the corrected contents of every dependent output.

This article studies when making origin information usable before a truth-checking decision changes investment in source quality and AI. The starting economic intuition has two competing parts. After a bad output is found, attribution can prevent replacement of the wrong source. But repairing one source in advance can itself identify the origin of a bad output: the known-safe source could not have caused it. That reduces the targeting value of provenance. In the opposite direction, lineage available before checking can identify outputs from the already repaired source and avoid checking them at all. Prior repair can therefore destroy one value of provenance while creating another.

The main result separates those margins and solves the resulting investment frontier. In a declared primitive region, late attribution and early lineage have the same operating value without prior repair, but different values after repair. Repair and late attribution are substitutes. Repair and early lineage can become complements, with an exact necessary and sufficient condition. We also characterize an open region in which offering AI has no effect without lineage, yet induces AI, lineage and retained source repair when all three choices are available.

This is an information comparison. Every paired provenance institution uses the same sample space, fault realization, output routing and physical action menu. The same repair cell is compared across institutions; repair itself changes error probabilities. The common resource stock is large enough for every plan and is unchanged. None of the new signs is a procurement-tier exposure effect or a scarcity rent. Splitting output exposure into smaller tasks leaves the result exactly unchanged.

The economic scope is deliberately limited. An economical planned repair project targets one specified source. Full-price replacement of either or both sources is also allowed and globally compared. If instead both sources can be repaired in advance at the same low project fee, a simple dominance argument eliminates a strictly optimal combination of provenance and a single prior repair. This repair-coverage boundary is part of the result, not a qualification hidden behind a numerical example.

The contribution candidate is this joint timing/coverage/investment characterization, rather than a new information-ordering or diagnostic principle. Bayesian diagnosis, Blackwell comparisons, metadata complementarity and inspection economics are inherited. The full policy solution and the two impossibility/null boundaries make the claim falsifiable within the model. They do not establish a general theory of provenance or an exhaustive priority claim.

# 2. Primary comparisons and economic scope

Blackwell's comparison of experiments provides the standard reason an organization can ignore additional information and weakly improve its decision value. We credit that principle. Here it supplies only a weak inequality; it does not sign an investment interaction. Our elementary policy-inclusion argument is proved directly. The 1953 publisher record and 1951 bibliographic record were located, but their full texts were not obtained in this round; no newly inspected Blackwell proof is claimed.

Breese and Heckerman's *Decision-Theoretic Troubleshooting* already combines observations, repairs and persistent latent faults. Its Section 2.3, equation (1), prices an observation followed by conditional repair plans; Section 3, equation (2), adds configuration changes and observations. We read these actual passages in the nine-page UAI 1996 manuscript archived as arXiv:1302.3563 in 2013. Diagnostic dynamic programming and the distinction between observation and intervention are inherited. Our model is a small decision-theoretic troubleshooting problem. The result under examination is its exact early/late-lineage and repair-coverage investment boundary, not the invention of adaptive diagnosis.

Koutroumpis, Leiponen and Thomas's *Markets for data* already links data value, metadata and provenance. We read the author-hosted 5 January 2020 manuscript, including the provenance discussion and conclusion, separately from the final journal record. Generic data/metadata complementarity is not new here. Longpre et al.'s March 2024 MIT release 2 motivates structured, attributable provenance and distinguishes its properties from other data assurances. We inspected Sections 1-2, Table 1 and Sections 5-6, not an economic investment theorem. Buneman, Khanna and Tan distinguish why- from where-provenance; their introduction and where-provenance/traceability passages were read in the author-hosted ICDT 2001 manuscript. We do not propose a new provenance semantics. The binary source label below is a minimal economic abstraction, not a database lineage algorithm.

Huang, Xiao and Vishnoi's arXiv v2, dated 25 June 2026, already optimizes AI delegation and verification. Section 8.2 constrains ex ante time/cognitive resources, excluding realized ex post correction from that budget; Section 8.6 permits multiple detection rounds. Those passages were checked in v2. The final proceedings record remains distinguished from that manuscript; no identical final appendix is assumed. Our aligned planner has no worker/institution incentive wedge. Its changed information concerns the identity of a persistent source and whether that identity is available when a paid check is selected.

Inspection and resource-design comparisons remain relevant but secondary. The actual final Tekin-Andradóttir article is available: its given station capacities, admission/inspection/repair controls, Theorems 1-2 and Appendix C already establish bottleneck release and shutdown-enabled activation. Its former full-text gap is resolved. Van Mieghem's 10 November 1997 extended report supplies inherited root capacity investment and recourse; it is distinguished from its abridged 1998 article. Zychlinski-Gurvich's actual final 2026 HTML supplies workload complementarity and capacity-dependent shadow-cost results. Their earlier recorded reading depths are retained in Appendix B. Our slack-stock comparison isolates a different observable-history margin, without inferring novelty merely from different labels.

The Yao-Zheng 1999 abstract and separately verified 2002 Chapter 6 excerpt remain differently scoped. Jang-Shanthikumar's full text remains unavailable. Dogonowski's inspected working-record description, with inaccessible full text, remains an unresolved comparison. Neither inability to read a source nor failure to identify an exact theorem implies absence or priority. Appendix B records actual inspection depth and the bounded result mapping.

# 3. Model: the same physical system under different histories

## 3.1 Sources, exposures and planned repair

There are two named reusable sources. Their original fault indicators $Z_1,Z_2$ are independent Bernoulli variables with probability $p$. A batch is routed to source $J\in\{1,2\}$, independently and uniformly. Each downstream exposure is wrong exactly when its source is faulty. Reuse creates a common persistent error, not independent new errors on each output. If the total loss weight is $W$, unrepaired batch loss is $W Z_J$.

At setup, before $J$ is drawn, the organization may undertake a planned project $r\in\{0,1\}$ for source 1 at all-in fee $F$. It replaces that source with a certified correct version, so

$$\widetilde Z_1=(1-r)Z_1,\qquad \widetilde Z_2=Z_2,\qquad Y=\widetilde Z_J.\tag{1}$$

The project is specific to one source, as when a controlled internal dataset can be improved economically but a second feed has no equivalent project. This restriction is economically material. It does not ban other repairs: full-price prior replacement of source 1, source 2 or both is available at $d$ per source. We study $0\leq F\leq d$. The cheap project is weakly preferred to full-price prior replacement of source 1; symmetry permits exact comparison with source 2. Section 4 proves that full-price extra replacements cannot improve the optimum in the stated region. Section 6 instead makes the cheap project available to both sources and proves the resulting impossibility.

## 3.2 Truth checks and final corrections

Before downstream release, an independent reference channel can check one pilot output from the same batch. A check costs $v$ and reveals the correctness bit $Y$, perfectly. It does not identify $J$, supply a complete replacement dataset, or automatically correct the batch. The reference returns a verdict, not an origin-addressable repair handle. A second identical pilot check reveals the same bit and is redundant.

After the checking decision and any resulting verdict, the organization can replace any subset $Q\subseteq\{1,2\}$ of named sources, at cost $d|Q|$. Replacement uses an independently certified version and recomputes all dependent outputs. Its residual loss is

$$W Y\,1\{J\notin Q\}.\tag{2}$$

These replacements are final batch actions; they do not open another diagnosis cycle. No original-fault status or new routing signal is returned before further decisions. The four subsets include no correction, either single correction and correction of both sources. A blind single-source correction is allowed. Replacing the already repaired source is allowed but wasteful. There is no free physical action called "repair whichever source generated this output": such an action would itself embed an origin-resolution service.

There is one fixed stock $B=6$ of independent service. A check and a full replacement each use one unit; the planned project uses $h=1/10$, already paid within $F$. Even two full prior replacements, a check and two redundant final replacements use at most five units. Every allowed plan is feasible in every positive-probability history, strictly below $B$. All provenance institutions have this same stock and supply schedule. Costs $v,d,F$ are real inputs; no extra service charge or shadow-price transfer is added. The source-information result is unchanged at any stock above five.

## 3.3 Three information institutions

We compare opaque operation $N$, late attribution $D$, and early lineage $E$.

::: longtable
@ \>

p(- 6) \* \>

p(- 6) \* \>

p(- 6) \* \>

p(- 6) \* @

Decision moment

&

Opaque $N$

&

Late $D$

&

Early $E$

\
Setup project and workflow & Same priors; future $J$ unknown & Same & Same\
Select whether to check & No $J$, no $Y$ & No $J$, no $Y$ & $J$ observed, no $Y$\
Final correction, if unchecked & Neither $J$ nor $Y$ & $J$ only & $J$ only\
Final correction, if checked & $Y$ only & $(J,Y)$ & $(J,Y)$\
:::

Late attribution arrives after the check selection window even when no check was ordered. Thus $D$ and $E$ have identical final information, physical actions and costs. They differ only in whether the checking decision can use source identity. A provenance record never reveals an unobserved fault. With $r=1$, knowing $J=1$ certifies safety only because source 1 was independently repaired beforehand.

A policy must be constant on each information set in this table. Randomization can depend on observed history and an independent coin, not on hidden $J$ or an unchecked $Y$. The platform must route and execute named replacements correctly, but its internal mapping is not automatically observable to the decision maker. This is an information-access restriction, not an assumed physical inability to replace a source.

For the matched comparison, couple all institutions on the exact same $(J,Z_1,Z_2)$. Fix the same repair and workflow choices. Potential $Y$, pre-correction error realizations, marginal accuracy, loss weights, physical action feasibility and service costs coincide state by state. Only the information partition changes. Without prior repair the marginal fault probability is $p$; with prior repair it is $p/2$ in every provenance institution. We do not claim repair leaves that marginal unchanged. The matched operating comparison excludes the purchase price of information itself: the same $v,d,F$ and stock are held fixed, while $K$ is added separately when the organization purchases the early foundation. Early-versus-late timing tests use the same installed mapping and its same setup cost. Buying a foundation is not asserted to be cost-neutral.

## 3.4 Optional AI and foundation fees

The no-AI workflow has exposure $W_0$; AI has $W_1>W_0$ and net production/scale benefit $S$. This represents expansion of source-dependent work. AI changes the amount at risk, not the per-output fault probability or the routing distribution. It is optional: $A=0$ is always available. An early-lineage foundation costs $K\geq0$ at setup; its installation makes $J$ usable at the early moment, not before routing exists. The baseline is opaque operation. Late attribution is a matched timing intervention and can alternatively be priced in the same way.

Write $V_r^m(W)$ for minimum operating cost under repair $r$ and information institution $m$, excluding $F,K,S$. The organization minimizes all real costs and residual losses. Both $W_a$ satisfy the declared region when the investment theorems are applied. A positive $S$ is net of the cost of producing additional AI-enabled exposures; no benefit from extra scale is silently omitted. There is no claim of harmful aligned uptake of free access.

# 4. Adaptive policies and information timing

## Theorem 1. All policies and all primitive operating cells

For nonnegative $W,v,d$ and $0\leq p\leq1$, define

$$L(W)=\min\{pW,d,v+p\min(W,d)\}.\tag{3}$$

The globally minimal operating costs are

$$\begin{aligned}
V_0^N&=\min\{pW,2d,v+p\min(W,2d)\},\\
V_0^D&=V_0^E=L(W),\qquad V_1^E=L(W)/2,\\
V_1^N&=\min\{pW/2,d,v+(p/2)\min(W,d)\},\\
V_1^D&=\min\{pW/2,d/2,v+(p/2)\min(W,d)\}.
\end{aligned}\tag{4}$$

Every minimum includes optional zero checking and blind correction. All optimal policies are obtained by taking the minimizing checking/no-checking branch at each observed pre-check node and the minimizing subset at each final observed node. Equality retains every minimizing branch, including independent mixtures. These are global policy minima, not values of imposed audit rules.

For the main investment results impose

$$0<p<1,\quad d>0,\quad 0<v<(1-p)d/2,\quad W\geq2d.\tag{5}$$

Set $x=pW$, $t=v+pd$, $u=v+2pd$, $z=2v+pd$, and $m_c(x)=\min(x,c)$. Then

  Institution     No prior repair   Prior repair of source 1
  ------------- ----------------- --------------------------
  Opaque $N$             $m_u(x)$                 $m_z(x)/2$
  Late $D$               $m_t(x)$                 $m_z(x)/2$
  Early $E$              $m_t(x)$                 $m_t(x)/2$

Opaque checks iff $x>u$ without repair and iff $x>z$ with repair; equality permits checking or no checking. Late checks iff $x>t$ without repair and iff $x>z$ with repair. Early checks iff $x>t$ on each potentially faulty route; after prior repair it never checks route 1. After a bad verdict it corrects the known faulty source under $D,E$ and both possible sources under $N$ without prior repair. After prior repair, a bad opaque verdict itself identifies source 2. At $W=2d$, opaque correction subsets can tie after a bad finding; (4) still describes all global optima.

Under (5) and $F\leq d$, the table also exhausts root replacement alternatives. A full-price replacement of source 2 alone has the same operating value as repairing source 1 but costs $d\geq F$. Replacing both at setup costs at least $F+d$, while the remaining operating optimum after one prior repair costs less than $d/2$. Both-source setup repair is therefore strictly dominated. All other redundant full-price setup actions are also dominated.

## Theorem 2. Opposing provenance values and exact repair promotion

In region (5), put $y=(x-t)_+$ and $b_0=pd$. The operating value of early lineage is

$$G_0=V_0^N-V_0^E=\min(y,b_0),\qquad
G_1=V_1^N-V_1^E=\tfrac12\min(y,v).\tag{6}$$

Late attribution has value $G_0$ without repair and zero with repair. The early-versus-late gain is zero without repair and $G_1$ with repair. Thus early delivery and prior repair are complements even though repair and purchasing provenance need not be.

Let $T_N=V_0^N-V_1^N$ and $T_E=V_0^E-V_1^E$ be repair-fee thresholds at a fixed information institution. Then

$$T_E-T_N=G_1-G_0
=\tfrac12\min(y,v)-\min(y,b_0)=:\mathcal J(x).\tag{7}$$

Prior repair is chosen below the relevant threshold, rejected above it and ties at equality. Hence early lineage strictly promotes repair for some fee precisely when

$$v>2pd\quad\text{and}\quad pW>v+3pd.\tag{8}$$

The actual fee interval is $T_N<F<T_E$. If $\mathcal J<0$, the reverse interval $T_E<F<T_N$ makes lineage discourage repair. Late attribution can never promote repair in (5): its threshold differs from $T_N$ by $-G_0$.

For completeness: $y=0$ gives zero interaction. If $v<2b_0$, the interaction is strictly negative for every $y>0$. If $v=2b_0$, it is negative on $0<y<2b_0$ and zero for $y\geq2b_0$. If $v>2b_0$, it is negative on $0<y<2b_0$, zero at $y=2b_0$, and positive above it. The existence of the complementary region within (5) requires $p<1/5$; it is not a universal effect of provenance.

When exposure is large enough that $x\geq\max(u,z)$, $G_0=pd$ and $G_1=v/2$. The first is a correction-targeting saving destroyed by prior repair's own identification of a bad source. The second is the cost of unnecessary checks avoided when early lineage identifies the already safe route. Equation (8) compares these two endogenous margins, not two savings appended to an objective by assumption.

# 5. Joint foundation investment and optional AI

## Theorem 3. Global fees, adoption and all ties

Fix $W$ in (5), and abbreviate $O=m_u(x)$, $L=m_t(x)$, $R=m_z(x)$. The four early-foundation alternatives $(r,P)=(0,0),(0,1),(1,0),(1,1)$ cost

$$O,\qquad K+L,\qquad F+R/2,\qquad F+K+L/2.\tag{9}$$

Their necessary and sufficient weak optimality conditions are

  Optimal root   Exact conditions
  -------------- ------------------------------------------------
  $(0,0)$        $K\geq O-L$, $F\geq O-R/2$, $F+K\geq O-L/2$
  $(0,1)$        $K\leq O-L$, $F\geq L/2$, $F-K\geq L-R/2$
  $(1,0)$        $F\leq O-R/2$, $K\geq(R-L)/2$, $K-F\geq R/2-L$
  $(1,1)$        $F\leq L/2$, $K\leq(R-L)/2$, $F+K\leq O-L/2$

Strict comparison with all three alternatives gives a unique root. Equality retains every tied root and its operating policies; no arbitrary tie selection is assumed. Let $C_a$ be the minimum of (9) at $W_a$. The global choice over all eight alternatives adopts AI iff

$$S>C_1-C_0,\tag{10}$$

rejects it if the inequality is reversed and retains both workflows at equality. Each workflow's foundation roots are exactly the corresponding table's minimizers. This also covers zero provenance fee and root-fee boundaries. With late instead of early lineage replace the $(1,1)$ operating entry by $R/2$; the same pairwise comparison procedure gives every root choice.

For a fixed repair choice $r$, provenance weakly encourages AI: its reduction in the AI entry threshold is $G_r(W_1)-G_r(W_0)\geq0$. It strictly changes adoption exactly when this difference is positive and $S$ lies strictly between the two corresponding thresholds. This is a conditional statement. Globally, the organization reoptimizes repair and lineage together according to (9)-(10).

## Theorem 4. An exact open region: lineage activates AI and retains repair

Suppose

$$2pd<v<(1-p)d/2,\qquad t<x_0<u<z<x_1,\quad x_a=pW_a,\tag{11}$$

with both $W_a\geq2d$. Consider the strict policy pattern:

1.  Without AI, the globally optimal root is repair without lineage.

2.  For committed AI without lineage, the optimal root abandons repair.

3.  For committed AI with optional lineage, repair and lineage are jointly optimal.

4.  Optional AI is rejected when lineage cannot be purchased, but adopted with repair and lineage when it can.

This entire pattern holds if and only if

$$\frac{3pd}{2}<F<\frac t2,\tag{12}$$

$$\frac{x_0-t}{2}<K<u-F-\frac t2,\tag{13}$$

$$K-\frac{x_0-t}{2}<S<u-F-\frac{x_0}{2}.\tag{14}$$

These are nonempty strict open inequalities. All weak boundaries are obtained from Theorem 3; at a binding comparison the corresponding policies tie, rather than retaining the strict pattern. The conclusion does not require a change in marginal source accuracy, repair technology or capacity between provenance institutions.

**Exact synthetic instance.** Let

$$\begin{gathered}
p=1/10,\quad d=1,\quad v=3/10,\quad W_0=9/2,\quad W_1=8,\\
F=9/50,\quad K=21/200,\quad S=9/100.
\end{gathered}\tag{15}$$

Then $(t,u,z)=(2/5,1/2,7/10)$. All eight total costs, including AI benefit, are

::: longtable
@ \>

p(- 8) \* \>p(- 8) \* \>p(- 8) \* \>p(- 8) \* \>p(- 8) \* @

Workflow

&

Neither foundation

&

Lineage only

&

Repair only

&

Repair and lineage

\
No AI & $90/200$ & $101/200$ & $81/200$ & $97/200$\
AI & $82/200$ & $83/200$ & $88/200$ & $79/200$\
:::

The unique global optimum is AI with repair and early lineage. Prohibiting lineage makes no-AI with repair optimal at $81/200$; free AI access is then unused. The gain from enabling the missing foundation choice is $1/100$. This is a model calculation, not an observed firm effect.

At $W_0$, repair and early lineage are substitutes: $G_0=1/20$, $G_1=1/40$, so $\mathcal J=-1/40$. At $W_1$, $G_0=1/10$, $G_1=3/20$, so $\mathcal J=1/20$. The sign reverses because the opaque repaired workflow's checking threshold is crossed, not because a paid label itself changes a fault.

# 6. Robustness, a coverage impossibility and disappearing effects

## Theorem 5. No task-quantization explanation; a sharp repair-coverage limit

Divide $W$ into any finite collection of positive loss weights $w_i$ summing to $W$, or a nonatomic mass of exposures with that total weight. All use the same batch source. For every state and feasible policy, residual loss remains $Y1\{J\notin Q\}\sum_iw_i$. Hence all operating costs, fee boundaries and the open result in Theorem 4 are exactly unchanged. There is no $1/n$ rounding premium. The independent check remains a source-fault diagnostic, not a count of independently correctable tasks.

For independent replicated batches with the same per-batch project and lineage fees, the optimum average cost is also unchanged. A policy may condition on other batches' independent outcomes, but those supply no information about this batch's faults or routing. Randomization cannot improve its conditional minimum. This does not claim invariance when one fixed infrastructure fee is amortized across infinitely many batches; that would change $K$ per batch and is a different investment comparison.

Now change repair coverage: allow both sources to be repaired at setup for $F$ each, while retaining the same information institutions. With early lineage, the one-repair root costs $F+K+L/2$. No repair with lineage costs $K+L$, and repairing both without lineage costs $2F$. For every $F,K\geq0$,

$$\min\{K+L,2F\}\leq F+K+L/2.\tag{16}$$

The inequality is strict for at least one alternative whenever $K>0$; for $K=0$ equality of all relevant comparisons can occur at $F=L/2$. Thus a strictly optimal early-lineage-plus-single-repair investment is impossible under symmetric cheap complete repair. This null holds separately for each workflow, so adding optional AI does not rescue that root. It is a coverage boundary of Theorem 4, not a claim that all provenance value vanishes in the enlarged model.

Other nulls are informative. If $x\leq t$ in (5), every provenance operating gain is zero and positive-fee lineage is dominated. Late attribution never generates the positive repair interaction in Theorem 2. If routing is already observable to the opaque controller, its information sets coincide with early lineage and the incremental label value is zero. At $p=0$, $W=0$ or $d=0$, the general solution (4) gives zero gain from purchasing provenance. The limits rely on their stated information/technology changes, not on assuming the same error rate across different repair choices.

The low-check-cost restriction in (5) is also substantive. Outside it, late attribution can promote repair through selective blind replacement rather than skipped checks. For example, $p=1/10,d=1,v=7/10,W=20$ gives $(V_0^N,V_0^D,V_1^N,V_1^D)=(9/10,4/5,3/4,1/2)$ from (4). Its late repair interaction is $3/20>0$. This counterexample rules out an unrestricted claim that early delivery is always necessary; Theorem 2's late-promotion null is confined to (5).

# 7. Identification, falsification and a prospective protocol

A matched-marginal comparison is not a mechanism test. Fix $r,A$ and couple all regimes on the same raw states. Before endogenous correction, every output and every potential pilot verdict have exactly the same distribution. Therefore marginal accuracy, output volume, source-independent test accuracy and physical stock cannot identify whether lineage was available before or after the checking decision. A regression of error rates on a broad data-maturity index has no identified interpretation in this model.

Even counts of checks can fail. In a saturated unrepaired cell $x>\max(u,t)$, opaque, late and early institutions all check every batch. Both attribution institutions can nevertheless save corrections by identifying the faulty origin. In a repaired cell $x>\max(z,t)$, opaque and late check all batches, while early checks only the half routed to the unrepaired source. Identifying this filtering margin requires the joint record of prior repair status, actual origin, lineage release time and checking decision, not a new estimate of standalone AI accuracy.

A prospective mechanism experiment would freeze routing, source versions, fault distribution, repair actions, verdict technology, exposure weights and resource availability. Independently randomize whether the same truthful mapping is displayed before or after a locked check/no-check decision. Late display must occur even when a check was skipped. Root repair availability or assignment must be varied independently if the repair interaction is to be identified. Analyse each fixed repair cell first, then the randomized root-choice environment separately. Potential defects can be injected only in a consented sandbox; no such study was conducted here.

The decisive records are: source identifier and version; whether that source was certified by prior repair; release timestamps; pilot verdict if checked; named source replacements; and independent downstream correctness measurement on a reserved evaluation channel. Under the strict region, early lineage should reduce checks on the known-safe route after repair while late attribution should improve targeting only before prior repair. Observing no such conditional differences, or observing that an opaque checker routinely receives a free origin-resolution handle, falsifies the proposed mechanism or its information restriction.

The measured intervention is offered lineage timing, an intention-to-treat effect. Conditioning on voluntary checking, actual AI use or realized lineage lookup does not identify that offer's causal effect. A committed-workflow interaction is a different estimand. Bundling lineage, source cleaning and structural corpus changes cannot identify their separate mechanisms. With a genuinely shared constrained audit pool, interference reappears; this paper's slack, batch-separable test should not be replaced silently by individual assignment within such a pool. The separate prospective appendix specifies these distinctions and reports no real outcomes.

# 8. Conclusion {#limitations-and-conclusion}

The model assumes a reliable source map, a truthful binary pilot diagnostic, persistent batch faults, final named-source replacement and a specific economical repair project. It is not a model of arbitrary hallucinations, noisy provenance, continuous source blending or unrestricted sequential source tests. A verdict returning the complete corrected source, or an anonymous repair action that resolves origin automatically, changes the technology and must be modeled rather than called the same intervention. Repair ownership/coverage is especially consequential: Theorem 5 shows that cheap complete prior repair invalidates the joint-foundation pattern. Finer tasks do not invalidate it; broader cheap repair does.

The economic lesson is correspondingly specific. Attribution after diagnosis and lineage before diagnosis need not support the same quality investment. Early lineage can make prior repair operationally useful by avoiding unnecessary truth checks, while late attribution's targeting value is partly replaced by repair itself. The exact threshold compares these margins and delivers an open joint AI/foundation choice region with matched latent histories and slack physical resources. The timing and coverage nulls distinguish this statement from "more information helps" and from the earlier procurement-exposure calculation.

Generic diagnostic optimization and metadata complementarity remain inherited. The result is a solved application-specific investment boundary, whose economic importance depends on whether organizations actually face the modeled information and repair-access restrictions. No field effect or general optimal verification system is established. Complete proofs follow; the exact earlier resource results are preserved as a secondary technical companion rather than used as evidence for an informational contribution.

# References {#references .unnumbered}

Blackwell, David. 1951. "Comparison of Experiments." *Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability*,93-102. Primary record: <https://digicoll.lib.berkeley.edu/record/112749>. Full text not obtained in this round.

Blackwell, David. 1953. "Equivalent Comparisons of Experiments." *Annals of Mathematical Statistics* 24(2):265-272. DOI 10.1214/aoms/1177729032. Publisher record inspected; proof not newly read.

Breese, John S., and David Heckerman. 1996. *Decision-Theoretic Troubleshooting: A Framework for Repair and Experiment*. UAI manuscript, nine pages, archived 2013 as arXiv:1302.3563. [Inspected manuscript](https://arxiv.org/pdf/1302.3563). Archival upload date is not the research date.

Buneman, Peter, Sanjeev Khanna, and Wang-Chiew Tan. 2001. "Why and Where: A Characterization of Data Provenance." *Database Theory, ICDT 2001*,316-330. DOI 10.1007/3-540-44503-X_20. [Inspected author manuscript](https://homepages.inf.ed.ac.uk/opb/papers/ICDT2001.pdf).

Dogonowski, Robert. 2026. "Verified Output and the Microeconomics of AI Adoption: Why AI Productivity Depends on Verification, Not Generation Alone." SSRN working paper 6701098, 3 May, revised 10 June. DOI 10.2139/ssrn.6701098. Primary indexed description inspected; full text inaccessible.

Huang, Lingxiao, Wenyang Xiao, and Nisheeth K. Vishnoi. 2026. "Delegation and Verification under AI." Final record: *Proceedings of ICML*, PMLR 306:48039-48071. Actual model comparison: [arXiv v2](https://arxiv.org/html/2603.02961v2), 25 June 2026. Final appendix equivalence not assumed.

Jang, Wooseung, and J. George Shanthikumar. 2002. "Stochastic Allocation of Inspection Capacity to Competitive Processes." *Naval Research Logistics* 49(1):78-94. DOI 10.1002/nav.1049. Abstract/metadata inspected; full text unavailable.

Koutroumpis, Pantelis, Aija Leiponen, and Llewellyn D. W. Thomas. 2020. "Markets for data." *Industrial and Corporate Change* 29(3):645-660. DOI 10.1093/icc/dtaa002. Actual text inspected: [author-hosted manuscript](https://www.oxfordmartin.ox.ac.uk/downloads/academic/Data-Marketplaces_ICC-ACC.pdf), 5 January 2020, 34 pages. Final record distinguished from inspected manuscript.

Longpre, Shayne, Robert Mahari, Naana Obeng-Marnu, William Brannon, Tobin South, Jad Kabbara, and Sandy Pentland. 2024. "Data Authenticity, Consent, and Provenance for AI Are All Broken: What Will It Take to Fix Them?" *An MIT Exploration of Generative AI*, 27 March, release 2. DOI 10.21428/e4baedd9.a650f77d. [Inspected release](https://mit-genai.pubpub.org/pub/uk7op8zs/release/2).

Tekin, Salih, and Sigrún Andradóttir. 2020 (published online 7 January 2019). "Inspection location in capacity-constrained lines." *Central European Journal of Operations Research* 28(3):905-937. DOI 10.1007/s10100-018-00604-x. User-supplied final publisher PDF, 33 pages; retained own and central reading scopes distinguished in Appendix B. Not identified with the 2011 thesis.

Van Mieghem, Jan A. 1997. *Investment Strategies for Flexible Resources*. Extended technical report, 10 November, 25 pages. [Author-hosted report](https://www.kellogg.northwestern.edu/faculty/vanmieghem/htm/flextec0.pdf). Title identifies abridged *Management Science* 44(8):1071-1078,1998, DOI 10.1287/mnsc.44.8.1071. Version equivalence not assumed.

Yao, David D., and Shaohui Zheng. 1999. "Sequential Inspection Under Capacity Constraints." *Operations Research* 47(3):410-421. DOI 10.1287/opre.47.3.410. Publisher abstract inspected; detailed theorem text not obtained.

Yao, David D., and Shaohui Zheng. 2002. "Sequential Inspection Under Capacity Constraints." Chapter 6 in *Dynamic Control of Quality in Production-Inventory Systems*, 89-107. DOI 10.1007/0-387-22779-2_6. Printed 89-90 excerpt centrally verified; later theorem/proof pages not inspected. Separate from 1999 article.

Zychlinski, Noa, and Itai Gurvich. 2026. "The Production of Service: A Workload View of Complementarity and Substitution." *Stochastic Systems* 16(2):165-185. DOI 10.1287/stsy.2025.0111. [Actual final HTML](https://pubsonline.informs.org/doi/full/10.1287/stsy.2025.0111), retained reading scope in Appendix B; Online Appendix proofs not inspected.

# Appendix A. Complete proofs

## A.1 Proof of Theorem 1 and completeness of information-feasible policies

Condition on a setup repair choice. The sample space has the eight states $(J,Z_1,Z_2)$ with their product probabilities; states with zero probability can be omitted. The potential verdict is (1). At each pre-check information set the only diagnostic choice is checking or not checking. At every resulting final information set the physical choice is one of four subsets $Q$. Selecting these actions independently at all positive-probability information sets enumerates every deterministic policy of the model. A randomized policy is a mixture of those finite deterministic contingent plans, with the same per-history stock feasibility. Its expected cost is linear in the mixture and cannot fall below the smallest deterministic expected cost. This is standard finite Bayesian decision logic; the claim here is its exact solution for the declared partitions.

Without prior repair and without provenance, an unchecked batch is faulty with probability $p$ and comes from either source with probability one half, independently. Correcting no source, a specified single source or both therefore costs $pW$, $d+pW/2$, or $2d$. The single-source value is the arithmetic mean of the other two and cannot strictly improve their minimum. After a bad check, the posterior origin probabilities are still one half each: both sources have the same prior, so the verdict alone supplies no origin discrimination. Conditional costs are $W$, $d+W/2$ and $2d$, whose minimum is $\min(W,2d)$. A clean verdict needs no correction. Adding checking cost gives $v+p\min(W,2d)$ and proves the first line of (4), including its terminal ties.

With the origin known, a single-source batch has no-check cost $\min(pW,d)$; after a bad verdict its correction cost is $\min(W,d)$. A clean verdict needs no action. Thus the minimum is $L(W)$. Before prior repair the two origins have identical conditional distributions. Allowing the checking decision to use $J$ cannot lower the average below the identical minimum in each origin, and not knowing $J$ until the final decision can attain the same minimum. This proves $V_0^D=V_0^E=L(W)$, without assuming a compulsory audit.

After prior repair, route 1 is safe and route 2 retains fault probability $p$. Early lineage allows the controller to do nothing on route 1 and use the preceding one-source optimum on route 2, giving $L(W)/2$. Without origin information, no checking leaves expected loss $pW/2$ or costs $d$ to replace source 2; replacing only source 1 is useless and replacing both is dominated. A bad check now reveals $J=2$, because $\widetilde Z_1=0$. Hence the checking branch costs $v+(p/2)\min(W,d)$. This proves $V_1^N$. Late lineage does not change the checking branch but allows a no-check correction to be ordered only on route 2, with average cost $d/2$ rather than $d$. This proves $V_1^D$. Every alternative has been compared, including blind correction and no checking. The formula also covers free checks, free corrections and deterministic faults as weak limits with their respective ties.

Under (5), $W\geq2d$ makes the bad-verdict correction minima $d$ or $2d$. Also $v+pd<d$, $v+2pd<2d$, and $v+pd/2<d/2$. Therefore all unconditional replacement branches in (4) are dominated by a checking branch, though not necessarily by no checking. Comparing the remaining branches gives the table and every checking threshold. Conditional correction choices follow from their just-derived posterior costs. If $W=2d$, the opaque bad-verdict branches tie, but checking then costs more than $pW$ since $v>0$; the formula still correctly includes all reachable optimal histories.

For root completeness, full-price repair of exactly source 2 has the same post-repair problem as exactly source 1 by a relabeling of the uniform routing and equal fault priors. Its fee is at least the planned source-1 fee $F$. Repair of both costs at least $F+d$, whereas each one-repair operating value is at most $v+pd/2<d/2$ in $N,D$ and at most $L(W)/2<d/2$ in $E$. A second full-price root repair is therefore strictly wasteful. Replacing source 1 at full price is weakly dominated by its project; redundant repetitions only add cost. These comparisons hold within each fixed provenance cell and workflow. At $F=d$, the two equivalent single-source full-price roots may tie; they can be included without changing any value. Every physical plan has load at most five and fits $B=6$. Thus no omitted root alternative or history-level infeasibility supports the result.

## A.2 Proof of Theorem 2 and all sign boundaries

For $c_2\geq c_1$, the elementary capped-cost identity is

$$m_{c_2}(x)-m_{c_1}(x)=\min\{(x-c_1)_+,c_2-c_1\}.\tag{17}$$

Subtract the early cells in Theorem 1 from the opaque cells and use $u-t=pd$, $z-t=v$. This gives (6). Late equals early without repair but opaque after repair, so the two timing assertions follow. These identities are consequences of optimized policy branches, not savings added to the primitive cost function.

A repair project changes optimized operating cost from $V_0^m$ to $V_1^m$ and adds $F$. Comparing these proves the fee thresholds. Their difference under early and opaque information is

$$(V_0^E-V_1^E)-(V_0^N-V_1^N)=G_1-G_0,$$

which is (7). If $y=0$ the interaction vanishes. For $0<y\leq\min(v,b_0)$ it equals $-y/2$. If $v<2b_0$, then for $y$ below $b_0$ either the first term has already capped at $v/2<y$ or it is $y/2<y$; for $y\geq b_0$ it is at most $v/2-b_0<0$. If $v=2b_0$, it stays negative until $y=2b_0$ and then equals zero. If $v>2b_0$, it equals $y/2-b_0$ on $b_0<y<v$, crosses zero only at $2b_0$, and remains positive once capped at $v/2-b_0$. These arguments establish every strict/weak/null case in the theorem.

Consequently positivity is equivalent to $v>2pd$ and $y>2pd$, or $pW>v+3pd$. The complementary interval lies below $T_E=L/2<d/2$, so its fees are compatible with $F\leq d$. Negative-interaction intervals are interpreted within the declared fee domain. For late information the repair-threshold difference is $V_0^D-V_0^N=-G_0\leq0$, proving its promotion impossibility. The inequalities $2pd<v<(1-p)d/2$ have a solution exactly when $p<1/5$. Finally, when both caps bind, (6) gives the explicit $pd$ versus $v/2$ decomposition.

## A.3 Proof of Theorem 3 and global root comparisons

Substitute the operating table into the sum of project fee, provenance fee and operating cost. This gives (9). Comparing each of its four entries with the other three gives the displayed inequalities. For example, root $(1,1)$ beats $(0,1)$ iff $F\leq L/2$, beats $(1,0)$ iff $K\leq(R-L)/2$, and beats $(0,0)$ iff $F+K\leq O-L/2$. The other rows follow by the same three explicit pairwise comparisons; no comparison is dropped. Equality means both corresponding expected costs are identical and both are feasible. A strict smaller entry uniquely minimizes root costs, irrespective of irrelevant prescriptions at zero-probability histories. Independent mixtures of tied roots cannot lower their common value.

Source replacements other than the planned project are already globally dominated or tied as in A.1. Comparing the minimum costs in the two workflows after subtracting AI's real benefit gives (10), including all adoption ties. Since the no-AI alternative remains available, optional free access weakly lowers optimized cost. It cannot harm aligned optimized welfare.

For a fixed $r$, define the AI entry threshold as $V_r^m(W_1)-V_r^m(W_0)$, excluding the common foundation fees. Subtracting the early threshold from the opaque threshold gives $G_r(W_1)-G_r(W_0)$. Equation (6) shows that both $G_r$ are nondecreasing in $W$, proving the conditional complementarity and its exact strict interval. This claim does not hold investments fixed when using (10); there all roots are recomputed. For late information its operating table supplies the same exhaustive pairwise procedure, rather than an assumed sign for the global investment optimum.

## A.4 Proof of Theorem 4, nonemptiness and openness

In (11), the four manual operating entries are $(x_0,t,x_0/2,t/2)$ and the AI entries are $(u,t,z/2,t/2)$. Committed opaque AI abandons repair exactly when

$$F>u-z/2=3pd/2.$$

Committed AI's repair-plus-lineage root beats lineage alone exactly when $F<t/2$, and beats neither foundation exactly when $K<u-F-t/2$. Given $F>3pd/2$, this upper bound is strictly below $(z-t)/2=v/2$, so it also beats repair alone. Manual repair alone beats repair-plus-lineage exactly when $K>(x_0-t)/2$. With $F<t/2<x_0/2$, it beats neither foundation. Moreover $F+x_0/2<t+(x_0-t)/2<t+K$, so it also beats lineage alone. These comparisons prove necessity and sufficiency of (12)-(13) for the stated committed-workflow pattern; the conditions not separately listed are implied, not omitted.

The no-lineage manual optimum is $F+x_0/2$, and the no-lineage AI optimum is $u-S$. Rejecting AI requires the strict upper bound in (14). With lineage available the AI optimum is $F+K+t/2-S$ and the manual optimum remains $F+x_0/2$. Selecting AI gives the strict lower bound in (14). Thus all eight root alternatives have been globally compared, proving the if-and-only-if claim.

Nonemptiness is analytic. Equation (11) has solutions because $2pd<v$ gives $t<u<z$ and permits $p<1/5$. Choose any $x_0\in(t,u)$ and $x_1>z$, with $W_a=x_a/p\geq2d$. Choose $F\in(3pd/2,t/2)$, whose width is $(v-2pd)/2>0$. The provenance-fee interval in (13) has width $u-F-x_0/2>u-t/2-u/2=pd/2>0$. After choosing $K$ inside it, the AI-benefit interval has width $u-F-K-t/2>0$, and its lower endpoint is positive. Every inequality is continuous and strict, so the region is open in the declared primitive vector, not an isolated witness. Substitution of (15) gives the eight rational costs and the two signed interactions reported in Section 5.

The strict root comparisons also persist under sufficiently small asymmetric perturbations of the two fault priors and the routing probability. There are finitely many contingent policies; their expected costs are continuous in these priors and in the real costs. A minimum over finitely many continuous functions is continuous. Positive gaps between the specified root choices therefore survive a neighborhood of the symmetric instance. We do not claim the same closed-form frontier outside the symmetric region.

## A.5 Proof of Theorem 5 and the coverage counterexample

For any partition of exposure, each component has the same $Y$ and is recomputed when its named source is replaced. Summing the realized losses gives exactly (2), state by state. Check and replacement actions do not depend on the number of output fragments. The policy set and every objective are therefore unchanged, with no limiting approximation. Integration proves the same equality for a nonatomic exposure measure. This isolates the result from indivisible recipient-audit quantization.

For independent replicated batches, condition on every external history available when this batch's policy is selected. Those histories are independent of its $(J,Z_1,Z_2)$. They can only select a random information-feasible policy, whose conditional expected cost is no smaller than this batch's minimum. Summing proves the lower bound; running an optimal per-batch policy attains it. A common fixed fee would alter the per-batch primitive and is not covered by this statement.

For the symmetric cheap-repair extension, if $F<L/2$, then $2F<F+L/2\leq F+K+L/2$. If $F>L/2$, then $K+L<F+K+L/2$. At $F=L/2$, both-source repair costs $L$, while the single-repair-plus-lineage root costs $L+K$. This proves (16), its strict qualifications and its workflow-by-workflow implication. In particular, applying this extension to (15) would select both prior repairs at cost $2F=9/25$, or $27/100$ net of AI benefit, instead of the reported single-project/lineage root. The extension invalidates that positive pattern; it has not been concealed by excluding a competing action from the same institution.

If $x\leq t$, all three caps in Theorem 1 equal $x$, so both provenance gains vanish. Coincident information partitions give identical policy sets and operating values. The cases $p=0$, $W=0$ and $d=0$ follow directly from (4). Late repair promotion is excluded by A.2. These establish the disappearing-effect boundaries.

## A.6 Matching, observation and testable restrictions

On a fixed repair/workflow cell, the distribution of $(J,Z_1,Z_2)$ does not involve the provenance regime. Formula (1) is therefore the same potential verdict in every paired state. Before endogenous corrections, $\Pr(Y=1)=p$ if $r=0$ and $p/2$ if $r=1$. The physical source subsets, reference technology and stock $B$ are also unchanged. Only pre-check and final information differ. Policy inclusion from $N$ to $E$ is obtained by ignoring $J$; from $D$ to $E$, choose the checking decision independently of $J$ and use the same final rule. This proves the generic weak value-of-information inequality without attributing it as a new theorem.

Any statistic of potential output correctness, exposure mass and physical stock alone has the same law under the coupled provenance regimes in a fixed cell. It cannot identify which information was displayed. This is a nonidentification statement for those measurements, not for every possible observed outcome. Checks and final correctness are endogenous and may differ. Under saturated optima Theorem 1 gives the stated audit propensities directly: one for both origins without repair, one for opaque/late with repair, and zero on the repaired route plus one on the other route with early lineage. Both provenance institutions have the same final $(J,Y)$ when checked, so randomized release before versus after a locked check decision isolates the checking-allocation margin. Randomized repair assignment or availability identifies its interaction; observational repair selection alone does not. These are prospective implications of the finite experiment, not claims of collected evidence.

# Appendix B. Result-level contribution and primary-source ledger

The claims below distinguish actual reading from retained previous reading and from inaccessible text. This is a bounded comparison, not priority certification or scientific acceptance. Two internal critical passes are documented separately; independent central assessment is still required.

::: longtable
@ \>

p(- 2) \* \>

p(- 2) \* @

Source/result

&

Actual inspection depth and mapping

\
Blackwell (1951,1953) & Primary bibliographic/publisher records located; full texts not obtained in this round. Generic information ordering is inherited. A.6 proves the elementary policy-inclusion inequality used here; no new Blackwell theorem.\
Breese-Heckerman & Actual nine-page 1996 manuscript archived as arXiv:1302.3563 in 2013; Sections 1-3, especially 2.3(1),3(2), and Section4 discussion inspected. Persistent faults, observation costs, conditional repairs and experimental configuration changes are inherited. Equations(3)-(4) are a small exact decision problem in that tradition.\
Koutroumpis-Leiponen-Thomas & Actual author-hosted 34-page manuscript dated 5 January 2020: introduction, Section2 provenance/metadata discussion and conclusion inspected. Journal record 29(3):645-660 verified separately. General data/metadata complementarity is inherited; final-version equivalence not assumed.\
Longpre et al. & Actual MIT 27 March 2024 release 2: Sections 1-2, Table 1,5-6 inspected. Source-lineage and structured documentation motivation inherited; not a solved repair/adoption theorem or our enterprise evidence.\
Buneman-Khanna-Tan & Author-hosted 15-page ICDT 2001 text: introduction and where-provenance/traceability discussion, Definition 9/Propositions 1-2 inspected. Origin tracking is inherited; the binary label model is not a new provenance semantics.\
Huang-Xiao-Vishnoi & arXiv v2 dated 25 June 2026, Sections 8.2/8.6 actually checked again. Ex ante resource constraint and repeated detection already present. Proceedings record is separate; final appendix equivalence not asserted. No new general delegation/verification claim.\
Tekin-Andradóttir FINAL & User-supplied 33-page final publisher PDF is available. Retained own reading: Sections 2-5/Theorems 1-2/(20)-(32), Appendix C(40)-(50); central review read the entire article. Given-capacity long-run inspection/repair and shutdown activation inherited. The final full-text gap is RESOLVED; no article redistribution or thesis equivalence.\
Van Mieghem & Retained actual 1997 extended report, Sections 1-5 through Proposition 7 and Appendix A Proposition 5 proof,(1)-(21),(48)-(49); not all appendices/numerical pages. Root investment/recourse/substitution inherited. Abridged 1998 article not assumed identical.\
Zychlinski-Gurvich FINAL & Retained actual 2026 final HTML Sections 3-4/Theorem 1/(2)-(12),5.2/Theorem 3/Lemma 3. Workload complementarity and capacity shadows inherited. Full Online Appendix/proofs not inspected; failed earlierPDF not equated with final.\
Yao/Jang/Dogonowski & Yao-Zheng 1999 publisher abstract only; distinct 2002 Chapter 6 printed 89-90 centrally verified, with(6.1) expected inspections upper bound AND defects-removed lower bound. Jang-Shanthikumar 2002 primary abstract/metadata only. Dogonowski SSRN 6701098 working record 3 May, revised 10 June 2026; primary description inspected, full text inaccessible. Neither absence nor exact overlap is inferred.\
:::

The result-specific ledger is as follows.

::: longtable
@ \>

p(- 2) \* \>

p(- 2) \* @

Present result

&

Increment being tested and inherited boundary

\
Theorem1,(3)-(5),A.1 & Full state/information-set solution, including blind corrections and late no-check attribution. Generic Bayesian optimization is inherited.\
Theorem2,(6)-(8),A.2 & Exact opposing targeting/filtering margins; necessary/sufficient repair-promotion condition; late-attribution promotion null. Blackwell alone does not sign these differences, but the diagnostic machinery remains standard.\
Theorems3-4,(9)-(15),A.3-A.4 & Global repair/provenance/AI regions and an exact open entry/retained-repair pattern against all root alternatives in the declared targeted-programme institution. The four-cost minimum itself is not the claimed increment.\
Theorem5,(16),A.5 & Exact exposure-divisibility invariance and impossibility of strict single-repair/lineage co-investment when both sources have symmetric cheap prior repair. The positive result explicitly requires its repair-coverage restriction.\
A.6 and Section7 & Matched potential histories and a pre-/post-check release experiment separate information from marginal accuracy and resource supply. The protocol is prospective; no empirical identification is claimed.\
:::

The complete joint timing/coverage frontier has not been established as an exact predecessor identity by the inspected passages. This is not proof of absence or substantial originality. The strongest remaining objection is that it may be a useful worked specialization of decision-theoretic troubleshooting rather than a sufficiently important new economic result. That judgment cannot be resolved by larger operation counts or stronger wording.

# Appendix C. Secondary resource theory and exact prior preservation

The separate technical companion retains the complete earlier 52-page article, all fifteen propositions and their proofs, source qualifications and runnable calculations. Its original mathematical results are not rewritten as false. Their role is now secondary: they analyze other declared institutions in which source attribution was available, and do not establish the present information mechanism.

::: longtable
@ \>

p(- 2) \* \>

p(- 2) \* @

Companion results

&

Retained scope and limitation

\
Propositions1-4 & Expected-capacity KKT allocation, capacity-release decomposition, demand ordering and optional adoption. Standard constrained optimization is inherited.\
Proposition5 & Open-loop reusable-source scale accounting, not an adaptive attribution theorem.\
Proposition6 & Adaptive two-exposure expected-resource benchmark and slack/resource-equivalence nulls. Corrected538=4+392+20+122 checks retained;100 candidates,98 accepted,two feasibility skips,not failures.\
Propositions7-8 & Every-history one-recipient capacity regions and matched-mean-resource comparison under indivisible auditing.588 prior frontier checks retained.\
Propositions9-10 & Positive timing advantage can be a quantization effect; fluid recipient costs and fixed-budget repair/access frontier. Finite-task checks retained.\
Propositions11-12 & Linear root procurement gives weak substitution in the specified fluid model.\
Propositions13-15 & Tiered/smooth supply sign frontier at fixed hard stocks. Its interaction reduces to $1/4+C(3)-C(5/2)-C(21/10)+C(11/10)$ on the stated slope strip, not an independent-recipient information premium.\
:::

Exact archived R7/R6/R5/R4 packages and the unchanged R7 companion are included. Every preexisting scientific script and result file remains available and unchanged; the launcher adds only the new information checks. The new main text restarts theorem numbering and supplies every proof of its own results, rather than appending another proposition to the old review sequence.

# Appendix D. Reproducible synthetic analysis

The standalone standard-library verifier enumerates all deterministic checking decisions on actual pre-check information sets and all four correction subsets on actual final information sets. It sums costs over the eight raw source/routing states and independently compares conditional minimization and the analytic formulas. It explicitly rejects policies using hidden origin, origin-dependent late checking or unaudited faults. Statewise coupling checks hold repair and workflow fixed across provenance institutions.

The targeted set covers switch/tie/null points, selected outside-region cases, all eight root alternatives, fee/adoption boundaries and exact exposure partitioning. A second independent script imports no model or first-verifier code; it recomputes every root source mask and checks small asymmetric prior/routing perturbations. Operation counts and full raw witnesses are recorded in the executable package, not interpreted as empirical sample sizes. All retained resource/estimator suites run separately and their old result files remain byte-identical. The continuum claims follow from Appendix A, not from the number of checks.
