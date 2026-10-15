# Reading Docket · 2026-10-10 · Sprint 0 Foundations

> **Researcher:** Human Lead  
> **Status:** Cleared - [Muskan Bhandari, 15 October 2026]  
> **Protocol Rule:** When resuming or starting a session, the AI agent must read this file first. If any answer is missing or incomplete, the agent MUST immediately stop, proceed no further with pipeline coding, and actively guide the researcher on the missing concepts.

---

## Instructions
1. Read the papers and targeted sections below.
2. Type your answers directly into the `### Your Answer:` sections under each question.
3. Save the file.
4. When you notify the agent or start the next turn, the agent will verify your answers before any downstream work proceeds.

---

## Module 1: Prediction-Powered Inference (PPI) — Statistical Engine

### Primary Sources
- **Angelopoulos et al. (Science 2023)**: *"Prediction-Powered Inference"* ([arXiv:2301.09652](https://arxiv.org/pdf/2301.09633)) — Focus on Section 1 & 2 (the core intuition and mathematical formulation).
- **Gao, Sicilia, & Shi (arXiv:2608.26638 / EMNLP 2026)**: *"Which Metrics Save the Most Human Annotation?"* — Focus on the introduction, the definition of PPSR, and Section 3 on paired evaluations.

### Questions

#### Q1.1: The Core Mechanism of PPI
*Why is an unlabelled dataset with proxy predictions able to shrink error bars on a small human-labelled set without introducing model bias? How does the debiasing/imputation term work mathematically and conceptually?*

### Your Answer:
<!-- Enter your answer below this line -->
**Short answer:** the predictions never replace the labels. They're used only to estimate the part of the target that the model gets right, and the labeled set is used to measure how much the model gets wrong. Because the correction is estimated on real labels drawn from the same distribution, the model's bias cancels in expectation. What's left is variance, and the residual Y − f(X) usually varies much less than Y does.

### The decomposition

Take mean estimation, θ* = E[Y]. Add and subtract the model's prediction:

$$\theta^* = \underbrace{\mathbb{E}[f(X)]}_{\text{what the model says}} \;-\; \underbrace{\mathbb{E}[f(X) - Y]}_{\text{rectifier } \Delta}$$

This is an identity. It holds for any function f, good or terrible. The estimator plugs in the cheapest available estimate for each piece:

$$\hat\theta^{PP} = \underbrace{\frac{1}{N}\sum_{i=1}^{N} f(\tilde X_i)}_{\tilde\theta^f \text{ (big unlabeled set)}} \;-\; \underbrace{\frac{1}{n}\sum_{i=1}^{n}\big(f(X_i) - Y_i\big)}_{\hat\Delta \text{ (small labeled set)}}$$

The first term alone is the "imputation" estimate: low variance, but biased by however wrong the model is. The second term is the measured average error on gold labels, subtracted to remove that bias.

### Why no bias is introduced

Take expectations of each term:

$$\mathbb{E}[\hat\theta^{PP}] = \mathbb{E}[f(X)] - \mathbb{E}[f(X)] + \mathbb{E}[Y] = \theta^*$$

The model's bias appears once with a plus sign (from the unlabeled set) and once with a minus sign (from the labeled set), so it cancels exactly. This needs two conditions. First, labeled and unlabeled data come from the same distribution, so both terms estimate the same E[f(X)]. Second, f must be independent of the observed data, for example trained on separate data. If f were fit on the labeled set, its errors there would look artificially small and the rectifier would under-correct.

Nothing is assumed about the model's accuracy, calibration, or form. That's why the guarantee is model-agnostic.

### Why the error bars shrink

The two terms are computed on independent samples, so their variances add:

$$\mathrm{Var}(\hat\theta^{PP}) = \frac{\sigma^2_f}{N} + \frac{\sigma^2_{f-Y}}{n} \qquad \text{vs.} \qquad \mathrm{Var}(\hat\theta^{class}) = \frac{\sigma^2_Y}{n}$$

When N ≫ n, the first term is negligible, so the comparison is between σ²_{f−Y} and σ²_Y. The labeled data now only has to pin down the mean of the residual, and when the model has small errors, the residual's variance is much smaller than the outcome's variance.

An intuitive way to see it: estimating the average of Y from 200 labels is hard if Y is noisy. Estimating the average of a small, consistent offset from 200 labels is easy. PPI converts the first problem into the second. Statisticians will recognize this as a control variate, or the classical difference estimator from survey sampling, which the authors acknowledge.

### Where the model's quality goes instead

A bad model doesn't bias the result. It inflates σ²_{f−Y}, which widens the interval. The paper derives the break-even condition: for a balanced binary outcome (p = 0.5), the model's error rate must be below 25% for PPI to beat the classical interval; at p = 0.1 it must be below roughly 9.5%. In their own failure cases, swapping in a weak linear model or shrinking N below n made PPI need more labels than classical inference. So a poor proxy costs you efficiency, never validity. Follow-up work (PPI++) adds a tuning weight on the prediction term so the estimator falls back to the classical one when the proxy is unhelpful.

### Beyond the mean

For general targets (quantiles, regression coefficients), the same trick is applied to the gradient of the loss rather than to the outcome itself. The rectifier becomes

$$\Delta_\theta = \mathbb{E}\big[g_\theta(X, Y) - g_\theta(X, f(X))\big]$$

which is the bias in the subgradient caused by using predictions. The confidence set contains every θ where the prediction-based gradient plus the rectifier is consistent with zero. For the mean, the gradient is θ − y, and this reduces exactly to the formula above.

### What this means for LLM evaluation

If Y is a human judgment and f is an LLM-judge score, PPI lets you report a valid accuracy or win-rate interval using judge scores on everything plus human labels on a random subset. The two practical requirements are that the human-labeled subset is a random sample from the same pool, and that the judge was not tuned on those human labels.

---

#### Q1.2: Fallback Under Poor Proxy Performance
*What happens to the confidence interval if the proxy evaluator has near-zero or negative correlation with human ground truth? How does PPI++ (adaptive tuning parameter $\lambda^*$) protect against variance inflation?*

### Your Answer:
<!-- Enter your answer below this line -->
**Short answer:** under plain PPI, a weak or anti-correlated proxy leaves the interval *valid* but makes it *wider* than ignoring the proxy entirely. PPI++ fixes this by scaling the proxy term with a weight λ chosen from the data. That weight shrinks toward zero when the proxy is useless, so the interval falls back to the classical one instead of getting worse.

### Plain PPI with a bad proxy

Validity never depends on the proxy's quality, so coverage still holds. What changes is the variance. Expand the rectifier's variance:

$$\sigma^2_{f-Y} = \sigma^2_f + \sigma^2_Y - 2\,\mathrm{Cov}(f, Y)$$

Plain PPI beats classical only when σ²_{f−Y} < σ²_Y, which (ignoring the small σ²_f/N term) is equivalent to

$$\rho_{fY} > \frac{\sigma_f}{2\sigma_Y}$$

For a proxy on the same scale as the human labels (σ_f ≈ σ_Y), you need correlation above **0.5** just to break even. Below that, the interval widens:

| Correlation ρ (with σ_f = σ_Y) | Var(PPI) / Var(classical) | Interval width vs classical |
|---|---|---|
| 0.9 | 0.2 | ~0.45× |
| 0.5 | 1.0 | same |
| 0 | 2.0 | ~1.41× wider |
| −0.5 | 3.0 | ~1.73× wider |
| −1 | 4.0 | 2× wider |

The cause: plain PPI subtracts the proxy's residual with a fixed weight of 1. If f carries no information about Y, you're adding pure noise to the estimate. If f is anti-correlated, you're adding noise that pushes the wrong way, which is even worse.

### What PPI++ changes

PPI++ introduces a tuning parameter λ into the rectified loss. The objective stays unbiased for any λ: λ = 1 recovers original PPI and λ = 0 reduces to classical inference that ignores the predictions. For the mean:

$$\hat\theta_\lambda = \underbrace{\frac{1}{n}\sum_{i=1}^n Y_i}_{\text{classical}} + \lambda\Big(\underbrace{\frac{1}{N}\sum_{j=1}^N f(\tilde X_j) - \frac{1}{n}\sum_{i=1}^n f(X_i)}_{\text{mean-zero correction term}}\Big)$$

Reading it this way is clarifying. PPI++ starts from the classical estimate and adds a correction whose expectation is zero no matter what λ is. Unbiasedness is therefore free, and λ only controls variance. This is exactly a control variate.

### The optimal λ and why it can't hurt (asymptotically)

The variance is quadratic in λ:

$$\mathrm{Var}(\hat\theta_\lambda) = \frac{\sigma_Y^2}{n} - \frac{2\lambda\,\mathrm{Cov}(f,Y)}{n} + \lambda^2\sigma_f^2\Big(\frac{1}{n} + \frac{1}{N}\Big)$$

Minimizing gives the value λ* = σ_fy / ((1 + n/N) σ²_f), which motivates a plug-in estimate λ̂ computed from the labeled data. Substituting back:

$$\mathrm{Var}(\hat\theta_{\lambda^*}) = \frac{\sigma_Y^2}{n}\left(1 - \frac{N}{N+n}\,\rho^2\right)$$

Three consequences follow from this one line:

- **Never worse than classical.** The factor in parentheses is at most 1, because λ = 0 is always available and the optimum can only beat it.
- **Near-zero correlation → λ̂ ≈ 0.** Cov(f, Y) ≈ 0 sends the weight to zero, and you get the classical interval back.
- **The gain depends on ρ², not ρ.** In the paper's formulation, λ ranges over all real numbers, so a strongly anti-correlated proxy gets a negative λ and is used as an inverted signal. A ρ = −0.9 judge is as useful as a ρ = +0.9 one. Some implementations and follow-up papers restrict λ to [0, 1], which forfeits this. With clipping, a negatively correlated proxy simply gets λ = 0.

The authors report that power tuning is essentially never worse than either classical or prediction-powered inference, and it can outperform both substantially. For general M-estimation, the same idea applies to the gradient of the loss, and λ* is defined as the value minimizing the trace of the asymptotic variance.

### Where the guarantee is weaker than it sounds

"Never worse" is an asymptotic statement. λ̂ is estimated from the same small labeled set, so with very small n its noise feeds into the interval. Recent work (the "No Free Lunch" non-asymptotic analysis) distinguishes using the full labeled sample for both estimating λ̂ and estimating θ̂ from cross-fitted variants, and shows the small-sample gains are less clean than the asymptotic story suggests. Rough guidance: with a few dozen labels, expect PPI++ to roughly match classical rather than beat it, unless the proxy is very strong.

### Practical reading for LLM-judge evals

The value of λ̂ is itself a diagnostic worth logging:

- **λ̂ near 1:** the judge is roughly calibrated to human labels; plain PPI would have been fine.
- **λ̂ near 0:** the judge carries little information about human judgment on this task. The interval is honest, but you've gained nothing from judge scores.
- **λ̂ negative:** almost always a bug, such as an inverted rubric, a flipped label mapping, or a "lower is better" score fed as "higher is better." PPI++ will silently exploit it, which keeps the statistics valid but hides the pipeline error. Check the sign before reporting.
- **λ̂ well above 1:** the judge's scale is compressed relative to human labels. This is a valid outcome, but it signals a calibration issue worth fixing upstream.



---

#### Q1.3: Paired vs. Unpaired Evaluation
*Why does our experimental design evaluate the exact same item across all three conditions ($C1$ cross-lingual, $C2$ raw MT, and $C3$ post-edited MT)? How does this paired structure exploit covariance cancellation when estimating $\Delta_{XL} - \Delta_{MT}$?*

### Your Answer:
<!-- Enter your answer below this line -->
Evaluating the exact same item across $C1$, $C2$, and $C3$ establishes a **paired (within-item) experimental design**, controlling for item-level confounding variables while maximizing statistical power.

### Why Evaluate the Exact Same Item Across Conditions?

Items in the corpus vary significantly in intrinsic difficulty—due to domain terminology, claim complexity, response length, or perturbation type. If $C1$, $C2$, and $C3$ used different items, any observed divergence in accuracy ($A$) could reflect item-selection bias or domain heterogeneity rather than true evaluation gaps.

By holding the generated English answer, atomic claim split, and underlying factual truth constant—varying only the representation of the Nepali context—the item itself acts as its own control.

---

### Covariance Cancellation in Estimating $\Delta_{XL} - \Delta_{MT}$

To test Hypothesis H1 ($\Delta_{XL} > \Delta_{MT}$), we evaluate the difference between the two gaps:

$$\Delta_{XL} - \Delta_{MT} = [A(C3) - A(C1)] - [A(C3) - A(C2)] = A(C2) - A(C1)$$

Notice that while the post-edited ceiling $A(C3)$ cancels out algebraically, the sample variance of the difference estimator depends directly on the pairing of $C2$ and $C1$.

#### Statistical Mechanics

Let $X_i$ be the evaluator's performance on item $i$ under condition $C2$, and $Y_i$ be the performance on the same item $i$ under condition $C1$. The variance of the sample mean difference $\bar{D} = \bar{X} - \bar{Y}$ is:

$$\text{Var}(\bar{X} - \bar{Y}) = \frac{1}{N} \left[ \text{Var}(X) + \text{Var}(Y) - 2\text{Cov}(X, Y) \right]$$

1. **High Positive Covariance ($\text{Cov}(X, Y) > 0$)**: Because $X_i$ and $Y_i$ are evaluated on the *exact same item*, an intrinsically ambiguous or complex claim will tend to cause failures in both conditions, while a straightforward item will succeed in both.
2. **Variance Reduction**: The covariance term $-2\text{Cov}(X, Y)$ actively subtracts out item-to-item background noise (variance in baseline task difficulty across the corpus).
3. **Implication for Prediction-Powered Inference (PPI)**: By drastically reducing the standard error of the estimator, covariance cancellation allows the benchmark to establish narrow, statistically valid confidence intervals for testing H1 using only ~120–150 human gold-labeled items.
---

## Module 2: Claim-Level Faithfulness in RAG — Primary Evaluation Unit

### Primary Sources
- **Es et al. (EACL 2024)**: *"RAGAS: Automated Evaluation of Retrieval Augmented Generation"* ([arXiv:2309.15217](https://arxiv.org/abs/2309.15217)) — Focus on the **Faithfulness** section and claim extraction prompts.

### Questions

#### Q2.1: Atomic Claim Decomposition
*How does RAGAS break down a generated answer into individual atomic claims? What constitutes a valid atomic claim, and why do we evaluate at the claim level rather than assigning a single scalar score to the entire answer?*

### Your Answer:
<!-- Enter your answer below this line -->
**Short answer:** Ragas uses a two-prompt pipeline. One LLM call rewrites the answer as a list of short statements; a second call checks each statement against the retrieved context. The paper never formally defines what a valid "atomic" statement is; it leaves that to the prompt and a single demonstration. Claim-level scoring is used because "is this one statement supported?" is a much easier and more checkable judgment than "how faithful is this whole answer, 0–10?"

### How the decomposition works

The faithfulness metric runs in two steps.

**Step 1, extraction.** An LLM extracts a set of statements from the answer, with the stated aim of decomposing longer sentences into shorter and more focused assertions. The prompt asks it to create one or more statements from each sentence in the given answer, given the question and answer. A demonstration is included in the prompt to clarify the task, though the paper doesn't show it.

**Step 2, verification.** For each statement, the LLM decides whether it can be inferred from the context, giving a brief explanation before a Yes/No verdict. The score is the number of supported statements divided by the total.

A worked example. Suppose the question is "Who directed Oppenheimer and who stars in it?" and the answer is:

> "Christopher Nolan directed Oppenheimer, which stars Cillian Murphy and won seven Oscars."

A reasonable decomposition gives three statements:

1. Christopher Nolan directed Oppenheimer.
2. Cillian Murphy stars in Oppenheimer.
3. Oppenheimer won seven Oscars.

If the retrieved context (like the paper's WikiEval example) mentions the director and cast but not awards, statement 3 gets "No" and faithfulness is 2/3 ≈ 0.67. Note that statement 3 is *true* in the world. It's penalized because it isn't grounded in the context, which is exactly what faithfulness is meant to measure.

### What counts as a valid atomic claim

The paper offers only "shorter and more focused." In practice, and in related work like FActScore (which the paper cites), a good atomic claim meets these criteria. These are my working definitions, not the paper's:

| Property | Meaning | Failure example |
|---|---|---|
| **Single proposition** | Asserts exactly one fact that is true or false as a unit | "Nolan directed it and Murphy stars" (two facts, one verdict) |
| **Self-contained** | Pronouns and references resolved, so it can be checked without the original answer | "He directed it" |
| **Faithful to the answer** | Adds nothing and drops nothing the answer asserted | Extractor "corrects" a wrong date while rewriting |
| **Checkable** | A factual assertion, not a hedge, opinion, or filler | "That's a great question" or "It's widely considered a masterpiece" |
| **Minimal but meaningful** | Not split so finely that fragments lose meaning | "Oppenheimer is a film" + "the film is from 2023" + "the film is biographical" |

The self-contained criterion explains why the extraction prompt includes the question: answers often use "it" or "the film" and depend on the question to resolve what they refer to.

### Why claim level instead of one scalar

**1. Easier sub-task.** Holistic scoring asks the LLM to find every assertion, check each, and weight them into a number all in one pass. Claim-level scoring turns this into a series of near-binary entailment checks, which LLMs do far more reliably. The paper's own comparison supports this: Ragas reached 0.95 agreement with humans on faithfulness, versus 0.72 for asking ChatGPT for a 0–10 faithfulness score.

**2. Partial hallucinations get proportional credit.** An answer with four grounded facts and one invented one is mostly faithful. A holistic score might give it anything from 3 to 9 depending on how salient the error is. The ratio gives 0.8, and that number has a fixed meaning.

**3. The score is interpretable.** Faithfulness becomes a precision: the fraction of asserted content that the context supports. A score of 0.6 means 40% of claims lacked support. A holistic "6/10" has no such reading.

**4. Errors become debuggable.** You get a list of which specific claims failed, not just a number. That tells you whether the generator is hallucinating, the retriever is missing a passage, or the extractor mangled a statement.

### Caveats worth knowing

The 0.95 vs 0.72 comparison doesn't isolate decomposition as the cause. In the GPT Score baseline, ties between the two candidates were broken randomly, and a coarse 0–10 scale produces many ties in a pairwise test, so part of the gap may come from the scoring format rather than claim splitting. The test set is also small (50 items) with deliberately degraded contrasts.

Beyond that, the method has several structural weaknesses:

- **The extractor is unvalidated.** Decomposition is itself an LLM step, and the paper measures only the final score's agreement with humans, never whether the extracted statements were correct or complete. A dropped claim silently disappears from the denominator.
- **Granularity changes the score.** Splitting a supported claim into three fragments raises the ratio; merging claims lowers it. The same answer can score differently across runs or extractor models.
- **All claims weigh the same.** A wrong central fact and a wrong side detail cost the same.
- **It measures grounding, not correctness or completeness.** A faithful answer can still be wrong if the context is wrong, and an answer that omits half of what the context supports can still score 1.0.

For your eval work, the practical takeaway is to spot-check extractions on a sample, not just verdicts, and to fix the extractor model and prompt across runs so that granularity drift doesn't show up as score changes. (The open-source Ragas library has evolved since this paper, so its current prompts may differ from what's described here.)

---

#### Q2.2: Entailment vs. Lexical Matching
*Why is faithfulness evaluation framed as an entailment / NLI problem rather than lexical or n-gram matching (like BLEU or ROUGE)? What specific failure occurs if you attempt cross-lingual lexical matching between Nepali and English?*

### Your Answer:
**Short answer:** faithfulness is a question about *meaning*: does the context logically support what the answer asserts? Lexical metrics measure *surface overlap*, which is a different property. The two diverge constantly even within one language. Across Nepali and English they don't merely diverge; the lexical signal disappears. Devanagari and Latin script share almost no tokens, so a faithful answer and a hallucinated one both score near zero and the metric can't tell them apart.

### Why faithfulness is an entailment problem

Ragas never uses the term "NLI," but its verification step is exactly that. An answer is faithful if the claims it makes can be inferred from the context, and each statement is checked for whether it can be inferred from the context. In NLI terms, the context is the premise and each claim is a hypothesis; the question is whether the premise entails the hypothesis.

This framing has three properties that n-gram matching lacks.

**1. It's directional.** Entailment asks "does A support B?", not "are A and B similar?" A short claim can be fully entailed by a long context with which it shares few words. BLEU and ROUGE are built for comparing a candidate against a reference *of the same kind* (one translation or summary against another), and a retrieved context is not a reference answer.

**2. It tracks meaning, not wording.** Lexical overlap fails in both directions:

| Case | Context | Claim | Lexical match | Entailed? |
|---|---|---|---|---|
| Paraphrase | "Nolan directed the film." | "The film's director was Nolan." | Partial | Yes |
| Inference | "Born 1904, died 1967." | "He died in his early sixties." | ~None | Yes |
| Negation | "The launch was not delayed." | "The launch was delayed." | Very high | No (contradiction) |
| Entity or number swap | "Murphy plays Oppenheimer." | "Cruise plays Oppenheimer." | Very high | No |

The last two rows are the dangerous ones. Hallucinations typically keep the sentence frame and change one critical token: a name, number, date, or negation. N-gram metrics score these as near-perfect matches, which is the exact opposite of what a faithfulness metric must do.

**3. It works without a reference answer.** Ragas is designed to be reference-free. BLEU/ROUGE need a gold output to compare against; entailment needs only the evidence.

### What happens with Nepali answers and English context

Suppose the context is English and the system answers in Nepali.

> **Context:** "Mount Everest is 8,849 metres tall."
> **Faithful answer:** सगरमाथाको उचाइ ८,८४९ मिटर हो।
> **Hallucinated answer:** सगरमाथाको उचाइ ९,००० मिटर हो।

Both answers share **zero tokens** with the context. Every word is in Devanagari, and even the numbers use Devanagari digits (८,८४९), which are different Unicode characters from 8,849. BLEU, ROUGE, and character-level metrics like chrF all return essentially 0 for both.

The core failure is a **total loss of discrimination**: the metric outputs a constant, so the correct answer and the wrong height are indistinguishable. In a lexical pipeline, a low score usually means "unfaithful." Here it's an artifact of script mismatch, so every Nepali answer looks like a hallucination, including perfect ones.

It gets worse once you look at what does create overlap. The few things that match across the two languages are:

- Arabic numerals, when an answer happens to use them instead of Devanagari digits
- Proper nouns or technical terms left in Latin script ("Everest", "API")
- Code-mixed English words, which are common in real Nepali usage

The score then ranks answers by **how much English or Latin-script text they contain**, not by faithfulness. A hallucinated answer that keeps "Everest" in English outscores a faithful one written entirely in Nepali. That's a spurious signal that looks like a real one, which is worse than no signal.

### Why the usual workarounds don't fix it

**Romanizing the Nepali.** Nepali romanization is inconsistent (सगरमाथा could become "sagarmatha" or "sagarmāthā"), and even perfect transliteration produces Nepali words, not English ones. "Sagarmatha" still doesn't match "Everest."

**Translating to English, then matching.** This brings back every same-language failure from the table above, plus machine translation errors. MT might also "fix" a hallucinated number or name, hiding exactly the error you wanted to catch.

**Matching within Nepali instead.** Even monolingually, Nepali is hard for n-grams. Postpositions attach directly to words (नेपाल, नेपालको, नेपालमा are "Nepal," "of Nepal," "in Nepal"), so the same entity appears as different tokens. Unicode normalization issues with conjunct characters can also make visually identical strings unequal.

**Multilingual embedding similarity.** Models like LaBSE do place Nepali and English in a shared space, which solves the script problem. But cosine similarity is symmetric and meaning-level; it isn't entailment. "8,849 metres" and "9,000 metres" embed almost identically, so you're back to missing number swaps and negations.

### What this implies in practice

For cross-lingual faithfulness, use an entailment judgment that operates across languages: either a multilingual NLI model or an LLM judge prompted to verify Nepali claims against English evidence. That moves the problem rather than solving it, since an LLM judge's reliability on Nepali is unknown until measured, and it's likely weakest on exactly the cases that matter (numbers in Devanagari, transliterated names, code-mixing). The realistic workflow is to validate the cross-lingual judge on a human-labeled sample that deliberately includes number swaps, entity swaps, and negations, then report its agreement before trusting its scores at scale.

---

#### Q2.3: Label Distinction: Contradicted vs. Not-in-Context
*In our rubric (`GLOSSARY.md`), why must `Contradicted` be strictly distinguished from `Not-in-context`? Give a concrete example showing how an LLM confabulation differs from an active factual contradiction.*

### Your Answer:
<!-- Enter your answer below this line -->
`Contradicted` and `Not-in-context` must be strictly distinguished because they represent fundamentally distinct error typologies with different safety risks, diagnostic requirements, and evaluation targets:

1. **Diagnostic Granularity (Testing Hypothesis H2)**: A primary objective of the NepFaith-120 benchmark is evaluating claim-type survival under perturbations. Perturbed hard negatives like *negation flips* or *entity swaps* generate active factual contradictions (`Contradicted`), whereas *unsupported additions* introduce external confabulations (`Not-in-context`). Conflating them destroys the ability to measure whether a scoring arm fails specifically at detecting direct factual conflicts versus identifying ungrounded claims.
2. **Safety and Risk Profiling**: An active contradiction directly falsifies reference truths, presenting severe misinformation risks in domain applications. An ungrounded confabulation (`Not-in-context`) introduces unverified external assertions, which may be unverified facts from general parametric memory rather than false statements.
3. **Scorer Calibration**: Cross-lingual judges often fail differently across these categories—for instance, dense retrieval models or cross-lingual NLI systems may penalize ungrounded additions too lightly while entirely missing subtle numerical contradictions.

---

### Concrete Example

**Source Context (Nepali → English)**:

> *"In June 2023, Prime Minister Pushpa Kamal Dahal signed a bilateral power trade agreement with India in New Delhi."*

* **LLM Confabulation (`Not-in-context`)**:
> *"Prime Minister Pushpa Kamal Dahal stayed at the ITC Maurya during his visit to New Delhi."*


* **Analysis**: The context mentions the visit, location, and power agreement, but does not state where the Prime Minister stayed. This claim adds external, ungrounded detail. It does not violate any facts in the context, but it cannot be verified by it.


* **Active Factual Contradiction (`Contradicted`)**:
> *"In June 2023, Prime Minister Pushpa Kamal Dahal signed a bilateral power trade agreement with China in Beijing."*


* **Analysis**: The source context explicitly establishes that the agreement was signed with *India* in *New Delhi*. Claiming it was signed with *China* in *Beijing* actively conflicts with and negates the facts asserted in the context.

---

## Module 3: Machine Translation & Indic Language Behavior

### Primary Sources
- **Gala et al. (AI4Bharat, 2023)**: *"IndicTrans2: Towards High-Quality and Accessible Machine Translation Models for all 22 Scheduled Indian Languages"* ([arXiv:2305.16438](https://arxiv.org/abs/2305.16438)) — Review Nepali (`npi_Deva`) translation performance and distilled variants.
- **Agrawal, Fazili, & Jyothi (EACL 2024)**: *"Translation Errors Significantly Impact Low-Resource Languages in Cross-Lingual Learning"* ([arXiv:2402.02080](https://arxiv.org/abs/2402.02080)).

### Questions

#### Q3.1: Translation Noise in Indic NLP
*What types of translation errors are most prevalent when translating low-resource Indic languages like Nepali to English (e.g. named entities, numbers, honorifics, complex predicates), and how do they corrupt downstream semantic evaluation?*

### Your Answer:
<!-- Enter your answer below this line -->
**Short answer:** neither of these two papers measures Nepali→English errors directly. Agrawal et al. study Hindi, Urdu, and Swahili in XNLI, and IndicTrans2 reports aggregate scores rather than an error taxonomy. But both point to the same pattern: the damaging errors are rarely garbled sentences. They're small, fluent-looking shifts in a single grammatical feature (aspect, tense, negation, a number, who did what) that leave the sentence readable but change its truth conditions. That's exactly what entailment-based evaluation is sensitive to. The taxonomy below combines what the papers document with Nepali-specific linguistic features; I flag which is which.

### What the papers actually document

**From Agrawal et al. (Hindi/Urdu XNLI).** Their examples are all meaning shifts, not fluency failures. "They were done speaking" was translated as "they were speaking," changing the label from contradiction to entailment; a tense error turned "had been captured" into not wanting to be caught; and "pretty scary" was rendered as just "pretty," inverting the sentiment. They also note that some issues are deviations rather than outright errors, arising from unfamiliar phrases or English-specific nuances that translations don't capture.

**From IndicTrans2.** The authors report that human evaluation of their earlier model showed poor handling of special cases such as emails, URLs, dates, numbers, and percentages, which they fixed by wrapping such spans in do-not-translate tags. They also motivated IN22 by noting that existing test sets had limited representation of Indian named entities, locale, and culture-specific terms. The conversational subset scores lowest for every system, including for Nepali.

### Nepali-specific error types

The rest of this table is my linguistic analysis, not findings from these papers. It's ordered roughly by how badly each error damages evaluation.

| Category | Nepali feature | Typical MT failure | Effect on meaning |
|---|---|---|---|
| **Aspect via compound verbs** | Vector verbs encode completion or manner: खाइसक्यो ("has already eaten"), गरिहाल्यो ("did it right away"), गरिदियो ("did it for someone") | Collapsed to a plain verb: "ate", "did" | Completion and timing lost, which is the exact XNLI "done speaking" failure |
| **Evidentiality** | रे marks hearsay ("reportedly"); रहेछ marks a newly discovered fact | Dropped entirely | A hedged report becomes a flat assertion; claim strength changes |
| **Negation** | Expressed by a verb prefix न-: गर्छ / गर्दैन, गर्नु / नगर्नु | Occasionally lost, especially in long or nested clauses | Direct polarity flip |
| **Pro-drop + agreement** | Subjects are often omitted; person, number, gender, and honorific live on the verb (गयो vs गइन् vs जानुभयो) | MT guesses the pronoun: wrong gender, wrong number, or "they" | Claims get attributed to the wrong person |
| **Honorifics** | Four levels of "you" (तँ / तिमी / तपाईं / हजुर) plus honorific verb forms | All collapse to "you"; honorific plurals can become literal plurals | Register lost; sometimes one person becomes "they" (several people) |
| **Fictive kinship** | दाइ, दिदी, भाइ used for strangers (addressing a shopkeeper as दाइ) | Translated literally as "brother" or "sister" | Invents a family relationship that was never asserted |
| **Number systems** | Devanagari digits; लाख (100,000) and करोड (10 million) | Digits copied as-is or misparsed; lakh/crore scale mistranslated | Quantities off by orders of magnitude |
| **Calendar** | Bikram Sambat dates (वि.सं. २०८१), about 56–57 years ahead of the Gregorian calendar | Year copied as if it were AD, or converted wrongly | Dates off by decades |
| **Named entities** | Names that are also common nouns: विकास (Bikash / "development"), आशा (Asha / "hope"); official names like नेपाल राष्ट्र बैंक | Names translated as words; inconsistent romanization (Sagarmatha vs Everest) | Entities disappear or split into variants |

The top three rows are the dangerous group. They produce perfectly fluent English, so they survive casual human review, and they change exactly the features (completion, certainty, polarity) that decide whether a claim is entailed.

### How these errors corrupt downstream semantic evaluation

**1. Gold labels silently become wrong.** When a benchmark is built by translating examples and copying the source label, any error in rows 1–4 can flip the true label while the stored label stays the same. Agrawal et al. measured this directly: re-annotated labels matched the inherited English labels only 66.5% of the time for Hindi and 60% for Urdu, versus 90.5% for English. Nepali is plausibly in the same range, but nobody has measured it here, so treat that as an open question.

**2. The noise is biased, not random.** These errors cluster by phenomenon. Evidential loss always strengthens claims, which pushes faithful-but-hedged answers toward "unsupported." Aspect collapse makes past-perfect and simple-past claims indistinguishable, which pushes contradictions toward "entailed." A judge evaluated on such data doesn't just look noisier; it looks systematically worse on specific constructions, and you might "fix" the judge to fit the corrupted labels.

**3. Ceilings get compressed.** If roughly a third of labels are wrong, even a perfect judge scores near 67% agreement. Differences between strong judges shrink inside that ceiling, so model comparisons lose resolution. Agrawal et al.'s headline finding is the same effect at the benchmark level: the cross-lingual gap for Swahili and Urdu shrank from about 14 points to under 4 once human translation errors were removed from the comparison.

**4. Translate-test pipelines get errors in both directions.** If you translate a Nepali answer to English before judging faithfulness against English context:
- **False negatives:** a faithful answer picks up an invented "brother," a wrong pronoun, or a lost hedge, and gets marked unfaithful.
- **False positives:** MT normalizes a hallucinated number or entity toward the more common form, which may happen to match the context, so the hallucination disappears before the judge sees it.

**5. PPI can't repair this.** This connects back to the first paper. PPI corrects the proxy's bias using gold labels, so it assumes those gold labels are true. If the "human" labels in your labeled subset were inherited through translation, the rectifier estimates the gap between the judge and corrupted labels, and the interval is confidently centered on the wrong value. Label quality is a precondition PPI takes as given.

### Practical safeguards

- **Normalize before translating:** convert Devanagari digits, flag BS dates for explicit conversion, and protect entities with do-not-translate spans or a glossary, as IndicTrans2 does.
- **Run the Agrawal gap check on your own data:** compare judge accuracy on human-translated versus machine-translated versions of the same items; a large gap flags translation problems.
- **Have native speakers re-label a sample in Nepali**, rather than inheriting English labels, before using it as a PPI gold set.
- **Stratify error audits by phenomenon** (aspect, evidentials, negation, numbers, entities) so a judge's weakness on one construction isn't hidden in an average.
- **Judge in the source language where possible**, instead of translating answers to English first, so MT errors can't enter between the answer and the verdict.

---

#### Q3.2: Rationale for Condition C3
*Why is Condition $C3$ strictly defined as human post-edited machine translation ($PE(MT)$) rather than a translation generated from scratch by a human translator? Why is this distinction crucial for isolating $\Delta_{MT} = A(C3) - A(C2)$?*

### Your Answer:
<!-- Enter your answer below this line -->
Condition $C3$ is strictly defined as human post-edited machine translation ($PE(MT)$) rather than a from-scratch human translation ($HT$) to eliminate stylistic, syntactic, and lexical divergence as confounding variables.

This distinction is crucial for isolating $\Delta_{MT} = A(C3) - A(C2)$ for two key reasons:

### 1. Minimal Pair / Counterfactual Isolation

Post-editing directly targets and fixes *only* the specific errors introduced by the MT model (e.g., entity mistranslations, dropped negations, grammatical distortions) while preserving the underlying sentence structure, phrasing, and vocabulary generated by $C2$.

As a result, $C3$ serves as a controlled counterfactual to $C2$: the two contexts are syntactically and lexically near-identical except for the correction of MT errors.

### 2. Preventing Confounding Variance in $\Delta_{MT}$

If $C3$ were generated from scratch by a human translator, it would introduce independent human translation variance—such as alternative phrasing, different clause structures, stylistic preferences, or reordered information.

Evaluating against a from-scratch translation would expand the delta equation into:

$$\Delta_{observed} = \text{Penalty from MT Errors} + \text{Evaluator Sensitivity to Stylistic/Syntactic Divergence}$$

By using $PE(MT)$, the stylistic noise is held constant ($PE(MT) \approx MT + \text{corrections}$), ensuring that $A(C3) - A(C2)$ isolates the performance penalty caused strictly by machine translation errors.
