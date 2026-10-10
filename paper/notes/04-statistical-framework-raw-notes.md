# Paper Section: 4. Statistical Inference with Prediction-Powered Inference (PPI)

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. Motivation: Statistically Valid Scaling
Human gold annotations ($n \approx 120\text{--}150$) are necessary for high-fidelity evaluation and Krippendorff's $\alpha$ calculation, but lack statistical power when assessing subtle effect sizes across sub-categories. Rather than relying on ungrounded automatic evaluations, we use **Prediction-Powered Inference (PPI)** via the **GLIDE** framework to produce finite-sample and asymptotic confidence intervals over the full corpus ($N \approx 1,500$) without introducing model bias.

## 2. Cluster-Robust Formulation for Nested Claims
Claims $k_{ij}$ ($j=1,\dots,M_i$) are nested within answer item $i$. Because claims within an item share context and prompt features, residuals exhibit intra-cluster correlation ($\rho_{\text{ICC}} > 0$). Standard i.i.d. PPI underestimates standard errors.

### Item-Level Cluster Residuals
For sampling stratum $s$, we define the item-level cluster residual:
$$U_{is} = \sum_{j=1}^{M_{is}} \left( Y_{ijs} - \lambda_s^* f(X_{ijs}) \right)$$
where $f(X)$ is the proxy autorater prediction, $Y$ is the human gold label, and $\lambda_s^*$ is the adaptive tuning parameter (PPI++).

### Stratified Cluster-Robust Variance
$$\hat{V}(\hat{\theta}_{\text{PPI}}) = \sum_{s} W_s^2 \cdot \frac{N_s}{N_s - 1} \sum_{i=1}^{n_s} \left( \frac{U_{is} - \bar{U}_s}{\sum_i M_{is}} \right)^2$$
where $W_s$ represents population stratum weights.

## 3. Paired Covariance Cancellation on $\Delta_{XL} - \Delta_{MT}$
Because all three conditions ($C1, C2, C3$) are evaluated on identical items:
$$\text{Var}(\hat{\Delta}_{XL} - \hat{\Delta}_{MT}) = \text{Var}(\hat{\Delta}_{XL}) + \text{Var}(\hat{\Delta}_{MT}) - 2\mathbf{Cov}(\hat{\Delta}_{XL}, \hat{\Delta}_{MT})$$
The positive covariance between conditions cancels shared noise, yielding tight confidence intervals for the hypothesis test $H1: \Delta_{XL} > \Delta_{MT}$ even with $n = 120\text{--}150$ gold items.
