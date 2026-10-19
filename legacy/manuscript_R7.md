---
title: 'AI and the Data Foundation'
subtitle: 'Source Repair, Independent Verification, and Capacity Supply'
author: 'Research manuscript prepared for Dr. Jan-Hendrik Weinert'
date: '18 October 2026, central-review revision R7'
geometry: margin=1in
fontsize: 11pt
colorlinks: true
---

**Evidence status.** Completed theoretical analysis with explicitly synthetic numerical validation. No firm observations, field experiment, or causal estimate. The prospective empirical module is a separate document.

# Abstract

Data repair and AI adoption can interact through a shared independent verification resource, even when the recipient department does not use the repaired source. We solve allocation and optional investment under expected and every-history capacity, then test the investment sign against recipient divisibility and capacity procurement. A positive matched-mean timing advantage can be an audit-quantization effect; its fluid limit is nonpositive. With a fixed stock, fluid repair/access complementarity can remain. Linear root procurement instead yields weak substitution. Holding the same information and action menu fixed, a two-tier supply curve produces an exact sign frontier: a higher expensive-tier price can restore complementarity while all optimal hard stocks remain unchanged. Complete source-policy dominance, expected occupation mixtures, capacity and fee ties are proved, including an additional endpoint interval at the maximum marginal price. The sign is differential exposure to procurement tiers and pooling costs, not information about the independent recipient. Strict complementarity and the repair choice persist under smooth strictly convex supply and a nondegenerate primitive neighborhood. All computational examples are synthetic; the field protocol is prospective. General inspection economics, workload complementarity, procurement/recourse, convexification, envelopes and stability tools are inherited. The supplied final inspection article and current service-design results sharpen attribution. This specialized supply-mediated frontier is not by itself evidence of a substantial original contribution, empirical validity or scientific acceptance.

# 1. The economic problem

The relevant bottleneck in a reporting workflow can be an independent expert who can establish whether an amount, definition, or source is correct. Generating another draft does not enlarge that expert's capacity. A source repair undertaken by one department can therefore have benefits outside its own outputs: it can release independent checking time for other work. The question is when that spillover changes the joint investment decision rather than simply producing a familiar statement that cleaner data help AI.

We study an institution choosing among finite workflow and source-validation alternatives before a reporting batch. Output checking and correction use an explicit common resource. All objectives in the main model are aligned. AI remains optional, and its production savings are compared with the globally reoptimized verification cost, not an inspection penalty added at an assumed fixed effort. The repair decision and, in an extension, the number of source-dependent tasks are endogenous.

The initial expected-capacity result concerns two classes with different interventions. Class 1 reuses a source that can be repaired. Class 2 can adopt an AI workflow but does not use that source. When the AI workflow has higher demand for independent reference service at relevant resource prices, repair in class 1 lowers the extra verification burden of AI in class 2. The original formulations contain regions where the institution rejects both investments separately but chooses both jointly. In the finite two-exposure benchmark, this includes a single indivisible recipient audit. Section 10 tests that audit technology under atomization and shows why its joint-only description is not robust: access alone then has positive value in the stated fluid region. This does not change the other propositions under their own verification technologies. This is cross-department complementarity in economic value, not a same-task accuracy result. In the isolated cross-department comparison the interaction is zero. With a common pool it can become positive, and a sharper allocation-share result shows when the repaired department's own measured interaction is negative despite that positive system interaction. These are economic account comparisons under explicit institutions, not universal properties of task technology.

A second, explicitly open-loop result concerns reuse. A one-time improvement to a source's marginal error probability benefits every exposure and releases checking capacity. Under a general inverse-resource technology, the gross value of repair increases with the number of exposures. If an AI capability improvement operates only through cheaper drafting, the institution expands task scale and can cross a source-repair threshold. An improvement that also changes error rates or checkability need not have this monotonic effect.

An additional adaptive benchmark allows source discovery and correction propagation between two exposures. Its finite contingent-policy solution retains an untouched recipient and a common reference pool. It proves that the investment interaction can survive information reuse, while a slack-capacity null shows why it need not. It does not extend the open-loop linear reuse accounting to adaptive settings. A pathwise counterpart then characterizes the investment frontier and proves that equal expected certification resources need not imply equivalent feasible histories for an untouched recipient. That result survives global optimization within the one-recipient action set. The positive adaptive advantage in that comparison does not survive fluid recipient divisibility: Section 10 bounds the positive matched-mean advantage by $\beta/n$ and derives its nonpositive fluid limit. A different result, the institution-dependent repair threshold with access, persists under the fluid technology, with positive access-alone gains.

Sections 11-12 test the procurement boundary. A tiered supply curve can restore a positive repair/access interaction even with unchanged optimal stocks; smooth supply and primitive perturbations preserve a strict region. Thus no universal investment sign follows from the data-foundation framing. Section 11 adds flat-price root capacity procurement and overturns any general inference that AI encourages source repair: the fixed-stock positive interaction becomes weak substitution, strictly negative on a proved open region. The fixed-stock institutional gap is exactly a capped recipient pooling penalty, not an additional information premium.

The contribution boundary is result-specific: inherited constrained-inspection methods solve the fixed policy problem, while the proposed additional economic characterization is the globally compared certification/recipient investment frontier and its granularity-qualified matched-mean timing boundary. Section 2 and Appendix B map this distinction to actual reading depth, including the centrally verified two-page Yao-Zheng chapter excerpt and directly read bounded-verification model. A missing full text is not evidence of novelty.

The earlier version's exponential optimizer and linear factorial decomposition are no longer the principal contribution. They are superseded by the joint constrained problem. The article provides complete analytic conditions and a finite algorithm; synthetic computations verify the algorithm against a separately coded constrained optimizer. No empirical research was conducted.

# 2. Relation to primary literature and contribution boundary

## 2.1 Inspection institutions and actual reading depth

Huang, Xiao, and Vishnoi (2026), arXiv v2 of June 25, is the nearest AI delegation theory. Its Section 8.2 restricts an individual worker's ex ante time/cognitive resources and excludes realized ex post correction from that budget. Section 8.6 already studies multiple verification rounds. Our adaptive margin is transfer of independently discovered source information across exposures, changing a separate recipient's service opportunity. The ICML proceedings record was verified separately; its PDF was inaccessible. The comparisons refer to v2, not an assumed identical final appendix.

Yao and Zheng (1999) is a direct predecessor. The publisher abstract reports constrained Markov inspection, threshold policies, LP construction and randomization at no more than two thresholds. Its PDF request redirected to the abstract. No later theorem text was read or shown absent. Their distinct 2002 book, Chapter 6, is now also relevant: the publisher identifies pp. 89-107. For printed pp. 89-90, central review supplied a verified excerpt scope, including equations (6.1)-(6.4). Our ordinary preview request failed, so the equation-level comparison below relies explicitly on that central verification, not an independent visual reading. No later chapter theorem or proof was inspected. The book chapter and 1999 article are separate sources; their equivalence is not assumed.

The centrally verified chapter equation (6.1) imposes $E[I^\pi]\leq u$ and $E[D^\pi]\geq\ell_{YZ}$, where the second inequality is a lower bound on defects removed. The subscript avoids confusing that bound with our source-service quantity $\ell=1+q\gamma$. Equations (6.2)-(6.4) provide the expected-cost objective and the inspection/defect-count state. This is actual model-level evidence for expected inspection constraints, not merely a thematic abstract comparison. It does not establish the contents of uninspected pages.

Our expected constraint (22) is the weighted-service analogue $E[Q^\pi]\leq B$. It includes checking, propagation and recipient auditing, with durations $1,\gamma,t_a$; inspection count and service time are not identical units. We impose no independent lower bound on expected defects removed. Instead, for an unrepaired fixed source policy, let $D_s$ count wrong source exposures corrected before release. Its expected source loss is $2qL_s-L_s E[D_s]$. Rewarding removals this way has the familiar form of a Lagrangian penalty for a lower removal target; it is not a new inspection objective or a proof that the two constrained feasible sets coincide. Prior validation changes the source before production, rather than merely sampling more outputs.

A state recording production stage, source finding, service used, and the root repair/access choices embeds each fixed cell of Section 8 in a finite constrained Markov program. Its expected cost and service criterion are standard occupancy-measure objects. The hard version instead forbids histories exceeding $B$; this feasible-set distinction is also inherited. Those mappings directly credit the generic formulation, LP/randomization and finite minimization. They do not by themselves establish an original economic theorem. All of these actions can be represented within generic constrained control; extra state labels alone establish no contribution. The original bounded regions (36)-(41) must now be assessed alongside their granularity test (43)-(56). Global source-policy dominance and the surviving fluid investment comparison, rather than generic formulation or enumeration, are the result-specific content; substantive originality remains unresolved.

Jang and Shanthikumar (2002) studies independent production processes sharing inspection, with partially observed dynamic control. Its primary abstract and metadata were inspected; the full text remains unavailable, so no detailed theorem non-overlap is certified. Naor (1969), inspected in the original article, establishes private/social congestion and toll logic. Our common multiplier is inherited scarcity pricing, not a new toll theorem. Bimpikis and Markakis (2019, online 2018), inspected at publisher-description level, jointly treats learning and service resources. Information and capacity joint choice is not claimed new.

## 2.2 Bounded AI verification, versions, and evidence

Bańka and Chudziak (2026), arXiv:2610.05547v1, submitted October 4, Section 3, was read directly. It samples $b$ of $n$ claims without replacement: the bad-pass probability is $\binom{n-f}{b}/\binom{n}{b}$ and posterior reliability is $p/[p+(1-p)q]$. Proposition 1 concerns evidentiary dilution; Section 3.3 inverts a posterior target into a verification budget. Those Bayesian and sampling results are not claimed here. Their object is a finite claim sample, whereas our action repairs a shared source and changes feasible service for an independent recipient. Their benchmark-label experiments are not enterprise evidence for this paper.

Dogonowski (2026), *Verified Output and the Microeconomics of AI Adoption*, remains a working-record comparison. The primary indexed SSRN record is dated May 3 and revised June 10. Its description already credits scarce verification and a reliability shadow price. Its full text was inaccessible. This establishes neither overlap nor absence of the narrower source-certification results; it leaves priority unresolved. The additional readable sources do not close that comparison.

Organizational evidence answers different questions. Brynjolfsson, Li, and Raymond (2025) studies a support-assistant rollout. Büchsenschuss et al. (2026), in the inspected INSEAD working version, randomizes grounded-assistant access and studies knowledge networks. Sagynbayeva et al. (2026), inspected at institutional-record level, describes a RAG-by-complexity experiment; publisher full text remains inaccessible. None of these inspected designs identifies our source intervention and reference-pool spillover. Chen et al. (2024) separates technical RAG failure modes. Brynjolfsson, Rock, and Syverson (2021) motivates intangible-investment accounting. Neither technical benchmarks nor these field studies supply empirical validation of our propositions.

## 2.3 The bounded result under review

The final contribution candidate is the exact joint source-repair/access frontier under alternative audit and capacity-supply institutions. Propositions 7-8 solve the indivisible-recipient case; Proposition 9 identifies its quantization boundary. Proposition 10 gives the fluid fixed-stock frontier, Proposition 12 its flat-price procurement boundary, and Proposition 14 the tiered-supply sign frontier. Proposition 15 removes a kink-only interpretation. These nested comparisons do not support a universal claim that AI encourages data repair, nor an independent-recipient information premium.

The constrained-control formulation, inspection optimization, shared capacity, downstream capacity release, joint-only activation, convexification, procurement/recourse and general capacity-dependent complementarity are inherited. The increment being assessed is a specialized, globally solved joint investment comparison, including all source alternatives and ties. Different labels, an unmatched numerical example or unsuccessful access do not establish substantive originality. The actual final inspection article is now accessible; remaining precise predecessor limitations are retained without priority inferences.

## 2.4 Granularity, stochastic knapsack, and an inherited activation mechanism

Dean, Goemans, and Vondrák (2008) is available as a 20-page final author-hosted PDF, distinct from an extended abstract. We read the introduction, Figure 1 and outline through printed p. 947. Its items have independent random sizes; a final overflow ends insertion and earns no value for the overflowing item. Its nonadaptive comparator fixes an insertion order. This is not our comparison between matched-mean prior validation and source-contingent residual budgets that must never overflow. We credit generic adaptivity/knapsack ideas, without claiming equivalence or absence of later theorems not read.

Tekin's 2011 thesis, Chapter IV, supplied an earlier centrally verified comparison: inspection can release downstream capacity. The central review reports a complete-chapter comparison and a synthetic witness with raw profits $(-82,-35/2,-18,2)$. If production shutdown at value zero is optional, these become $(0,0,0,2)$. Thus joint-only profitable inspection activation is already obtainable in that prior institution; it is not our originality claim. The thesis title is *Efficient System Design: Stability and Flexibility*. Its earlier failed request is historical, not a current final-article access limitation. The user-supplied final Tekin-Andradóttir article, *Inspection location in capacity-constrained lines*, DOI 10.1007/s10100-018-00604-x, is now available. We inspected actual model/result text in Sections 2-5 (Theorems 1-2, (20)-(32)) and Appendix C (40)-(50); the central comparison reports complete 33-page reading. Given station capacities, admission control and inspection/repair determine long-run flows. Theorem 1 balances operation/inspection stations; Theorem 2 gives maximal throughput with adequate repair capacity. Equations (45)-(48), with shutdown in (40)-(44), directly support the synthetic raw-profit/shutdown comparison above. This final-article gap is resolved. It supplies inherited bottleneck release and joint-only activation, including defect-contingent repair. Its long-run flow institution is not an every-batch hard stock guarantee. No direct mapping to the whole root repair/access/supply frontier is established, nor is originality established by that fact. Thesis/final-article equivalence is unnecessary and is not assumed.

The added boundary test in Section 10 stays within our source institution and varies only recipient granularity. Its Jensen/rounding and lower-convex-envelope tools are inherited. Proposition 9 shows that the positive matched-mean timing advantage in Proposition 8 can be an indivisible-audit effect and is nonpositive in the fluid limit. Proposition 10 separates that disappearing effect from a surviving repair/access threshold comparison. Access alone is then valuable: the robust statement is conditional complementarity, not joint-only activation. This narrows, rather than upgrades, the originality claim. The available comparisons still do not establish that this bounded investment region is a substantive original mechanism beyond the closest inspection theory.

## 2.5 Capacity procurement and the actual primary comparison

Van Mieghem's author-hosted *Investment Strategies for Flexible Resources* is an extended technical report dated 10 November 1997, whose title identifies an abridged 1998 Management Science article. Actual text was inspected in Sections 1-5 through Proposition 7 and Appendix A's Proposition 5 proof, equations (48)-(49); not all appendices or numerical pages, and no equivalence to the final abridged version, are asserted. Its equations (1)-(6) specify recourse production subject to dedicated/shared capacities, (7) linear root investment cost and (8) expected operating profit less investment. Proposition 1 uses expected marginal capacity values; Propositions 3 and 5 map substitution and distribution sensitivity, while 6-7 treat extreme dependence. These establish that procurement, recourse and substitution are inherited. Our Section 11 adds the explicit two-history common-source repair comparison and optional recipient access, rather than claiming a new general investment principle. That bounded calculation does not certify substantive originality. No failed-source retrieval loop is used.

## 2.6 Current service-design result and the remaining boundary

Zychlinski-Gurvich's final 2026 HTML was inspected in Sections 3-4, Theorem 1, (2)-(12), and Section 5.2, Theorem 3/Lemma 3. Brownian quality and CES effort determine rework workloads. Theorem 1 characterizes their convex attainable set; (10) constrains station loads, and Theorem 3 changes relative costs by capacity shadow prices. Lemma 3 makes the complementarity effect capacity-regime dependent. General workload complementarity and shadow pricing are inherited. Our comparison instead changes real root supply cost for one common stock and compares optional source repair/access, including expected occupation mixtures. This specific frontier is not automatically a substantive increment. The full Online Appendix/proofs were not reviewed; a failed earlier PDF is not the final article.

# 3. Technology, information, and timing

## 3.1 Task classes and a genuinely independent resource

There are $J\geq2$ task classes. Class $i$ has mass $n_i>0$, initial draft-error probability $p_i\in[0,1]$, loss $L_i>0$ per undetected error, and production cost $c_i$ per task. A workflow choice can change these primitives. An error means a wrong economically relevant output, including an omission, assessed against an authoritative independent reference. Data availability, factual reliability, semantic consistency, and retrieval are not defined by observed success. They determine $p_i$ and checkability as separate engineering primitives.

Verification is not a second call to the generator or a reread of the same unreliable source. It requires an independent reference analyst, access to an authoritative ledger, independent recomputation, or an equivalent source of truth. Only this service reduces residual error from $p_i$ to $v_i\leq p_i$. The required expected capacity per task is

$$T_i(p_i,v_i)=b_i(p_i)-b_i(v_i). \tag{1}$$

Assume $b_i$ is strictly increasing and strictly concave, twice continuously differentiable on $(0,1]$ with $b_i''<0$, and with $b_i'(0+)=\infty$. Its derivative can depend on task class and workflow. This difference form is a substantive restriction; not every detection technology has it. It permits a broader result than an exponential miss curve. At $p_i=0$, choose no verification and set $T_i=0$ by convention. At $v_i=0$, use the limit, possibly infinite.

A useful special case explicitly includes correction time:

$$b_i(x)=\lambda_i^{-1}\log x+\tau_i x,\quad
T_i=\lambda_i^{-1}\log(p_i/v_i)+\tau_i(p_i-v_i). \tag{2}$$

The first term is independent reference-examination time. Equivalently, $v_i=p_i\exp(-\lambda_i e_i)$ after $e_i$ examination units. The second term is the expected correction time of that same scarce service: each detected error needs $\tau_i\geq0$ units to correct. Successful correction is assumed perfect once the independent evidence is obtained. Correction time is not assumed free or outside capacity. Positive false alarms and imperfect correction require extensions discussed below.

The organization has $B\geq0$ service units for the batch. A source-repair choice $d\in\{0,1\}$ can reserve $h d$ units before output checking, leaving $B_d=B-hd\geq0$. Its monetary cost $Fd$ includes the actual wage cost $kh$ of that validation, other setup, and maintenance attributed to this batch. The same independent service costs $k>0$ per unit when used on outputs. No shadow-price transfer is charged as an additional resource cost.

## 3.2 Reusable sources and the batch restriction

The institution first chooses source validation/repair and a workflow for each class. It then produces a frozen batch and allocates independent reference work before observing the error realizations. Source validation can replace an uncertain definition or record with a validated version; it lowers the ex ante error probability on all relevant exposures, from $p_H$ to $p_L<p_H$. Full repair $p_L=0$ is permitted and handled separately from logarithmic expressions.

One interpretation is a shared source-fault indicator with probability $q$ and task-specific interpretation failures. An exposure's marginal draft-error probability can be $p=q+(1-q)u$, where $u$ is the interpretation error conditional on a sound source. A one-time validation lowers $q$. All results use marginal error probabilities and expected additive losses. Common-source correlation is compatible with this accounting but does not create the expected-value benefit by itself. Increasing the number of exposures does. Holding marginals and losses fixed, changing only correlation does not change our objective. We derive no tail-risk, variance, or chance-constraint result.

The batch institution is deliberately open loop: reference checks produce task-specific corrections within the window; source-version changes and propagation require a prior validation step. No within-window adaptive discovery and free global source correction is allowed. This could represent a designed shadow batch with parallel checks and a frozen source version. It is an assumption, not a statement about an existing firm's practice. If a first checked output reveals the common fault and permits immediate correction of all other outputs, repeated independent checking is wasteful and the present program overstates its necessity. Section 8 separately solves a two-exposure adaptive policy and shows both survival and null regions. Propositions 1-5 do not cover that alternative technology or general dynamic learning.

The common capacity constraint is an expected batch workload constraint. It can represent divisible service over many batches or a fluid planning budget. It does not guarantee that stochastic realized correction time never exceeds staffing in a particular batch. A hard almost-sure deadline cannot be justified from these KKT equations alone. Section 9 separately imposes a pathwise bound on the finite two-exposure technology; it does not extend the KKT program to a stochastic queue.

## 3.3 Organizational problem and optional AI

For fixed workflows and $d$, remove their production constants and solve

$$V(\mathbf p,\mathbf n,B_d)=\min_{0\leq v_i\leq p_i}
 \sum_i n_i\{kT_i(p_i,v_i)+L_i v_i\},
\quad \sum_i n_iT_i(p_i,v_i)\leq B_d. \tag{3}$$

Total monetary cost is $C=Fd+\sum_i n_i c_i+V$. The institution minimizes $C$ over all feasible finite workflow/repair choices. AI is one alternative, never a requirement when access is offered. An access intervention expands the feasible set; with aligned objectives and no fee for unused access, optimized cost cannot rise.

For two classes we study source repair in class 1 and optional AI in class 2. Write $V_a(p,B)$ for (3), where $p$ is class 1's initial error and $a$ specifies class 2's manual or AI technology. Production savings from choosing the AI workflow are $S$ for the whole class, net of compute and integration costs attributable to adoption. They do not enter the interaction proof. Define

$$H(p,B)=V_1(p,B)-V_0(p,B). \tag{4}$$

AI is selected if $S\geq H$. This comparison reoptimizes every class's verification. It is not a private worker comparing only drafting minutes.

# 4. Optimal verification and capacity spillovers

## Proposition 1. Unique conditional allocation

Define the initial marginal loss reduction per reference unit

$$m_i(p_i)=L_i/b_i'(p_i),\quad m_i(0)=0.$$

For a resource price $w\geq k$, let

$$v_i(w)=\begin{cases}
p_i,& w\geq m_i(p_i),\\
(b_i')^{-1}(L_i/w),& w<m_i(p_i),
\end{cases}
\quad z_i(w)=b_i(p_i)-b_i(v_i(w)). \tag{5}$$

Let $Q(w)=\sum_i n_i z_i(w)$. If $Q(k)\leq B_d$, the optimum has $w=k$ and unused capacity is allowed. Otherwise, for $B_d>0$, the unique price solving $Q(w)=B_d$ gives the unique optimal residual risks and allocation. The capacity multiplier is $\eta=w-k$. If $B_d=0$, all examination and correction loads are zero and $v_i=p_i$; a valid multiplier has $w\geq\max_i m_i$. Zero-effort classes are included, not extrapolated through an interior formula.

For (2), the interior residual and load are

$$v_i(w)=\frac{w}{\lambda_i(L_i-\tau_i w)},\quad
z_i=\lambda_i^{-1}\log(p_i/v_i)+\tau_i(p_i-v_i), \tag{6}$$

used only when $w<m_i=L_i\lambda_i p_i/(1+\tau_i\lambda_i p_i)$. Otherwise $z_i=0$. Thus a nonpositive denominator never enters the interior expression. The familiar exponential inspection formula appears only as this conditional special case.

*Proof.* Given in Appendix A.1, including existence, sufficiency, boundaries, and the multiplier at zero capacity.

## Proposition 2. Repair releases capacity and improves other tasks

Fix workflows, $B_d>0$, and a binding region with a constant active set. Suppose class 1 is actively checked. Let $Q_w<0$ denote aggregate demand slope. Then

$$\frac{dw}{dp_1}=-\frac{n_1 b_1'(p_1)}{Q_w}>0. \tag{7}$$

Every other actively checked class has $dv_j/dw>0$. Consequently reducing class 1 error lowers $w$, increases class $j$'s allocation, and lowers its residual errors even though its source, model, initial error probability, and production are unchanged. An unchecked class can enter checking when the price falls through its activation threshold. If the repaired class was unchecked and stays unchecked, its source improvement does not release service capacity locally. If all relevant capacity is slack, the cross-class spillover is zero.

The envelope derivative of total optimized cost is

$$V_{p_1}=n_1 M_{1p}(p_1,w),\qquad
M_{1p}=\min\{L_1,w b_1'(p_1)\}. \tag{8}$$

This derivative counts direct and allocation effects correctly. It is not a second charge for the multiplier. To separate actual class accounts, let $C_i=n_i(kz_i+L_i v_i)$. In a binding active region,

$$\frac{dC_1}{dp_1}=n_1k b_1'(p_1)-\eta n_1 z_{1w}w_{p_1},
\qquad
\frac{dC_j}{dp_1}=-\eta n_j z_{jw}w_{p_1}\geq0\quad(j\ne1). \tag{9}$$

The first expression is the repaired class's own benefit; the second is the recipient spillover. They sum to (8). At the optimum, lowering error may save little final error loss within class 1 at a fixed service price but free valuable examination and correction capacity for others. The spillover is an outcome change on other tasks, not simply the shadow price assigned an economic label.

*Proof.* Appendix A.2. The equations require a smooth active set; integrated value comparisons remain valid at entry/exit corners.

# 5. A cross-department repair-and-adoption result

## Proposition 3. Demand ordering determines the investment interaction

Let class 2's reference demands under its AI and manual workflows be $z_{2,1}(w)$ and $z_{2,0}(w)$. Suppose throughout an interval containing the optimal prices for $p\in[p_L,p_H]$,

$$z_{2,1}(w)\geq z_{2,0}(w). \tag{10}$$

At the same $p,B$, the optimal prices obey $w_1\geq w_0$. Thus $H(p,B)$ is nondecreasing in $p$ and

$$H(p_H,B)-H(p_L,B)
=n_1\int_{p_L}^{p_H}\!
 [M_{1p}(p,w_1)-M_{1p}(p,w_0)]\,dp\geq0. \tag{11}$$

Strict inequality holds when a positive-length subset has $w_1>w_0$ and class 1 is active under the lower price (hence (8) strictly increases until saturation). Source repair then lowers the AI adoption threshold in another class. The result does not require exponential detection, equal losses, a proportional repair, or an additive structure benefit. If (10) is reversed on the relevant range, the price and threshold comparisons reverse. Scarcity alone does not imply complementarity.

For positive source-service reservation $h$, define $H_H=H(p_H,B)$ and $H_L=H(p_L,B-h)$. The exact net threshold reduction is

$$H_H-H_L=[H(p_H,B)-H(p_L,B)]
 -\int_{B-h}^{B}[\eta_1(p_L,b)-\eta_0(p_L,b)]\,db. \tag{12}$$

The source improvement must outweigh its own pressure on the independent channel. This is an endogenous opportunity-cost qualification, not a structural interaction imposed in production costs.

*Proof.* Appendix A.3. We state conditions rather than asserting demand order from the word AI. A faster generator can require either more or less independent service.

### A primitive sufficient test in the log-correction case

Suppose class 2 has common $L,\tau$ across workflows and $a_1=1/\lambda_{2,1}>a_0=1/\lambda_{2,0}$. While both alternatives are active,

$$\frac{d}{dw}(z_{2,1}-z_{2,0})
=-\frac{(a_1-a_0)L^2}{w(L-\tau w)^2}<0. \tag{13}$$

Choose an upper price $\bar w>k$ below all activation thresholds over the source range. If $z_{2,1}(\bar w)\geq z_{2,0}(\bar w)$ and

$$Q_1(p_H,\bar w)\leq B<Q_0(p_L,k), \tag{14}$$

both workflow problems have binding prices in $[k,\bar w]$, and (10) follows on that range. This is a check on primitives and capacity, not an assumption that the sign of the desired interaction is positive. With $h>0$, evaluate (12) or strengthen (14) for all $b\in[B-h,B]$ and bound the reservation penalty. Equal technologies, slack capacity, or an unchecked repaired class eliminate the strict cross-class mechanism.

### Corollary 3.1. Own-department substitution and system complementarity

Suppose two classes are active throughout the repair interval, have common $L,\tau$, and use (2). Let $a_i=1/\lambda_i$ and

$$\theta_a=\frac{n_1 a_1}{n_1 a_1+n_2 a_{2,a}},$$

the repaired class's share of the pool's marginal response to price. If, throughout $[p_L,p_H]$,

$$0<\eta_0<\eta_1,\qquad
\theta_1\eta_1<\theta_0\eta_0, \tag{15}$$

then source repair has a smaller benefit in class 1's own cost account under AI in class 2, but a larger benefit in total system cost. The recipient class's larger gain more than offsets that own-account substitution. These are consequences of optimal capacity reallocation, without an assumed additive interaction term.

For $\tau=0$, $w_a(p)$ is explicitly

$$w_a(p)=\exp\left[\frac{n_1a_1\log(pL/a_1)+n_2a_{2,a}\log(p_{2,a}L/a_{2,a})-B}
{n_1a_1+n_2a_{2,a}}\right]. \tag{16}$$

If $a_{2,1}>a_{2,0}$ and the demand-order conditions give $w_1>w_0>k$ throughout, $\eta_1/\eta_0$ decreases with $p$. Thus checking $\eta_1(p_L)/\eta_0(p_L)<\theta_0/\theta_1$ is a sufficient endpoint test for the own-account reversal over the whole interval. This is a parameter condition using the solved prices. Strict conditions continue to hold for sufficiently small positive correction load $\tau$ by continuity.

*Proof.* Appendix A.3b. The result is about the repaired class's actual resource-and-loss account. It is not a claim that two technologies have negative technical interaction when considered in isolation.

## Proposition 4. Optional access and globally joint investment

For $d\in\{0,1\}$ let $B_d=B-hd$, $p_d=p_H$ or $p_L$, and

$$G_d=[S-H(p_d,B_d)]_+.$$

Under aligned optional access, the access gain at data state $d$ is exactly $G_d$, and its factorial interaction is $G_1-G_0$. In particular, when $H_L<H_H$, access and repair have nonnegative interaction. There is no negative access gain from a rational free option.

Let $R_0=V_0(p_H,B)-V_0(p_L,B-h)$. The following strict conditions are sufficient for neither investment to pay alone while their combination is the unique optimal binary configuration:

$$H_L<S<H_H,\qquad R_0<F<R_0+S-H_L. \tag{17}$$

All four workflow/repair costs must be compared. Within the availability regimes, unused AI is permitted. The fixed repair cost and source-capacity reservation are included in those comparisons.

*Proof.* Appendix A.4. This is an adoption-and-repair result, not an accounting identity with an exogenous sign. Its benefit can arise entirely outside the AI task's information set. It does not prove a general technology cross-partial, and nonlinear transformations of economic value need not preserve the finite interaction.

# 6. Reuse, repeated checking, and easier drafting

## Proposition 5. When one-time repair beats repeated output checks (open loop)

Hold workflows and $B$ fixed; let class 1 have $n$ exposures to a reusable source. First suppose the source repair is completed before this period's pool is committed, so $h=0$ but all upstream monetary cost remains in $F$. Define

$$R(n)=V(p_H,n,B)-V(p_L,n,B).$$

For $p_H>p_L>0$, the gross value has the representation

$$R(n)=n\int_{p_L}^{p_H}\min\{L_1,w(n,p)b_1'(p)\}\,dp. \tag{18}$$

It is increasing in $n$. In particular, with

$$r_{iso}=\int_{p_L}^{p_H}\min\{L_1,kb_1'(p)\}\,dp>0,$$

we have

$$n r_{iso}\leq R(n)\leq nL_1(p_H-p_L). \tag{19}$$

Source repair dominates optimally allocated repeated checking exactly when $F\leq R(n)$. Reuse therefore produces a one-crossing repair threshold, without assuming that uncorrected errors are independent. With same-period validation load $h>0$, the exact threshold becomes

$$F\leq R(n)-\int_{B-h}^{B}\eta(p_L,n,b)\,db. \tag{20}$$

The second term is the displaced output-verification benefit. It excludes the actual wage $kh$, already included in $F$. We do not assert monotonicity of the net expression in (20) without additional conditions, although the lost-capacity penalty is bounded by $h\max_i m_i$ for fixed technologies and source probabilities.

For a pure drafting-cost improvement, allow the institution to select $n$ from a finite set including zero and maximize

$$U(n)-c n-V(p_d,n,B)-Fd. \tag{21}$$

With $h=0$, a decrease in $c$ weakly increases the largest optimal task scale; because repair is selected at a threshold in $n$, it weakly increases the largest optimal repair choice. Thus easier AI drafting can make source repair worthwhile through endogenous reuse, even if it does not improve source truth or checking technology. Changes to $p_i,b_i,L_i$, or the timing of repair can overturn this statement.

*Proof.* Appendix A.5. The theorem distinguishes exposure count from dependence. If a repair merely decorrelates errors and leaves every marginal $p_i$ unchanged, (3) values it at zero unless another primitive changes. The model is explicitly risk neutral with additive losses.

## General finite-choice solution

For each feasible repair state and vector of workflow alternatives, solve Proposition 1 and add production, validation, setup, compute, and maintenance costs. Choose the lowest total. For finite scale, repeat over the finite task counts. This enumeration is globally correct because each conditional residual-allocation problem is convex and all discrete alternatives are covered. A KKT solution from only one adoption regime is not a global solution. The code independently solves every numerical alternative as well as the selected optimum.

# 7. Completed synthetic results and numerical checks

All examples use invented primitives to verify logic, not calibrated magnitudes. In the main batch, class 1 contains two exposures to one source, with $p_H=0.5$, $p_L=0.1$, $\lambda_1=1$, $L_1=100$, and $\tau_1=0.5$. Class 2 contains one task: manual $(p,\lambda)=(0.2,1)$ or AI $(0.3,0.25)$, with $L_2=100$ and $\tau_2=0.5$. Each manual task costs 20 to produce; AI saves $S=14$ on class 2. Total reference budget is $B=7$, service price $k=1$, source reservation $h=0.1$, and all-in repair cost $F=10$. The AI workflow here is faster but less accurate and harder to check; its optional adoption is the result to be explained, not presumed.

\newpage

| Committed workflow and repair | Total cost | Capacity multiplier | Class 1 residual | Class 2 residual |
|:--|--:|--:|--:|--:|
| Manual, unrepaired | 79.814 | 3.182 | 0.0427 | 0.0427 |
| AI, unrepaired | 81.697 | 3.671 | 0.0478 | 0.1913 |
| Manual, repaired | 80.924 | 0.332 | 0.0134 | 0.0134 |
| AI, repaired | 79.032 | 1.653 | 0.0269 | 0.1075 |

A separate exact-price example verifies Corollary 3.1: retain $n_1=2$, $B=7$, $k=1$, $L=100$ and the two class-2 technologies, set $\tau=0$, $h=0$, and repair class 1 from 0.5 to 0.3. The endpoint ratio is 1.7565, below $\theta_0/\theta_1=2$, and both classes remain active. Class 1's repair benefit falls from 2.4027 to 2.0575 under AI, but total repair benefit rises from 3.0933 to 4.1293. Thus the own-account interaction is -0.3452 and the system interaction is +1.0360. Strictness guarantees a positive-correction neighborhood; the main example separately includes positive correction and validation load.

The CSV contains full precision, allocated examination/correction loads, own-class costs, and independent-optimizer comparisons. The unrounded thresholds are $H_H=15.8832$, $H_L=12.1079$, and $R_0=8.8900$. Thus $12.1079<14<15.8832$ and $8.8900<10<10.7821$, satisfying (17). The source and AI investment are each rejected alone, but their joint adoption reduces cost by 0.7821 relative to baseline. AI access without repair is unused; with repair it is used. This avoids the earlier draft's positive interaction with negative conditional opt-in gains.

| Access intervention | Repair intervention | AI actually selected | Optimized total cost |
|:--|:--|:--|--:|
| No | No | No | 79.814 |
| Yes | No | No | 79.814 |
| No | Yes | No | 80.924 |
| Yes | Yes | Yes | 79.032 |

The access interaction on negative total cost is 1.8921. Data repair's own conditional effect can still be negative after its fixed cost; it is not free. No uncertainty interval is attached to deterministic expected-cost examples.

Holding class 2's workflow fixed, class 1 repair improves both classes' accounts. The program separately records those own and recipient savings. When baseline verification quotas are frozen and cannot be reassigned, class 1's local repair benefit is smaller than $F$, and it declines the investment. Central reallocation makes the joint package valuable. This comparison concerns two explicit institutions, not irrational free opt-in.

The sufficient demand-order test in (14) holds for the no-reservation benchmark with $\bar w=4.8$; positive $h$ is then evaluated by the exact comparison (12). A capacity grid provides boundary examples. With very tight capacity the demand order can reverse and the committed-workflow interaction is negative; with sufficiently large capacity the cross-department interaction is zero. These are counterexamples to an unconditional scarcity-complementarity claim. A separate example with AI raw error 0.15 instead of 0.30 also exhibits positive interaction at some capacities, showing that the mechanism does not require AI to be less accurate. Such parameter examples support existence only.

The reuse calculations and finite-scale optimization use (18) and (21). For the latter, $U(n)=35n-1.5n^2$, $n\in\{0,\ldots,12\}$, $F=10$, $B=7$, $h=0$, and class 2 is manual. At drafting cost 22, the optimum uses one source exposure and does not repair; at cost 20 it uses three and repairs. This is a synthetic illustration of the proved cost-only comparative static, not evidence on real AI-induced task creation.

The executable code validates 480 conditional allocation problems across every discrete alternative in 40 heterogeneous cases, using both log-correction and square-root inverse-resource technologies. A separately coded SLSQP primal optimizer minimizes cost subject to the actual residual-risk capacity constraint from three starts; it does not use the KKT price solution. Maximum objective discrepancy in the executed run was $9.7\times10^{-11}$ or less. There were 425 binding cases, 55 slack cases, and 290 class-level zero-effort cases. Explicit tests include zero capacity, zero initial error, shadow-price and source-value envelope derivatives, finite-choice cost comparisons, and a slack regime. These checks establish computational consistency, not empirical validity or priority.

# 8. A solved adaptive source-discovery benchmark

## 8.1 Timing, actions, and exhaustive contingent plans

This is a separate technology, not a reinterpretation of (1). A source department produces two sequential exposures to one binary fault $Z\sim\mathrm{Bernoulli}(q)$, $0<q<1$. There is no idiosyncratic error in this benchmark. Each released wrong exposure causes loss $L_s>0$. Without prior repair, an independent first check consumes one service unit, costs $k>0$, reveals $Z$ perfectly, and corrects the first exposure before release. After discovering a fault, the organization may leave the second exposure unchanged, propagate the evidenced correction for $\gamma$ service units, or independently check and correct it for one unit, where $0<\gamma<1$. Monetary service cost is $k$ per unit. The initial unit bundles examination and first-output correction; propagation costs $k\gamma$ and is not another generation from the faulty source. A clean finding makes a second source check useless.

If the first exposure is unchecked, it is released before the second check and its loss cannot be reversed. Checking the second reveals the same fault and corrects only that exposure. A direct independent source validation before production is the alternative $d=1$: it guarantees both exposures are correct, uses $h\geq0$ common service units and costs $F\geq kh$ all in. The repair decision is made before $Z$. Redundant checks or propagation without independent evidence are not available useful actions. These timing rules define the benchmark's action space; a cheaper pre-release source-certification option would need to be added and compared explicitly.

An untouched recipient has one task whose errors are unrelated to $Z$. It can choose manual $M$ or, with access $A=1$, AI. Production costs are $c$ and $c-S$. Unaudited expected losses are $D_M,D_A>0$. An independent audit perfectly corrects the task, using $t_M,t_A>0$ service units and costing $kt_M,kt_A$. Thus each recipient action $j=(a,r)$ has capacity $r t_a$ and cost $c-Sa+kr t_a+D_a(1-r)$, with $a=0,1$ and audit indicator $r=0,1$. Its errors do not inform the source. Recipient workflow and audit may depend on an observed source-check finding, so adoption is optional even after that information arrives.

The source policies below exhaust useful deterministic source plans. Their displayed costs exclude the recipient and prior repair. Write $\ell=1+q\gamma$ and $T=2qL_s$.

\newpage

| Source plan | Expected service | Expected residual loss | Recipient information |
|:--|--:|--:|:--|
| $N$: neither exposure checked | 0 | $2qL_s$ | No signal |
| $C_2$: only second checked | 1 | $qL_s$ | $Z$ observed |
| $C_{1N}$: first checked, no propagation | 1 | $qL_s$ | $Z$ observed |
| $C_{1P}$: first checked, propagate if faulty | $\ell$ | 0 | $Z$ observed |
| $C_{1C}$: first checked, recheck second if faulty | $1+q$ | 0 | $Z$ observed |
| $R$: prior source repair | $h$ | 0 | Source already certified |

With $m=2$ recipient actions without access and $m=4$ with access, there are $m+4m^2$ unrepaired complete contingent plans: $m$ for $N$ and $m^2$ for each signal-producing source plan. There are $m$ repaired plans. This gives 18 and 68 unrepaired columns, and 2 and 4 repaired columns. Choosing a recipient action separately after each finding includes information-contingent adoption, not just a committed workflow. Any within-plan behavioral randomization is a mixture of these deterministic plans.

Let $(Q_j,C_j)$ denote a complete plan's expected service and total monetary-plus-loss cost, including $h,F$ when repaired. For each offered-access and repair cell solve

$$C_{Ad}=\min_{\pi\geq0}\sum_j\pi_j C_j,\qquad
\sum_j\pi_j=1,\quad\sum_j\pi_jQ_j\leq B. \tag{22}$$

Randomization is ex ante and independent of $Z$. As in the batch model this is an expected-capacity institution, possibly repeated across batches, not an almost-sure staffing bound. At most two complete plans need positive weight. Enumerating feasible single columns and pairs on opposite sides of $B$ solves (22) globally, including no checking, slack capacity, and infeasible prior repair when $h>B$. Appendix A.6 proves completeness and the finite solution.

## Proposition 6. Adaptive certification and a surviving cross-department interaction

At effective service price $w\geq k$, the source's minimum expected cost is

$$\min\{T,w\ell\}. \tag{23}$$

Learning therefore replaces repeated checks by a single informative check with conditional propagation. It does not remove the positive cost of independent certification.

Let $\Delta=t_A-t_M>0$ and $w_0=D_M/t_M$. Suppose

$$D_M>kt_M,\quad T/\ell>w_0,\quad
k\Delta<S<w_0\Delta,\quad D_A>S+D_M, \tag{24}$$

$$\ell<B<\ell+t_M,\qquad h+t_A<B,\qquad F\geq kh. \tag{25}$$

Put $y=(B-\ell)/t_M\in(0,1)$. Even allowing signal-contingent adoption, the four globally optimized cell costs are

$$C_{00}=C_{10}=c+kB+D_M(1-y), \tag{26}$$

$$C_{01}=F+c+kt_M,\qquad C_{11}=F+c-S+kt_A. \tag{27}$$

The first subscript denotes offered AI access and the second prior repair. In both unrepaired cells the source uses $C_{1P}$ and the recipient remains manual, audited with probability $y$. Prior repair makes capacity slack and the recipient fully audited; with access it adopts AI. For outcome $Y=-C$, the access-by-repair interaction is

$$\delta=(C_{01}-C_{11})-(C_{00}-C_{10})=S-k\Delta>0. \tag{28}$$

The gross value of prior repair without access, before paying $F$, is

$$R_0(B)=k\ell+(D_M-kt_M)(1-y). \tag{29}$$

Without access repair is selected if $F\leq R_0$; with access it is selected if $F\leq R_0+\delta$. Hence $R_0<F<R_0+\delta$ makes neither investment valuable alone while their combination is strictly globally best. All inequalities can hold strictly, so survival is not a capacity knife edge. The proof uses the shared service price and actual contingent plans, not an additive structural benefit.

Conditions (24) also characterize a useful adoption interval: before repair AI is strictly excluded whenever $S<\min\{w_0\Delta,D_A-D_M\}$; after repair audited AI beats audited manual once $S>k\Delta$, provided it also beats both unaudited actions. Under (24) that last comparison is strict. These are sufficient entry bounds for this region, not a general scalar threshold for arbitrary adaptive technologies. At boundaries mixtures and ties must be retained.

## 8.2 Synthetic solution, exact entry thresholds, and null cases

Every number in this subsection is invented. Set $q=\gamma=0.5$, $L_s=10$, $k=1$, $t_M=1$, $t_A=2$, $D_M=4$, $D_A=8$, $c=10$, $S=2$, $B=2.2$, $h=0.1$, $F=1.7$. For example, recipient losses could be severity 100 times marginal error probabilities 0.04 and 0.08. Then $\ell=1.25$, $w_0=4$, $y=0.95$, $R_0=1.4$, and $\delta=1$.

| Offered access $A$ | Prior repair $d$ | Optimized expected cost | Recipient AI probability |
|--:|--:|--:|--:|
| 0 | 0 | 12.40000000 | 0 |
| 1 | 0 | 12.40000000 | 0 |
| 0 | 1 | 12.70000000 | 0 |
| 1 | 1 | 11.70000000 | 1 |

The joint gain is 0.7; repair alone loses 0.3 and access alone is unused. Without repair a first independent check always occurs, and a discovered fault is propagated with probability one. The recipient gets 0.95 expected audit units. Prior repair uses 0.1 service units and recipient AI auditing uses 2, leaving 0.1 slack. A possible unrepaired realization uses 2.5 units, exceeding $B$; the example establishes no hard-capacity guarantee.

Holding the other numbers fixed and varying $S\geq0$, the exact optional-adoption entry values are 4 without repair and 1 with repair. At an entry value adoption is indifferent; above it some AI is optimal, although unrepaired adoption need not immediately be one. Below 4 the unrepaired dual certificate at $w=4$ excludes AI. Above 4, shifting a small mass from the unaudited manual recipient action to unaudited AI saves $S-4>0$ without using capacity. After repair the audited AI action beats audited manual at $S>1$ and beats unaudited AI by 6, with enough capacity; below 1 manual is best. These observations prove the entry statements rather than infer them from a grid.

There is also an adaptive null. With the same primitives but $B=10$, both source certification and the preferred recipient audit fit before repair. The source contributes $k\ell$ before repair and $F$ after it, independently of access. The interaction is zero. More generally, in a region where $C_{1P}$ remains optimal, replacing it by an exactly resource-equivalent prior certification ($h=\ell,F=k\ell$) cannot change recipient opportunities or total cost. This conditional equivalence is not asserted when foregoing source certification is itself optimal.

The new script evaluates every complete contingent column by its two realized branches, then compares the single/pair algorithm with independently constrained HiGHS linear programming. It exports the four policy matrices, optimal mixtures, entry grid and null/boundary cases. In 538 cell comparisons, including 98 accepted strict-region parameter draws from 100 candidates and zero-capacity cases, the largest objective discrepancy was $7.11\times10^{-15}$. The closed-form costs and adoption choices in Proposition 6 are also asserted on each strict-region draw. Two candidates were skipped before theorem checks because $h+t_A<B$ was not satisfied; they were not failed checks. The asserted comparison decomposition is $538=4+392+20+122$: four main cells, four cells for each of 98 accepted candidates, 20 boundary cells, and 122 entry-grid cells. These are computational checks of the specified finite action space, not empirical evidence or validation of stochastic hard-capacity control.

The reuse interpretation must consequently be narrower than a linear count of repeated copies. Proposition 5 remains an open-loop theorem. Adaptive information can collapse the source's two-exposure burden to $1+q\gamma$, and with free propagation it collapses further to one independent check. Source reuse alone then does not imply a growing requirement to inspect each copy. What survives here is the difference between the capacity used by that informative check and by prior certification, coupled to a separate recipient's adoption demand. This is a small solved robustness result, not a general dynamic inspection theorem.

# 9. Pathwise capacity, certification timing, and investment

## 9.1 Institution and global frontier

Keep exactly Section 8's source fault, release timing, independent examination, correction, recipient actions and optional access. Change only the service institution: total service must be at most $B$ in every positive-probability fault history and every realized lottery. There is no borrowing between histories. A pre-finding decision cannot depend on $Z$. A first or second check can reveal $Z$ before recipient decisions; no check leaves the recipient decision unsignaled. Prior repair still costs $F$ all in, including $kh$ once. Its source service is deterministically $h$, not a separate additional monetary charge. Each check or audit bundles its correction at the fixed service requirement specified in Section 8. Thus the fault and workflow lotteries are the only load-relevant uncertainty; a recipient error does not cause an additional unbudgeted correction service. All costs below include production and expected losses; feasibility itself is pathwise.

The complete useful deterministic contingent plans remain those in Section 8.1. For each plan compute its two realized loads $Q_j(0),Q_j(1)$. Delete a plan if either exceeds $B$; then minimize cost over the retained plans, and compare the two root repair alternatives. This solves global optional repair and access. Any lottery is supported only on retained plans. Giving positive probability to an infeasible plan makes some positive-probability history/lottery pair violate capacity; a low-load history of another plan cannot compensate. Thus lotteries can mix tied minimizers but cannot improve the minimum or rescue an excluded plan. This contrasts with the expected-capacity convexification in (22).

The solution can be reduced analytically beyond an enumeration identity. Define the recipient's net cost with remaining service $x$ by

$$G_0(x)=\min\{D_M,kt_M\text{ if }x\geq t_M\},$$

$$G_1(x;S)=\min\{D_M,D_A-S,kt_M\text{ if }x\geq t_M,
kt_A-S\text{ if }x\geq t_A\},\quad x\geq0. \tag{30}$$

A conditional minimum includes only feasible actions. For $0<q,\gamma<1$, put $\ell=1+q\gamma$. The globally minimized unrepaired cost is

$$U_A(B)=c+\min\left\{\begin{array}{l}
2qL_s+G_A(B),\\
k+qL_s+G_A(B-1)\quad\text{if }B\geq1,\\
k\ell+(1-q)G_A(B-1)+qG_A(B-1-\gamma)
\quad\text{if }B\geq1+\gamma.
\end{array}\right. \tag{31}$$

These three branches are respectively no checking, one output checked without propagation, and first check with fault-contingent propagation. Independently rechecking the second exposure after a detected fault is strictly dominated by propagation: it yields the same evidence and corrections but uses more service. The two single-check source plans have identical remaining capacities and expected loss. The repaired cost is

$$R_A(B)=F+c+G_A(B-h),\quad B\geq h; \tag{32}$$

it is infeasible otherwise. Consequently repair is optimal exactly when $R_A\leq U_A$, with equality giving both choices. Equations (30)-(32) are a closed finite frontier for arbitrary budgets and primitives in this benchmark, including zero effort and unavailable audits. Recipient choices are the minimizing actions at each reached history. Their ties, and source ties, are retained. They require no inference about recipient quality from the independent source finding.

## Proposition 7. Exact benchmark cost regions and an institutional investment reversal

Use the rational Section 8.2 primitives $q=\gamma=1/2$, $L_s=10$, $k=1$, $t_M=1$, $t_A=2$, $D_M=4$, $D_A=8$, $c=10$, $h=1/10$. Let $S\geq0$, $F\geq1/10$. These are synthetic primitives, not estimates. The complete contingent-menu load-breakpoint set, including root repair and the separately dominated second-check option, is

$$\{0,1/10,1,11/10,3/2,2,21/10,5/2,3,7/2,4\}. \tag{33}$$

Between consecutive breakpoints the feasible columns do not change; at a breakpoint columns with exactly that load become feasible. On the decisive strip $21/10\leq B<5/2$, the unique optimal unrepaired source architecture checks the first exposure and propagates on a fault. The no-access cost is $U_0=55/4$. With access the exact frontier is

$$U_1(S)=\begin{cases}
55/4,&0\leq S\leq4,\\
63/4-S/2,&4\leq S\leq7,\\
77/4-S,&S\geq7.
\end{cases} \tag{34}$$

For $S<4$ the recipient stays manual, audited only after a clean finding. For $4<S<7$ it uses audited manual work after a clean finding and unaudited AI after a fault. For $S>7$ it uses unaudited AI in both histories. At $S=4$ fault-branch manual and AI are tied; at $S=7$ clean-branch audited manual and unaudited AI are tied. Their feasible lotteries give adoption probabilities $[0,1/2]$ and $[1/2,1]$, respectively. All specified inequalities for branch uniqueness are strict.

Prior repair leaves enough service for either recipient audit throughout this strip. Therefore $R_0=F+11$ and $R_1=F+\min\{11,12-S\}$. With access repair is globally optimal if and only if $F\leq T_H(S)$, where

$$T_H(S)=\begin{cases}
11/4,&0\leq S\leq1,\\
7/4+S,&1\leq S\leq4,\\
15/4+S/2,&4\leq S\leq7,\\
29/4,&S\geq7.
\end{cases} \tag{35}$$

Strict inequality gives strictly preferred repair; equality gives both root decisions; reversing the inequality rejects repair. Without access the repair threshold is $11/4$. After repair adoption is manual for $S<1$, AI for $S>1$, and any mixture of the two audited workflows at $S=1$. These statements also apply at $B=21/10$, since exactly filling capacity is allowed. At $B=5/2$ a fault-branch manual audit becomes feasible and (34)-(35) must be replaced by (30)-(32), not extrapolated.

For an exact comparison with the expected institution, restrict further to

$$21/10<B<9/4,\qquad1<S<4. \tag{36}$$

Here its unrepaired cost is $19-3B$ with or without offered access, while its repaired-access cost is $F+12-S$. Its access-conditional repair threshold is $T_E(B,S)=7+S-3B$, and its no-access repair threshold is $8-3B$. The open region in which hard capacity selects the joint investment, repair alone is rejected, access alone is unused, and expected capacity strictly rejects the pair is exactly

$$\max\{11/4,\,7+S-3B\}<F<7/4+S \tag{37}$$

within (36). The interval is nonempty throughout (36): each lower bound is strictly below the upper bound. At $F=11/4$ hard repair alone is indifferent; at $F=T_E$ expected joint investment is indifferent; at $F=T_H$ hard joint investment is indifferent. These are weak-choice boundaries, not strict reversals.

At $S=2$, condition (37) becomes simply $11/4<F<15/4$ for every $21/10<B<9/4$. The centrally suggested synthetic seed $B=11/5,F=29/10$ gives the following exact global costs, verified here independently from raw histories.

| Access, repair | Pathwise cost | Expected-capacity cost |
|:--|--:|--:|
| 00 | $55/4$ | $62/5$ |
| 10 | $55/4$ | $62/5$ |
| 01 | $139/10$ | $139/10$ |
| 11 | $129/10$ | $129/10$ |

The hard joint gain is $17/20$, while hard repair alone loses $3/20$. The expected institution rejects the pair because its unrepaired cost is lower by $1/2$ than the repaired-access cost. Hard unrepaired loads are 2 after a clean finding and $3/2$ after a fault, with recipient audit only in the clean history. Prior repair plus audited AI uses $21/10$. The mechanism is the value of reallocating feasible service after discovery, not a new private/social incentive conflict. Free optional access cannot worsen aligned optimized welfare under either institution.

## Proposition 8. Equal expected source resources need not be pathwise equivalent

Consider no AI access, general $0<q,\gamma<1$, $D_M>kt_M$, and set $h=\ell=1+q\gamma$, $F=k\ell$. Suppose

$$\max\{1+t_M,1+\gamma\}\leq B<\ell+t_M,\quad
\frac{2qL_s}{\ell}>\frac{D_M}{t_M}, \tag{38}$$

$$L_s>k\gamma+D_M-kt_M,\qquad
2qL_s>k\ell+q(D_M-kt_M). \tag{39}$$

The budget interval is nondegenerate whenever $t_M>(1-q)\gamma$. In the expected institution the two source alternatives have equal globally optimized cost

$$c+kB+D_M\left(1-\frac{B-\ell}{t_M}\right). \tag{40}$$

Under pathwise capacity, however, no prior repair costs

$$c+k\ell+(1-q)kt_M+qD_M,$$

whereas prior repair costs $c+k\ell+D_M$. Thus prior repair is strictly worse by

$$(1-q)(D_M-kt_M)>0. \tag{41}$$

These are global comparisons against every source policy, not costs conditional on imposed checking. Both selected source alternatives have zero source loss and identical expected source service and monetary cost. The difference is their service histories: a clean finding leaves a full audit unit, while deterministic validation leaves less than $t_M$ in every history. Its absence of a finding is not missing information about recipient quality; the recipient is independent, and only feasible remaining service differs.

For the rational synthetic benchmark with $h=F=5/4$ and $2\leq B<9/4$, (40) is $19-3B$ for both alternatives. Hard costs are $55/4$ without repair and $61/4$ with repair. In particular $B=11/5$ reproduces the central seed. The hard comparison reverses at $B=9/4$: validation plus the manual audit then fits exactly and costs $49/4$, while adaptive certification remains $55/4$ until $B=5/2$. At $B=5/2$ both cost $49/4$. Thus the timing premium has a discontinuous budget boundary rather than a universal sign. The expected-resource null in Section 8 remains valid within its institution.

The new exact-rational script imports no prior model code. It enumerates raw action histories, including redundant clean-source rechecks, forbids pre-finding dependence on the hidden fault, and evaluates both realized loads and every competing cost. Its 152 seed columns include all four cells. It compares the analytic frontier against all raw columns in 588 budget/access/repair/savings checks at every load breakpoint and one point in each intervening interval, with explicit savings and fee ties. It also retains separate exact expected-capacity comparisons and checks (38)-(41) at a second rational primitive witness. This is finite boundary verification, not a random campaign or empirical evidence. Detailed matrices and all minimizers are supplied in the executable package.

# 10. Recipient granularity and the robust investment boundary

## 10.1 The same histories with independently allocable recipient tasks

Propositions 6-8 concern one indivisible recipient audit. Replace only that recipient by $n$ equal tasks. Aggregate production cost $c$, unaudited losses $D_M,D_A$, audit service $t_M,t_A$ and AI saving $S$ stay fixed; every task has $1/n$ of each quantity. Workflow and audit can be chosen taskwise after a source finding. Without a check, the allocation cannot depend on hidden $Z$. No new signal or error process is introduced. Recipient service includes its correction at the same fixed requirement per task. Every complete allocation and every lottery realization must still fit $B$ in each source history. Source fault, release timing, first check, propagation and every competing source plan remain unchanged.

A finite recipient allocation consists of counts of the four actions $M0,M1,A0,A1$, summing to $n$, with their service and net costs divided by $n$. For a given remaining service $x$, let $g_{A,n}(x)$ be the minimum net cost of such a feasible count vector. This integer allocation problem, followed by the three source branches (31) with $G_A$ replaced by $g_{A,n}$, is the complete finite-$n$ solution. Recipient labels have no effect on cost or service. Conditional source histories factor into separate recipient minima; no finding permits hidden-state conditioning. Lotteries over feasible allocations cannot beat the minimum, and lotteries containing an infeasible allocation remain prohibited. Thus atomization changes the available audit technology, not the feasibility rule.

## Proposition 9. Matched-mean timing advantage is a quantization effect

First allow no AI access, set $h=\ell=1+q\gamma$, $F=k\ell$, and write $\beta=D_M-kt_M>0$. For $x\geq0$, define

$$f_n(x)=\frac{\min\{n,\lfloor nx/t_M\rfloor\}}{n},
\qquad f_\infty(x)=\min\{1,x/t_M\}. \tag{43}$$

At most $nf_n(x)$ tasks can be audited, and all should be audited when feasible. Therefore $g_{0,n}(x)=D_M-\beta f_n(x)$. For $B\geq1+\gamma$, the following sufficient conditions make first-check propagation strictly globally best among all unrepaired source policies, for every $n$ and in the fluid limit:

$$L_s>k\gamma+\beta,\qquad 2qL_s>k\ell+\beta. \tag{44}$$

They compare with neither check, either single check and all conditional or redundant rechecks, not just a selected pair of actions. The matched-mean adaptive advantage, defined as prior-repair cost minus globally optimized unrepaired cost, is exactly

$$\Delta_n=\beta\{(1-q)f_n(B-1)+qf_n(B-1-\gamma)-f_n(B-\ell)\}. \tag{45}$$

The corresponding fluid gap satisfies

$$\Delta_\infty\leq0,\qquad
|\Delta_n-\Delta_\infty|\leq\beta/n,\qquad \Delta_n\leq\beta/n. \tag{46}$$

These are applications of concavity and rounding, not new Jensen or rounding theorems. The source alternatives have the same mean service and source money, but an indivisible recipient can value residual capacity nonconcavely. Fluid allocation removes that quantization. On the budget strip in (38),

$$\Delta_\infty=-\frac{\beta(1-q)}{t_M}(B-1-t_M). \tag{47}$$

It is zero at $B=1+t_M$ and strictly negative above that point. Formula (47) is used only where the strip's residual-capacity inequalities hold. Outside it, (45) with $f_\infty$ remains the correct fluid comparison. Conditions (44) are uniform sufficient conditions, not necessary ones. With non-strict inequalities they support weak global dominance; another source plan can tie. The exact cost difference still holds when propagation is a minimizer.

All following numbers are synthetic central seeds, independently verified here. With the original matched-mean primitives, $B=11/5$, $h=F=5/4$, the globally optimized no-access costs are:

| Recipient tasks | No prior repair | Prior repair | $\Delta_n$ |
|--:|--:|--:|--:|
| $1$ | $55/4$ | $61/4$ | $3/2$ |
| $4$ | $13$ | $13$ | $0$ |
| $7$ | $361/28$ | $355/28$ | $-3/14$ |
| Fluid | $127/10$ | $62/5$ | $-3/10$ |

Proposition 8 remains correct for its original single indivisible audit. Its positive timing advantage is not a universal benefit of waiting or of observing an unrelated source. No posterior improvement in recipient quality explains any of these comparisons.

## Proposition 10. A repair/access frontier survives fluid allocation

Return to cheap prior validation $h=1/10$ and all-in fee $F\geq1/10$. Use $q=\gamma=1/2$, $L_s=10$, $k=1$, $c=10$, $t_M=1$, $t_A=2$, $D_M=4$, $D_A=8$. For $1\leq S\leq4$, the fluid recipient cost is the lower convex envelope of

$$(0,4),\quad(1,1),\quad(0,8-S),\quad(2,2-S), \tag{48}$$

where the first coordinate is service and the second is net cost. It is not the minimum of four indivisible actions. On $x\geq0$ it equals

$$g_{1,\infty}(x)=\begin{cases}
4-3x,&0\leq x\leq1,\\
1+(1-S)(x-1),&1\leq x\leq2,\\
2-S,&x\geq2.
\end{cases} \tag{49}$$

The finite solution has the same form with each segment's allocated task mass rounded down: replace $x$ by $\lfloor nx\rfloor/n$ in the first segment and $x-1$ by $\lfloor n(x-1)\rfloor/n$ in the second. Thus $0\leq g_{1,n}-g_{1,\infty}\leq3/n$. At $S=1$ the second segment is flat; at $S=4$ the first two segments are collinear and $A0$ ties $M0$. Multiple allocations can then minimize. All zero-audit and partially audited allocations remain feasible options.

Put $W=2+S$. The sufficient uniform source-dominance conditions are $L_s>k\gamma+W$ and $2qL_s>k\ell+W$. They hold strictly throughout this saving interval for the benchmark, for every $n$ and in the fluid limit. Hence first-check propagation is globally optimal before repair, even after all taskwise recipient choices and alternative source plans are admitted.

On $21/10\leq B\leq9/4$, the four fluid hard-capacity costs are

$$\begin{aligned}
U_0&=16-3B/2, &U_1&=15-B-S(B-2)/2,\\
R_0&=F+11, &R_1&=F+12-S.
\end{aligned} \tag{50}$$

Here $U$ denotes no repair and $R$ prior repair, with subscript access. Clean-history residual service $B-1$ lies on the second segment of (49); fault-history service $B-3/2$ lies on its first. Both histories satisfy capacity separately. After repair both complete audits fit, so $R_1$ is attained by audited AI for $S>1$, with audited manual also optimal at $S=1$.

For finite $n$, define

$$m_n=\lfloor n(B-3/2)\rfloor/n,\qquad
b_n=\lfloor n(B-2)\rfloor/n.$$

The exact hard costs and useful error bounds on this strip are

$$\begin{aligned}
U_{0,n}&=55/4-3m_n/2,\\
U_{1,n}&=U_{0,n}-(S-1)b_n/2,\quad R_{a,n}=R_a.
\end{aligned} \tag{51}$$

$$0\leq U_{0,n}-U_0\leq\frac{3}{2n},\qquad
0\leq U_{1,n}-U_1\leq\frac{S+2}{2n}. \tag{52}$$

The expected-capacity institution remains a separate comparison. Ex ante lotteries convexify the task actions even at finite $n$, without a pathwise restriction on each lottery. Its four costs on this strip are $19-3B,19-3B,F+11,F+12-S$. These agree with the retained expected solution, not with the hard convexification (49) performed separately after each finding.

The fluid repair thresholds without and with access, and the expected access threshold, are

$$T_0=5-3B/2,\qquad T_H=3-B+S(2-B/2),\qquad
T_E=7+S-3B. \tag{53}$$

A root investment is optimal when $F$ is at most its threshold; strict inequality makes it strictly preferred, and equality gives both root choices. Finite hard thresholds are $T_{0,n}=U_{0,n}-11$ and $T_{H,n}=U_{1,n}-12+S$. For $21/10<B<9/4$, $1<S<4$, the necessary and sufficient fluid region in which hard capacity selects repair with access, hard repair alone is rejected, and expected capacity rejects repair with access is

$$\max\{T_0,T_E\}<F<T_H. \tag{54}$$

It is nonempty because

$$T_H-T_E=(B-2)(4-S)/2>0,\quad
T_H-T_0=(S-1)(2-B/2)>0. \tag{55}$$

Expected repair alone is also rejected in (54), since $T_E>8-3B$ for $S>1$. Replacing $T_0,T_H$ by their finite counterparts gives the exact finite-$n$ region; it is nonempty too. A fixed fluid witness remains in that finite region for all $n$ with $3/[2n]<F-T_0$, because $T_{H,n}\geq T_H$ and the expected threshold is unchanged. This establishes a nonvanishing decision boundary rather than a disappearing indivisibility artifact.

Access alone now yields

$$U_0-U_1=(S-1)(B-2)/2>0. \tag{56}$$

After repair its gain is $S-1$. Their difference is $T_H-T_0>0$: conditional repair/access complementarity survives, but joint-only activation with unused access alone does not. At finite $n$, access-alone gain is $(S-1)b_n/2$ and can vanish when no task upgrade fits. Thus neither the positive matched-mean timing advantage nor the old joint-only description is claimed robust to atomization.

At the synthetic central seed $B=11/5,S=2,F=5/2$, fluid hard costs in order 00,10,01,11 are $127/10,63/5,27/2,25/2$, versus expected $62/5,62/5,27/2,25/2$. Hard access alone gains $1/10$, hard joint investment gains $1/5$ relative to neither, and the expected institution rejects the pair. At $F=T_0,T_E,T_H$ the corresponding comparisons tie. The cost formulas extend to the displayed budget endpoints, where exact capacity filling is allowed; the open strict region (54) is stated separately. At $S=1$ its hard joint-versus-alone interval closes, and at $S=4$ its hard-versus-expected interval closes. Outside the stated budget/saving strip the full finite allocation/frontier problem must be solved, rather than extrapolating these expressions.

The standalone exact-rational verifier checks 288 labeled-task allocation problems against a separate count solution and 48 globally optimized raw source-history cases, including redundant clean checks and all source competitors. It verifies finite witnesses $n=1,4,7$, deterministic convergence/boundary cases, saving and fee ties, and the fluid seed. No random campaign or new enterprise data are used. The retained 588/538 suites remain separate.

# 11. Endogenous procurement: the boundary of the repair claim

## 11.1 One additional root choice

Keep the fluid recipient and source institution of Section 10. Only capacity changes: the organization buys one deterministic stock $B\geq0$ before any finding, at additional real cost $\rho B$, $0\leq\rho\leq3$. Every positive-probability history must fit that stock in the hard institution. Procurement cannot respond to a finding. Realized service still costs $k=1$; $\rho$ is a real procurement input, not a shadow-price transfer. Repair is optional at all-in fee $F\geq h=1/10$, which already includes $kh$. Each repair/access cell optimizes its own stock. All previous fixed-$B$ propositions retain their stated scope.

Write $a=S-1\in[0,3]$. The recipient cost envelopes, including realized audit service but excluding procurement and common production cost $c=10$, are

$$g_0(x)=4-3\min(x,1),\qquad
 g_1(x)=4-3\min(x,1)-a\min((x-1)_+,1),\quad x\geq0.\tag{57}$$

For a small robustness extension let $q,\gamma\in[2/5,3/5]$, $\ell=1+q\gamma$, $d=1+\gamma$. Propagation after a first check uses $X=1$ with probability $1-q$ and $X=d$ with probability $q$. Other primitives stay fixed. The benchmark is $q=\gamma=1/2$.

## Proposition 11. Global procurement solution and complete capacity choices

Define $M_j=\min_{x\geq0}\{g_j(x)+\rho x\}$. Globally over every admissible source plan, the unrepaired optimum uses first checking and fault-contingent propagation. Repaired pre-fee costs $r_j$, expected-capacity unrepaired costs $e_j$, and hard unrepaired costs $u_j$ satisfy

$$M_0=1+\rho,\quad M_1=1+\rho+\min(0,\rho-a),\qquad
r_j=10+\rho h+M_j,\quad e_j=10+\ell+\rho\ell+M_j,\tag{58}$$

$$u_j=10+\ell+\min_{B\geq d}\{(1-q)g_j(B-1)+qg_j(B-d)+\rho B\}.\tag{59}$$

Thus the globally optimized root cell is $\min(u_j,F+r_j)$ in the hard institution and $\min(e_j,F+r_j)$ in the expected institution. Repair is strictly selected below its threshold, rejected above it, and both root choices are optimal at equality. Free optional access cannot increase optimized cost.

Here are all hard optimal stocks. For no access: at $\rho=0$, $B\in[2+\gamma,\infty)$; for $0<\rho<3q$, $B=2+\gamma$; at $\rho=3q$, $B\in[2,2+\gamma]$; for $3q<\rho<3$, $B=2$; at $\rho=3$, $B\in[d,2]$.

For access and $0<a<3$, put $H=a+q(3-a)$. The complete list is

| Procurement price | Optimal hard stock |
|---|---|
| $0$ | $[3+\gamma,\infty)$ |
| $(0,qa)$ | $3+\gamma$ |
| $qa$ | $[3,3+\gamma]$ |
| $(qa,a)$ | $3$ |
| $a$ | $[2+\gamma,3]$ |
| $(a,H)$ | $2+\gamma$ |
| $H$ | $[2,2+\gamma]$ |
| $(H,3)$ | $2$ |
| $3$ | $[d,2]$ |

At $a=0$ access has the no-access list. At $a=3$, replace that list by $[3+\gamma,\infty)$ at zero; $3+\gamma$ on $(0,3q)$; $[3,3+\gamma]$ at $3q$; $3$ on $(3q,3)$; and $[d,3]$ at three. These endpoint rules include merged kinks.

For repaired stock, $B=h+x$, where $x$ minimizes $g_j(x)+\rho x$. For no access this set is $[1,\infty)$ at zero, $\{1\}$ on $(0,3)$, and $[0,1]$ at three. For access with $0<a<3$, it is $[2,\infty)$ at zero, $\{2\}$ on $(0,a)$, $[1,2]$ at $a$, $\{1\}$ on $(a,3)$, and $[0,1]$ at three. At $a=0$ use the no-access set; at $a=3$ it is $[2,\infty)$ at zero, $\{2\}$ on $(0,3)$, $[0,2]$ at three. The same sets shifted by $\ell$ give expected unrepaired stocks. Unbounded zero-price sets reflect unused free stock, not unlimited realized service. Fee ties take the union of the repaired and unrepaired sets; they do not license a pathwise-infeasible plan.

## Proposition 12. Procurement removes positive conditional complementarity

The expected repair threshold is independent of access:

$$T^E=\ell+(\ell-h)\rho.\tag{60}$$

Let $P_j=u_j-e_j$. The hard pooling premiums and thresholds are

$$P_0=\gamma\min\{(1-q)\rho,q(3-\rho)\},\qquad T^H_j=T^E+P_j,\tag{61}$$

$$P_1=\begin{cases}
\gamma\min\{(1-q)\rho,q(a-\rho)\},&\rho\leq a,\\
\gamma\min\{(1-q)(\rho-a),q(3-\rho)\},&\rho\geq a.
\end{cases}\tag{62}$$

Consequently $I_E=T^E_1-T^E_0=0$ and $I_H=T^H_1-T^H_0=P_1-P_0\leq0$. For $0<a<3$, strict substitution holds if and only if

$$qa<\rho<a+q(3-a).\tag{63}$$

Outside that open interval, at its endpoints, or at $a=0,3$, the interaction is zero. These claims hold throughout the stated nondegenerate primitive neighborhood, not just at the benchmark. On the open set

$$0<a<3,\quad qa<\rho<a+q(3-a),\quad T^E+P_1<F<T^E+P_0,\tag{64}$$

repair is strictly chosen without access and strictly rejected with access. At either fee boundary the corresponding repair choice ties. For $F$ below both thresholds both choose repair; above both neither does. This is substitution in investment incentives, not a welfare loss from optional free access.

## 11.2 Exact synthetic witnesses and economic interpretation

All numbers here are synthetic. At $S=2,\rho=1$, hard unrepaired costs without/with access are $59/4,29/2$; repaired pre-fee costs are both $121/10$. The thresholds are $53/20,12/5$, and $I_H=-1/4$. At $F=5/2$ repair is selected without access but rejected with access; optimized costs fall from $73/5$ to $29/2$ when free access is offered. Hard unrepaired access has all optimal stocks $[5/2,3]$. Repaired access has stocks $[11/10,21/10]$; repaired no access has only $11/10$. Expected unrepaired access has stocks $[9/4,13/4]$ and rejects repair at this fee.

The strict investment comparison is not an artifact of these capacity ties. At $S=2,\rho=11/10,F=13/5$, $T^H_1=127/50<F<279/100=T^H_0$. Unrepaired hard stocks are uniquely $5/2$ and repaired stocks uniquely $11/10$. More generally $0<a<\rho<3/2$ at the benchmark gives the open fee interval $5/4+7\rho/5-a/4<F<5/4+7\rho/5$. Its positive width $a/4$ proves a genuine open region. Equation (64) extends it to nearby $q,\gamma$.

At the same $\rho=1$ but fixed $B=11/5$, procurement adds the same $11/5$ to all four Section 10 cells, leaving their conditional interaction $9/10$ unchanged. Endogenizing stock, rather than relabeling a scarcity payment, changes the sign. Section 10's hard/expected threshold gap is exactly its unrepaired recipient pooling penalty $(B-2)(4-S)/2$, not an additional recipient-information premium. With root procurement, access changes the capped recipient payoff and reduces or preserves that pooling premium. Nothing learned about the source changes the independent recipient's quality.

The exact result is a solved boundary of the repair claim within a two-history technology. Procurement, recourse, convex conjugacy, newsvendor logic and substitution are inherited. The analysis supplies explicit global source dominance, full capacity and fee ties, and a sign reversal relative to the fixed-budget comparison; it does not establish a new general capacity-investment principle or demonstrate substantive originality over all prior inspection/investment results.

# 12. Capacity supply, rather than a universal investment sign

## 12.1 One change to the procurement technology

Retain the fluid benchmark, binary root repair/access choices and the full source menu. Fix $S=2$, $q=\gamma=1/2$, $L_s=10$, $k=1$, $c=10$, $h=1/10$. Replace linear procurement only by

$$C(B)=\rho B+\kappa(B-b)_+,\qquad
21/10<b<9/4,\quad 1/2<\rho<1,\quad0\leq\kappa\leq3-\rho.\tag{66}$$

Here $b$ is a price threshold, not a ceiling. One deterministic stock is procured before any finding. No history buys additional stock. Realized service still costs $k$ and the repair fee $F\geq h$ includes $kh$ once. Conditional on each binary investment cell, all admissible source-policy lotteries and recipient allocations are included. A root lottery over complete investment/stock choices, with procurement paid for the realized root choice, cannot beat the best such choice. We do not pool capacity across different realized root investment choices. The expected institution does allow policy mixtures within a cell at its one root stock, with procurement charged as $C(B)$, not as the expectation of procurement on realized service.

Let $v=\rho+\kappa$. Write $U_j,E_j$ for globally minimized unrepaired costs under hard and expected capacity, respectively, and $R_j$ for repaired costs before $F$. Access $j=1$ remains optional usage, not compulsory AI.

## Proposition 13. Complete tiered-procurement cells and capacity ties

Propagation after a first check is globally optimal among unrepaired source plans in both institutions, including expected mixtures across source plans. The cells are

$$R_0=11+11\rho/10,\qquad R_1=10+21\rho/10,\tag{67}$$

$$U_0=\begin{cases}49/4+5\rho/2+\kappa(5/2-b),&v\leq3/2,\\16-3b/2+\rho b,&v\geq3/2,\end{cases}\tag{68}$$

$$U_1=\begin{cases}23/2+3\rho+\kappa(3-b),&v\leq1,\\12+5\rho/2+\kappa(5/2-b),&1\leq v\leq2,\\17-2b+\rho b,&v\geq2,\end{cases}\tag{69}$$

$$E_0=49/4+9\rho/4+\kappa(9/4-b),\qquad
E_1=\begin{cases}45/4+13\rho/4+\kappa(13/4-b),&v\leq1,\\E_0,&v\geq1.\end{cases}\tag{70}$$

Adjacent formulas agree at every boundary. Repaired stocks are uniquely $11/10$ and $21/10$, both below $b$. Hard unrepaired stocks are:

| Cell | Price condition | All optimal stocks |
|---|---|---|
| $U_0$ | $v<3/2$; $v=3/2$; $v>3/2$ | $\{5/2\}$; $[b,5/2]$; $\{b\}$ |
| $U_1$ | $v<1$; $v=1$ | $\{3\}$; $[5/2,3]$ |
| $U_1$ | $1<v<2$; $v=2$; $v>2$ | $\{5/2\}$; $[b,5/2]$; $\{b\}$ |

Expected stocks are uniquely $9/4$ for no access when $v<3$. For access they are uniquely $13/4$ when $v<1$, the whole interval $[9/4,13/4]$ when $v=1$, and uniquely $9/4$ when $1<v<3$. **At $v=3$, both expected cells have the full optimal stock interval $[b,9/4]$.** This last endpoint tie corrects an incomplete candidate list; it leaves all cost formulas intact.

The expected solution minimizes $45/4+g_j(x)+C(5/4+x)$ over $x\geq0$ after globally eliminating other source plans. This reduction is proved using occupation mixtures and the procurement Lipschitz bound. It does not use Section 11's linear effective-price identity with a nonlinear $C$.

## Proposition 14. Exact investment-sign and fee frontier

Set $T^H_j=U_j-R_j$, $T^E_j=E_j-R_j$ and $I_H=T^H_1-T^H_0$, $I_E=T^E_1-T^E_0$. Then

$$I_H=\begin{cases}
(\kappa-\rho+1/2)/2,&v\leq1,\\
3/4-\rho,&1\leq v\leq3/2,\\
3/4-\rho+(v-3/2)(5/2-b),&3/2\leq v\leq2,\\
2-b/2-\rho,&2\leq v\leq3,
\end{cases}\qquad I_E=\min(\kappa,1-\rho).\tag{71}$$

All four pieces are continuous. Write $r_c=2-b/2\in(7/8,19/20)$. The exhaustive hard sign classification is:

- For $1/2<\rho<3/4$, the sign is negative, zero or positive as $\kappa$ is below, equal to or above $\rho-1/2$.
- For $\rho=3/4$, it is negative for $v<1$, zero for $1\leq v\leq3/2$, and positive for $v>3/2$.
- For $3/4<\rho<r_c$, put $v_* =3/2+(\rho-3/4)/(5/2-b)$. The sign is negative, zero or positive as $v$ is below, equal to or above $v_*\in(3/2,2)$.
- For $\rho=r_c$, it is negative for $v<2$ and zero for $v\geq2$.
- For $r_c<\rho<1$, it is strictly negative for every allowed $\kappa$.

Expected interaction is zero only at $\kappa=0$ and positive for $\kappa>0$ in this strip. No positive hard region exists at the high base prices $\rho\geq r_c$, although a zero plateau remains at equality. This classification does not assert a universal curvature comparative static outside the solved institution.

For either institution $K\in\{H,E\}$, repair is strictly chosen in cell $j$ iff $F<T^K_j$, rejected iff $F>T^K_j$, and ties iff equality holds. Thus $I_K>0$ gives the actual strict access-induced repair region $T^K_0<F<T^K_1$; $I_K<0$ gives $T^K_1<F<T^K_0$, in which access discourages repair. When $I_K=0$ neither strict region exists. Below both thresholds both cells repair, and above both neither does. Fee equality retains both root choices and all their capacity ties. Thresholds in this strip exceed $h$, so the displayed nonempty intervals respect $F\geq h$.

In the inner strip $1/2<\rho<3/4$, $0\leq\kappa<1-\rho$, all hard stocks remain $5/2,3$ and repaired stocks $11/10,21/10$. Nevertheless the exact inner sign boundary is $\kappa_*=\rho-1/2$. At differentiability points the standard envelope identity is

$$\frac{d I_H}{d\kappa}=(B_{U_1}-b)_+-(B_{U_0}-b)_+-(B_{R_1}-b)_++(B_{R_0}-b)_+.\tag{72}$$

It equals $1/2$ in this inner strip. Differential exposure to the expensive capacity tier changes the investment interaction without changing any optimal hard stock. This is a supply-cost comparison, not an independent-recipient information premium.

## 12.2 Exact synthetic witnesses, not a fixed-fee reversal

At $b=11/5$, $\rho=3/5$, the three synthetic values $\kappa=0,1/10,1/5$ give respectively

$$I_H=-1/20,\ 0,\ 1/20;\qquad I_E=0,\ 1/10,\ 1/5.\tag{73}$$

At zero tier surcharge the hard thresholds are $T^H_0=209/100$, $T^H_1=51/25$. Fees $51/25<F<209/100$ select repair without access and reject it with access. At surcharge $1/5$ the thresholds are $43/20,11/5$; fees $43/20<F<11/5$, including $F=87/40$, reject repair without access and select it with access. **These are different fee intervals.** They do not establish a fixed-$F$ investment reversal between the two supply curves. All four hard stocks are unique throughout these three witnesses. Free optional access still weakly lowers the globally optimized cost.

## Proposition 15. Smooth supply and a nondegenerate primitive neighborhood

For $\delta>0$, define

$$H_\delta(z)=\frac{z+\sqrt{z^2+\delta^2}}2,\qquad
C_\delta(B)=\rho B+\kappa[H_\delta(B-b)-H_\delta(-b)].\tag{74}$$

Then $C_\delta(0)=0$, its slope is strictly between $\rho$ and $\rho+\kappa$ when $\kappa>0$, and it is strictly convex when $\kappa,\delta>0$. For all $B\geq0$,

$$|C_\delta(B)-C(B)|\leq\kappa\delta/2.\tag{75}$$

Every optimized cell in either institution changes by at most $\epsilon=\kappa\delta/2$, every repair threshold by at most $2\epsilon=\kappa\delta$, and the interaction by at most $4\epsilon=2\kappa\delta$. Global source dominance remains valid. At the positive witness in Section 12.2, every $0<\delta<1/8$ preserves $I_H>0$ and the particular strict repair comparison at $F=87/40$. Thus the sign and choice are not artifacts of the procurement kink or capacity ties.

A primitive neighborhood also exists. Keep $\rho=3/5$, $\kappa=1/5$, $b=11/5$, $h=1/10$, and allow $q,\gamma\in(49/100,51/100)$, $S\in(199/100,201/100)$. The same source plan is globally optimal; hard stocks are $2+\gamma,3$, repaired stocks $h+1,h+2$. In this box,

$$I_H=q(S-1)\gamma-\rho\gamma+\kappa(1-\gamma)>0,\tag{76}$$

and the same fee $87/40$ strictly selects repair only with access. Strict branch slopes, source-dominance gaps and fee margins imply persistence under sufficiently small additional changes in $\rho,\kappa,b,h,F$. No full general-primitive supply frontier is claimed.

## 12.3 What is and is not added

Sections 10-12 supply nested institutional boundaries. Fixed stock can yield positive conditional repair/access interaction; flat-price root procurement yields weak substitution; a steeper capacity supply curve can restore complementarity even at unchanged optimal stocks. The algebra measures procurement-tier exposure and pooling, not information about the untouched recipient. The proofs compare every source plan, expected occupation mixtures and all fee/capacity ties. They narrow a broad data-foundation claim to a restricted, supply-mediated investment comparison.

The new verifier enumerates raw history actions and expected occupation columns, including chords across source plans that cross $b$. It charges procurement once at the root stock. Separate high-precision smooth diagnostics complement, but do not replace, the uniform analytic proof. All validation is synthetic and separate from the prospective protocol. The earlier 588/538 and finite-task suites remain intact.

This solved frontier is a specific economic boundary within the declared institution. Constrained control, convex hulls, procurement/recourse, envelope identities, uniform stability and general capacity-dependent complementarity are inherited. The inspected predecessors below do not provide an established direct theorem mapping to the entire joint root repair/access/supply comparison. That bounded distinction is not proof of substantial originality; the result may remain a worked special case of established capacity economics.

# 13. Organizational implementation and boundaries

## Aligned optimization versus local quotas

The main institution internalizes all classes' residual losses and service costs. Free AI access cannot lower its optimized value. Harmful rational opt-in therefore is not a conclusion of this model. Under nontransferable department quotas, a department chooses source repair and AI using only its own quota and own costs. That is a different feasible set. Released quota may remain idle instead of improving another class; central investment can then be underprovided. The supplied example explicitly solves the repaired department's quota problem. It does not establish universal over-adoption under unpriced access.

For fixed workflows, a service charge $\eta$ per output-reference unit supports the optimal continuous allocation, with transfers not counted as social costs. This is standard marginal scarcity pricing. With binary adoption or fixed repair costs, a single marginal price need not decentralize the global optimum; a finite coordination or fixed-cost sharing decision remains. No unproved claim of full implementation by a Pigouvian toll is made.

## General technology, false alarms, and unavailable truth

The general results use the concave difference technology (1). A non-exponential example is $b(x)=2\sqrt{x}/\lambda+\tau x$. Its interior residual is $v=[w/(\lambda(L-\tau w))]^2$, truncated at $p$ by (5). The same capacity-release and adoption theorems apply. This is broader than an exponential example, but not technology invariant.

False positives can break the ordering. Suppose scrutiny turns a correct draft into an incorrect one with probability $\alpha(1-\exp(-\lambda e))$. Residual error becomes $\alpha(1-p)+[p-\alpha(1-p)]\exp(-\lambda e)$. If $p<\alpha/(1+\alpha)$, more scrutiny increases errors, and with positive service cost the optimum is zero scrutiny. A source repair crossing that threshold changes the optimal institution discontinuously. The zero-false-positive demand formula is invalid in this case; we provide this as a counterexample, not an extension silently covered by Proposition 3.

If source errors are unverifiable through the permitted reference channel, write residual risk as $f_i+r_i$, where $f_i$ is an irreducible floor. Capacity can reduce $r_i$ only. The program applies to reducible risk with the constant loss $n_iL_i f_i$ added; repair that changes the floor requires an independently capable source-validation channel. If no such channel exists, $p_L$ is unattainable and that repair option must be deleted. Rerunning the same source cannot manufacture the missing evidence.

Loss heterogeneity is already allowed across classes. If severity varies within a class and is observable before allocation, split the class into severity-specific tasks with their own $L_i$. If it is hidden or correlated with detection difficulty, an average $L_i$ is insufficient without a joint distribution; the proved allocation need not hold. Likewise, with correlated catastrophic aggregate losses and a nonlinear risk objective, the additive expected-cost theorem cannot rank tail-risk policies.

## Attribution, granularity and information reuse boundary

Proposition 9 shows that the positive matched-mean timing advantage relies on recipient indivisibility and disappears in the fluid comparison. Proposition 10 retains an exact institution-dependent repair region, with finite-task error bounds, but explicitly gives up unused-access/joint-only activation. Jensen, rounding and convexification are inherited tools; generic downstream capacity release and joint-only activation are also already present in the now-accessible final Tekin-Andradóttir institution.

The expected/pathwise feasible-set distinction itself is inherited constrained-inspection logic. Within this application Proposition 7 calculates the exact investment frontier against all alternatives; Proposition 8 calculates a globally justified matched-mean certification ranking with a recipient-audit feasibility threshold. These are bounded claims, not priority certification. The actual primary-text support and gaps are recorded in Section 2 and Appendix B.

Section 8 replaces the former learning counterexample with an explicit solved benchmark. If a source check certifies all copies with free propagation, repeating independent checks is wasteful. The additive workload in Proposition 5 must not be applied to that case. The adaptive survival result depends instead on residual certification demand and the recipient's scarce-service opportunity. The expected-capacity benchmarks establish no almost-sure guarantee. Section 9 enforces such a bound only for its finite histories; none of the models establishes dynamic queue stability or optimal staffing.

# 14. Measurement implications and completion status

The tiered-supply result in Section 12 further narrows that conclusion: the interaction depends on exposure to the expensive supply tier, not new recipient information. It can turn positive under endogenous capacity and remain positive after smoothing. The flat-price procurement result changes the conclusion at its model boundary: optimizing a separate real capacity input removes the positive fluid repair/access interaction and yields weak substitution, with an exact strict region. This does not invalidate fixed-budget results. It limits their investment interpretation. All procurement conclusions are theoretical and synthetic; the prospective protocol would have to measure stock procurement separately from realized service costs and scarcity transfers. No new study was run.

A field study should randomize at the complete independent reference-pool level or explicitly model spillover exposures. Individual or team assignment within a shared pool can change control outcomes through capacity reallocation even without information sharing. A pool-level two-by-two design identifies the total effect of offered AI and a corpus intervention under that capacity regime; it cannot separately identify source reliability, structure, and the verification mechanism.

To study the present cross-department theorem, the repair must target a designated source-consuming class while AI access is offered to a different class sharing its reference service. Measure recipient outcomes, review-time transfers, source-validation workload, maintenance, and all task classes' final audited losses. Hold model version, prompts, retrieval code, training, task frame, and incentives comparable. A separate mechanism experiment would randomize repair types or service budgets. Neither voluntary usage nor a common observed maturity index supplies that identification.

The separate empirical appendix contains a feasible shadow-workflow pilot, an independent audit rubric, a cost dictionary, assignment rules with pool-level interference, and a runnable design-based estimator with an exact sharp-null randomization test for a small balanced design. Its synthetic test fixture is labeled as such. A single small firm experiment is unlikely to estimate a modest interaction precisely; no confirmatory study or uncollected results shell appears in the main article.

The completed analysis includes the conditional resource solution, spillover decomposition, optional adoption, open-loop reuse and adaptive expected-capacity results. Their KKT, envelope, finite-choice and inspection foundations are inherited. Propositions 7-8 retain their original indivisible-audit scope. Proposition 9 identifies its quantization boundary; Proposition 10 derives the surviving fluid investment frontier and distinguishes conditional complementarity from joint-only activation. These are supported by explicit global source-dominance conditions, not merely a minimum-over-columns identity. The present source comparisons still do not establish substantive originality of this bounded economic result. The Yao-Zheng chapter excerpt establishes an expected inspection/removal-constrained institution; it does not certify the scope of later chapter results or equivalence to the separate 1999 article. Bańka-Chudziak's directly read sampling/posterior model is credited without treating its label-benchmark experiments as our firm evidence. Dogonowski's inaccessible full working text leaves a material overlap/priority question unresolved. These results may still be specializations of existing theory; a different object label is insufficient to establish originality. The restricted two-exposure adaptive action space, the open-loop restriction of the scale theorem, the expected-capacity restriction of Propositions 1-6, the finite fixed-duration histories and restricted supply curves of Propositions 7-15, and unmeasured loss/service primitives limit relevance. These are the strongest remaining reasons a journal might reject the article. They do not invalidate the restricted propositions, but prevent a claim of publication readiness or empirically established organizational importance.

# 15. Conclusion

Within this restricted common-source institution, the sign of the source-repair/AI investment interaction depends on both the audit technology and the capacity supply curve. Divisible recipient work removes a positive matched-mean timing advantage; linear procurement removes positive conditional investment interaction. A two-tier supply curve can restore that interaction even while every optimal hard stock is unchanged. The exact fee regions, all ties, expected occupation mixtures and smooth/primitive robustness are solved, rather than inferred from witnesses. The cost mechanism is differential tier exposure and pooling, not informative evidence about an independent recipient. Free optional access still improves optimized welfare.

The result is a boundary of the claim that AI encourages investment in data foundations, not a universal replacement claim. Earlier propositions remain valid under their declared institutions. Shared inspection, workload complementarity, capacity procurement/recourse and convex/stability methods are inherited. The now-accessible final inspection article resolves a real source-access gap, but the available result-level comparisons do not establish a substantial original economic increment. The theory and synthetic validation provide no enterprise evidence or scientific self-acceptance; the prospective protocol remains separate.

# Appendix A. Complete proofs

## A.1 Proof of Proposition 1

For $p_i>0$, $T_i$ is strictly convex in $v_i$, because $-b_i''(v_i)>0$. The feasible set is convex, as the sublevel set of a sum of convex functions with box constraints. The objective has strictly positive second derivative $-n_i k b_i''$, so any optimum in positive-risk coordinates is unique. A finite-cost feasible point exists at $v_i=p_i$, requiring zero capacity. For $B_d>0$ there is a strictly capacity-feasible point and a minimizer: restrict to the compact box, assign the lower limit of the objective at zero, and use lower semicontinuity. If $b_i(0)=-\infty$, zero residual has infinite resource requirement and is excluded. If $b_i(0)$ is finite, the derivative $L_i-kb_i'(v)$ tends to minus infinity at zero; increasing a zero residual slightly lowers cost and frees capacity. Thus an optimum for $k>0$ has $v_i>0$ whenever $p_i>0$.

The Lagrangian is

$$\mathcal L=\sum_i n_i\{(k+\eta)[b_i(p_i)-b_i(v_i)]+L_i v_i+c_i\}-\eta B_d.$$

For $w=k+\eta$, each positive-risk coordinate minimizes a strictly convex function. Its derivative is $L_i-wb_i'(v_i)$. If $w\geq L_i/b_i'(p_i)$, the constrained minimizer is $v_i=p_i$; otherwise the unique zero of the derivative gives (5). Positive-resource demand strictly decreases with $w$ since $dv_i/dw=-L_i/[w^2 b_i''(v_i)]>0$ and $z_{iw}=-b_i'(v_i)v_{iw}<0$. Demand is continuous at activation and becomes zero at the largest threshold. This gives either slack capacity at $w=k$ or a unique root for $B_d\in(0,Q(k))$. These choices satisfy feasibility, stationarity, nonnegative multiplier, and complementary slackness. Convexity makes them globally sufficient. Conversely any optimum satisfies these conditions, proving the characterization. At $B_d=0$, only $v_i=p_i$ is feasible. The stated multiplier inequalities support it; uniqueness of that multiplier is unnecessary. For (2), $b_i'=1/(\lambda_i v)+\tau_i$; solving $wb_i'(v)=L_i$ gives (6) within its stated activation range.

## A.2 Proof of Proposition 2 and own/recipient accounting

In a binding region with unchanged active set, $Q(p_1,w)=B_d$. For an active class, $v_i(w)$ does not depend directly on its initial $p_i$, so $z_{1p}=b_1'(p_1)$. Differentiating the constraint gives $n_1b_1'(p_1)+Q_w w_{p_1}=0$, proving (7). The derivatives in A.1 imply $v_{jw}>0$ and $z_{jw}<0$. Thus repair reduces price, risk and actual expenditure on loss for other active classes while increasing their service allocation. At slack capacity $w=k$ is fixed. At a class's zero-effort corner, its local resource derivative is zero.

Let $M(p,w)=\min_{0<v\leq p}\{w[b(p)-b(v)]+Lv\}$. In the active region, the envelope gives $M_p=wb'(p)$. At no verification, $M=Lp$ and $M_p=L$. They coincide at activation $w b'(p)=L$, so the piecewise derivative is the continuous expression (8). Strong duality gives $V=\max_{\eta\geq0}\{\sum_i n_iM_i(p_i,k+\eta)-\eta B_d\}$. The envelope theorem, or direct differentiating the primal and using its constraint, yields $V_{p_1}=n_1M_{1p}$. At finitely many active-set changes, integrate the continuous piecewise derivative; no interior formula is extrapolated.

For active class $i$, $C_{iw}=n_i[k z_{iw}+L_i v_{iw}]$. The stationary equation gives $L_i v_{iw}=-w z_{iw}$, hence $C_{iw}=-\eta n_i z_{iw}$. Class 1 also has direct derivative $n_1 k b_1'(p_1)$. The chain rule proves (9). Summing and substituting $Q_w w_{p_1}=-n_1 b_1'(p_1)$ gives $n_1(k+\eta)b_1'(p_1)$, agreeing with (8). Thus accounting across actual class outcomes exactly reproduces the total benefit.

## A.3 Proof of Proposition 3 and the primitive test

For fixed class 1 primitives, (10) implies $Q_1(w)\geq Q_0(w)$ on the relevant price range. Both are decreasing on positive-demand regions. If manual capacity is binding, evaluating $Q_1$ at its manual root gives demand at least $B$, so the assisted root is at least as large. If manual capacity is slack, its price is $k$, the minimum possible. Thus $w_1\geq w_0$. Equation (8) is nondecreasing in $w$. The envelope applied separately to $V_1,V_0$ yields $H_p=n_1[M_{1p}(p,w_1)-M_{1p}(p,w_0)]\geq0$. Integration proves (11), with strictness under the stated active-price conditions. The argument reverses when the demand order reverses. It remains valid at entry/exit points by continuity and piecewise integration.

The capacity envelope is $V_B=-\eta$ wherever differentiable; one-sided versions and integration apply at regime changes. Therefore $H_B=-(\eta_1-\eta_0)$. First change $p_H$ to $p_L$ at capacity $B$, then change capacity from $B$ to $B-h$. Integrating that capacity derivative proves (12) with the stated minus sign.

For (13), differentiating (6) gives $v_w=L/[\lambda(L-\tau w)^2]$ and $b'(v)=L/w$. Thus $z_w=-L^2/[\lambda w(L-\tau w)^2]$. Subtract the two workflows. The difference is decreasing up to the first activation boundary. Positivity at $\bar w$ therefore establishes (10) on $[k,\bar w]$. The lower inequality in (14) gives $w_1(p_H,B)\leq\bar w$, and source-demand monotonicity gives the same upper bound at every smaller $p$. The upper inequality gives a binding manual root at $p_L$; monotonicity extends binding to higher $p$ and to the AI alternative. These facts establish the claimed sufficient conditions. They are sufficient, not necessary.

## A.3b Proof of Corollary 3.1

Under common $L,\tau$, (13)'s class-specific slope is $z_{iw}=-a_i L^2/[w(L-\tau w)^2]$. Hence class 1's share of $-Q_w$ is exactly $\theta_a$. Substituting (7) into (9) gives

$$\frac{dC_1^a}{dp}=n_1 b_1'(p)[k+\theta_a\eta_a],\qquad
\frac{dV_a}{dp}=n_1 b_1'(p)[k+\eta_a].$$

Integrate each from $p_L$ to $p_H$. Conditions (15) imply a strictly negative AI interaction in class 1's repair benefit and a strictly positive system interaction. The difference is borne by class 2's account by identity (9), not by an extra benefit appended to the objective.

For $\tau=0$ and both classes active, summing $n_i a_i\log(p_i L/(a_i w))=B$ and solving yields (16). Differentiating gives $d\log w_a/d\log p=\theta_a$. Therefore

$$\frac{d\log(\eta_1/\eta_0)}{d\log p}
=\theta_1\frac{w_1}{w_1-k}-\theta_0\frac{w_0}{w_0-k}<0,$$

because $\theta_1<\theta_0$, $w_1>w_0>k$, and $w/(w-k)$ decreases in $w$. The maximum ratio is at $p_L$, proving the endpoint test. Strict inequalities and a fixed positive-capacity active region persist under small changes in $\tau$, since the resource root and residuals are continuous in the primitives. This establishes a nonempty positive-correction neighborhood, not a claim that the result holds at every $\tau$.

## A.4 Proof of Proposition 4 and global finite choice

At data state $d$, the organization compares manual cost $V_0(p_d,B_d)+c_M+Fd$ with AI cost $V_1(p_d,B_d)+c_M-S+Fd$. Their cost difference is $H-S$. If access is offered, take the lower; the value gain is $[S-H]_+$. Monotonicity of the positive-part function gives nonnegative access interaction when $H_L\leq H_H$.

Relative to the manual/unrepaired baseline, AI alone has benefit $S-H_H<0$, repair alone has benefit $R_0-F<0$, and the combined configuration has benefit $R_0+S-H_L-F>0$ under (17). There are exactly four binary configurations; thus combined repair and AI uniquely minimizes their costs under strict inequalities. Under access without repair the manual configuration is retained, whereas under access with repair AI is selected because $S>H_L$. Fixed costs and service reservation have already entered these quantities. For more finite alternatives, solving (3) globally within each and taking the minimum is globally valid by exhaustion of the feasible union. No convexity of the discrete union is assumed.

## A.5 Proof of Proposition 5 and the drafting-cost result

For fixed $n$, integrate (8) over the source-error interval to obtain (18). For fixed $p,w$, total demand has form $n z_1(p,w)+Q_{-1}(w)$, nondecreasing in $n$. The capacity-root argument in A.3 therefore implies that $w(n,p)$ is nondecreasing in $n$, including slack and zero-effort regimes. The integrand $\min\{L_1,w b_1'(p)\}$ is nonnegative and nondecreasing in $w$. Multiplication by $n$ preserves monotonicity, and positivity over a nonzero source interval makes $R(n)$ increase for positive $n$. For $n=0$, define $R(0)=0$. Bounding $w$ below by $k$ gives the lower bound (19); bounding the integrand above by $L_1$ gives the upper bound. The exact binary source comparison is $F\leq R(n)$.

For $h>0$, decompose $V(p_H,n,B)-V(p_L,n,B-h)$ into source improvement at $B$ minus the cost of lowering output capacity under the repaired state. Integrate $V_B=-\eta$ to obtain (20). Since a valid optimal $w$ never needs exceed the largest activation threshold, $\eta\leq\max_i m_i$ is a valid loose bound. Hence the capacity penalty is at most $h\max_i m_i$. The model does not guarantee monotonicity of that penalty in $n$.

Finally, write $W(n)=U(n)-\min_d\{V(p_d,n,B)+Fd\}$ for $h=0$. At drafting costs $c_H>c_L$, let $n_H,n_L$ maximize $W(n)-cn$. Adding their two optimality inequalities gives $(c_H-c_L)(n_L-n_H)\geq0$, so $n_L\geq n_H$ (with the largest-optimum selection at ties). At a given $n$, repair is optimal if and only if $R(n)\geq F$. Since $R(n)$ increases, the largest repair selection is nondecreasing in $n$. Together these facts prove the stated monotonicity. The finite set ensures existence. The conclusion does not concern cost changes that also perturb source probabilities, severity, reference technology, or $h$.

## A.6 Complete proof of Proposition 6 and the finite adaptive solution

First consider deterministic histories. Without a first check, the only useful source choices are neither check or a second-only check. Once the first is checked, a clean finding implies both source-dependent outputs can be correct without further work. On a fault finding the three useful actions are leave the second unchanged, propagate its correction, or check it separately. Extra checks on a certified clean source and checks after a perfectly corrected output weakly increase cost and capacity without reducing loss or adding information. Removing them cannot destroy optimality. This proves the five unrepaired source plans in Section 8.1 exhaust undominated histories. Prior repair makes all output source checks redundant. The recipient has no informative action about $Z$, and its errors are independent, so it can be placed after source information is observed without restricting any useful policy under expected capacity. It has $m$ actions at an unsignaled history or $m$ at each of the two signaled histories. This proves the column counts. Randomized decisions at histories can be sampled as a deterministic contingent action table before $Z$; averaging such tables reproduces their probability law. Thus their attainable expected cost/resource pairs form precisely the convex hull used in (22).

A finite feasible simplex intersected by one resource half-space is compact. A linear objective attains a minimum at an extreme point. If its resource constraint is slack an extreme point has only one positive weight: two positive weights admit a nonzero simplex-preserving perturbation that remains feasible in both directions. If capacity binds, three or more positive weights admit a nonzero perturbation preserving both normalization and resource, since two linear equations in at least three unknowns have a nontrivial nullspace. Small perturbations in both directions preserve nonnegativity, contradicting extremality. Two supported columns with the same capacity also admit a perturbation, unless reduced to one. Otherwise their weights are uniquely determined by their capacities and $B$, so they straddle $B$. This proves exhaustive single/pair minimization, including a feasible column exactly on the boundary. Infeasibility is detected if no column has capacity at most $B$.

For (23), source dual costs after subtracting the common recipient constant are $T$, $w+qL_s$, $w+qL_s$, $w\ell$, and $w(1+q)$. The last is no smaller than $w\ell$, since $\gamma<1$. If $w\leq T/\ell$, then $w\gamma\leq2q\gamma L_s/(1+q\gamma)<L_s$. Consequently $w\ell\leq w+qL_s$. If $w>T/\ell$, then $w>qL_s$ because $\ell<2$, so $w+qL_s>T$. Neither middle plan can beat the smaller of $T,w\ell$. This proves the envelope; the equalities include ties. Source certification is strictly best at $w=w_0$ under (24).

For a general feasible adaptive plan, add $\eta Q$ to cost with $\eta=w_0-k>0$. In this dual objective, service costs $w_0$ per unit, while actual production and residual loss are unchanged. Recipient actions $M0,M1,A0,A1$, net of $c$, cost respectively

$$D_M,\quad w_0t_M=D_M,\quad D_A-S,\quad w_0t_A-S.$$

Both AI costs are strictly greater than $D_M$ under (24). The recipient's best action is therefore manual at each source history. Contingent recipient choices cannot improve this minimum because its primitives do not depend on the signal and the same price applies in both branches. Source policy $C_{1P}$ costs $w_0\ell$, strictly less than its alternatives by (23). Thus every feasible unrepaired plan satisfies the dual bound

$$C\geq c+w_0\ell+D_M-(w_0-k)B.$$

Always using $C_{1P}$ and auditing the manual recipient with probability $y$ has expected workload $\ell+y t_M=B$. Such a plan is attainable by mixing two complete columns, and its cost is $c+kB+D_M(1-y)$. Substitution of $w_0t_M=D_M$ shows it attains the bound. This proves (26), including exclusion of AI even when it is chosen after the source finding. Binding capacity and the shadow price $w_0-k$ follow, with no assumed fixed verification effort.

After prior repair, use price $w=k$ and zero scarcity multiplier. Manual auditing beats no audit since $D_M>kt_M$. AI auditing beats manual auditing since $S>k\Delta$. It beats unaudited AI since $D_A>S+D_M>k\Delta+kt_M=kt_A$. It also beats unaudited manual by transitivity. Without access manual auditing is consequently optimal; with access AI auditing is optimal. Both fit because $h+t_A<B$ and $t_M<t_A$. No other action or mixture has smaller unconstrained cost, proving (27) globally. Subtracting the four cells proves (28), and subtracting the repaired manual cost before $F$ from (26) gives (29). Comparing the two repaired versus unrepaired access cells gives the investment inequalities. If $R_0<F<R_0+\delta$, (26) ties the two unrepaired cells while (27) places the repaired-access cell strictly below them and the repaired-no-access cell strictly above. The joint binary choice is therefore globally optimal. The numerical parameters strictly satisfy all restrictions, proving nonemptiness; continuity makes a neighborhood admissible. This also proves the stated adoption interval by the same action comparisons.

For the synthetic entry thresholds, when $0\leq S<4$ the unrepaired dual bound continues to hold strictly against both AI actions, while a manual mixture attains it. At $S=4$ the AI actions tie, so AI can be optimal. At $S>4$ any zero-AI optimum would have the no-access value 12.4. That optimum contains an unaudited manual recipient mass $1-y=0.05$; replacing any positive part by unaudited AI strictly lowers cost by $(S-4)$ times the replaced mass with unchanged capacity. Hence no zero-AI policy remains optimal. After repair, for $S<1$ manual audit strictly beats both AI actions, and at $S>1$ AI audit strictly beats all other actions and is feasible. The entry values are thus exactly 4 and 1, with set-valued choices at equality.

For the slack null in Section 8.2, at price $k$ source plan $C_{1P}$ is optimal because $k\ell<T$; recipient audits are optimal with and without access under the displayed synthetic primitives. All fit at $B=10$. The total is a source term $k\ell$ or $F$ plus a recipient optimum independent of source repair. The factorial contrast cancels. Finally, if unrepaired $C_{1P}$ is optimal in each relevant regime and prior certification has $h=\ell,F=k\ell$, the two source alternatives have identical expected resource, monetary cost, and zero loss. The source signal cannot improve an independent recipient's primitives; any conditional recipient distribution can be implemented as an unconditional mixture, with identical expected service and loss. Replacing source plans in either direction therefore preserves feasible value in this region, proving the conditional resource-equivalence null. These null arguments do not claim equivalence where choosing $N$ can dominate certification. $\square$

## A.7 Completeness, pathwise frontier, and proof of Proposition 7

The history reduction in A.6 remains valid because deleting a redundant check weakly reduces load in every history, not merely on average. If no first check is chosen, a second check is chosen before its finding and the recipient can condition on the finding only if it is made. Otherwise its action must be identical in both hidden-fault histories. If a first check is chosen, clean and fault findings permit distinct recipient decisions. The only useful fault actions are no propagation, propagation, or a separate second check. Clean-source rechecks add positive cost without new information or accuracy and are dominated history by history. Hence the 18/68 unrepaired and 2/4 repaired useful columns are complete. The standalone raw-history verifier additionally enumerates redundant clean rechecks, giving 30/116 unrepaired columns and 2/4 repaired columns, or 152 across all four cells. Every useful column is included among them.

A randomized sequential policy can be implemented by drawing its complete contingent decision table independently of $Z$ before production. With finitely many histories, any table of positive probability containing a positive-probability history that violates $B$ is inadmissible. Conversely a distribution supported on admissible tables satisfies the bound for every realized table and history. Expected cost is a convex combination of admissible column costs, no smaller than their minimum. This proves the finite global solution and why expected-load mixtures of inadmissible columns are excluded. Tied minimum columns can be mixed freely. Removing a signal never permits hidden-state conditioning; this is enforced by the single recipient action in the no-check plan.

For a fixed source plan, remaining capacities determine the recipient action minima (30). Without source checking, its action is unconditional and source loss is $2qL_s$. Either single-check plan has source load one in both histories, expected loss $qL_s$ and the same available recipient actions. First-check propagation has source loads 1 and $1+\gamma$, with zero source loss and expected source cost $k\ell$. Separate fault-branch rechecking has loads 1 and 2, hence weakly smaller feasible recipient sets in the fault history, the same correction/information, and strictly higher expected source cost $kq(1-\gamma)$. It is strictly dominated. This proves (31), including all zero-check corners; (32) follows from deterministic source load $h$ and the all-in cost convention. Minimizing these two root alternatives solves the full investment problem, because the root binary decision is fixed before the fault. A root lottery supported on feasible complete plans also cannot beat their minimum.

For the benchmark, all useful realized loads are a source load from $\{0,1,3/2,2\}$ plus a recipient load from $\{0,1,2\}$, with the unsignaled and signaled constraints just described; repaired loads are $1/10,11/10,21/10$. Taking the maximum across the two source histories for every contingent combination gives precisely (33). Every listed maximum is realized by a column, and there are no others. Equality at the capacity boundary is feasible. This proves the breakpoint characterization without a grid argument.

On $21/10\leq B<5/2$, the recipient at residual capacity $B$ can audit either workflow, whereas at $B-1$ it can audit only manual work and at $B-3/2$ it cannot audit either. Consequently the three branches in (31), net of $c=10$, are

$$10+\min\{1,2-S\},\quad
6+\min\{1,8-S\},\quad
5/4+\tfrac12\min\{1,8-S\}+\tfrac12\min\{4,8-S\}. \tag{42}$$

The third is strictly below the second: their difference (second minus third) is $19/4+[\min\{1,8-S\}-\min\{4,8-S\}]/2\geq13/4>0$. To compare the first and third, split $S\geq0$ at 1, 4 and 7. For $S\leq1$ the gap is $29/4$; for $1\leq S\leq4$ it is $33/4-S\geq17/4$; for $4\leq S\leq7$ it is $25/4-S/2\geq11/4$; for $S\geq7$ it is $11/4$. Thus propagation strictly dominates every alternative source architecture throughout the strip. Expanding its two recipient minima proves (34). The clean-branch comparison is $1$ versus $8-S$ and the fault-branch comparison is $4$ versus $8-S$, giving exactly the stated switches and ties. Independent branch lotteries span the stated adoption intervals. In the no-access cell both branches are manual, so its cost is $10+5/4+1/2+2=55/4$.

After repair $B-h\geq2$, so either audit fits. Audited manual costs 1 net of $c$, and audited AI costs $2-S$. Unaudited actions are strictly dominated by their own audited counterparts, saving respectively 3 and 6. Thus the recipient switches at $S=1$, with both audited actions optimal at equality. Subtracting the repaired cost before $F$ from (34) gives all four pieces of (35). Both root choices minimize at equality, while strict inequalities select the stated one. These are necessary and sufficient comparisons over all feasible plans.

On (36), the expected-capacity proof in A.6 applies: $\ell=5/4$, $w_0=4$, $2qL_s/\ell=8>4$, $1<S<4$, $D_A>S+D_M$, $\ell<B<\ell+t_M$, and $h+t_A<B$. Its formula (26) simplifies to $19-3B$; repaired audited AI costs $F+12-S$. Subtracting gives $T_E=7+S-3B$; for manual access the repair threshold is $8-3B$. Hard joint repair requires $F<7/4+S$, hard rejection of repair alone requires $F>11/4$, and expected rejection of joint repair requires $F>7+S-3B$. Their conjunction is exactly (37), and expected repair alone is then also rejected because $11/4>8-3B$ on (36). Access alone is unused because $S<4$. Nonemptiness follows from $S>1$ and $B>21/10>7/4$, respectively for the two lower bounds. At each equality the corresponding compared costs coincide, which proves all weak-choice qualifications. Setting $S=2$ makes $9-3B<11/4$ on (36), yielding the claimed simplified interval. Substitution gives the exact seed costs and gains. No empirical premise is used. $\square$

## A.8 Proof of Proposition 8 and the timing boundary

The left budget bound in (38) implies $B\geq1+\gamma>\ell$ and $B-1\geq t_M$. The upper bound gives $B-\ell<t_M$ and $B-1-\gamma<t_M$, because $\ell<1+\gamma$. Hence first-check propagation permits the manual audit only after a clean finding, whereas prior repair permits no recipient audit. Their hard costs are the two expressions stated above. The interval has positive length exactly when $1+\gamma<\ell+t_M$; the other left endpoint, $1+t_M$, is always below $\ell+t_M$. This is $t_M>(1-q)\gamma$.

It remains to establish global optimality without imposing propagation. Since $B\geq1+t_M$, the no-source-check branch audits the manual recipient and costs $c+2qL_s+kt_M$. Subtracting propagation's cost yields $2qL_s-k\ell-q(D_M-kt_M)>0$ by (39). Either single-check/no-propagation branch audits the recipient and costs $c+k+qL_s+kt_M$. Subtracting propagation yields $q[L_s-k\gamma-D_M+kt_M]>0$. Separate second checking is strictly dominated history by history as in A.7. Thus propagation is globally best among all unrepaired policies. Prior repair has no feasible audit and its zero-audit recipient action is the only undominated no-access action. Subtracting their costs gives (41). All mixtures satisfy the same ranking.

For expected capacity, use $w_0=D_M/t_M>k$. The source frontier (23) and strict inequality in (38) make first-check propagation source-optimal in the dual problem. Manual audit and no audit tie at this price. The unrepaired policy can therefore use certification always and audit the recipient with probability $(B-\ell)/t_M\in(0,1)$, attaining the bound (40). With prior repair, source monetary cost is $k\ell$ and remaining expected service is $B-\ell$. The same recipient lottery gives exactly (40); its one-task linear program is minimized by using all that service because $D_M>kt_M$. This proves equality of the globally optimized expected alternatives. Expected randomization can include a recipient audit in a history whose realized load exceeds $B$; pathwise capacity cannot, which is why the two arguments do not contradict each other.

At the rational benchmark, (38)-(39) hold on $2\leq B<9/4$. Substitution gives hard costs $55/4$ and $61/4$, and expected common cost $19-3B$. At $B=9/4$ repaired load $\ell+t_M$ fits exactly, dropping its cost by $D_M-kt_M=3$ to $49/4$. Until $B=5/2$ the fault-branch recipient audit still does not fit after propagation. Its global hard cost remains $55/4$: the competing source costs in (31) remain strictly larger. At $B=5/2$ both recipient audits fit after propagation and cost $10+5/4+1=49/4$, equal to prior repair. This proves the full stated boundary behavior, including equality budgets. The beneficiary of the source finding is capacity allocation, not a posterior improvement in the unrelated recipient's quality. $\square$

## A.9 Proof of Proposition 9

For $n$ manual tasks an audit saves $\beta/n>0$ and uses $t_M/n$ service. The maximum feasible audit count is $\min(n,\lfloor nx/t_M\rfloor)$, so the recipient optimum is exactly $D_M-\beta f_n(x)$. This argument concerns deterministic feasible counts. A lottery over them cannot improve the minimum or make a larger count feasible on a realized history.

The source-plan reduction in A.7 remains complete: after a finding every history permits an independently selected recipient count vector; without a finding one vector must be used. The first action cannot depend on the hidden fault. Removing a clean-source redundant check frees capacity history by history and never increases loss. Separate second checking after a detected fault is dominated by propagation when $\gamma<1$: it corrects the same exposure with the same information but uses more service. Any behavioral lottery can again be implemented by a distribution over complete contingent tables; hard feasibility requires every supported table to be feasible.

Let $g(x)=D_M-\beta f_n(x)$, or its fluid counterpart. It is nonincreasing and lies in $[kt_M,D_M]$, a range of width $\beta$. Propagation minus either single-check/no-propagation policy has expected cost difference

$$q\{k\gamma-L_s+g(B-1-\gamma)-g(B-1)\}
\leq q(k\gamma-L_s+\beta)<0.$$

Propagation minus no checking is at most $k\ell-2qL_s+\beta<0$. Both follow from (44), uniformly over all recipient allocations and $n$. The no-check policy still cannot condition on $Z$; its recipient capacity is $B$ in both hidden histories. These comparisons establish global unrepaired dominance. Weak versions support ties. With prior repair the recipient service is deterministically $B-\ell$ and the all-in cost is $k\ell$. Subtracting the two optimized costs gives (45), with no second charge for $kh$.

The two random residual capacities have mean $B-\ell$. Concavity of $f_\infty$ on nonnegative service gives the Jensen inequality in (46). Write $e_n(x)=f_\infty(x)-f_n(x)\in[0,1/n]$. The difference $\Delta_n-\Delta_\infty$ divided by $\beta$ is $e_n(B-\ell)-(1-q)e_n(B-1)-qe_n(B-1-\gamma)$. Both its first term and weighted latter terms lie in $[0,1/n]$, so its absolute value is at most $1/n$, not the looser $2/n$. Combining this with $\Delta_\infty\leq0$ gives the positive-gap bound. On (38), the clean residual is at least $t_M$, while fault and deterministic residuals are less than $t_M$. Substituting these three branches of $f_\infty$ into (45) and using $\ell=1+q\gamma$ gives (47). The synthetic values follow by exact floors; none are empirical estimates. $\square$

## A.10 Proof of Proposition 10

The four recipient action points are precisely their aggregate service and net costs. In the fluid limit arbitrary nonnegative action masses summing to one are feasible; their mean service must not exceed the residual budget at that same source history. Thus the lower convex envelope solves the one-history problem. It does not average service between clean and faulty histories. For $1<S<4$, $A0$ is strictly dominated by $M0$. The segment slopes between $M0,M1,A1$ are $-3$ and $1-S\in(-3,0)$, proving (49); complete audited AI is optimal when $x\geq2$. At $S=1,4$ weak slope comparisons give the stated ties.

For finite $n$, costs depend only on action counts. Labeling tasks differently merely duplicates equivalent allocations. With $1<S<4$, if an allocation contains both an $M0$ task and an $A1$ task, replacing them by two $M1$ tasks uses the same service and lowers net cost by $(4-S)/n>0$. For $x<1$ any $A1$ would imply an $M0$ since total load is below $n/n$; hence only $M0,M1$ are needed, with audited count $\lfloor nx\rfloor$. For $1\leq x<2$, all $M1$ tasks fit and any optimum can be selected with no $M0$; upgrading $\lfloor n(x-1)\rfloor$ to $A1$ is optimal because each upgrade saves $(S-1)/n$. This proves the finite formula and sufficiency of count enumeration. At endpoints the same replacements are weakly improving, so the displayed value remains attained, although other minimizers exist. Segment rounding costs at most $3/n$ and $(S-1)/n$, respectively.

Every recipient optimum, finite or fluid, lies between $2-S$ (the lowest action cost) and 4 (the always-feasible manual/no-audit cost). Its range is therefore at most $W=2+S$. Repeat A.9's source comparisons with $W$ in place of $\beta$: propagation beats either single check if $L_s>k\gamma+W$, and no checking if $2qL_s>k\ell+W$. Redundant clean and fault rechecks remain dominated. At $S\in[1,4]$, $W\leq6$, so $10>1/2+W$ and $10>5/4+W$ strictly. This establishes globality, including all recipient allocations and source lotteries, rather than imposing propagation.

On the budget strip, clean residual $B-1\in[11/10,5/4]$ permits the $M1/A1$ segment and fault residual $B-3/2\in[3/5,3/4]$ permits the $M0/M1$ segment. With source mean service $5/4$ and production 10, substituting into these minima gives (50). In the finite case the fault manual-audit mass is $m_n$ and clean audited-AI upgrade mass is $b_n$, giving (51). No-access clean auditing is complete; all rounding occurs in the fault branch. Its loss is $(3/2)[B-3/2-m_n]\leq3/(2n)$. With access the additional clean rounding loss is $(S-1)[B-2-b_n]/2$, proving (52). Prior repaired full audits fit because $B\geq h+t_A=21/10$, so those cells are exact for every $n$.

For expected capacity, the convex hull of equal task allocations with ex ante lotteries is the same four-point hull even at finite $n$: each pure action applied to all tasks supplies a vertex, and every finite allocation is a convex combination of vertices. More importantly, this institution can average service across fault histories, unlike the hard model. Use the retained dual certificate at effective service price $w=4$: source propagation strictly minimizes the source price envelope, and the recipient's manual/no-audit and audited-manual actions tie, while AI actions are strictly worse for $S<4$. A feasible manual audit lottery uses expected recipient service $B-5/4\in[17/20,1]$. Its actual cost is $19-3B$. At $S=4$ extra actions can tie but cannot improve this bound; at $B=9/4$ the manual audit is complete and still attains it. Repaired full audit cells are unchanged. This proves the expected comparison globally, including optional access and every source policy.

Subtract the respective repaired costs before $F$ from (50) to obtain (53). Repair is a binary root choice over optimized cells, so each weak threshold condition is necessary and sufficient; equality retains both choices. The three strict requirements in (54) are respectively rejection of hard repair without access, rejection of expected repair with access, and selection of hard repair with access. Elementary subtraction gives both identities in (55); each is strictly positive on the declared open strip, proving nonemptiness. Expected rejection without access follows from $T_E-(8-3B)=S-1>0$. The finite thresholds have $T_{H,n}\geq T_H$, $T_{0,n}\leq T_0+3/(2n)$, and $T_{H,n}-T_{0,n}=(S-1)(1-b_n/2)>0$; hence their exact comparison interval is also nonempty and the stated finite robustness bound follows. No limit exchange of infeasible policies is used.

Finally (51) directly gives the finite access-alone gain, and its limit yields (56). Repaired access gain is $S-1$, so the interaction equals the difference of repair thresholds in (55). It is positive while access alone is already valuable. Thus conditional complementarity does not imply joint-only activation. The endpoint and fee ties follow from the same weak comparisons and feasible exact capacity filling; outside this strip different hull segments or source choices can apply. All numerical witnesses are exact substitutions into the proved formulas, not additional empirical evidence. $\square$

## A.11 Proof of Proposition 11, completeness and all ties

First establish the recipient envelope independently of source information. The four recipient actions have (service,cost) pairs $(0,4),(1,1),(0,7-a),(2,1-a)$. For $0\leq a\leq3$ the second zero-service point is weakly dominated. The remaining three lower-hull vertices give (57); at $a=3$ the middle vertex is collinear, and at $a=0$ the second segment is flat. A mass allocation is selected within each observed history, so its load is deterministic within that history. No mixing between histories is used. Minimizing the two segment slopes plus $\rho$ proves (58)'s formulas for $M_j$ and every listed recipient argmin, including flat rays at zero procurement price. The fee includes prior source service; adding $kh$ again would be incorrect.

We next prove globality rather than impose propagation. The same two-exposure action tree permits no checking; a single first or second check; a first check followed by propagation or an independent second check after a fault; and a redundant second check after a clean finding. Before the first finding all decisions are independent of the hidden fault. Root randomization and random recipient allocations are allowed only over plans feasible in every realized history. The first-check clean/fault branches exhaust information from the binary source. After a clean finding, another source check has no correction value. After a fault finding, propagation removes the second exposure's error using $\gamma<1$ service instead of one independent check. Hence removing clean rechecks and replacing fault rechecks by propagation weakly reduces every history's load and strictly reduces expected service cost whenever the removed action occurs. These replacements cannot reduce recipient options. The remaining partial plans are no checking, one check, or propagation. Optional omission of fault correction is precisely the one-check plan. This exhausts the original source menu, including redundant and conditional checks.

For a single-check plan at hard stock $b\geq1$, propagation at stock $b+\gamma$ leaves residuals $b+\gamma-1$ and $b-1$, both at least its residual $b-1$. Replicate the competitor's recipient allocation without using hidden information. The change in expected source service, source loss and procurement is at most $\gamma(q+\rho)-10q$. For no checking at $b\geq0$, propagation at $b+1+\gamma$ leaves residuals $b+\gamma,b$, both at least $b$. The change is at most $\ell+\rho(1+\gamma)-20q$. Both bounds are strictly negative on $q,\gamma\in[2/5,3/5]$, $\rho\in[0,3]$: the first is at most $54/25-4<0$ and the second at most $159/25-8<0$. These conservative separate extrema suffice. Thus even stocks below $d$ in competing plans cannot be globally optimal. Dominance applies to each realized lottery column; averaging cannot restore a dominated optimum or make an infeasible column feasible. The benchmark bounds reduce to $-19/4+\rho/2$ and $-35/4+3\rho/2$.

For expected capacity, $B\geq E[\text{service}]$ implies $\rho B\geq\rho E[\text{service}]$. At positive price equality can be chosen. The effective price of source service is therefore $1+\rho$, independently of recipient allocations. Source propagation costs $(1+\rho)\ell$; no checking costs $20q$; a single check costs $1+\rho+10q$. Propagation is strictly cheaper: its excess over a single check is $q((1+\rho)\gamma-10)<0$, and $(1+\rho)\ell\leq136/25<8\leq20q$. A lottery cannot beat the smallest component of this linear expected objective. The recipient's minimum is $M_j$, even if its actions depend on a finding, because each conditional term has the same price and the same quality primitives. This proves the expected solution and null without assuming a fixed recipient workflow. At zero procurement price excess stock is free and the minimum service needed for a cost-minimizing allocation gives the lower endpoint of the stated ray.

Under hard propagation, convexity of $g_j$ gives a convex piecewise linear objective on $[d,\infty)$. For access its slopes on $(d,2),(2,2+\gamma),(2+\gamma,3),(3,3+\gamma),(3+\gamma,\infty)$ are respectively

$$\rho-3,\quad\rho-H,\quad\rho-a,\quad\rho-qa,\quad\rho.\tag{65}$$

Its minimum occurs where these nondecreasing slopes cross zero; a zero slope gives the entire closed intervening interval. For $0<a<3$, $0<qa<a<H<3$, producing exactly the table. If $a=0$, merge all zero-benefit segments, obtaining the no-access list. If $a=3$, merge the first three equal-slope segments, obtaining the endpoint list. Since $\gamma<1$ in the robustness neighborhood, the ordered breakpoints are distinct except for these slope mergers. In the benchmark they are $3/2,2,5/2,3,7/2$, giving the requested slopes $\rho-3,\rho-(3+a)/2,\rho-a,\rho-a/2,\rho$. The repaired and expected argmin sets follow from the already proved envelope minimization. Strict source dominance leaves no additional source ties. Fee equality joins the two root choices with their entire capacity sets. This proves completeness of the solution.

## A.12 Proof of Proposition 12 and the strict region

Subtracting repaired pre-fee cost from (58) gives (60). To compute the hard premium evaluate (59) at its slope-selected breakpoints. For no access the expected optimum uses recipient mass one; hard stocks $2+\gamma$ or $2$ yield excesses $\gamma(1-q)\rho$ and $\gamma q(3-\rho)$, respectively. Their equality is $\rho=3q$, giving (61). For access with $\rho\leq a$, the expected optimum uses mass two. Hard stocks $3+\gamma$ or $3$ yield excesses $\gamma(1-q)\rho$ and $\gamma q(a-\rho)$. For $\rho\geq a$, the expected optimum uses mass one. Hard stocks $2+\gamma$ or $2$ yield excesses $\gamma(1-q)(\rho-a)$ and $\gamma q(3-\rho)$. At $\rho=a$, all intermediate stocks in the table have identical objective and both formulas give zero. This establishes (62), including endpoints and all slope ties. Nonnegativity also follows from the relaxation from hard to expected capacity, but that generic nesting is not the derivation of the exact premiums.

If $\rho\leq a$, the two branches for $P_1$ meet at $qa$. Below that price both premiums equal $\gamma(1-q)\rho$. Above it, $q(a-\rho)$ is strictly below each of $(1-q)\rho$ and $q(3-\rho)$ whenever $0<a<3$, so $P_1<P_0$. If $\rho\geq a$, the branches for $P_1$ meet at $H=a+q(3-a)$. Below $H$, $(1-q)(\rho-a)$ is strictly below both branches defining $P_0$. Above $H$, both premiums equal $\gamma q(3-\rho)$. Equality holds at the boundaries; at $a=0$ or $a=3$ direct substitution gives equality everywhere. This proves the necessary and sufficient strict interval and excludes any positive interaction in the declared domain.

Comparing each unrepaired cost with $F+r_j$ proves every repair/fee qualification in (64). Its inequalities are strict and continuous, hence define an open set in $(a,\rho,F,q,\gamma)$ in the interior of the primitive neighborhood. The explicit unique-stock witness lies strictly inside that set. Substitution into (58)-(62) gives all rational examples in Section 11.2. At fixed stock the additional procurement charge cancels from all fee thresholds, which verifies rather than contradicts the old fixed-stock interaction. Optional access enlarges the action set and therefore cannot worsen the globally minimized objective, even when it reverses repair selection. All examples are synthetic model calculations; no empirical inference is involved.

## A.13 Proof of Proposition 13, including expected source mixtures

Use the source tree established in A.11: no checking; either single check; first checking followed by no correction, propagation or an independent fault recheck; and optional redundant clean rechecking. Recipient allocations cannot depend on the hidden fault without a finding. The recipient envelopes are (57) with $a=1$. In particular the four primitive recipient points are $(0,4),(1,1),(0,6),(2,0)$; their lower hull gives $g_0(x)=4-3\min(x,1)$ and $g_1(x)=g_0(x)-\min((x-1)_+,1)$. No-check recipient actions are identical across hidden fault states. After a source check, actions may depend on its finding, with unchanged recipient quality primitives.

For hard capacity, $C$ is nondecreasing and 3-Lipschitz. Propagation at stock $b_0+1/2$ replicates or improves every recipient residual of any single-check plan at stock $b_0\geq1$. The source service/loss change is $-19/4$, and procurement increases by at most $3/2$, leaving a strict improvement at least $13/4$. Against no checking at any stock $b_0\geq0$, propagation at $b_0+3/2$ replicates every recipient allocation and changes source cost by $-35/4$, with procurement increasing by at most $9/2$: improvement is at least $17/4$. These comparisons include all low-stock competitors. Independent fault rechecking uses one unit instead of propagation's half unit with the same source correction; redundant clean checking has no quality benefit. Removing either reduces service and cannot increase procurement or restrict recipient choices. This proves global source dominance, not just a local propagation optimum. A hard lottery at a given root stock averages costs of individually feasible plans, each bounded below by the globally minimized pure-plan cost. It cannot improve that bound or use infeasible plans.

Expected capacity requires a different argument. Let $Q$ be total realized service. Since $C$ is strictly increasing, a feasible occupation mixture can choose its root stock as $B=E Q$. Apply the following transformation to each source-policy component, replicating its recipient actions after a first-check finding. Replacing a single check by propagation increases mean source service by $1/4$ and decreases expected source service-plus-loss cost by $19/4$. Replacing no checking by propagation increases mean service by $5/4$ and decreases source service-plus-loss cost by $35/4$; replicate its unconditional recipient actions in both findings. At the aggregate mean, the procurement increment is at most three times the weighted increment in mean service. Consequently the improvement per unit mixture weight is at least $4$ for a single check and $5$ for no checking. Replacing redundant/fault rechecks decreases mean service and service cost. Thus any mixture with positive weight on these other plans is strictly dominated. This transformation operates on the aggregate $E Q$ and on $C(E Q)$, not on $E C(Q)$ or a separate price for each column. Source lotteries with zero weight on inferior plans reduce to propagation with conditional recipient mixtures.

Under propagation, mean source service is $5/4$. If $x$ is mean recipient service, convexity gives $E g_j(x_Z)\geq g_j(x)$, even allowing conditional allocations and lotteries. Conversely a common fluid recipient allocation attains $g_j(x)$ at mean service $x$. Hence the complete expected occupation problem is exactly $\min_{x\geq0}\{45/4+g_j(x)+C(5/4+x)\}$. The same lower convex envelope is obtained by convexifying all raw source/action columns, including cross-source chords; the dominance proof explains why those extra columns cannot improve it. Repair gives $\min_{x\geq0}\{10+g_j(x)+C(h+x)\}$, before all-in $F$. These reductions include zero-effort choices $x=0$. Binary repair/access choices compare their optimized cells; a lottery of complete root choices is evaluated with procurement on its realized root stock, not on a fictitious stock pooled across root choices.

For repair, $h+1=11/10$ and $h+2=21/10$ lie below $b$. The recipient cost slopes before/after these vertices, plus $\rho\in(1/2,1)$, give unique minima at $h+1$ without access and $h+2$ with access. This proves (67). Hard propagation has source base cost $45/4$ and objective $45/4+[g_j(B-1)+g_j(B-3/2)]/2+C(B)$ on $B\geq3/2$. For no access the pre-procurement slopes are $-3$ on $(3/2,2)$, $-3/2$ on $(2,5/2)$, and zero afterwards. Since $b\in(21/10,9/4)$ lies in the middle interval, its unique minimum is $5/2$ for $v<3/2$, $b$ for $v>3/2$, with the whole interval $[b,5/2]$ at equality. For access the successive slopes on $(3/2,2),(2,5/2),(5/2,3),(3,7/2),(7/2,\infty)$ are $-3,-2,-1,-1/2,0$. Below $b$, $\rho<1$; above it, compare $v$ with $1,2$. Since $\rho>1/2$, the optimum never exceeds 3. The resulting stocks and flat intervals are exactly those listed. Substituting them proves (68)-(69).

For expected capacity, below stock $9/4$ the recipient marginal improvement is 3 and above it the no-access improvement is zero. Below $b$ the slope is $\rho-3<0$; from $b$ to $9/4$ it is $v-3\leq0$. This gives unique stock $9/4$ if $v<3$, but **every stock in $[b,9/4]$** if $v=3$. Access adds the recipient segment with marginal improvement one between stocks $9/4$ and $13/4$, both above $b$. Comparison of $v$ with one proves the remaining stocks and the interval at equality. At $v=3$ the same earlier interval is optimal. Substitution gives (70). All adjacent formulas coincide at shared boundaries. This completes both the global and tie claims.

## A.14 Proof of Proposition 14 and fee qualifications

Equation (67) gives $R_1-R_0=\rho-1$. Subtract (68) from (69), then add $1-\rho$. The successive unrepaired cost differences are $-3/4+v/2$, $-1/4$, $-1/4+(v-3/2)(5/2-b)$ and $1-b/2$. They give all four pieces in (71). Similarly, (70) gives $E_1-E_0=v-1$ for $v\leq1$ and zero for $v\geq1$, proving $I_E=\min(\kappa,1-\rho)$.

At $\kappa=0$ the hard interaction is $1/4-\rho/2<0$. The first piece increases at rate $1/2$ until $v=1$, reaching $3/4-\rho$, followed by a plateau until $v=3/2$. The third piece increases at rate $5/2-b>0$ until $v=2$, reaching $r_c-\rho$; the final piece is constant. If $\rho<3/4$ its first zero is $\kappa=\rho-1/2<1-\rho$ and it stays positive afterwards. At $\rho=3/4$ the first and second transitions create precisely the zero plateau $1\leq v\leq3/2$. For $3/4<\rho<r_c$ the unique zero lies in the third segment at the stated $v_*$. At $\rho=r_c$ the third segment ends at zero and the last segment remains zero. Above $r_c$ every piece is negative. This proves necessity as well as sufficiency of every sign condition, including boundary/plateau cases.

The global root objective in each access cell is $\min(U_j,F+R_j)$, or $\min(E_j,F+R_j)$ in the expected benchmark. Subtracting $R_j$ proves the strict/weak/tie fee classification. All fee thresholds exceed $h$. For example, $T^E_0=5/4+23\rho/20+\kappa(9/4-b)>h$ and $T^E_1=T^E_0+I_E\geq T^E_0$. Hard capacity restricts the expected feasible set with the same procurement technology, so $T^H_j\geq T^E_j>h$. Hence the strict fee intervals of nonzero width are admissible, not formal intervals below the minimum allowed fee. When the optimized root costs tie, both roots retain their own stocks, including their closed flat intervals. Optional access enlarges each recipient action set, so it cannot increase any optimized aligned cost, regardless of the repair choice.

The envelope identity (72) differentiates each optimized cell with respect to the tier coefficient; it is a standard parameter-envelope result and is asserted at differentiability points. In the inner strip every optimum is unique and all stocks are unchanged. Both repaired stocks are below $b$ and the two unrepaired stocks differ by $1/2$, giving derivative $1/2$. Exact substitution of the three parameter choices gives (73) and both stated fee intervals. They are disjoint, so no same-fee cross-supply reversal has been inferred. This proves every numerical witness analytically.

## A.15 Proof of Proposition 15 and neighborhood persistence

Put $e_\delta(z)=H_\delta(z)-z_+=(\sqrt{z^2+\delta^2}-|z|)/2$. For every real $z$, $0\leq e_\delta(z)\leq\delta/2$. Since $(-b)_+=0$,

$$C_\delta(B)-C(B)=\kappa[e_\delta(B-b)-e_\delta(-b)],\tag{77}$$

whose absolute value is at most $\kappa\delta/2$. Direct differentiation gives

$$C'_\delta(B)=\rho+\frac{\kappa}{2}\left(1+\frac{B-b}{\sqrt{(B-b)^2+\delta^2}}\right),\qquad
C''_\delta(B)=\frac{\kappa\delta^2}{2((B-b)^2+\delta^2)^{3/2}}>0\tag{78}$$

when $\kappa,\delta>0$. Normalization gives $C_\delta(0)=0$. The same slope bound $C'_\delta\leq3$ preserves every global source comparison in A.13. Objectives remain coercive because $C_\delta(B)\geq\rho B$ for $B\geq0$ (its derivative is at least $\rho$ and it vanishes at zero), so minima exist. On each complete feasible set the procurement replacement changes the objective uniformly by at most $\epsilon$. Taking infima both ways proves the cell bound even when optimizers move and for expected mixtures. Threshold differences involve two cells and interaction differences four, proving the stated bounds without differentiability or stability of the optimizing stock.

At the positive witness $\kappa=1/5$, $I_H=1/20$. The interaction remains positive if $2\kappa\delta<1/20$, namely $\delta<1/8$. At $F=87/40$, both hard repair-choice margins are $1/40$; their perturbation is at most $\kappa\delta<1/40$ under exactly the same strict bound. The conclusion concerns the optimized global cells, not only evaluation at the old stocks. Equality at $\delta=1/8$ is not certified by this sufficient bound. No new general smoothing theorem is claimed.

For the primitive box in the proposition, the recipient envelope has $a=S-1\in(.99,1.01)$. Source dominance follows from A.11's uniform inequalities on $q,\gamma\in[.4,.6]$, with procurement Lipschitz constant at most 3; the hard shifted-stock and expected mean-load arguments of A.13 apply. The ordered breakpoints and strict slopes retain hard stocks $B_{U_0}=2+\gamma$, $B_{U_1}=3$: the slopes just before/after the first are $v-3q<0<v$, and for the second $v-a<0<v-qa$. Repaired stocks $h+1,h+2$ remain below $b$, with negative preceding and positive following slopes. These strict inequalities hold throughout the closed box $q,\gamma\in[.49,.51]$, $a\in[.99,1.01]$. Expected stocks $\ell+1,\ell+2$ both exceed $b$ and their relevant slopes retain the same strict signs.

Direct evaluation at these global stocks gives $T^H_0=\ell+C(2+\gamma)-C(h+1)$ and $T^H_1=\ell+qa\gamma+C(3)-C(h+2)$. Their difference is (76), since the unrepaired stocks are above $b$ and repaired ones below it. At the fixed supply parameters these thresholds simplify to $3/2+\gamma(q+4/5)$ and $17/10+q\gamma(1+a)$, respectively. Their bounds are

$$T^H_0\leq21681/10000<87/40<2177799/1000000\leq T^H_1.\tag{79}$$

Thus the fee choices are strict throughout a genuine primitive box, not just along the original parameter line. The smallest explicit fee margin is $2799/1000000$. For direct positivity one can also bound (76) below by $.039401$. Finally all cell objectives and the finite-history occupation sets depend continuously on nearby primitives, and a positive lower bound on $\rho$ gives a common compact set containing all optimizers. Consequently optimized costs and fee margins are continuous. Strict source and branch gaps therefore permit an open enlargement in the remaining supply/fee primitives. For any fixed $\delta<1/8$ at the central witness, the already strict smooth margins similarly persist in a sufficiently small neighborhood. This is local robustness, not an unrestricted capacity-supply theorem.

# Appendix B. Theorem-level contribution and inspection-depth ledger

This ledger distinguishes demonstrated mathematics from an originality claim. It records the actual source depth available for this revision, not hypothetical contents of inaccessible pages. R7 reconciliation dated 18 October 2026; prior R4-R6 source scopes below are retained and current final-text additions are distinguished. Source access dated 18 October 2026; earlier direct readings are identified as retained readings.

## B.1 Constrained inspection: exact institution mapping

**Yao-Zheng 2002, Chapter 6, printed pp. 89-90 only.** The publisher chapter record was opened directly. The preview request failed. Equation-level evidence therefore comes from the central review's verified two-page excerpt: (6.1) has expected inspection count at most $u$ and expected defects removed at least the stated lower target; (6.2)-(6.4) give expected cost and inspection/defect-count state. This is not a claim of independent visual inspection or of access to pp. 91-107.

For our fixed root/workflow cell, (22) imposes expected weighted service at most $B$. Terminal service can be attached to each finite history, so stage, source finding and accumulated service give a finite constrained-MDP representation. This supports attribution of the formulation, expected criterion and generic optimization logic. It is not a unit-for-unit identity: our $Q$ counts service durations, including propagation/correction and recipient audit, rather than only inspections. We have no separate lower constraint on removals. For an unrepaired source, correcting $D_s$ wrong exposures yields expected loss $2qL_s-L_sE[D_s]$. Thus the loss penalty corresponds to the familiar multiplier form of a removal target, while a fixed target is a different feasible-set restriction. No dual equivalence at a particular target is asserted without establishing the corresponding multiplier/target conditions.

Prior source repair instead changes the source before the exposures. The independent recipient has its own production saving $S$, expected loss $D_a$ and audit duration $t_a$. Its quality does not depend on the source finding. These are the application primitives that must be substituted and solved to obtain our investment boundaries; the preview scope does not establish a theorem about them. It also cannot establish that later chapter pages lack an equivalent result.

**Separate Yao-Zheng 1999 article.** The publisher abstract was inspected, reporting constrained Markov inspection, thresholds, LP construction and randomization at at most two thresholds. PDF redirected to abstract. Generic LP and randomization are inherited. The 2002 chapter is not treated as the same version or a proof of the article's detailed theorems.

## B.2 Proposition-by-proposition dependency boundary

1. **Propositions 1-4 and Corollary 3.1, equations (1)-(17).** Conditional KKT allocation, resource multipliers, envelope derivatives, finite workflow choice and the positive-part access comparison are standard optimization/inspection logic. Shared inspection is already established by the inspected Jang-Shanthikumar abstract; congestion pricing by the retained direct Naor reading. The application-specific conditions are demand ordering across an untouched recipient's workflows, an explicit source-validation service reservation $h$, and the allocation-share inequality for own-account versus total interactions. These are proved here but no inaccessible predecessor theorem is ruled out. Free unused access expands a common aligned feasible set, so an adverse access ITT does not follow.

2. **Proposition 5, equations (18)-(21).** The reuse/scale result holds only with frozen open-loop marginal-error technology and pure drafting-price changes. Its monotonic accounting is not claimed as a new law of verification sample-size scaling. The directly read Bańka-Chudziak Section 3 instead samples a finite artifact; changing claim count while fixing false-claim count changes sampling evidence. An adaptive common-source discovery can invalidate repeated-copy workload accounting, which is why our open-loop scope remains essential.

3. **Proposition 6, equations (22)-(29).** The expected-capacity LP and support-size argument are inherited finite constrained-program logic. The solved source-action envelope $\min\{2qL_s,w(1+q\gamma)\}$ follows from the specified common binary fault, independent first check and conditional propagation, not from a Bayesian artifact pass. Its recipient adoption comparison uses service demands $t_M,t_A$ and the independent recipient's optional production saving. Its conditional matched-mean expected-resource null is retained. No first multi-round verification or constrained-MDP claim is made.

4. **Proposition 7, equations (30)-(37), proof A.7.** The hard feasible-set restriction and minimum over feasible columns are inherited. This necessary-and-sufficient investment region remains valid within the declared one-recipient primitive strip. R5 Proposition 10 supplies a different fluid frontier; access alone there is positive, so the joint-only description is not granularity-robust. For $q=\gamma=1/2$, $L_s=10$, $k=1$, $t_M=1$, $t_A=2$, $D_M=4$, $D_A=8$, $c=10$, $h=1/10$, equations (34)-(35) give the full saving/fee frontier on $21/10\leq B<5/2$. On $21/10<B<9/4$ and $1<S<4$, the exact strict contrast is $\max\{11/4,7+S-3B\}<F<7/4+S$. This comes from hard and expected repair thresholds $T_H=7/4+S$ and $T_E=7+S-3B$, plus the hard no-access threshold 11/4, not merely from nesting feasible sets. Globality requires the three source branches in (42): propagation strictly beats the single-check branch by at least 13/4 and no checking by at least 11/4 over the strip. Independent rechecking is dominated history by history since $\gamma<1$. The recipient switches at 4 and 7 before repair and at 1 after it, with all ties retained. These primitive substitutions and dominance comparisons are not supplied by the inspected two-page chapter scope; whether later predecessor results imply an equivalent region remains unresolved.

5. **Proposition 8, equations (38)-(41), proof A.8.** Expected-versus-pathwise differences alone are inherited. The characterization holds source loss, expected source service and source money equal, then establishes global optimized nonequivalence for one indivisible recipient. R5 Proposition 9 shows this positive advantage is quantization-dependent and bounded by $\beta/n$, with a nonpositive fluid gap. It needs $h=\ell=1+q\gamma$, $F=k\ell$, $D_M>kt_M$, $\max\{1+t_M,1+\gamma\}\leq B<\ell+t_M$, and $2qL_s/\ell>D_M/t_M$. Global source dominance additionally requires $L_s>k\gamma+D_M-kt_M$ and $2qL_s>k\ell+q(D_M-kt_M)$. These are not decorative assumptions: the differences between the single-check/no-check costs and propagation are respectively $q[L_s-k\gamma-D_M+kt_M]$ and $2qL_s-k\ell-q(D_M-kt_M)$, both strictly positive. The budget interval has positive length when $t_M>(1-q)\gamma$. Expected optimized costs coincide by (40); hard prior validation costs more by $(1-q)(D_M-kt_M)$. Clean-source service leaves an audit feasible, while deterministic matched-mean validation does not. No posterior information about recipient quality is involved. The chapter preview does not establish this matched-mean investment comparison, and uninspected source results are not certified to exclude it.

## B.3 AI verification and other primary comparisons

**Bańka-Chudziak v1 (4 October 2026), Section 3, directly read.** Its Section 3.1 gives hypergeometric bad-pass probability and Bayesian predictive value; Proposition 1 proves dilution, and Section 3.3 gives a target-posterior budget. We claim none of these results. Its sampling unit is an artifact's claims; ours is a reusable source correction plus a separate recipient choice. Its labeled-benchmark experiments supply no enterprise evidence here.

**Huang-Xiao-Vishnoi, arXiv v2 (25 June 2026), retained direct Sections 8.2/8.6 reading.** Individual ex ante time/cognitive restriction and multiple verification rounds are existing theory. This supports crediting delegation/verification choice and resource restrictions. Our cross-exposure correction and independent recipient's history-specific service are additional primitives, not an asserted missing theorem. The separately verified ICML/PMLR final record does not establish identical final appendices; that PDF was unavailable.

**Jang-Shanthikumar 2002, primary abstract/metadata only.** Shared independent production processes, partial observation, dynamic allocation and threshold control were inspected. This establishes inherited shared-inspection logic, but not a theorem-level exclusion of our investment frontier. Full text remains unavailable.

**Naor 1969, retained original article reading, Sections 1-5.** Private/social congestion and tolls predate this paper. Our multiplier is not a novel implementation theorem. Binary fixed-cost adoption/repair does not imply decentralization by one marginal price.

**Dogonowski working record, primary indexed description only.** SSRN 6701098, May 3 2026, revised June 10, explicitly includes verification scarcity and reliability shadow pricing. Those ideas are credited already. Full manuscript inaccessible: neither equivalent source-investment results nor their absence have been established. R4's accessible comparisons do not resolve that material priority limit.

## B.4 R5 granularity boundary and inherited mechanisms

**Proposition 9, (43)-(47), A.9.** The source plans and pathwise institution are unchanged. Recipient tasks have fixed aggregate costs and service split by n. Uniform globality uses $L_s>k\gamma+\beta$ and $2qL_s>k\ell+\beta$; the first exploits that only the fault branch differs from a single-check policy. The exact floor-audit gap reduces to a Jensen comparison in the fluid limit. Concavity and the $\beta/n$ rounding bound are inherited tools, not originality claims. The positive one-recipient matched-mean advantage is not a universal value of adaptive timing.

**Proposition 10, (48)-(56), A.10.** Per-history convexification, not averaging between histories, gives the fluid recipient envelope. $W=2+S$ uniformly bounds recipient cost improvement and certifies propagation globally against all source plans. The explicit region $\max(T_0,T_E)<F<T_H$ survives fine allocation; finite costs and rounding errors are given exactly. Access alone gains $(S-1)(B-2)/2$ in the fluid region. The narrowed conclusion is conditional investment complementarity and a nonvanishing institution-dependent repair choice, not new Jensen/knapsack/control logic or robust joint-only activation.

**Dean-Goemans-Vondrák 2008.** Direct final author-hosted PDF, 20 pages; introduction/Figure 1/outline through printed 947 used. Its final overflow and fixed-order comparison are not our no-overflow/matched-mean comparison. No later-theorem equivalence or absence is asserted.

**Tekin thesis and now-accessible final article.** The prior thesis comparison remains historical. The final publisher article supplied by the user resolves its specific full-text gap: actual Sections 2-5, Theorems 1-2, equations (20)-(32), Appendix C (40)-(50) were inspected here; central review read all 33 pages. Given station capacities, admission control and long-run flows differ from one purchased every-history stock. Generic bottleneck release, defect-contingent repair and shutdown-enabled joint activation are inherited directly from the final article. No whole-thesis/final equivalence or exact containment/absence theorem is asserted.

## B.5 What this ledger establishes

Generic constrained inspection, expected/pathwise feasibility, LP/randomization, Bayesian audit evidence, sample-size scaling, adaptivity/knapsack, downstream capacity release, joint-only activation, Jensen and convexification are outside the claimed increment. R5 establishes a concrete granularity limit and a remaining exact repair frontier within the existing institution. The present evidence still does not certify that the surviving bounded comparison is a substantive original economic mechanism. Yao/Jang/Dogonowski and thesis-version access limits remain as logged; missing text proves neither absence nor overlap. All examples are synthetic and no empirical validation or self-acceptance follows.

## B.6 R6 result-level procurement ledger

| Result or tool | Actual comparison and contribution boundary |
|---|---|
| Root procurement and recourse | Van Mieghem 1997 extended report, equations (1)-(8), Proposition 1: inherited staged investment and operating allocation; no new newsvendor or shadow-price claim. |
| Substitution and dependence | Actual report Propositions 3,5-7; Appendix A (48)-(49) for Proposition 5 read. General substitution/distribution dependence is inherited; no claim these results exclude our case. |
| Proposition 11, (57)-(59),(65), A.11 | One stock before a common-fault finding, independent fluid recipient, optional all-in repair. Explicit shifted-stock dominance proves globality over all source alternatives; full stock ties are solved. This is a specialized application of inherited convex optimization. |
| Proposition 12, (60)-(64), A.12 | The exact repair threshold difference equals the change in pooling premiums. Access-independent expected threshold, weak hard substitution and an open strict repair reversal replace any universal positive investment claim. No independent-recipient information premium is claimed. |
| Remaining priority boundary | Earlier Yao/Jang/Huang/Dogonowski version and full-text limits remain. Neither inaccessible text nor different state labels establishes novelty. Whether this solved boundary is a substantive economic contribution remains for central review. |

## B.7 R7 result-level supply ledger

| Result | Actual comparison and bounded increment |
|---|---|
| Proposition 13, (66)-(70), A.13 | Complete joint root cells under tiered procurement. Global source dominance uses a Lipschitz transformation at aggregate expected load; source/action occupation mixtures include chords crossing the price tier. Convex control and procurement are inherited. |
| Proposition 14, (71)-(73), A.14 | Exact four-piece hard interaction and expected interaction; inner sign change occurs at unchanged stocks. The contribution candidate is a specialized root repair/access/supply frontier, not generic capacity-dependent complementarity or recipient information. |
| Proposition 15, (74)-(79), A.15 | Smooth-supply and local primitive persistence, using inherited uniform-stability tools. It removes a kink-only interpretation, without proving a new general smoothing result. |
| Tekin-Andradóttir final | Supplied 33-page final publisher article; own reading scope Sections 2-5/Theorems 1-2/(20)-(32), Appendix C (40)-(50). Central full-article comparison is separately attributed. The specific final-text gap is resolved. Given station rates, admission and inspection/repair produce long-run bottleneck release; (40)-(48) permit inherited shutdown activation. No article redistribution. |
| Zychlinski-Gurvich final | Actual final HTML Sections 3-4/Theorem 1/(2)-(12), Section 5.2/Theorem 3/Lemma 3: inherited workload complementarity, capacity-dependent cost ratios and shadow prices. Online Appendix proofs not inspected; earlier PDF not equated with final. |
| Remaining originality objection | Different root choices and a correct exact frontier do not prove substantial novelty. Van Mieghem's actual 1997 report scope and Yao/Jang/Huang/Dogonowski limits remain. No unavailable-text priority inference or central self-acceptance. |

# References

Bimpikis, Kostas, and Mihalis G. Markakis. 2019. “Learning and Hierarchies in Service Systems.” *Management Science* 65(3): 1268-1285. First online May 4, 2018. https://doi.org/10.1287/mnsc.2017.2976.

Brynjolfsson, Erik, Danielle Li, and Lindsey Raymond. 2025. “Generative AI at Work.” *Quarterly Journal of Economics* 140(2): 889-942. https://doi.org/10.1093/qje/qjae044.

Brynjolfsson, Erik, Daniel Rock, and Chad Syverson. 2021. “The Productivity J-Curve: How Intangibles Complement General Purpose Technologies.” *American Economic Journal: Macroeconomics* 13(1): 333-372. https://doi.org/10.1257/mac.20180386.

Büchsenschuss, Ralf, Irmela Koch-Bayram, Torsten Biemann, and Phanish Puranam. 2026. “GenAI Adoption Increases the Density of Knowledge and Collaboration Networks: Evidence from a Field Experiment.” INSEAD Working Paper 2026/22/STR, revised from 2026/01/STR. https://sites.insead.edu/facultyresearch/research/doc.cfm?did=75355.

Chen, Jiawei, Hongyu Lin, Xianpei Han, and Le Sun. 2024. “Benchmarking Large Language Models in Retrieval-Augmented Generation.” AAAI 2024; inspected accessible manuscript arXiv:2309.01431v2, December 2023. https://arxiv.org/abs/2309.01431.

Dogonowski, Robert. 2026. “Verified Output and the Microeconomics of AI Adoption: Why AI Productivity Depends on Verification, Not Generation Alone.” SSRN working paper 6701098, May 3; primary record last revised June 10. https://doi.org/10.2139/ssrn.6701098. Primary abstract inspected; full text inaccessible. No theorem-level priority comparison claimed.

Huang, Lingxiao, Wenyang Xiao, and Nisheeth K. Vishnoi. 2026. “Delegation and Verification under AI.” *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306: 48039-48071. https://proceedings.mlr.press/v306/huang26bp.html. Model/resource-extension comparison uses arXiv:2603.02961v2, June 25, rather than treating March v1 as current. https://arxiv.org/html/2603.02961v2.

Jang, Wooseung, and J. George Shanthikumar. 2002. “Stochastic Allocation of Inspection Capacity to Competitive Processes.” *Naval Research Logistics* 49(1): 78-94. First published January 14. https://doi.org/10.1002/nav.1049. Publisher abstract and metadata inspected; full text inaccessible.

Naor, P. 1969. “The Regulation of Queue Size by Levying Tolls.” *Econometrica* 37(1): 15-24. https://www.jstor.org/stable/1909200. Original article inspected through a university-hosted scan.

Sagynbayeva, Aktilek, Ajin Pyo, Sang-Hyeak Yoon, and Sung-Byung Yang. 2026. “Evaluating user performance with RAG-based generative AI: A scenario-based experiment on AI-assisted information retrieval.” *Computers in Human Behavior* 180: 108952. https://doi.org/10.1016/j.chb.2026.108952. Published institutional record/design verified; full publisher text inaccessible.

Yao, David D., and Shaohui Zheng. 1999. “Sequential Inspection Under Capacity Constraints.” *Operations Research* 47(3):410-421. https://doi.org/10.1287/opre.47.3.410. Publisher abstract inspected; PDF request redirected to abstract. Detailed theorem text unavailable.

Bańka, Feliks, and Jarosław A. Chudziak. 2026. “More Claims, Less Evidence: Bounded Verification of AI-Generated Digital Knowledge Artifacts.” arXiv:2610.05547v1, submitted October 4. https://arxiv.org/html/2610.05547v1. Section 3 directly read; working preprint, not a verified final publication.

Yao, David D., and Shaohui Zheng. 2002. “Sequential Inspection Under Capacity Constraints.” Chapter 6 in *Dynamic Control of Quality in Production-Inventory Systems*, pp. 89-107. Springer. https://doi.org/10.1007/0-387-22779-2_6. Publisher record read; printed pp. 89-90 equation scope centrally verified, preview request failed here; no later theorem/proof inspection. Separate from the 1999 article.

Dean, Brian C., Michel X. Goemans, and Jan Vondrák. 2008. “Approximating the Stochastic Knapsack Problem: The Benefit of Adaptivity.” *Mathematics of Operations Research* 33(4):945-964. https://doi.org/10.1287/moor.1080.0330. Final author-hosted 20-page PDF: https://theory.stanford.edu/~jvondrak/data/knapsack-MOR.pdf. Reading used introduction, Figure 1 and outline through printed p. 947; no later-proof comparison claimed.

Tekin, Salih. 2011. *Efficient System Design: Stability and Flexibility*. Doctoral thesis, Chapter IV, Georgia Institute of Technology. Centrally supplied repository identifier: https://repository.gatech.edu/bitstreams/86c994d5-d8cf-44d1-918a-b528238ed48e/download. Chapter comparison and synthetic raw-profit witness centrally verified; request failed here, title centrally verified in R6; no new thesis retrieval attempted. Not identified with a final 2020 article.

Van Mieghem, Jan A. 1997. *Investment Strategies for Flexible Resources*. Extended technical report, 10 November, 25 pages. [Author-hosted extended report](https://www.kellogg.northwestern.edu/faculty/vanmieghem/htm/flextec0.pdf). Title identifies abridged Management Science 44(8), 1071-1078, August 1998, DOI 10.1287/mnsc.44.8.1071. Reading scope specified in Section 2.5; final-version equivalence not assumed.

Tekin, Salih, and Sigrún Andradóttir. 2019 (online 7 January). “Inspection location in capacity-constrained lines.” *Central European Journal of Operations Research*. DOI 10.1007/s10100-018-00604-x. User-supplied final publisher PDF, 33 pages; actual and central reading scopes distinguished above. No equivalence to the 2011 thesis is assumed.

Zychlinski, Noa, and Itai Gurvich. 2026. “The Production of Service: A Workload View of Complementarity and Substitution.” *Stochastic Systems* 16(2): 165-185; online 5 June. DOI 10.1287/stsy.2025.0111. [Final HTML](https://pubsonline.informs.org/doi/full/10.1287/stsy.2025.0111), inspected at the scope stated in Section 2.6; Online Appendix proofs not inspected.
