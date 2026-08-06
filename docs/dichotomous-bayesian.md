# Dichotomous Endpoints - Bayesian Model Averaging Methods

As described in the [Continuous Endpoints - Bayesian Model Averaging Methods](./continuous-bayesian.md) section, Bayesian model averaging (BMA) methods offer several advantages to typical MLE single-model selection methods. 

Briefly, traditional BMD modeling involves fitting a number of dose-response models to the observed data and selecting the single “best” model based on predefined criteria (see [**Goodness of Fit Table**](./dichotomous-mle.md#goodness-of-fit-table) and [**AIC and Model Comparisons**](./dichotomous-mle.md#aic-and-model-comparisons)). However, no single traditional dose-response model can be expected to capture the underlying biology or toxicological modes of action, and each candidate model represents only a possible hypothesis about the biologic processes leading to the observed endpoint being modeled. 

Model averaging accounts for uncertainty across both individual model parameters and the suite of models analyzed ([Hinne et al., 2020](https://journals.sagepub.com/doi/10.1177/2515245919898657)). In addition, Bayesian inference is commonly employed for model averaging, as it improves characterization of uncertainty in risk value estimation by incorporating prior information and using observed data to estimate a posterior distribution of the parameter of interest (in this case, the BMD). Prior information is incorporated by specifying prior probability distributions for unknown model parameters. BMDS model averaging proceeds from the basis of Bayesian analyses, for which the parameters of the models under consideration are updated using
the dataset of interest.  

Currently, there are two approaches for Bayesian model averaging for dichotomous endpoints available in BMDS:

1. [LOUD](./dichotomous-bayesian.md#mathematical-details-for-loud-bayesian-dichotomous-models) methods, using MCMC sampling and WAIC weights (fully described in Jacketti et al., 2026 **ADD REF**)

2. [ToxicR](./dichotomous-bayesian.md#mathematical-details-for-toxicr-bayesian-dichotomous-models) methods, using  *a posteriori* and Laplace approximation methods (fully described in [Wheeler et al. 2020](https://hero.epa.gov/reference/5939422/) and [Wheeler, 2022](https://hero.epa.gov/reference/12902051/)), and 

:::{important}
At this time, EPA does not offer technical guidance on Bayesian modeling or Bayesian model averaging.
:::

## LOUD Model Averaging - Dichotomous Endpoints

The EPA has developed an approach to BMA for dichotomous data, termed "***L***everaging ***O***ptimized ***U***nified prior ***D***istributions" (LOUD) that seeks to balance prior influence and data-driven inference by employing both empirical and weakly-informative priors, which may reduce the risk overly dominant prior effects on the posterior distribution.  The LOUD approach is applied to dichotomous dose-response data, where each response can take on one of only two possible outcomes, positive (effect present) and negative (effect absent). 

In the LOUD framework, dose-response models are reparametrized in terms of interpretable response levels at the minimum and maximum doses of the dose-response dataset, corresponding to parameters directly tied to the observed data (e.g., the response probabilities for dichotomous data). This allows for a consistent set of priors to be applied across model forms. The priors for two of each model’s parameters can be derived directly from the priors for the response levels at the minimum and maximum doses. For models with three or more parameters, the priors for the remaining parameters are defined separately, as discussed below. 

(priors-for-p0-and-p1)=
### Priors for p{sub}`0` and p{sub}`1` 

In an animal toxicological experiment with $r$ increasing doses, ${x}_{1}, \ldots, {x}_{r}$, let $Y = ({y}_{1}, {y}_{2}, \ldots, {y}_{r})$ represent the vector of observed positive responses for each dose group, where each ${y}_{i}$ corresponds to the observed number of positive responses at dose ${x}_{i}$, and let ${n}_{1}, \ldots, {n}_{r}$ denote the total number of animals per group.  Then ${y}_{i} \sim \text{Binomial}({n}_{i},p({x}_{i}))$, where $p({x}_{i})$ is the probability of a positive response at dose ${x}_{i}$.  Specifically, when dose levels are scaled such that the control dose = 0 and the highest dose = 1, ${p}_{0}$ and ${p}_{1}$ refer to the probabilities of response at the minimum and maximum dose levels, respectively. 

Since ${p}_{0}$ and ${p}_{1}$ are proportions (the proportion of responders at the relevant doses), Beta distributions were selected as priors because Beta is the conjugate prior class for modeling Binomial proportions.  For prior development, priors for ${p}_{0}$ and ${p}_{1}$ were sought that presented invariance under reparameterization and aligned with reference prior theory ([Bernardo, 1998](https://www.uv.es/~bernardo/Monograph.pdf); [Tiao and Box, 1973](https://www.jstor.org/stable/2682897?seq=1)), namely the development of a prior that maximizes divergence between the prior and the posterior as data observations are made.  By maximizing divergence, the data are allowed to have the maximum effect on the posterior estimates.  

For the case of a proportion (probability), if the generation of responses is assumed to follow a binomial distribution with fixed (unknown) probability of response, the reference prior would correspond to a $p \sim \text{Beta}(\frac{1}{2}, \frac{1}{2})$ distribution.

This is the prior used for ${p}_{0}$ and ${p}_{1}$, subject to ${p}_{0} > {p}_{1}$; the $\text{Beta}(1/2, 1/2)$ probability density function assigns higher probabilities to values closer to 0 or 1.  To obtain a computationally tractable joint prior satisfying the constraint ${p}_{0} > {p}_{1}$, the joint prior for ${p}_{0}$ and ${p}_{1}$ was reformulated using a Dirichlet distribution induced by three latent Gamma random variables:

$${G}_{1} \sim \text{Gamma}({\alpha}_{1},1)$$
$${G}_{2} \sim \text{Gamma}({\alpha}_{2},1)$$
$${G}_{3} \sim \text{Gamma}({\alpha}_{3},1)$$

and

$$K = {G}_{1} + {G}_{2} + {G}_{3}$$

Then, ${p}_{0}$ and ${p}_{1}$ were defined as ${p}_{0} = {G}_{1}/K$ and ${p}_{1} = {G}_{1} + {G}_{2}/K$.  This approach ensures that ${p}_{0}$ and ${p}_{1}$ are naturally constrained such that ${p}_{0} > {p}_{1}$.  The resulting Beta marginal distributions maintain a weakly informative form consistent with the reference priors and are more stable under BMA by avoiding boundary constraints and improving the reliability of model-weight estimation.

By default, the LOUD hyperparameters used in BMDS are: 

$${G}_{1} \sim \text{Gamma}(0.5, 1)$$
$${G}_{2} \sim \text{Gamma}(0.6 ,1)$$
$${G}_{3} \sim \text{Gamma}(0.5 ,1)$$

which produces heavy tails near 0 and 1 and approximate the marginal $\text{Beta}(1/2, 1/2)$ form of the original reference prior.

### Mathematical Details for LOUD Bayesian Dichotomous Models

In BMDS, the set of Bayesian dichotomous models used in LOUD model averaging is identical to the set of models used for maximum-likelihood estimation (MLE) approaches ([**Dichotomous Response Models**](./dichotomous-mle.md#dichotomous-response-models)) and ToxicR model averaging ([**Individual Model Specifications (ToxicR)**](./dichotomous-bayesian.md#individual-model-specifications-toxicr)). 

```{figure} _static/img/LOUD_dichot_models.png
:alt: Window showing the dichotomous models available for LOUD Bayesian model averaging
:scale: 80%
:name: f106

Dichotomous models available for LOUD Bayesian model averaging
```

Note that the considerations regarding the [**Definition of the BMD**](./dichotomous-mle.md#bmr) (i.e., selection of the appropriate BMR level) are the same for the Bayesian and MLE implementations of the dichotomous models. The same two-dataset and two-option set limit applies to dichotomous data as for continuous data.

#### Individual Model Specifications (LOUD)

The dichotomous dose-response functions and their prior distributions are shown below.  One or two of each model's parameters can be expressed in terms of ${p}_{0}$ and ${p}_{1}$, which are the probabilities of a positive response at the minimum and maximum dose levels ${d}_{0}$ and ${d}_{1}$, and the priors for these parameters can then be derived using the distributions for ${p}_{0}$ and ${p}_{1}$ listed above.  For example, for the Weibull model:

$$p(x|\theta) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta \cdot {x}^{\alpha} \right\rbrack \right)$$

the background parameter ($g$) can be defined explicitly as ${p}_{0}$:

$$p({d}_{0}) = {p}_{0} = g + (1 - g) \cdot (1 - exp^{(-\beta \cdot {0}^{\alpha})}) = g$$

and the slope parameter ($\beta$) can be defined in terms of both ${p}_{0}$ and ${p}_{1}$: 

$$p({d}_{0}) = {p}_{1} = {p}_{0} + (1 - {p}_{0}) \cdot (1 - exp^{(-\beta \cdot {1}^{\alpha})})$$

$$\beta = -\ln \left\lbrack \frac{1 - {p}_{1}}{1 - {p}_{0}} \right\rbrack$$

The priors for the remaining parameters are listed below explicitly and were obtained from [Wheeler et al., 2022](https://hero.epa.gov/reference/10330529/). For example, the prior for the power parameter (e.g., $\alpha$ in the Weibull model) was chosen to take any positive value but places a low prior probability on values less than 1 that would lead to an infinite slope at the origin.  The parameterization of the dichotomous Hill model was adjusted due to redundancy:  both ${p}_{1}$ (probability of response at the maximum dose) and $v$ (maximum extra risk) implictily describe the maximum response, which can cause unstable sampling during model fitting.  Thus, the dichotomous Hill model is reparameterized such that ${p}_{1}$ was set equal to $v$.  For all models, parameters that identify curvature were assigned separate priors based on the priors in ToxicR (see [Individual Model Specifications (ToxicR)](./dichotomous-bayesian.md#individual-model-specifications-toxicr)) because ${p}_{0}$ and ${p}_{1}$ do not contain information to identify the shape of the curve.  

::::{tab-set}

:::{tab-item} Multistage

**Model Form**

$$p(x|\theta) = g + (1 - g)\left( 1 - \exp\left\lbrack - \sum_{i = 1}^{2}{\beta_{i}{x}^{i}} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\beta_{i}$ = dose coefficients

**Priors**

$g = {p}_{0}$

${\beta}_{i} = \Upsilon \cdot \left(-\ln\left\lbrack \frac{1-{p}_{1}}{1-{p}_{0}}\right\rbrack\right)$

$\Upsilon \sim \text{Dirichlet}(1,1)$

:::

:::{tab-item} Weibull

**Model Form**

$$p(x|\theta) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta \cdot {x}^{\alpha} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\ln(\alpha) \sim \text{Normal}(\ln(2),\sqrt(0.18))$

$\beta = - \ln \left\lbrack \frac{1-{p}_{1}}{{p}_{1} - {p}_{0}} \right\rbrack$

:::

:::{tab-item} Quantal Linear

**Model Form**

$$p(x|\theta) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta \cdot {x} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\beta =  \left(-\ln\left\lbrack \frac{1-{p}_{1}}{1-{p}_{0}}\right\rbrack\right)$

:::

:::{tab-item} Gamma
**Model Form**

$$p(x|\theta) = g + (1 - g) \cdot \text{pgamma}(\beta \cdot x, \alpha, 1)$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\alpha \sim \text{Normal}(\ln(2),\sqrt(0.18))$

$\text{pgamma}(\beta, \alpha, 1) = frac{{p}_{1}-{p}_{0}}{1-{p}_{0}}$

**Notes**

$\text{pgamma}(\beta,\alpha,1) = \frac{1}{\Gamma(\alpha)}\int_{0}^{\beta x}{t^{\alpha - 1}\exp( - t)dt\ }$
:::

:::{tab-item} Logistic
**Model Form**

$$p(x|\theta) = \frac{1}{1 + exp\lbrack - \alpha - \beta \cdot (x)\rbrack}$$

**Parameters**

$\alpha$ = intercept

$\beta$ = slope

**Priors**

$\alpha = \text{logit}({p}_{0})$

$\beta = \text{logit}({p}_{1}) - \text{logit}({p}_{0})$

:::

:::{tab-item} Log-Logistic
**Model Form**

$$p(x|\theta) = g + \frac{1 - g}{1 + exp\lbrack - \alpha - \beta \cdot log(x)\rbrack}$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\alpha = -\ln \left\lbrack \frac{1-{p}_{1}}{{p}_{1}-{p}_{0}}\right\rbrack$

$\ln(\beta) \sim \text{Normal}(\ln(2),0.5)$

:::

:::{tab-item} Probit
**Model Form**

$$p(x|\theta) = \ \Phi(\alpha + \ \beta \cdot x)$$

**Parameters**

$\alpha$ = intercept

$\beta$ = slope

**Priors**

$\alpha = {\Phi}^{-1}({p}_{0})$

$\beta = {\Phi}^{-1}({p}_{1}) - {\Phi}^{-1}({p}_{0})$

**Notes**

$\Phi(x) = \int_{- \infty}^{x}{\frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}}dt$

:::

:::{tab-item} Log-Probit
**Model Form**

$$p(x|\theta) = g + (1 - g)\Phi\left\lbrack \alpha + \beta \cdot \log(x) \right\rbrack$$

**Parameters**

$g$ = background

$\alpha$ = intercept

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\alpha = {\theta}^{-1} \left(\frac{{p}_{1}-{p}_{0}}{1-{p}_{0}}\right)$

$\beta \sim \text{Normal}(\ln(2),0.5)$

**Notes**

$\Phi(x) = \int_{- \infty}^{x}{\frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}}dt$

:::

:::{tab-item} Dichotomous Hill
**Model Form**

$$p(x|\theta) = g + \frac{(v - vg)}{1 + exp( - \alpha - \beta \cdot \log(x))}$$

**Parameters**

$g$ = background

$v$ = maximum extra risk

$\alpha$ = intercept

$\beta$ = slope

**Priors**

$g = {p}_{0}$

$\alpha \sim \text{Normal}(0,0.5)$

$\beta \sim \text{Lognormal}(\ln(2),0.5)$

$v = {p}_{1}$

**Notes**

For the dichotomous Hill model, ${p}_{0}$ and ${p}_{1}$ are assigned $\beta(0.05,0.05)$ priors.
:::

::::

#### Bayesian Parameter Estimation (LOUD)

The same Markov Chain Monte Carlo (MCMC) latent slice sampling used for continuous data (see [Bayesian Parameter Estimation (continuous)](./continuous-bayesian.md#bayesian-parameter-estimation)) is used to derive posterior distributions for the standard model parameters and BMDs for dichotomous data. The same statistics (potential scale reduction ($\hat{R}$) and effective sample size (ESS)) are used to judge convergence. The same MCMC sampling options also apply to dichotomous analyses.

### Bayesian Model Averaging (LOUD)

The BMD is estimated from a cross-model posterior distribution formed by combining posterior samples from each model, weighted by their prior weight (usually equally distributed across the model suite) and posterior model probability. 

For dichotomous data, there are a total of nine models that can be included in the model average (see [above](#individual-model-specifications-loud)).  

So, given there are K = 9 models are under consideration, for the ${k}^{th}$ model, ${M}_{k}$, let ${θ}_{k}$ denote its vector of model-specific parameters, and define the model-specific BMD as a function of these parameters, ${BMD}_{k}$. The model ${M}_{k}$ is associated with a likelihood function $\ell \left(Y|{M}_{k},{θ}_{k} \right)$, which describes the data-generating process. The cross-model/distribution posterior distribution for the BMD can be expressed as:

$$p \left(BMD|Y \right) = \sum_{k = 1}^{K}{{w}_{k}p \left( {BMD}_{k}|Y,{M}_{k} \right)}$$

where ${w}_{k}$ represents the normalized weight for model ${M}_{k}$.

The model weights used for generating the model-averaged posterior can be calculated using the WAIC or posterior model probabilities as for continuous data (see [Bayesian Model Averaging (continuous)](./continuous-bayesian.md#bayesian-model-averaging)).   

#### BMD and BMDL Estimation (LOUD)

Once the model-averaged posterior density of the BMD is estimated, the model-averaged BMD is simply the median of the posterior distribution and the 5$^{th}$ and 95$^{th}$ percentiles of the posterior distribution are used as the BMDL and BMDU, respectively.

#### Specific Dichotomous Bayesian Model Averaging Results

BMDS displays the results for dichotomous LOUD model averaging analyses identically as those for [**continuous data**](./continuous-bayesian.md#specific-continuous-bayesian-model-averaging-results). The same considerations of convergence and sampling efficiency pertain to dichotomous data as for continuous data.  

## ToxicR Model Averaging - Dichotomous Endpoints

The EPA, in conjunction with statisticians at the National Institute of Environmental Health Sciences (NIEHS), developed the ToxicR approach for dichotomous model averaging.  This approach uses maximum *a posteriori* approaches for model parameter estimation and a Laplacian approximation to estimate the posterior densities and posterior model weights of individual models.  

### Mathematical Details for ToxicR Bayesian Dichotomous Models

In BMDS, the set of Bayesian dichotomous models used in ToxicR model averaging is identical to the set of models used for MLE approaches ([**Dichotomous Response Models**](./dichotomous-mle.md#dichotomous-response-models)) and LOUD model averaging ([**Individual Model Specifications (LOUD)**](./dichotomous-bayesian.md#individual-model-specifications-loud)). The model forms and parameter priors for the BMDS dichotomous models are defined below.

#### Individual Model Specifications (ToxicR)

The priors for the parameters used in ToxicR model averaging are based on scaled doses and scaled responses; BMDS performs this scaling automatically by dividing by the maximum dose in the dataset under consideration, *i.e.*, that the doses under consideration range from 0 to 1 (inclusive). **BMDS automatically scales the responses** by dividing by the mean response in the control (or lowest dose) group. The user does ***not*** need to scale anything beforehand. That means that the parameter estimates and BMD values returned by the program have been adjusted back to the original scale of the doses and the original scale of the responses specified in the input data file.

::::{tab-set}

:::{tab-item} Multistage

**Model Form**

$$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \sum_{i = 1}^{n}{\beta_{i}dose^{i}} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\beta_{i}$ = dose coefficients

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$\beta_{i} > 0$

$N \geq 2$

**Priors**

$logit(g) \sim Normal(0,2)$

$\alpha \sim Normal(0,1)$

$\beta \sim Lognormal(\ln(2),0.5)$

**Notes**

The prior for $\beta_{1}$ reflects the belief that the linear term should be strictly prositive if the quadratic term is positive in the two-hit model of carcinogenesis.  The difference in priors between the Multistage and Quantal Linear models is by design.  The objective is to emphasize the higher-order terms in each model. The Multistage 1 model uses a prior favoring shallow dose-response relationships, while the Quantal Linear model uses a more diffuse prior.

For model averaging purposes, $N = 2$.

:::

:::{tab-item} Weibull

**Model Form**

$$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta{dose}^{\alpha} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$-40\  < \ \alpha\  \leq \ 40$

$0\  < \ \beta < \ 10,000$

**Priors**

$logit(g) \sim Normal(0,2)$

$\alpha \sim Lognormal(\sqrt(0.18),0,5)$

$\beta \sim Lognormal(0,1.5)$

:::

:::{tab-item} Quantal Linear

**Model Form**

$$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta{dose} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$0\  < \ \beta < \ 10,000$

**Priors**

$logit(g) \sim Normal(0,2)$

$\beta \sim Lognormal(0,1)$

**Notes**

The difference in priors between the Quantal Linear model and the Multistage 1 model is by design. The objective is to emphasize the higher-order terms in each model.  The Quantal Linear model is not the same as the Multistage 1 model. This is important for model averaging purposes. The Multistage 1 model uses a prior favoring shallow dose-response relationships, while the Quantal Linear model uses a more diffuse prior.

:::

:::{tab-item} Gamma
**Model Form**

$$p(dose) = g + \frac{1 - g}{\Gamma(\alpha)}\int_{0}^{\beta d}{t^{\alpha - 1}\exp( - t)dt\ }$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$0.2\  < \ \alpha\  \leq \ 20$

$0\  < \ \beta\  < 10,000$

**Priors**

$logit(g) \sim Normal(0,2)$

$\alpha \sim Lognormal(\ln(2)\sqrt(0.18))$

$\beta \sim Lognormal(0,1)$

**Notes**

The prior for $\alpha$ entails that there is only a 0.05 prior probability that the power parameter will be less than 1. This allows for models that are supralinear; however, it requires a large amount of data for the $\alpha$ parameter to go much below 1.

The $\alpha$ parameter is also constrained to be greater than 0.2 for numerical reasons.
:::

:::{tab-item} Logistic
**Model Form**

$$p(dose) = \frac{1}{1 + exp\lbrack - \alpha - \beta(dose)\rbrack}$$

**Parameters**

$\alpha$ = intercept

$\beta$ = slope

**Parameter Constraints**

$- 20 < \alpha < 20$

$0 < \ \beta\  < 40$

**Priors**

$\alpha \sim Normal(0,2)$

$\beta \sim Lognormal(0,2)$

:::

:::{tab-item} Log-Logistic
**Model Form**

$$p(dose) = g + \frac{1 - g}{1 + exp\lbrack - \alpha - \beta log(dose)\rbrack}$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$- 40\  < \ \alpha\  \leq \ 40$

$0\  < \ \beta < 20$

**Priors**

$logit(g) \sim Normal(0,2)$

$\alpha \sim Normal(0,1)$

$\beta \sim Lognormal(\ln(2),0.5)$

:::

:::{tab-item} Probit
**Model Form**

$$p(dose) = \ \Phi(\alpha + \ \beta dose)$$

where

$\Phi(x) = \int_{- \infty}^{x}{\phi(t)dt}$

and

$\phi(t) = \ \frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}$

**Parameters**

$\alpha$ = intercept

$\beta$ = slope

**Parameter Constraints**

$- 20 < \alpha < 20$

$0\  < \ \beta < 40$

**Priors**

$\alpha \sim Normal(0,2)$

$\beta \sim Lognormal(0,1)$

**Notes**

$\Phi$ is the standard Normal cumulative distribution function, $\phi$ is the standard Normal density function.
:::

:::{tab-item} Log-Probit
**Model Form**

$$p(dose) = g + (1 - g)\Phi\left\lbrack \alpha + \beta\log(dose) \right\rbrack$$

where

$\Phi(x) = \int_{- \infty}^{x}{\phi(t)dt}$

and

$\phi(t) = \ \frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}$

**Parameters**

$g$ = background

$\alpha$ = intercept

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$- 40\  \leq \alpha < 40$

$0\  < \ \beta\  \leq 20$

**Priors**

$logit(g) \sim Normal(0,2)$

$\alpha \sim Normal(0,1)$

$\beta \sim Lognormal(\ln(2),0.5)$

**Notes**

$\Phi$ is the standard Normal cumulative distribution function, $\phi$ is the standard Normal density function.
:::

:::{tab-item} Dichotomous Hill
**Model Form**

$$p(dose) = g + \frac{(v - vg)}{1 + exp( - \alpha - \beta\log(dose))}$$

**Parameters**

$g$ = background

$v$ = maximum extra risk

$\alpha$ = intercept

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$- 40\  < \ v\  \leq 40$

$- 40\  < \alpha\  \leq 40$

$0\  < \ \beta\  \leq 40$

**Priors**

$logit(g) \sim Normal(-1,2)$

$\alpha \sim Normal(-3,3.33)$

$\beta \sim Lognormal(\ln(2),0.5)$

$logit(v) \sim Normal(0,3)$
:::

::::

:::{important}
For all the models described above, $\text{logit}(g) = \ln\left( \frac{g}{1 - g} \right)$. $Normal(x, y)$ denotes a Normal distribution with mean $x$ and standard deviation $y$. $Lognormal(w, z)$ denotes a Lognormal distribution with log-scale mean $w$ and log-scale standard deviation $z$.  Further, the background parameter constraints above are on the logit scale, which is the form in which BMDS uses these constraints for calculation. The constraints are input into the software on the real number scale, with values of -18/18 for the MLE model and -20/20 for the Bayesian model minimum/maximum. The software then performs a logit transformation on these values. The background parameter values output by BMDS in the results will have a range of 0 to the maximum dose for each model.
:::

:::{note}
As the number of observations in a dataset increases, there should be less quantitative difference between the parameters and BMDs obtained from the Bayesian approach and from the MLE approach.

When there are fewer data points, the priors will affect the Bayesian estimation. The impact may be most noticeable when the data suggest a "hockey-stick" shaped dose-response relationship, or when those data suggest strong supralinear behavior. In these cases, the priors specified above for the Bayesian approach will tend to "shrink back" parameter estimates to obtain smoother dose-response relationships where changes in the slope are more gradual.
:::

#### Bayesian Model Averaging Methods (ToxicR)

From a Bayesian perspective, inference proceeds by defining a data-generating mechanism, given a model, $M$, and its parameters, $\theta$. For our purposes, $M$ would be one of the models listed above in [**Individual Model Specifications (ToxicR)**](./dichotomous-bayesian.md#individual-model-specifications-toxicr) that determines the probability of response. For the dichotomous models, the data-generating mechanism would be the assumption that the observations were obtained from binomial sampling, having the dose-dependent probability of response defined by one of those models (with specific values of the parameters in that model).

For each model, $M$, there is a likelihood for the data, $\mathcal{l}(D|M,\theta)$, based on the data-generating mechanism (binomial sampling in the case of the dichotomous endpoints).

Suppose for model averaging, $K$ models are considered, such that $M_{k}, k  = 1, \ldots, K$.

For each model, BMDS approximates the posterior density for the BMD using a Laplacian approximation; call that density $g_{k}\left( BMD \middle| M_{k},D \right)$ for model $k$. If the parameter vector for model $k$ is denoted $\theta_{k}$, let ${\widehat{\theta}}_{k}$
designate the value of that vector that maximizes the posterior likelihood (the maximum *a posteriori*, or MAP, estimate).

The posterior density of the model-averaged BMD is

$$g_{ma}\left( BMD|D \right) = \ \sum_{k = 1}^{K}{\pi_{k}\left( M_{k} \middle| D \right)g_{k}\left( BMD \middle| M_{k},D \right),}$$

where $\pi_{k}$ is the posterior probability of model $M_{k}$ given the data.

Clearly, this approach requires estimation of the posterior probabilities for each model considered. These are the weights for the averaging process. Unlike approaches that have been used elsewhere, we eschew the use of information-criteria-based weights (*e.g.*, those based on Bayesian information criteria (BIC) or Akaike information criteria(AIC)). Rather, BMDS generates weights using the Laplace approximation to the marginal density of the data. That is, for model $M_{k~}$, $1 ≤ k ≤ K$, with parameter vector $\theta_{k}$ of length s, one approximates the marginal density as

$$I_{k} = (2\pi)^{\frac{s}{2}}\left| {\widehat{\Sigma}}_{k} \right|^{\frac{1}{2}}\mathcal{l}\left( D \middle| {M_{k},\widehat{\theta}}_{k} \right)g\left( {\widehat{\theta}}_{k}|M_{k} \right)$$

where

${\widehat{\theta}}_{k}$ is the MAP estimate,

${\widehat{\Sigma}}_{k}$ is the negative inverse Hessian matrix evaluated at ${\widehat{\theta}}_{k}$,

$\mathcal{l}\left( D \middle| {M_{k},\ \widehat{\theta}}_{k} \right)\ $ is the likelihood of the data, for model $k$ evaluated at the MAP, and

$g\left( {\widehat{\theta}}_{k} \middle| M_{k} \right)$ is the value of the prior density for $M_{k}$ evaluated at the MAP parameter estimates.

To compute the posterior model probabilities for the $M_{k}$, one calculates the MAP and then calculates $I_{k}$ using the preceding equation. The posterior probability of the model is

$$\pi_{k}\left( M_{k} \middle| D \right) = \ \frac{w_{k}I_{k}}{\sum_{i = 1}^{K}{w_{k}I_{k}}},$$

where $w_{k}\ $is the prior probability of model $M_{k}$. In BMDS, the user can specify those weights; the default is equal weight for each model (all models being considered are equally probable *a priori*).

This approximation is similar to the Model Averaged Profile Likelihood (MAPL) approach of Fletcher and Turek ([2012](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4286986)). However, while MAPL relies only on the likelihood, our approach incorporates prior information in calculating the marginal profile density of the BMD. In other words, both the likelihood and prior are used. The model-specific density is defined by treating profile density bounds as quantiles of a marginal posterior density for the parameter of interest, and the relation to the present approach and the MAPL approach is justified asymptotically.

This approach can be related to the MAPL framework by substituting the posterior density for the likelihood in each of the steps. This method approximates the marginal likelihood using the posterior MAP estimate and Hessian of the log-posterior.

:::{note}
For the model average approach, the models listed in [**Individual Model Specifications (ToxicR)**](./dichotomous-bayesian.md#individual-model-specifications-toxicr) are available in the model average. For dichotomous model averaging, the Multistage model is capped to a maximum degree of 2. The reasoning for this follows upon the work of Nitcheva, et al. ([2007](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/729569)) who show that higher-order polynomials are not necessary given the fact that other models in the model averaging suite (*e.g.*, dichotomous Hill) can provide increased curvature.
:::

#### BMD and BMDL estimation (ToxicR)

The BMDS model-averaged BMD point estimate is the weighted average of BMD MAP estimates from individual models, weighted by posterior weights $\pi_{k}\left( M_{k} \middle| D \right).$ This estimate is equivalent to the median of the approximate posterior density of $\theta$. For the BMDL or BMDU estimates, the equation defining $g_{ma}$ is integrated. A $100(\alpha)%$ BMDU estimate or $100(1 - \alpha)%$ BMDL estimate is the value $BMD_{α}$ such that:

$$\alpha = \ \int_{- \infty}^{BMD_{\alpha}}{g_{ma}\left( BMD|D \right)\ dBMD,}$$

$$= \sum_{k = 1}^{K}{\pi_{k}\left( M_{k} \middle| D \right)\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}.}$$

The quantity $\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}$ is approximated by,

$$\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}$$

$$\approx {\frac{1}{2}\Pr}\left( \  - 2{\text{ log}\lbrack\widehat{g}}_{k}\left( \widehat{BMD} \middle| M_{k},D \right) \right\rbrack - 2{\ log\lbrack\widehat{g}}_{k}\left( BMD_{\alpha} \middle| M_{k},D \right)\rbrack < \ \chi_{1,\alpha\ }^{2}),$$

where ${\ \widehat{g}}_{k}\left( x \middle| M_{k},D \right)$ is the maximum value of the posterior evaluated at *x,* $\widehat{BMD}$ is the MAP estimate of the BMD and $\chi_{1,\alpha\ }^{2}$ is the *α* quantile of a Chi-square random variable with one degree of freedom. The above approximation assumes $BMD_{\alpha} < \widehat{BMD}$. When $\widehat{BMD} < BMD_{\alpha}$ the right-hand side of this equation is replaced by

$$\approx 1 - {\frac{1}{2}\Pr}\left( \  - 2{\ log\lbrack\widehat{g}}_{k}\left( \widehat{BMD} \middle| M_{k},D \right) \right\rbrack - 2{\ log\lbrack\widehat{g}}_{k}\left( BMD_{\gamma} \middle| M_{k},D \right)\rbrack < \ \chi_{1,\gamma\ }^{2}).$$

This approximation is like the profile-likelihood used when estimating the BMDL and BMDU using the MLE methods (see [Maximum Likelihood and Related Non-Bayesian Methods](./modeling-methods.md#maximum-likelihood-and-related-non-bayesian-methods)), but in this case ${\ \widehat{g}}_{k}\left( x \middle| M_{k},D \right)$ is the posterior density, which incorporates both the likelihood and the prior.

#### Results Specific to ToxicR Bayesian Model Averaing

To compare the difference between any two Bayesian models, the unnormalized Log Posterior Probability (LPP) is given, which allows the computation of a Bayes factor (BF) to compare any two models. BF equals the exponentiated difference between the two LPP. For example, if one wishes to compare the Log-Logistic model (Model A) (yielding $LPP_{A}$) to the Multistage 2{sup}`nd` degree model (Model B, $LPP_{B}$) one estimates the BF as

$$BF = \exp\left( LPP_{A} - LPP_{B} \right),$$

This computation assumes that both models have equal probability *a priori.* This value is then interpreted as the posterior odds one  model is more correct than the other model and is used in Bayesian hypothesis testing. In the example above, if the Bayes Factor was 2.5, the interpretation would be that the Log-logistic model is *a posteriori* 2.5 times more likely than the multistage model. When these values are normalized into proper probabilities, they are equivalent to the posterior model probabilities given in model averaging (again, assuming equal model probability *a priori*). The table below is adapted from Jeffreys ([1998](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4850043)) and is a common interpretation of Bayes Factors.

```{csv-table} Bayes factors for dichotomous models.
:header: >
: "Bayes Factor","Strength of Evidence for $H_{A}$"
:widths: 40, 60

< 1,negative (supports $H_B$)
1 to 3.2,not worth mentioning
3.2 to 10,substantial
10 to 31.6,strong
31.6 to 100,very strong
100,decisive
```
For BMDS, all LPP and corresponding posterior model probabilities are computed using the Laplace approximation. This value is different from the commonly used BIC, and the two should not be confused based upon other model averaging approaches, which use the BIC exclusively. Errors in the posterior probabilities estimated from the BIC are $O(1)$ estimators. Errors in the posterior probabilities estimated using the Laplace approximation are $O(n^{- 1})$. This means the latter approximation goes to the true posterior model probability with increasing data and the former, using the BIC, may not go to the true value.

```{figure} _static/img/ToxicR_bayesian_plot.png
:alt: Multiple model result curves plotted on single graph, with legend
:scale: 75%
:name: f107

Sample ToxicR Bayesian dichotomous results plot.
```
