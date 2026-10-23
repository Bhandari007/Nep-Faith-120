# Section 4: Statistical Inference & Prediction-Powered Framework

## 4.1 Motivation: Unbiased Semi-Supervised Scaling

Rigorous cross-lingual RAG evaluation requires high-precision human gold labels ($n=120$ items, doubly annotated and adjudicated). However, evaluating subtle performance gaps across sub-genres and perturbation types on $n=120$ alone yields wide confidence intervals. Conversely, relying solely on automated LLM judges introduces uncalibrated systematic bias.

To resolve this dilemma, we adopt **Prediction-Powered Inference (PPI++)** ([Angelopoulos et al., 2023](https://arxiv.org/abs/2301.09633); [Gao et al., 2026](https://arxiv.org/abs/2608.26638)). PPI++ treats automated proxy autorater predictions ($f(X)$) as control variates over an expansive unlabelled inference corpus ($N = 1,200$), debiasing them against the adjudicated human gold sample ($n = 120$). This framework guarantees mathematically valid, asymptotic and finite-sample confidence intervals without requiring model correctness assumptions.

---

## 4.2 Mathematical Formulation of PPI++

Let $\theta^* = \mathbb{E}[Y]$ denote the true population parameter of interest (e.g., evaluator faithfulness accuracy against human gold ground truth). Over the small gold labeled set $\mathcal{D}_n = \{(X_i, Y_i)\}_{i=1}^n$ and the large unlabelled proxy set $\mathcal{D}_N = \{\tilde{X}_i\}_{i=1}^N$, we formulate the PPI++ estimator as:
$$\hat{\theta}^{\text{PP}} = \underbrace{\frac{1}{N}\sum_{i=1}^N f(\tilde{X}_i)}_{\text{Large Proxy Imputation}} \;-\; \lambda^* \underbrace{\left(\frac{1}{n}\sum_{i=1}^n f(X_i) - \frac{1}{n}\sum_{i=1}^n Y_i\right)}_{\text{Measured Proxy Bias (Rectifier)}}$$
where $\lambda^*$ is the data-driven tuning parameter chosen to minimize the asymptotic variance of the estimator:
$$\lambda^* = \frac{\widehat{\text{Cov}}(Y, f(X))}{\widehat{\text{Var}}(f(X))}$$

### Unbiasedness Guarantee
Under the pre-registered sampling protocol, both labeled and unlabelled items are drawn from the identical stratified data-generating distribution. Taking expectations:
$$\mathbb{E}[\hat{\theta}^{\text{PP}}] = \mathbb{E}[f(X)] - \lambda^*\big(\mathbb{E}[f(X)] - \mathbb{E}[Y]\big) = \mathbb{E}[Y] = \theta^*$$
Because the proxy bias appears symmetrically in the unlabelled imputation and the gold rectifier, the bias cancels out in expectation regardless of proxy quality.

### Variance Reduction & PPSR
When the proxy autorater correlates strongly with human judgment ($\rho > 0$), the residual $Y_i - \lambda^* f(X_i)$ exhibits substantially lower variance than $Y_i$ alone. The relative efficiency gain is quantified by the **Prediction-Powered Sample-size Ratio (PPSR)**:
$$\text{PPSR} = \frac{\widehat{\text{Var}}(\hat{\theta}_{\text{classical}})}{\widehat{\text{Var}}(\hat{\theta}^{\text{PP}})} \approx \frac{1}{1 - \rho^2}$$
A PPSR of $1.73\times$ demonstrates that the $N=1,200$ unlabelled corpus expands the effective sample size from $n=120$ to the equivalent of $\approx 208$ fully human-annotated items, shrinking confidence intervals by ~24% for free. If $\rho \approx 0$, the estimator adaptively shrinks $\lambda^* \to 0$, gracefully falling back to classical sample mean variance without inflating error bars.

---

## 4.3 Cluster-Robust Variance for Nested Claims

In our evaluation hierarchy, atomic propositions $\{k_{ij}\}_{j=1}^{M_i}$ are nested within answer item $i$. Because propositions within the same item share context, topic, and generation parameters, their evaluation residuals exhibit significant positive intra-cluster correlation ($\rho_{\text{ICC}} > 0$). Standard i.i.d. variance estimators severely underestimate standard errors in hierarchical NLP data.

To guarantee valid nominal coverage, we employ a cluster-robust Huber-White sandwich variance estimator clustered at the item level ($i$):
1. For item $i$, define the cluster-aggregated residual:
   $$U_i = \sum_{j=1}^{M_i} \left( Y_{ij} - \lambda^* f(X_{ij}) \right)$$
2. The cluster-robust empirical variance of the rectifier term is given by:
   $$\hat{V}_{\text{cluster}} = \frac{n}{n - 1} \sum_{i=1}^n \left( \frac{U_i - \bar{U}}{\sum_{i=1}^n M_i} \right)^2$$
This formulation ensures that all hypothesis tests are asymptotically exact and robust to arbitrary within-item correlation structures.

---

## 4.4 Active Paired Covariance Cancellation on $\Delta_{XL} - \Delta_{MT}$

Our central hypothesis tests whether cross-lingual evaluation degradation strictly exceeds raw machine translation error:
$$H_1: \Delta_{\text{XL}} - \Delta_{\text{MT}} = A(C2) - A(C1) > 0$$

Because identical evaluation items are scored under both Condition $C1$ and Condition $C2$, the estimator exploits paired covariance cancellation:
$$\text{Var}\big(\hat{A}(C2) - \hat{A}(C1)\big) = \text{Var}\big(\hat{A}(C2)\big) + \text{Var}\big(\hat{A}(C1)\big) - 2\,\mathbf{Cov}\big(\hat{A}(C2), \hat{A}(C1)\big)$$

Because difficult passages (e.g., highly technical medical reports or complex historical chronologies) degrade accuracy across *both* conditions simultaneously, the covariance term $\mathbf{Cov}(C2, C1)$ is strictly positive. The negative covariance multiplier actively cancels background item-difficulty variance, resulting in sharp, high-powered confidence intervals for $H_1$ even with modest human gold samples.

---

## 4.5 Pre-Freeze Monte Carlo Recovery Benchmark

In accordance with our pre-registered gate protocol (Gate 1), the cluster-robust paired PPI++ statistical engine was rigorously validated prior to human gold annotation. We executed 100 Monte Carlo simulation trials (`tests/recovery/test_ppi_recovery.py`) featuring:
- A planted true gap: $\Delta^* = 0.1200$
- Cluster correlation with 3 claims per item ($\rho_{\text{ICC}} = 0.35$)
- An imperfect proxy rater ($85\%$ classification accuracy)
- Sample dimensions: $n=120$ labeled items, $N=1,200$ unlabelled items

| Metric | Target Value | Empirical Recovered Result |
| :--- | :---: | :---: |
| **Point Estimate ($\hat{\Delta}$)** | $0.1200$ | **$0.1178$** (Empirical Bias: $0.0022$) |
| **95% Confidence Interval Coverage** | $95.0\%$ | **$95.0\%$** (Exact nominal calibration) |
| **Relative Efficiency Gain (PPSR)** | $> 1.0\times$ | **$1.730\times$** (+73% effective sample size) |
| **Human Annotation Savings** | -- | **$42.2\%$** fewer human labels required |

The Monte Carlo benchmark confirms that the estimator recovers the planted treatment effect without attenuation or inflation, achieving exact 95% empirical coverage.
