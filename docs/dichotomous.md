# Dichotomous Endpoints

BMDS includes models for dichotomous endpoints in which the observations
are independent of each other. In these models, the dose-response model
defines the probability that an experimental unit (*e.g.*, a rat or a
mouse in a test of toxicity) will have an adverse response at a given
dose. The actual number of animals that have an adverse response is
assumed to be binomially distributed.

A specific example of such a dataset is a study in which adult animals
are exposed to different concentrations of a toxicant and then evaluated
for the presence of liver toxicity.

For models for dichotomous endpoints in which the responses are nested
(for example, pups within litters, and litters nested within doses), see
[Nested Dichotomous Endpoints](./nested-dichotomous.md).

For dichotomous cancer models, and the combination of model predictions
for multiple tumor endpoints, see [Multiple Tumor Analysis](./multiple-tumor-analysis.md).

For more information, refer to [Bayesian Dichotomous Analysis](./bayesian-dichotomous.md).

## Dichotomous Response Models

BMDS offers the traditional MLE dichotomous response models available in
previous versions of BMDS plus Bayesian versions of each model, and a
Bayesian model averaging feature.

[]{#_Toc47700647 .anchor}**Figure 76.** Default dichotomous model
selection.

![Dichotomous model table with default models
selected](_static/img/image81.png){width="6.5in"
height="2.839583333333333in"}

Most MLE models can be run restricted or unrestricted. The EPA default
recommendation for initial runs is to restrict the Dichotomous Hill,
Gamma, Log-Logistic, Multistage, and Weibull models and un-restrict the
Logistic, Log-Probit, Probit and Quantal Linear models. Note that the
Logistic, Probit, and Quantal Linear models have no restricted option
([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

See Table 8 on page [74](#tbl-model) for the effect of the user
selecting the restricted version of the models (refer to the paragraphs
in the *Notes* column marked with **User parameter restriction
options**). In general, the restrictions prevent the slope of the
dose-response curve from becoming infinite at 0 dose. This is often
considered to be biologically unrealistic and can lead to numerical
problems when computing confidence limits, so several authors have
recommended restricting the appropriate parameter.

A BMDS Online analysis can have a maximum of six datasets (for
continuous, dichotomous, and nested dichotomous) or 10 datasets (for
multitumor).

## Maximum Multistage Degree

The dataset-specific **Maximum multistage degree** picklist will contain
choices for degree 1 to the lesser of $n‑1$ or 4.

The default value for number degrees to run will be the lesser of $n‑1$ or
3, but the user can change this to a higher number of degrees up to the
lesser of $n‑1$ or 4. 

[]{#_Toc77956743 .anchor}**Figure 77.** Maximum Multistage Degrees for
dichotomous datasets.

![Maximum Multistage Degree picklist selections displayed, with degree 3
highlighted](_static/img/image82.png){width="4.925426509186352in"
height="1.7001476377952756in"}

Hovering over the help text icon for **Maximum multistage degree**
displays the following text:

:::{note}
Studies have indicated that higher degree polynomial models are not
warranted in that they generally do not sufficiently improve fit over
simpler models (Nitcheva et al., 2007; PMC2040324). Complex models also
increase computer processing time and the chance of model failure.
:::

## Option Sets

On the Settings tab, the user can define up to six Option Sets in BMDS
Online (unlimited in BMDS Desktop and pybmds) to apply to multiple
user-selected models and multiple user-selected datasets in a single
batch process.

Select the blue Plus button in the table header to define a new Option
Set configuration row; select the red Trash Can button to delete the
row.

[]{#_Toc47700648 .anchor}**Figure 78.** Dichotomous Model options.

![Dichotomous model options with Risk Type picklist values
displayed](_static/img/image83.png){width="5.03in" height="1.22in"}

### Risk Type

Choices for the Risk Type option are Extra Risk (Default) or Added Risk.

Added risk is the additional proportion of the total experimental units
that respond in the presence of the dose, or the predicted probability
of response at dose $d$, $P(d)$, minus the predicted probability of
response in the absence of exposure, $P(0)$:

$$Added\ risk\ at\ dose\ d\  = P(d)\ –\ P(0)$$

Extra risk is the additional risk divided by the predicted proportion of
animals that will not respond in the absence of exposure
($1\  - \ P(0))$:

$$Extra\ risk\ at\ dose\ d\  = \ \frac{P(d)\ –\ P(0)}{1 - P(0)}$$

### BMR

The BMR is the value of risk (extra or added, as specified by the user)
for which a BMD is estimated. BMR must be between 0 and 1 (not
inclusive).

If $P(0)\  > \ 0$, then values for BMR greater than $1 - \ P(0)$ will
result in an error when the risk type is added risk. That is because the
maximum added risk that can ever be achieved is $1 - \ P(0)$. In
practice, this should not typically be an issue because one usually is
interested in BMR values in the range of 0.01 to around 0.10.

### BMR and Plots

The response associated with the BMR that is displayed in the graphical
model output will only be the same as the BMR when $P(0)\  = \ 0$.

This is because to obtain the actual response value one must solve for
$P(d)$ in the equation for added or extra risk discussed above.

The horizontal bar depicting the response level used to derive the BMD
(*add figure cross-reference*) that is displayed in the graphical model output will only be the same
as the user-defined BMR (*e.g.*, 10% Extra Risk) when the response at
background, P(0), equals zero.

When P(0) does not equal zero, the true response level can be calculated
using the Extra Risk equation described in [Risk Type](#risk-type)

[]{#_Ref157091435 .anchor}**Figure 79**. Results plot, with horizontal
bar centered on the y-axis at the modeled BMR.

![Close-up of horizontal bar of results plot, centered on a BMR of
0.1](_static/img/image64.png){width="2.556971784776903in"
height="1.596398731408574in"}

### Confidence Level (one sided)

The Confidence Level is a fraction between 0 and 1; 0.95 is recommended
by EPA ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

The value for confidence level must be between 0 and 1 (not inclusive).
For a confidence level of $x$, BMDS will output BMDL and BMDU estimates,
each of which is a one-sided confidence bound at level $x$.

For example, if the user sets the confidence level to 0.95 (the
default), then the BMDL is a 95% one-sided lower confidence bound for
the BMD estimate; the BMDU is a 95% one-sided lower upper confidence
bound for the BMD estimate. In that example, the range from BMDL to BMDU
would constitute a 90% confidence interval (5% in each tail outside that
interval).

## Specific Dichotomous Results

### Goodness of Fit Table

[]{#_Toc185445256 .anchor}**Figure 80.** Goodness of Fit table for MLE
Dichotomous.

![Goodness of Fit
table](_static/img/image84.png){width="5.014235564304462in"
height="1.8556955380577427in"}

The Goodness of Fit table in the individual model results shows a
listing of the data (*N* and *Observed*) , the model-estimated
probability of response (*Estimated Probability*) and corresponding
expected number of responders (*Expected*). This is a good place for the
user to assess the appropriateness of the model, in addition to the
overall goodness-of-fit statistics reported in the Summary table (refer
[Summary Table of Key Fit Statistics (All Endpoints)](./result-output-mle.md#summary-table-of-key-fit-statistics-all-endpoints) and [Analysis of Deviance Table](#analysis-of-deviance-table). If a model fits well, the
observed and expected number of responders should be relatively close.

The scaled residual values printed at the end of the table are defined
as follows:

$$\frac{(Obs\  - \ Expected)}{SE}$$ 

where *Expected* is the predicted number of responders from the model
and SE equals the estimated standard error of that predicted number. For
these models, the estimated standard error is equal to
$\sqrt{\lbrack n \times p \times (1 - p)\rbrack}$, where

$n$ is the sample size ($N$ in the goodness-of-fit table), and

$p$ is the model-predicted probability of response (*Estimated
Probability* in the goodness-of-fit table).

The fit of the model to the data may be called into question if the
scaled residual value is greater than 2 or less than -2 for any dose
group, particularly the control group or the group with dose closest to
the BMD.

### Analysis of Deviance Table

[]{#_Toc185445257 .anchor}**Figure 81.** Analysis of Deviance table for
MLE Dichotomous.

![Analysis of Deviance
table](_static/img/image85.png){width="4.779691601049869in"
height="1.3379046369203849in"}

The analysis of deviance table displays three log-likelihood values.

::::{tab-set}

:::{tab-item} Full Model

The full model posits a separate and independent
    probability of response for each dose group. There is no
    dose-response function constraining those probabilities. The
    log-likelihood displayed is the maximum that could ever be achieved
    for the given dataset. The number of parameters for the full model
    is equal to the number of dose groups (each has its own, independent
    probability parameter).
:::

:::{tab-item} Fitted Model

The maximum log-likelihood value obtainable for
    the model under consideration. It corresponds to the model with the
    parameters set equal to the values shown in [Model Parameters
    table](#tbl-model). The number of
    parameters equals the number of parameters in that table that are
    not reported as *Bounded*.
:::

:::{tab-item} Reduced Model

The maximum log-likelihood obtainable if one
    assumed that the same probability of response applied to all the
    dose groups, *i.e.*, no difference in response over the dose levels.
    There is only 1 parameter for the reduced model, *i.e.*, the assumed
    constant probability of response.
:::

::::

Associated with each of these three models are three values: Deviance,
degrees of freedom (Test d.f.), and P-value.

::::{tab-set}

:::{tab-item} Deviance

The Deviance is twice the difference between the fitted or reduced
    model and the full model log-likelihood values. This Deviance is
    another goodness-of-fit metric: if the Deviance is small, then the
    smaller model (*i.e.*, the fitted or reduced model) describes the
    data nearly as well as the full model does.
:::

:::{tab-item} Degrees of Freedom (Test d.f.)

Deviance is approximately a Chi-square random variable with degrees
    of freedom specified by *Test d.f.*, which is the difference
    in the number of parameters for the two models being compared.
:::

:::{tab-item} P-value

The *P-Value* reflects the use of this Chi-square approximation to
    assess significance of the difference in fits. Larger deviances
    correspond to smaller p-values, so a small p-value indicates that
    the smaller model does not fit as well as the full model. The user
    may choose a rejection level (0.05 is common) to test if the model
    fit is appropriate.

***For the fitted model***, this is another measure of the fit of the
model to the data.

***For the reduced model***, failure to reject that model (p-values
greater than the rejection level chosen by the user) might lead the user
to infer that there is no dose-related effect on response probabilities.
:::

::::

### Plot and Error Bar Calculation

The graphical output, *i.e.*, plot, is a visual depiction of the results
of the modeling. Because plots, in general, were discussed in [Graphs/Plots (All Endpoints)](./result-output-mle.md#graphsplots-all-endpoints), here we
describe the one additional detail specific to the dichotomous models,
*i.e.*, computation of the error bars:

[]{#_Ref157091436 .anchor}**Figure 82.** Dichotomous endpoint plot with
error bars on the data points.

![Graph displaying error bars on the data
points](_static/img/image86.png){width="3.5378587051618546in"
height="3.398998250218723in"}

The error bars shown on the plots of dichotomous data () are derived
using a modification of the Wilson interval (based on the score
statistic) but with a continuity correction method ([Fleiss et al.,
2003](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4829616)).
The calculation finds the proportion, $p_{i}$, such that

$$\frac{\left| p - p_{i} \right| - \frac{1}{2n}}{\sqrt{\frac{p_{i} \times (1 - p_{i})}{n}}} = z$$

where

-   $p$ is the observed proportion

-   $n$ is the total number in the group in question, and

-   $z = Z_{1 - \frac{\alpha}{2}}$ is the inverse standard Normal
    cumulative distribution function evaluated at $1 - \frac{\alpha}{2}$

This leads to equations for the lower and upper bounds of:

$$LB = \frac{\left( 2np + z^{2} - 1 \right) - z\sqrt{z^{2} - (2 + \ \frac{1}{n})\  + \ 4p(nq + 1)}}{2(n + z^{2})}$$

and

$$UB = \frac{\left( 2np + z^{2} + 1 \right) + z\sqrt{z^{2} + (2 - \ \frac{1}{n})\  + \ 4p(nq - 1)}}{2(n + z^{2})}$$

where $q\  = \ 1 - p$.

The error bars shown in BMDS plots use alpha = 0.05 and so represent the
95% confidence intervals on the observed proportions (independent of
model).

## Mathematical Details for Models for Dichotomous Endpoints in Simple Designs

BMDS contains nine models for dichotomous endpoints as defined below.

### Individual Dichotomous Models and their Respective Parameters

::::{tab-set}

:::{tab-item} Multistage

**Model Form**

$$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \sum_{j = 1}^{n}{\beta_{j}dose^{j}} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\beta_{j}$ = dose coefficients

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$n\  \leq \ 23$

$0\  < \beta < \ 10,000$

**User Parameter Restriction Options**

Can restrict all $\beta$ coefficients to $leq$ 0. Doing so will guarantee that
the multistage model will be either perfectly flat or always increasing.

Per [EPA Technical Guidance
(2012)](https://www.epa.gov/risk/benchmark-dose-technical-guidance),
when the Multistage model is used for cancer analyses (e.g., in
Multitumor analyses) all $\beta$ coefficients are restricted to be
non-negative.
:::

:::{tab-item} Weibull (and Quantal Linear)

**Model Form**

$$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta{dose}^{\alpha} \right\rbrack \right)$$

**Parameters**

$g$ = background

$\alpha$ = power

$\beta$ = slope

**Parameter Constraints**

$0\  \leq \ g\  < \ 1$

$0\  < \ \alpha\  \leq \ 18$

$0\  < \ \beta < \ 100$

**User Parameter Restriction Options**

$1\  \leq \ \alpha$

**Notes**

The Quantal Linear model results from setting $\alpha$ = 1.
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

$0.2\  < \ \alpha\  \leq \ 18$

$0\  < \ \beta\  < 100$

**User Parameter Restriction Options**

$1\  \leq \ \alpha$

**Notes**

For the unrestricted Gamma model, $\alpha >$ 0.2 for numerical reasons.
:::

:::{tab-item} Logistic
**Model Form**

$$p(dose) = \frac{1}{1 + exp\lbrack - \alpha - \beta(dose)\rbrack}$$

**Parameters**

$\alpha$ = intercept

$\beta$ = slope

**Parameter Constraints**

$- 18 < \alpha < 18$

$0 < \ \beta\  < 100$

**User Parameter Restriction Options**

None.
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

$- 18\  < \ \alpha\  \leq \ 18$

$0\  < \ \beta < 18$

**User Parameter Restriction Options**

$1\  \leq \beta$
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

$- 18 < \alpha < 18$

$0\  < \ \beta < 18$

**User Parameter Restriction Options**

None.

**Notes**

$\Phi$ is the standard Normal cumulative distribution function, $\phi$
is the standard Normal density function.
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

$- 18\  \leq \alpha < 18$

$0\  < \ \beta\  \leq 18$

**User Parameter Restriction Options**

$1\  \leq \ \beta$

**Notes**

For the log-probit model, the slope of the model will always approach
zero as dose approaches zero regardless of the restriction on $\beta$.
However, for some relatively low doses (perhaps less than those
corresponding to the BMR), the slope can be quite steep depending on the
data and parameter estimates. In such cases, the BMDL estimate may be
relatively low or perhaps NA if the steepness of the slope causes
convergence problems as the BMDL estimate approaches zero.
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

$- 18\  < \ v\  \leq 18$

$- 18\  < \alpha\  \leq 18$

$0\  < \ \beta\  \leq 18$

**User Parameter Restriction Options**

$1\  \leq \ \beta$
:::

::::

:::{note}

The upper bound for the power parameter in some of the models,
and the slope parameter for some of the other models, has been set to
18. That value was selected because it represents a very high degree of
curvature that should accommodate almost every dataset, even ones with
very (or absolutely) flat dose-response at low doses followed by a very
steep dose-response at higher doses.

If such parameter values are reported to be equal to 18 and/or the
estimate in question is reported as *Bounded* (see the description of
the output from dichotomous model runs in [Analysis of
Deviance Table](#analysis-of-deviance-table)), the
parameter estimates are maximum likelihood estimates only in the
restricted sense that the parameter in question has been assigned a
value and the other parameters are MLEs conditional on that assigned
value. Such model results are not strictly comparable with others in
terms of AIC. In such a case, the BMD and BMDL could depend on the
choice of power parameter; thus, sensitivity analysis is recommended if
one intends to rely on the reported BMD or BMDL.
:::

:::{note}

The model descriptions above present the background parameter constraints on the logit
scale, which is the form in which BMDS uses these constraints for
calculation. The constraints are input into the software on the real
number scale, with values of -18/18 for the MLE model and -20/20 for the
Bayesian model minimum/maximum. The software then performs a logit
transformation on these values. The background parameter values output
by BMDS in the results will have a range of 0 to the maximum dose for
each model.
:::


### Likelihood Function

The non-Bayesian dichotomous models are fit using maximum likelihood
methods. This section describes the likelihood function used to fit the
dichotomous models.

Suppose the dataset has G dose groups with doses:

$$dose_{1},dose_{2},\ldots,dose_{G}$$

The total numbers of observations and numbers of responders in each dose
group are

$$N_{1},N_{2},\ldots,\ N_{G}$$

and, respectively,

$$Sn_{1},n_{2},\ldots,\ n_{G}$$

The distribution of $n_{i}$ is assumed to be binomial with probability

$$p_{i} = p\left( dose_{i};\ \theta \right),\ i = 1,2,\ldots G$$

where $\theta$ is a vector of dose-response model parameters (see [Individual Dichotomous Models and their Respective Parameters](#individual-dichotomous-models-and-their-respective-parameters)). Then the log-likelihood
function $LL$ can be written as

$$LL = \ \sum_{i = 1}^{G}{{LL}_{i}(N_{i},\ n_{i},\ dose_{i};\ \theta)}$$

where

$${LL}_{i}(N_{i},\ n_{i},\ dose_{i};\ \theta) = n_{i}\ln\left( p_{i} \right) + \left( N_{i} - n_{i} \right)\ln\left( 1 - p_{i} \right),\ i = 1,2,\ldots,G.$$

This expression ignores a constant term that is independent of the
parameter vector values and so does not affect estimation of those
parameters.

### AIC and Model Comparisons

The Akaike Information Criterion (AIC) ([Akaike,
1973](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=591))
can be used to compare different models fit (by the same fitting method,
*e.g.*, by maximizing the likelihood) to the same dataset. The AIC is a
statistic that depends on the value of LL (the log-likelihood function;
see the previous section) and the number of estimated parameters, p:

$$AIC\  = \  - 2 \times LL\  + \ 2 \times p$$

:::{note}
The AICs for the dichotomous endpoints ignore the
parameter-independent term, because LL as defined in the previous
section ignores that term. This differs from the case of the continuous
endpoints, where the parameter-independent term was not ignored, because
its value depended on the assumed underlying data distribution (Normal
or Lognormal). For dichotomous endpoints, there is only one assumed
distribution for the counts of responders (the Binomial distribution),
so the parameter-independent term has no effect and therefore can be
ignored.
:::

The AIC balances the goals of getting the highest LL value possible
while being parsimonious with respect to the number of parameters needed
to achieve a high LL value. Since the equation for AIC has a negative
multiplier for LL (which one wants to be greater) and positive
multiplier for p (which one wants to be as small as possible and still
get "good fit"), a model with a **smaller value of AIC** than other
models is presumed to be the better model on the basis of AIC. Although
such methods are not exact, they can provide useful guidance in model
selection.

In the current version of BMDS, the number of estimated parameters
includes only those that have not been estimated to equal a bounding
value, either from the model-imposed constraints or user-imposed
restrictions. For more details, see Table 8 on [74](#tbl-model).

:::{note}

The parameter counting process may or may not be reasonable, depending
on the boundary value that a parameter in question hits.

For example, if the power parameter in a model hits (*i.e.*, is
estimated to be equal to) the upper bound of 18, it would usually be the
case that one would want to count that parameter as one that is
estimated, but BMDS does ***not*** do that.

For this reason, the user is apprised to carefully consider the cases
where parameter bounds have been hit and to consider the implications
for issues such as model comparison and model selection.
:::

### BMD Computation

The BMD is computed as a function of the parameters of the model under
consideration (see [Individual Dichotomous Models and their Respective Parameters](#individual-dichotomous-models-and-their-respective-parameters)). Solutions
for the BMD for all the dichotomous models are shown below.

#### Calculation of the BMD for the Individual Dichotomous Models[^1]

::::{tab-set}

:::{tab-item} Multistage
There is no general analytical form for the BMD in terms of the BMR and the estimated model parameters for the multistage model.  Instead, the BMD is the root of the equation 

$\beta_{1}BMD+\ldots{+ \ \beta}_{n}BMD^{n} + \ln(1-A) = 0$

where

$A = \left\{\begin{array}{r}BMR\ extra \ risk \\ \\ \frac{BMR}{1-g}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Weibull
$BMD = \left\{\begin{array}{r}\left\lbrack \frac{- ln(1-BMR)}{\beta} \right\rbrack^{\frac{1}{\alpha}}\ extra\ risk \\ \\ \left\lbrack \frac{- ln(1 - \frac{BMR}{1-g})}{\beta} \right\rbrack^{\frac{1}{\alpha}}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Gamma
Let 

$G(x;\alpha) = \frac{1}{\Gamma(\alpha)}\int_{0}^{x}{t^{\alpha -1}e^{-t}dt}$

be the incomplete Gamma function and 

$G^{-1}( \bullet ;\ \alpha)$

be its inverse function.  Then

$BMD = \left\{\begin{array}{r}\frac{G^{-1}(BMR;\alpha)}{\beta}\ extra\ risk \\ \frac{G^{-1}(\frac{BMR}{1-g};\alpha)}{\beta}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Logistic
$BMD = \frac{ ln(\frac{1-Z}{1 + Z \times e^{-\alpha}})}{\beta}$

where

$Z = \left\{ \begin{array}{r}BMR\ extra\ risk \\ \\ BMR \times \frac{1 + e^{- \alpha}}{e^{- \alpha}}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Log-logistic
$\ln(BMD) = \left\{ \begin{array}{r}\frac{\ln\left( \frac{BMR}{1-BMR} \right) - \alpha}{\beta}\ extra\ risk \\ \\ \frac{\ln\left( \frac{BMR}{1 - g - BMR} \right) - \alpha}{\beta}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Probit
$BMD = \left\{ \begin{array}{r}\frac{\Phi^{-1}\left( BMR\left\lbrack 1-\Phi(\alpha) \right\rbrack + \Phi(\alpha) \right) - \alpha}{\beta}\ extra\ risk \\ \\ \frac{\Phi^{- 1}\left( BMR  + \Phi(\alpha) \right) - \alpha}{\beta}\ added\ risk \end{array} \right.\\$
:::

:::{tab-item} Log-Probit
$ln(BMD) = \left\{ \begin{array}{r}\frac{\Phi^{- 1}(BMR) - \alpha}{\beta}\ extra\ risk \\ \\  \frac{\Phi^{- 1}\frac{BMR}{1 - g} - \alpha}{\beta}\ added\ risk\end{array} \right.\\$
:::

:::{tab-item} Dichotomous Hill
$BMD = \left\{ \begin{array}{r} e\frac{- \alpha - \log\left( - \frac{BMR - v + gv}{BMR} \right)}{\beta}\ extra\ risk \\ \\ e\frac{- \alpha - \log\left( - \frac{BMR - v + gv- BMRgv}{BMR( - 1 + gv)} \right)}{\beta}\ added\ risk\end{array} \right.\\$
:::

::::

[^1]: All models represented in [Calculation of the BMD for the Individual Dichotomous Models](#calculation-of-the-bmd-for-the-individual-dichotomous-models1) use the same model forms as
    presented in [Individual Dichotomous Models and their Respective Parameters](#individual-dichotomous-models-and-their-respective-parameters). The BMR is the value specified by the user to
    correspond to the risk level of interest (see [BMR](#bmr)).

### BMDL and BMDU Computation

BMDS currently calculates one-sided confidence intervals, in accordance
with current BMD practice. The general approach to computing the
confidence limits for the BMD (called the BMDL and BMDU here) is the
same for all the models in BMDS, and is based on the asymptotic
distribution of the likelihood ratio ([Crump and Howe,
1985](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/3198)).
Two different specific approaches are followed in these models.

For the Multistage model, it is impractical to explicitly reparameterize
the dose-response model function to allow BMD to appear as an explicit
parameter. For these models, the BMR equation is used as a non-linear
constraint, and the minimum value of BMD is determined such that the
resulting log-likelihood is less than that at the maximum likelihood
estimates by exactly

$$\frac{\chi_{1,1 - 2\alpha}^{2}}{2}$$

For the remaining models, the equations that define the benchmark
response in terms of the benchmark dose and the dose-response model
([Calculation of the BMD for the Individual Dichotomous Models](#calculation-of-the-bmd-for-the-individual-dichotomous-models1)) are solved for one of the model parameters. The resulting
expression is substituted back into the model equations, with the effect
of reparameterizing the model so that BMD appears explicitly as a
parameter. A value for BMD is then found such that, when the remaining
parameters are varied to maximize the likelihood, the resulting
log-likelihood is less than that at the maximum likelihood estimates by
exactly

> $$\frac{\chi_{1,1 - 2\alpha}^{2}}{2}$$

In all cases, the additional constraints specify that the BMDL be less
than the BMD and the BMDU be greater than the BMD.

