# Continuous Endpoints - Bayesian Model Averaging Methods

Traditional BMD modeling involves fitting a number of dose-response models to the observed data and selecting the single “best” model based on predefined criteria (see [**Goodness of Fit Table**](./continuous-mle.md#goodness-of-fit-table) and [**AIC and Model Comparisons**](./continuous-mle.md#aic-and-model-comparisons)). However, no single traditional dose-response model can be expected to fully capture the underlying biology or toxicological modes of action, and each candidate model represents only a possible hypothesis about the biologic processes leading to the observed endpoint being modeled. Hence, using the associated BMDL from the “best” model may not fully reflect the true model uncertainty ([Haber et al., 2018](https://hero.epa.gov/reference/11400398/); [Wheeler & Bailer, 2007](https://hero.epa.gov/reference/669774/)). 

Therefore, model averaging in BMD modeling has been recommended by the National Institute for Occupational Safety and Health (NIOSH), World Health Organization (WHO), and the European Food Safety Authority (EFSA) as an approach that incorporates results from multiple candidate models, combined through weighted averaging to better account for model uncertainty ([Wheeler et al., 2020](https://hero.epa.gov/reference/5939422/);[Wheeler et al., 2022](https://hero.epa.gov/reference/10330529/)). Model averaging accounts for uncertainty across both individual model parameters and the suite of models analyzed ([Hinne et al., 2020](https://journals.sagepub.com/doi/10.1177/2515245919898657)). In addition, Bayesian inference is commonly employed for model averaging, as it improves characterization of uncertainty in risk value estimation by incorporating prior information and using observed data to estimate a posterior distribution of the parameter of interest (in this case, the BMD). Prior information is incorporated by specifying prior probability distributions for unknown model parameters. 

The EPA has developed an approach to Bayesian model averaging (BMA) for continuous data, termed "***L***everaging ***O***ptimized ***U***nified prior ***D***istributions" (LOUD) that seeks to balance prior influence and data-driven inference by employing both empirical and weakly-informative priors, which may reduce the risk of overly dominant prior effects on the posterior distribution.  The LOUD approach described in this section is applied to continuous dose-response data. 

In the LOUD framework, dose-response models are reparametrized in terms of interpretable response levels at the minimum and maximum doses of the dose-response dataset, corresponding to parameters directly tied to the observed data (e.g., the predicted means for continuous data). This allows for a consistent set of priors to be applied across model forms. The priors for two of each model’s parameters can be derived directly from the priors for the response levels at the minimum and maximum doses. For models with three or more parameters, the priors for the remaining parameters are defined separately, as discussed below. 

Note that the considerations regarding the [**Definition of the BMD**](./continuous-mle.md#defining-the-bmd)(i.e., selection of the appropriate BMR level) are the same for the Bayesian implementation of the continuous models.

:::{important}
At this time, EPA does not offer technical guidance on
Bayesian modeling or Bayesian model averaging.
:::

## LOUD Model Averaging - Continuous Endpoints

In an animal toxicological experiment with $r$ doses $x_i, i=1…r$, let $Y={\left({y}_{i1},{y}_{i2},…,{y}_{in_i }\right)}^{'}$ represent ${n}_{i}$ observations at the ${i}^{th}$ dose. Here, we assume all observations are independent and share a common error distribution, either normal or lognormal, such that the central tendency changes as a smooth dose-response function m of dose. If ${y}_{i}$ are normally distributed, $m({x}_{i})$ is the mean response given ${x}_{i}$, and if ${y}_{i}$ are lognormally distributed, $m({x}_{i})$ is the median response given ${x}_{i}$.  Specifically, when dose levels are scaled as explained above, ${m}_{0}$ and ${m}_{1}$ refer to the observed means at the minimum and maximum dose levels, respectively.

(priors-for-m0-and-m1)=
### Priors for m{sub}`0` and m{sub}`1`

For the continuous LOUD framework, the true mean responses at the minimum and maximum doses, ${m}_{0}$ and ${m}_{1}$, were assigned priors that reflect both the structure of the data and the theoretical motivation from reference prior theory. In a Normal model with unknown mean and variance, the reference prior is $\pi(\mu,\sigma) ∝ 1/\sigma$, where $\pi$ denotes the joint reference prior to making inferences about $\mu$ (Bernardo, 1979, **ADD REF**). When this prior is combined with data, the marginal posterior distribution for $\mu$ follows a non-standardized Student-t form with $n-1$ degrees of freedom, reflecting both the uncertainty in the mean and the sampling variability in the variance: 

$${m}_{0} \sim \text{student_t}\left({n}_{0}-1, {\overline{y}}_{0},\sqrt{\frac{{s}_{0}^{2}}{{n}_{0}-1}}\right)$$

$${m}_{1} \sim \text{student_t}\left({n}_{1}-1, {\overline{y}}_{1},\sqrt{\frac{{s}_{1}^{2}}{{n}_{1}-1}}\right)$$

where ${n}_{0}$ and ${n}_{1}$ are the numbers of observations, ${\overline{y}}_{0}$ and ${\overline{y}}_{1}$ are the observed mean responses, and ${s}_{0}^{2}$ and ${s}_{1}^{2}$ are the observed standard deviations of responses at the minimum and maximum dose levels ${d}_{0}$ and ${d}_{1}$, respectively. Here, the parameters for the non-standardized Student-t distributions represent degrees of freedom $\left({n}_{i}-1\right)$, location $\left({\overline{y}}_{i}\right)$, and scale $\left(\sqrt{\frac{{s}_{1}^{2}}{{n}_{1}-1}}\right)$, respectively.

The probability density function of the non-standardized Student-t distribution is:

$$\text{Student-t}\left(y|\nu,\mu,\sigma\right)=\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)} \times \frac{1}{\sqrt{\nu\pi}\sigma}{\left(1+\frac{1}{\nu}{\left(\frac{y-\mu}{\sigma}\right)}^{2}\right)}^{-\frac{\nu+1}{2}}$$

where $\nu$, $\mu$, and $$\sigma$ are the degrees of freedom, location, and scale parameters, respectively, and $\Gamma$ is the gamma function.

### Variance priors

For continuous models, variance refers to the variability of individual responses within each dose group and it must be explicitly modeled.  Consistent with how BMDS models variance for the MLE models [**Variance Model**](./continuous-mle.md#variance-model), the LOUD approach considers three variance structures:

- Normal distribution with constant variance
- Normal distribution with non-constant variance modeled as a power function of the mean response, and
- Lognormal distribution with a constant coefficient of variation

In all cases, an inverse-gamma prior was assigned to the variance term.  The inverse-gamma distribution is the conjugate prior for the variance of a Normal model and correspondes the reference prior for dispersion parameters ([Gelman, 2006](https://hero.epa.gov/reference/4235805/)).  The shape and scale hyperparameters were chosen to reflect the degrees of freedom and observed variability in the control and high-dose groups.  The probability function for the inverse-gamma distribution is:

$$\text{InvGamma}\left(y|\alpha,\beta\right)=\frac{{\beta}^{\alpha}}{\Gamma(\alpha)}{y}^{-\left(\alpha+1\right)}\text{exp}\left(-\beta \cdot \frac{1}{y}\right)$$

where $\alpha$ and $\beta$ are the shape and scale parameters, respectively, and $\Gamma$ is the gamma function.  The specific priors for the three variance structures are: 

1. **Normal distribution with constant variance**

The variance of observations in dose group $i$, ${Var}_{i}$ is:

$${Var}_{i} \sim \text{InvGamma}\left(\frac{{n}_{01}-1}{2},\frac{{n}_{01} \cdot {s}_{01}^{2}}{2}\right)$$

where ${n}_{01}$ is the total number of observations and ${s}_{01}^{2}$ is the total observed variance observed in both the ${x}_{0}$ and ${x}_{1}$ dose groups.  ${n}_{01}$ is subtracted by 1 to account for the degree of freedom lost from the estimation of ${s}_{01}^{2}$ itself. Here, the parameters in the inverse-gamma distribution represent the shape $\left(\frac{{n}_{01}-1}{2}\right)$ and scale $\left(\frac{{n}_{01} \cdot {s}_{01}^{2}}{2}\right)$, respectivley.  The observations from ${x}_{0}$ and ${x}_{1}$ dose groups are excluded from the likelihood when forming the posterior to avoid double counting.

2. **Normal distribution with non-constant variance**

The variance of observations is modeled as a power function of the mean:

$${Var}_{i}= \alpha \cdot {\lbrack\mu\left({d}_{i}\right)\rbrack}^{\rho}$$

where the parameters $\alpha$ and $\rho$ represent scale and power parameters and are estimated simultaneously with the other parameters in the dose-response model, and $\mu\left({d}_{i}\right)$ is the predicted response from the dose-response model under consideration for the ${i}^{th}$ dose group.  To estimate $\alpha$ and $\rho$, such that 

$${Var}_{i} \sim \text{InvGamma}\left(\frac{{n}_{0}-1}{2},\frac{{n}_{0} \cdot {s}_{0}^{2}}{2}\right)$$ 

$${Var}_{i} \sim \text{InvGamma}\left(\frac{{n}_{1}-1}{2},\frac{{n}_{1} \cdot {s}_{1}^{2}}{2}\right)$$

where ${n}_{0}$ and ${n}_{1}$ are the total number of observations and ${s}_{0}^{2}$ and ${s}_{1}^{2}$ are the total observed variances observed in both the ${x}_{0}$ and ${x}_{1}$ dose groups, respectively.  ${n}_{0}$ and ${n}_{1}$ are both subtracted by 1 to account for the degree of freedom lost from the estimation of ${s}_{1}^{2}$ and ${s}_{1}^{2}$ themselves. Using those estimates along with the estimates for ${m}_{0}$ and ${m}_{1}$, the esimates for $\alpha$ and $\rho$ may be calculated using the relationship described above for the definition of non-constant variance:

$$\rho = \frac{\log\left(\frac{{Var}_{1}}{{Var}_{0}}\right)}{\log\left(\frac{{m}_{1}}{{m}_{0}}\right)}$$

$$\alpha = \frac{{Var}_{0}}{{m}_{0}^{\rho}}$$

3. **Lognormal distribution with constant coefficient of variation**

For lognormal data with constant log-scale variance, the inverse-gamma prior is defined as:

$${Var}_{i} \sim \text{InvGamma}\left(\frac{{n}_{01}-1}{2},\frac{{n}_{01} \cdot {s}_{\log, 01}^{2}}{2}\right)$$

where ${s}_{\log, 01}$ is the overall observed log-scale variance across the ${x}_{0}$ and ${x}_{1}$ dose groups.

## Mathematical Details for Bayesian Continuous Models

BMDS Online (version 26.1) contains a total of nine Bayesian models for continuous endpoints as defined below. From the existing suite of MLE continuous models included in previous versions of BMDS, Bayesian versions of the Power, Exponential-3, Exponential-5, and additive Hill models were developed, as shown below. Bayesian versions of the polynomial and linear models were not developed as monotone restrictions on polynomials are difficult to enforce and non-monotone functions lead to difficulties when evaluating the BMD (such as the possibility of having two BMDs for the same BMR). 

```{figure} _static/img/cont_models_table_LOUD_BMDS.png
:alt: BMDS Online model table showing the default BMDS models available for continuous LOUD model averaging
:scale: 60%
:name: f83

BMDS models available for LOUD Bayesian model averaging
```

In addition to the existing BMDS continuous models, dose-response models from RIVM and EFSA have also been incorporated into BMDS.  These dose-response functions from [EFSA](https://hero.epa.gov/reference/12033104/) and [PROAST](https://hero.epa.gov/reference/4850042/) were the 4-parameter multiplicative Hill, Inverse-Exponential, and Lognormal models (termed “canonical” models in ([Slob et al., 2025](https://pubmed.ncbi.nlm.nih.gov/40202288/)) and the Gamma, and linearized multistage (LMS)-two-stage  models. 

```{figure} _static/img/cont_models_table_LOUD_extended.png
:alt: BMDS Online model table showing the extended models available for continuous LOUD model averaging
:scale: 60%
:name: f84

Extended models available for LOUD Bayesian model averaging
```
:::{note}
Note that, with respect to the BMDS Hill model, the term "additive" connotes that the portion of the dose-response curve that changes with dose is treated additively relative to the background response variable, i.e., the model takes the form $m(x|\theta) = g + \frac{v \times {dose}^{n}}{k^{n} + {dose}^{n}}$.  For the multiplicative Hill model (see [PROAST](https://hero.epa.gov/reference/4850042/)), the background is treated multiplicatively instead:  $m\left(x|\theta\right) = a \left\lbrack 1 + \left(c -1\right) \cdot \frac{{x}^{d}}{{b}^{d}+{x}^{d}} \right\rbrack$
:::

Additionally, the Bayesian model averaging performed by BMDS considers not only uncertainty across models, but also uncertainty across distributional forms. So, for every model, all three distributional forms (normal/constant, normal/non-constant, lognormal) can be included in the model average, except for the lognormal assumption for the Power and additive Hill models.  These two models are additive to background and can conceivably estimate negative responses, possibly violating the lognormal distribution assumption.

For example, see below, where the Exponential 3 model is included three times, once each for each variance assumption.

```{figure} _static/img/LOUD_cont_model_and_dist.png
:alt: BMDS Online model table showing the exponential three is included three times in the averaging suite.  
:scale: 30%
:name: f85

LOUD continuous model and distribution combinations
```
Therefore, considering the combination of available models and distribution types, running a LOUD continuous model averaging analysis using the default BMDS models would consist of 10 model + distribution combinations.  Running the full extended suite of BMDS + PROAST + EFSA models would consist of either 22 or 23 model + distribution combinations, depending on whether the additive Hill or multiplicative Hill model was included in the suite, respectively.

:::{note}
Although there are a total of nine Bayesian continuous models, the user must select whether the additive or multiplicative Hill will be used in the model average.  Thus, the full model averaging suite of continuous models would be Power, Exponential 3, Exponential 5, Inverse Exponential, Lognormal, Gamma, LMS two-stage and either the additive Hill (BMDS) or multiplicative Hill (PROAST) models
:::

### Individual Model Specifications

The continuous dose-response functions and their prior distributions used in Bayesian parameter estimation are shown below.  One or two of each model's parameters can be expressed in terms of ${m}_{0}$ and ${m}_{1}$ and the priors for these parameters cna derived using the distributions for ${m}_{0}$ and ${m}_{1}$ listed [**above**](#priors-for-m0-and-m1).  For example, for the Power model:

$$m\left(x|\theta\right)= g + v \cdot {x}^{n}$$

The background parameter ($g$) can be defined explicitly as ${m}_{0}$: 

$$m\left({d}_{0}\right) = {m}_{0} = g + v \cdot {0}^{n} = g$$

and the slope parameter ($v$) can be defined in terms of both ${m}_{0}$ and ${m}_{1}$:

$$m\left({d}_{1}\right) = {m}_{1} = {m}_{0} + v \cdot {1}^{n}$$

$$\nu = {m}_{1} - {m}_{0}$$

The priors for the remaining parameters are listed below explicitly and were obtained from [Wheeler et al., 2022](https://hero.epa.gov/reference/10330529/).  For example, the power parameter prior for each model was chosen to reflect the assumption that large amounts of curvature are not expected.  Similar to the dichotomous models, the parameters that identify curvature were assigned separate priors because ${m}_{0}$ and ${m}_{1}$ do not provide information to identify the shape of the curve.  

::::{tab-set}

:::{tab-item} Power

**Model Form**

$$m\left(x|\theta\right) = g + v \times (dose)^{n}$$

**Parameters**

$g$ = control response (intercept)

$v$ = slope

$n$= power

**Parameter Priors**

$g = {m}_{0}$

$v = {m}_{1} - {m}_{0}$

$n \sim \ln(\log(1.6), 0.421)$

:::

:::{tab-item} Hill (additive)

**Model Form**

$$m\left(x|\theta\right) = g + \frac{v \times {dose}^{n}}{k^{n} + {dose}^{n}}$$

**Parameters**

$g$ = control response (intercept)

$k$ = dose with half-maximal change (normalized)

$n$= power

$v$= maximum change

**Parameter Priors**

$g = {m}_{0}$ 

$k \sim \ln(0,2)$ 

$n \sim \ln(\log(1.6, 0.421)$

$v = \left({m}_{1} - {m}_{0}\right) \cdot \left({k}^{n}+1\right)$
:::

:::{tab-item} Exponential 3

**Model Form**

$$m\left(x|\theta\right) = a \times e^{\pm (b \times dose)^{d}}$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b = {\brack\log\left(\frac{{m}_{1}}{{m}_{0}}\right)\rbrack}^{\frac{1}{c}}$ 

$d \sim \ln(\log(1.6, 0.421)$

**Notes**

The sign in "$\pm b$" will change depending on
the user-designated or auto-detected direction of change:

-   \+ for responses increasing with dose

-   \- for responses decreasing with dose

#### Reference for Exponential models

RIVM (National Institute for Public Health and the Environment (Netherlands)). ([RIVM, 2018](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4850042)).
:::

:::{tab-item} Exponential 5

**Model Form**

$$m\left(x|\theta\right) = a \times (c - (c - 1) \times e^{- (b \times dose)^{d}})$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b = \sim \ln(0,2)$ 

$c = \frac{{m}_{0}-{m}_{1} \cdot \exp^\left({b}^{n}\right)}{{m}_{0}-{m}_{0} \cdot \exp^\left({b}^{n}\right)}$

$d \sim \ln(\log(1.6, 0.421)$

#### Reference for Exponential models

RIVM (National Institute for Public Health and the Environment (Netherlands)). ([RIVM, 2018](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4850042)).
:::

:::{tab-item} Hill (multiplicative)

**Model Form**

$$m\left(x|\theta\right) = a \left\lbrack 1 + \left(c -1\right) \cdot \frac{{x}^{d}}{{b}^{d}+{x}^{d}} \right\rbrack$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b \sim \ln(0,2)$ 

$c = \frac{{m}_{0}-{m}_{1}}{{m}_{0}} \cdot \left(b + 1\right) + 1$

$d \sim \ln(\log(1.6, 0.421)$
:::

:::{tab-item} Inverse Exponential

**Model Form**

$$m\left(x|\theta\right) = a \left\lbrack 1 + \left(c-1\right) \cdot e^{\left(-b \cdot {x}^{-d}\right)} \right\rbrack$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b \sim \ln(0,2)$ 

$c = \frac{{m}_{1}-{m}_{0} + {m}_{0} \cdot \exp^{-b}}{{m}_{0} \cdot e^{(-b)}}$

$d \sim \ln(\log(1.6, 0.421)$
:::

:::{tab-item} Lognormal
**Model Form**

$$m\left(x|\theta\right) = a \left\lbrack 1 + \left(c-1\right) \cdot \Phi\left(\log(b) + d \cdot \log(x)\right) \right\rbrack$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b \sim \ln(0,2)$ 

$c = \frac{{m}_{1}-{m}_{0} + {m}_{0} \cdot \Phi\left(\log(b)\right)}{{m}_{0} \cdot \Phi\left(\log(b)\right)}$

$d \sim \ln(\log(1.6, 0.421)$

:::

:::{tab-item} Gamma
**Model Form**

$$m\left(x|\theta\right) = a \left\lbrack 1 + \left(c-1\right) \cdot pgamma(b \cdot x, d, 1) \right\rbrack$$

where 

$$pgamma\left(\beta \cdot x,\alpha,1 \right) = \int_{0}^{\beta x}{t^{\alpha - 1}\exp( - t)dt\ }$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b \sim \ln(0,2)$ 

$c = \frac{{m}_{1}-{m}_{0}}{{m}_{0} \cdot pgamma(b,d,1)} + 1$

$d \sim \ln(\log(1.6, 0.421)$

:::

:::{tab-item} LMS two-stage
**Model Form**

$$m\left(x|\theta\right) = a \left\lbrack 1 + \left(c-1\right) \cdot \left(1 - exp^{-b \cdot x - d \cdot {x}^{2}} \right) \right\rbrack$$

**Parameters**

$a$ = control response (intercept)

$b$ = slope

$c$ = asymptote term

$d$= power

**Parameter Priors**

$a = {m}_{0}$ 

$b \sim \ln(0,2)$ 

$c = \frac{{m}_{1}-{m}_{0} \cdot \exp^{-b-d}}{{m}_{0}-{m}_{0} \cdot \exp^{-b-d}}$

$d \sim \ln(\log(1.6, 0.421)$

:::
::::

### Option Sets and Datasets for LOUD Model Averaging

For LOUD model averaging, the considerations of parameterizing the modeling analysis using the Option Set table is largely the same as for the MLE models [Option Sets](./continuous-mle.md#option-sets) with some important differences.  First, given the computational load that MCMC sampling entails, only two option sets are allowed when using LOUD model averaging.

```{figure} _static/img/LOUD_option_set_limit.png
:alt: BMDS Online option set table demonstrating the two option set limit.  
:scale: 90%
:name: f86

Only two option sets are allowed if LOUD continuous model averaging is used
```
Additionally, only the standard deviation and relative deviation BMR types are currently available for LOUD model averaging.  Additional BMR types (e.g., Hybrid approach, absolute deviation, etc.) will be available in future versions of BMDS.

In addition to the two option set limit, only two datasets are allowed when using LOUD model averaging.  Therefore, if using LOUD model averaging, only 4 dataset * option sets are allowed.

```{figure} _static/img/LOUD_dataset_limit.png
:alt: BMDS Online data tab demonstrating the two dataset limit.  
:scale: 80%
:name: f87

Only two option sets are allowed if LOUD continuous model averaging is used
```

### Bayesian Parameter Estimation
Markov chain Monte Carlo (MCMC) sampling is used to derive posterior distributions for the standard model parameters and BMDs. MCMC sampling is conducted by using a latent slice sampler in compiled the C++ bmdscore library.  The latent slice sampler is a more computationally efficient alternative to the Metropolis-Hastings algorithm and addresses the issues raised in other sampling algorithms ([Li, 2022](https://repositories.lib.utexas.edu/items/e2c66f3f-a89f-4a32-8d29-6c5162d16c5d); [Li & Walker, 2023](https://www.sciencedirect.com/science/article/pii/S0167947322002328)). 

The structure of the MCMC sampling is customizable in BMDS: the default is 1 chain of 50,000K samples with 5,000 samples discarded as burn-in, but up to 4 separate chains can be used. The maximum number of iterations across all chains is 50,000.  The minimum number of samples per chain is 2,500 with a minimum burn-in of 100 per chain. The default seed used for MCMC sampling is zero, but any value (between 0 and 2,147,483,647) can be selected by the user. 

```{figure} _static/img/LOUD_MCMC_settings.png
:alt: BMDS Online MCMC settings for LOUD model averaging.  
:scale: 80%
:name: f88

MCMC settings for LOUD continuous model averaging
```
Convergence diagnostics for all analyses are calculated and provided to the user for consideration: 

- The potential scale reduction statistic ($\hat{R}$)
- Markov Chain standard error
- Bulk effective sample size (ESS)
- Tail effective sample size 

See [Specific Continuous Bayesian Model Averaging Results](#specific-continuous-bayesian-model-averaging-results) for more details on these diagnostics and their interpretation.

### Bayesian Model Averaging

The BMD is estimated from a cross-model/distribution posterior distribution formed by combining posterior samples from each model, weighted by their prior weight (usually equally distributed across the model suite) and posterior model probability. 

For continuous data, there are a total of eight models that can be included in the model average, corresponding to a total of 22 or 23 model/distribution combinations, depending on whether the additive or multiplicative Hill model was included.

So, suppose there are K = 23 model/distribution combinations are under consideration, for the ${k}^{th}$ model, ${M}_{k}$, let ${θ}_{k}$ denote its vector of model-specific parameters, and define the model-specific BMD as a function of these parameters, ${BMD}_{k}$. The model ${M}_{k}$ is associated with a likelihood function $\ell \left(Y|{M}_{k},{θ}_{k} \right)$, which describes the data-generating process. The cross-model/distribution posterior distribution for the BMD can be expressed as:

$$p \left(BMD|Y \right) = \sum_{k = 1}^{K}{{w}_{k}p \left( {BMD}_{k}|Y,{M}_{k} \right)}$$

where ${w}_{k}$ represents the normalized weight for model ${M}_{k}$.

The model weights used for generating the model-averaged posterior can be calculated in one of two ways in BMDS:

1. The Watanabe-Akaike Information Criterion (WAIC), which computes a log pointwise posterior predictive density and adds a correction for the effective number of parameters to adjust for overfitting ([Gelman, 2013](https://hero.epa.gov/reference/13243402)).  The WAIC is asymptotically equivalent to leave-one-out cross-validation (LOO) ([Vehtari, et al. (2016)](https://hero.epa.gov/reference/13243404)). For model averaging, the WAIC weights are computed by normalizing the inverse of the WAIC for each model. If ${WAIC}_{k}$ is the WAIC for model ${M}_{k}$, the WAIC weight for ${M}_{k}$, ${w}_{k}$, is given by:

$${w}_{k} = \frac{e^{\left(-\frac{1}{2}{WAIC}_{k}\right)}}{\sum_{k=1}^{K}e^{\left(-\frac{1}{2}{WAIC}_{k}\right)}}$$

2. Posterior predictive model probabilities, $P\left({M}_{k},{\theta}_{k}|Y\right)$, determined by Bayes' theorem:

$$P\left({M}_{k},{\theta}_{k}|Y\right) = \frac{f\left({M}_{k}\right)\int{L\left(Y|{M}_{k},{\theta}_{k}\right)\pi\left({M}_{k},{\theta}_{k}\right)d{\theta}_{k}}}{\sum_{i=1}^{K}f\left({M}_{i}\right)\int{L\left(Y|{M}_{i},{\theta}_{i}\right)\pi\left({M}_{i},{\theta}_{i}\right)d{\theta}_{i}}}$$

Estimating the posterior model probabilities requires numerical approximation techniques and BMDS uses bridge sampling to estimate these quantities ([Fang et al, 2015](https://hero.epa.gov/reference/4141312/)).

The WAIC approach to estimating model weights is used by default in BMDS as it consistently provides stable BMD estimation for continuous endpoints.  For continuous endpoints, the observations from the ${d}_{0}$ and ${d}_{1}$ groups are excluded from the likelihood when forming the posterior to avoid double-counting, as these same data are used to update the prior hyperparameters.

### Summary Level Data vs. Individual Responses

The LOUD approach can be applied to summary level statistics (i.e., reported means and standard deviations) as well as to individual response data (i.e., a series of response values for each test subject, from which means and standard deviations are derived).

When individual response data are reported and used for dose-response modeling, the summary statistics are calculated by the software and used for statistical calculations.  When summary statistics are used, given that they are most often generated under the normal distribution assumption (i.e., are arithmetic means and standard deviations), the data must be transformed to the log-scale for the lognormal variance model.  BMDS uses the method employed in [ToxicR](https://hero.epa.gov/reference/12902051/) to do so:

$${\overline{y}_{i}}^{'} = \log\left(\overline{y}_{i}\right) - 0.5 \cdot \left\lbrack{\left(\frac{{s}_{i}}{\overline{y}_{i}}\right)}^{2}+1\right\rbrack$$

$${s}_{i}^{'} = \sqrt{ \log\left\lbrack{\left(\frac{{s}_{i}}{\overline{y}_{i}}\right)}^{2}+1\right\rbrack}$$

where $\overline{y}_{i}$ and ${s}_{i}$ are the arithmetic mean and standard deviation, respectively ([Crump, 1995](https://hero.epa.gov/reference/2258/); [Slob, 2002](https://hero.epa.gov/reference/24962/)). 

:::{important}
Extensive simulation testing of the continuous LOUD model averaging methods indicated that almost identical results were obtained when using either summary data or individual data.
:::

### BMD and BMDL estimation

Once the model-averaged posterior density of the BMD is estimated, the model-averaged BMD is simply the median of the posterior distribution and the 5$^{th}$ and 95$^{th}$ percentiles of the posterior distribution are used as the BMDL and BMDU, respectively.

## Specific Continuous Bayesian Model Averaging Results

Results for continuous LOUD model averaging are displayed on the Output tab, including the dataset modeled, the option set used, the MCMC options used, and the modeling summary table and plot.

```{figure} _static/img/LOUD_cont_output_tab.png
:alt: BMDS Online Output tab for LOUD model averaging.  
:scale: 70%
:name: f89

Output tab for continuous LOUD model averaging analysis
```
Clicking on an individual model will display that model's results in a separate window.  As on the main Output tab, the dataset, option set, and MCMC options are displayed, along with the modeling summary for that individual model. Note that the model p-value is displayed in the Model Summary table.  Although p-values are not used as cut-off values to exclude models in Bayesian model averaging, it is useful to check individual model p-values to ensure that at least one model in the averaging suite adequately fits the observed data.

```{figure} _static/img/LOUD_cont_individual_model.png
:alt: Individual modeling results for a LOUD continuous model averaing analysis.  
:scale: 80%
:name: f90

Modeling results for a single model included in a LOUD model averaing analysis
```
Scrolling down the individual model window will display the model parameters table, the Goodness of Fit table, and the BMD cumulative distribution table and plot.

```{figure} _static/img/LOUD_cont_individual_model_2.png
:alt: Additional individual modeling results for a LOUD continuous model averaing analysis.  
:scale: 80%
:name: f91

Additional modeling results for a single model included in a LOUD model averaing analysis
```

The model parameter table provides users with MCMC convergence and sampling diagnostics:

- **The potential scale reduction statistic ($\hat{R}$)**: the ratio of the average variation of samples within each Markov chain to the variance of samples across all chains.  When chains have reached equilibrium (i.e., have converged), the $\hat{R}$ statistic will equal 1; when chains have not converged the $\hat{R}$ statistic will be greater than 1.  In general, values less than 1.01 indicate convergence; values less than 1.1 may be also be acceptable for some analyses, but 1.01 is a stricter target for convergence. Note, that the $\hat{R}$ statistic will only be reported when greater than one Markov chain is used.

- **Markov Chain standard error (median)**: estimates the Monte Carlo error in the posterior summaries of the parameters due to using a finite MCMC sample.  This diagnostic quantifies how much of the posterior median varies due to simulation noise. In general, values of the Markov Chain standard error much lower than the reported median absolute deviation indicate the Monte Carlo estimate of the median is likely stable. 

- **Bulk and Tail effective sample size (ESS)**: Bulk ESS measures the sampling efficiency for estimating the posterior median whereas Tail ESS measures the sampling efficiency for estimating the boundaries of the posterior (i.e., the 5th and 95th percentiles).  Higher values of both indicate good sampling efficiency.

A reasonable rule of thumb is that the Markov chains can be considered to have converged when both $\hat{R}$ is below 1.1 and ESS values are greater than 100 per Markov chain. When these targets are not met, the number of MCMC iterations can be increased to try to acheive convergence.  If convergence for an individual model is not acheivable, that model/distrbution combination can be removed from the model averaging suite and the analysis re-run without it.

Scrolling to the bottom of the individual model window will display the model parameter distributions table, where posterior distributions of the model BMD and parameter values are displayed along with trace plots of those same parameters.  

```{figure} _static/img/LOUD_cont_individual_model_3.png
:alt: Plots for model parameter posterior distributions and associated trace plots for a LOUD continuous model averaing analysis.  
:scale: 80%
:name: f92

Model specific posterior parameter distribution and trace plots
```

Trace plots show the sampled values of a parameter across all iterations of the MCMC chains. Trace plots can help assess whether chains are mixing well and whether they have reached a stable, stationary distribution. Ideally, trace plots will look like a "hairy caterpillar" where the chain moves around a constant level without obvious trends, shifts, or abrupt jumps.  Occasionally, a few extreme samples might be observed (individual values inconsistent with the overall trend in the chain).  These divergent value transitions may be problematic but overall are less of a concern in an well-behaved trace plot.  

Overall, trace plots are diagnostic and not definitive. Trace plot behavior should always be considered alongside the $\hat{R}$, Markov Chain standard error, and bulk and tail ESS values.

Clicking on the Model Average in the LOUD Bayesian Model Results table will display the detailed modeling results for the Bayesian model average.

```{figure} _static/img/LOUD_cont_model_average_results.png
:alt: Detailed modeling results for LOUD modeling averaging.  
:scale: 80%
:name: f93

Continuous LOUD model averaging results
```

The Individual Model Results table provides the same convergence and sampling diagnostics for individual model and model averaged BMD posteriors, along with the model-specific prior weights and posterior probabilities.