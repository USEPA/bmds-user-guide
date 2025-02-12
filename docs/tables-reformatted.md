# Model Descriptions

## Continuous Model Descriptions

### Linear and Polynomial Models

#### Model Form

The Linear model is a form of the polynomial model.

$$m(dose) = g\  + \ \beta_{1} \times dose + \beta_{2} \times dose^{2} + \ldots + \beta_{n} \times dose^{n}$$

$n\ $is the degree of the polynomial, specified by user and must be a
positive integer (maximum value = 8)

#### Parameters

$g$ = control response (intercept)

$\beta_{0}\ldots\beta_{n}$: polynomial coefficients

#### Parameter Constraints

None.

#### User Parameter Restriction Options

**Restrict the value of the polynomial coefficients.** Restricting them
to be either non-positive or non-negative guarantees that the resulting
function will be strictly decreasing, strictly increasing, or perfectly
flat (when all the coefficients are zero). If the coefficients are
unrestricted (*i.e.*, an unrestricted form of the model is run), then
more complicated shapes are possible, and, particularly as the degree of
the polynomial approaches the number of dose groups minus one, the
polynomial will often be quite wavy.

### Linear

#### Model Form

The Linear model is a form of the polynomial model.

$$m(dose) = g\  + \ \beta\  \times dose$$

#### Parameters

$g$ = control response (intercept)

$\beta$ = slope

#### Parameter Constraints

None.

#### User Parameter Restriction Options

None.

### Power

#### Model Form

$$m(dose) = g + v \times (dose)^{n}$$

#### Parameters

$g$ = control response (intercept)

$v$ = slope

$n$= power

#### Parameter Constraints

0 [\<]{.underline} $n$ [\<]{.underline} 18

#### User Parameter Restriction Options

$n$ may be further restricted to values [\>]{.underline} 1.

#### Notes

If $n$ \< 1, then the slope of the dose-response curve becomes infinite
at the control dose. This is biologically unrealistic and can lead to
numerical problems when computing confidence limits, so several authors
have recommended restricting $n$ ≥ 1.

Note that the upper bounds for the power parameters in the Power, Hill,
and Exponential models have been set to 18. That value was selected
because it represents a very high degree of curvature that should
accommodate almost every dataset, even ones with very (or absolutely)
flat dose-response at low doses followed by a very steep dose-response
at higher doses.

### Hill

#### Model Form

$m(dose) = g + \frac{v \times {dose}^{n}}{k^{n} + {dose}^{n}}$

#### Parameters

$g$ = control response (intercept)

$k$ = dose with half-maximal change (normalized)

$n$= power

$v$= maximum change

#### Parameter Constraints

0 [\<]{.underline} $k$ [\<]{.underline} 5

0 [\<]{.underline} $n$ [\<]{.underline} 18

#### User Parameter Restriction Options

$n$ may be further restricted to values \> 1.

#### Notes

BMDL estimates from models that have an asymptote parameter (including
the Hill model) can be unstable when a wide range of parameter values
can give nearly identical likelihoods. One indicator of that problem is
that the estimated asymptotic response is far outside the range of the
observed responses. The user should consult a statistician if this
behavior is seen or suspected.

Note that the upper bounds for the power parameters in the Power, Hill,
and Exponential models have been set to 18. That value was selected
because it represents a very high degree of curvature that should
accommodate almost every dataset, even ones with very (or absolutely)
flat dose-response at low doses followed by a very steep dose-response
at higher doses.

### Exponential

#### Model Form

Dr. Wout Slob of RIVM in The Netherlands has proposed a set of nested
models known as the exponential models. Currently, these models should
be fit only to data having positive (mean) values.

There are four exponential models fit by BMDS and they are defined and
labeled as follows:

$$Exp2:\ m(dose) = a \times e^{\pm b \times dose}$$

$$Exp3:\ m(dose) = a \times e^{\pm (b \times dose)^{d}}$$

$$Exp4:\ m(dose) = a \times (c - (c - 1) \times e^{- b \times dose})$$

$$Exp5:\ m(dose) = a \times (c - (c - 1) \times e^{- (b \times dose)^{d}})$$

#### Parameters

$a$ = control response (intercept)

$b$ = slope

$c$= asymptote term

$d$= power

#### Parameter Constraints

$a$ \> 0

0 \< $b$ \< 100

$c$ \> 1 for responses increasing with dose

0 \< $c$ \< 1 for responses decreasing with dose

1 \< $d$ \< 18

#### Notes

The sign in "$\pm b"$ (Exp2 and Exp3 models) will change depending on
the user-designated or auto-detected direction of change:

-   \+ for responses increasing with dose

-   \- for responses decreasing with dose

BMDL estimates from models that have an asymptote parameter (including
the Hill model) can be unstable when a wide range of parameter values
can give nearly identical likelihoods. One indicator of that problem is
that the estimated asymptotic response is far outside the range of the
observed responses. The user should consult a statistician if this
behavior is seen or suspected.

Note that the upper bounds for the power parameters in the Power, Hill,
and Exponential models have been set to 18. That value was selected
because it represents a very high degree of curvature that should
accommodate almost every dataset, even ones with very (or absolutely)
flat dose-response at low doses followed by a very steep dose-response
at higher doses.

#### Reference

RIVM (National Institute for Public Health and the Environment
(Netherlands)). ([RIVM,
2018](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4850042)).
PROAST.

## Dichotomous Model Descriptions

### Notes on the Dichotomous MLE Models

Note that the upper bound for the power parameter in some of the
dichotomous models presented here, and the slope parameter for some of
the other models, has been set to 18. That value was selected because it
represents a very high degree of curvature that should accommodate
almost every dataset, even ones with very (or absolutely) flat
dose-response at low doses followed by a very steep dose-response at
higher doses.

If such parameter values are reported to be equal to 18 and/or the
estimate in question is reported as Bounded (see the description of the
output from dichotomous model runs in Section 9.4.2, "Analysis of
Deviance Table," on page 78), the parameter estimates are maximum
likelihood estimates only in the restricted sense that the parameter in
question has been assigned a value and the other parameters are MLEs
conditional on that assigned value. Such model results are not strictly
comparable with others in terms of AIC. In such a case, the BMD and BMDL
could depend on the choice of power parameter; thus, sensitivity
analysis is recommended if one intends to rely on the reported BMD or
BMDL.

***Note:*** The following dichotomous model descriptions present the
background parameter constraints on the logit scale, which is the form
in which BMDS uses these constraints for calculation. The constraints
are input into the software on the real number scale, with values of
-18/18 for the maximum-likelihood estimation (MLE) model and -20/20 for
the Bayesian model minimum/maximum. The software then performs a logit
transformation on these values. The background parameter values output
by BMDS in the results will have a range of 0 to the maximum dose for
each model.

### Multistage

#### Model Form

$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \sum_{j = 1}^{n}{\beta_{j}dose^{j}} \right\rbrack \right)$

#### Parameters

$g$ = background

$\beta_{j}$ = dose coefficients

#### Parameter Constraints

$$0\  \leq \ g\  < \ 1$$

$$n\  \leq \ 23$$

$0\  < \ \beta < \ $`<!-- -->`{=html}10,000

#### User Parameter Restriction Options

Can restrict all β coefficients to \> 0. Doing so will guarantee that
the multistage model will be either perfectly flat or always increasing.

Per [EPA Technical Guidance
(2012)](https://www.epa.gov/risk/benchmark-dose-technical-guidance),
when the Multistage model is used for cancer analyses (e.g., in
Multitumor analyses) all β coefficients are restricted to be
non-negative.

### Weibull (and Quantal Linear)

#### Model Form

$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta{dose}^{\alpha} \right\rbrack \right)$

#### Parameters

$g$ = background

$\alpha$ = power

$\beta$ = slope

#### Parameter Constraints

$$0\  \leq \ g\  < \ 1$$

$$0\  < \ \alpha\  \leq \ 18$$

$0\  < \ \beta < \ $`<!-- -->`{=html}100

#### User Parameter Restriction Options

$1\  \leq \ \alpha$

#### Notes

The Quantal Linear model results from setting $\alpha$ = 1.

### Gamma

#### Model Form

$p(dose) = g + \frac{1 - g}{\Gamma(\alpha)}\int_{0}^{\beta d}{t^{\alpha - 1}\exp( - t)dt\ }$

#### Parameters

$g$ = background

$\alpha$ = power

$\beta$ = slope

#### Parameter Constraints

$$0\  \leq \ g\  < \ 1$$

$$0.2\  < \ \alpha\  \leq \ 18$$

$$0\  < \ \beta\  < 100$$

#### User Parameter Restriction Options

$1\  \leq \ \alpha$

#### Notes

For the unrestricted Gamma model, α \> 0.2 for numerical reasons.

### Logistic

#### Model Form

$p(dose) = \frac{1}{1 + exp\lbrack - \alpha - \beta(dose)\rbrack}$

#### Parameters

$\alpha$ = intercept

$\beta$ = slope

#### Parameter Constraints

$$- 18 < \alpha < 18$$

$$0 < \ \beta\  < 100$$

#### User Parameter Restriction Options

None.

### Log-Logistic

#### Model Form

$p(dose) = g + \frac{1 - g}{1 + exp\lbrack - \alpha - \beta log(dose)\rbrack}$

#### Parameters

$g$ = background

$\alpha$ = power

$\beta$ = slope

#### Parameter Constraints

$${0\  \leq \ g\  < \ 1
}{- 18\  < \ \alpha\  \leq \ 18
}$$$0\  < \ \beta < 18$

#### User Parameter Restriction Options

$1\  \leq \beta$

### Probit

#### Model Form

$p(dose) = \ \Phi(\alpha + \ \beta dose)$, where

$\Phi(x) = \int_{- \infty}^{x}{\phi(t)dt}$ and
$\phi(t) = \ \frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}$

#### Parameters

$\alpha$ = intercept

$\beta$ = slope

#### Parameter Constraints

$$- 18 < \alpha < 18$$

$$0\  < \ \beta < 18$$

#### User Parameter Restriction Options

None.

#### Notes

$\Phi$ is the standard Normal cumulative distribution function, $\phi$
is the standard Normal density function.

### Log-Probit

#### Model Form

$$p(dose) = g + (1 - g)\Phi\left\lbrack \alpha + \beta\log(dose) \right\rbrack$$

$\Phi(x) = \int_{- \infty}^{x}{\phi(t)dt}$ and
$\phi(t) = \ \frac{1}{\sqrt{2\pi}}e^{\frac{- t^{2}}{2}}$

#### Parameters

$g$ = background

$\alpha$ = intercept

$\beta$ = slope

#### Parameter Constraints

$$0\  \leq \ g\  < \ 1$$

$$- 18\  \leq \alpha < 18$$

$$0\  < \ \beta\  \leq 18$$

#### User Parameter Restriction Options

$1\  \leq \ \beta$

#### Notes

For the log-probit model, the slope of the model will always approach
zero as dose approaches zero regardless of the restriction on β.
However, for some relatively low doses (perhaps less than those
corresponding to the BMR), the slope can be quite steep depending on the
data and parameter estimates. In such cases, the BMDL estimate may be
relatively low or perhaps NA if the steepness of the slope causes
convergence problems as the BMDL estimate approaches zero.

### Dichotomous Hill

#### Model Form

$$p(dose) = g + \frac{(v - vg)}{1 + exp( - \alpha - \beta\log(dose))}$$

#### Parameters

$g$ = background

$v$ = maximum extra risk

$\alpha$ = intercept

$\beta$ = slope

#### Parameter Constraints

$$0\  \leq \ g\  < \ 1$$

$$- 18\  < \ v\  \leq 18$$

$$- 18\  < \alpha\  \leq 18$$

$$0\  < \ \beta\  \leq 18$$

#### User Parameter Restriction Options

$1\  \leq \ \beta$

## Nested Dichotomous Models

### Logistic Nested

#### Model Form

if $dose > 0$

$$p(dose) = {a + \theta}_{1}r_{ij} + \frac{(1 - \alpha - \theta_{1}r_{ij})}{(1 + e^{\left\lbrack - \beta - \theta_{2}r_{ij} - \rho \times \ln(dose) \right\rbrack})}$$

if $dose = 0$

$$p(dose) = \alpha + \theta_{1}r_{ij}$$

#### Parameters

#### Parameter Constraints

$\alpha$ = intercept (≥0)

$\rho$ = power (≥0, can restrict ≥1)

$\beta$ = slope (≥0)

$\theta_{1}$ = first coefficient for the litter-specific covariate

$\theta_{2}$ = second coefficient for the litter-specific covariate

$\phi_{1},\ \ldots,\ \phi_{g}$ = intra-litter correlation coefficients

#### Notes

In the model equation, $r_{ij}$ is the litter-specific covariate for the
*j^th^* litter in the *i^th^* dose group. In addition, there are *g*
intra-litter correlation coefficients; *g* is the number of dose groups.
${0 \leq \phi}_{i} \leq 1\ (i = 1,\ \ldots,\ g).$

$1 > \alpha + \rho \geq \theta_{1}r_{ij} \geq 0$ for every $r_{ij}$.

If $r_{m}$ represents either the control mean value for the
litter-specific covariate or its overall mean, then the BMD is computed
as:

$$BMD = e^{\left\{ \frac{\left\lbrack \ln\left( \frac{A}{(1 - A)} \right) - \beta - \theta_{2}r_{m} \right\rbrack}{\rho} \right\}}$$

where

$$A = \left\{ \begin{array}{r}
\ BMRF\ extra\ risk \\
 \\
\frac{BMRF}{(1 - a - \theta_{1}r_{m})}\ added\ risk
\end{array} \right.\ $$

For the BMDL, the parameter $\beta$ is replaced with an expression
derived from the BMD definition and the BMDL is derived as described in
Section 10.5.2., "Goodness of Fit Information---Litter Data."

### NCTR (National Center for Toxicological Research)

#### Model Form

$$p(dose) = 1 - e^{\left\{ - (\alpha + \theta_{1}\left( r_{ij} - r_{m} \right)) - (\beta + \theta_{2}\left( r_{ij} - r_{m} \right)) \times dose^{\rho} \right\}}\ $$

#### Parameters

$\alpha$ = intercept (≥0)

$\rho$ = power (≥0, can restrict ≥1)

$\beta$ = slope (≥0)

$\theta_{1}$ = first coefficient for the litter-specific covariate

$\theta_{2}$ = second coefficient for the litter-specific covariate

$\phi_{1},\ \ldots,\ \phi_{g}$ = intra-litter correlation coefficients

#### Notes

In the model equation, $r_{ij}$ is the litter-specific covariate for the
jth litter in the ith dose group, $r_{m}$ is the overall mean for the
litter-specific covariate

$\theta_{1}(r_{ij} - r_{m}) \geq 0$ and
$\theta_{2}(r_{ij} - r_{m}) \geq 0$

In addition, there are g intra-litter correlation coefficients; g is the
number of dose groups.
${0 \leq \phi}_{i} \leq 1\ (i = 1,\ \ldots,\ g);\ 1 > \alpha + \rho \geq \theta_{1}r_{ij} \geq 0$
for every $r_{ij}$.

$$BMD = \left\lbrack \frac{- (\ln(1 - A))}{(\beta + \theta_{2}\delta_{r})} \right\rbrack \times \left( \frac{1}{\rho} \right)$$

where

$$A = \left\{ \begin{array}{r}
BMRF\ extra\ risk \\
 \\
\frac{BMRF}{(1 - a - \theta_{1}\delta_{r})}\ added\ risk
\end{array} \right.\ $$

and $\delta_{r}$is the average of $r_{ij} - r_{m}$ over either the
control group or over all observations (depending on user selection).

For the BMDL, the parameter $\beta$ is replaced with an expression
derived from the BMD definition and the BMDL is derived as described in
Section 10.5.2., "Goodness of Fit Information---Litter Data.".

## Bayesian Dichotomous Models

### About the Priors

All the Bayesian model descriptions in this section contain the
following as a prior:

$$logit(g)\sim\ Normal(0,\ 2)$$

For this prior, $\text{logit}(g) = \ln\left( \frac{g}{1 - g} \right)$.
Normal(x, y) denotes a Normal distribution with mean x and standard
deviation y. Priors with Lognormal(w, z) denote a Lognormal distribution
with log-scale mean w and log-scale standard deviation z.

### Notes on the Bayesian Dichotomous Models

As the number of observations in a dataset increases, there should be
less quantitative difference between the parameters and BMDs obtained
from the Bayesian approach and from the maximum-likelihood estimation
(MLE) approach.

When there are fewer data points, the priors will affect the Bayesian
estimation. The impact may be most noticeable when the data suggest a
"hockey-stick" shaped dose-response relationship, or when those data
suggest strong supralinear behavior. In these cases, the priors
specified for the Bayesian approach will tend to "shrink back" parameter
estimates to obtain smoother dose-response relationships where changes
in the slope are more gradual.

***Note*** The following sections present the background parameter
constraints on the logit scale, which is the form in which BMDS uses
these constraints for calculation. The constraints are input into the
software on the real number scale, with values of -18/18 for the MLE
model and -20/20 for the Bayesian model minimum/maximum. The software
then performs a logit transformation on these values. The background
parameter values output by BMDS in the results will have a range of 0 to
the maximum dose for each model.

### Multistage

#### Model Form

$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \sum_{i = 1}^{N}{\beta_{i}{dose}^{i}} \right\rbrack \right)$

#### Constraints

$$0 \leq g < 1$$

$$\beta_{i} > 0$$

$$N\  \geq 2$$

#### Priors

$$logit(g)\sim\ Normal(0,\ 2)$$

$$\beta_{i}\sim\ Lognormal(0,1),\ i \geq 2)$$

#### Notes

The prior over the β~1~ parameter reflects the belief that the linear
term should be strictly positive if the quadratic term is positive in
the two-hit model of carcinogenesis.

The difference in priors between Multistage and Quantal Linear models is
by design. The objective is to emphasize the higher-order terms in each
model. Multistage 1 uses a prior favoring shallow dose-response
relationships, while Quantal Linear uses a more diffuse prior.

For model averaging purposes, N = 2.

### Weibull

#### Model Form

$p(dose) = g + (1 - g)\left( 1 - \exp\left\lbrack - \beta{dose}^{\alpha} \right\rbrack \right)$

#### Constraints

$$0 \leq g < 1$$

$$0 < \alpha < 40$$

$$0 < \beta < 10,000$$

#### Priors

$$logit(g)\sim\ Normal(0,\ 2)$$

$\alpha\sim\ Lognormal(\sqrt{0.18},\ 0.5$)

$$\beta\sim\ Lognormal(0,\ 1.5)$$

### Quantal Linear

#### Model Form

$p(dose) = g + (1 - g)\left( 1 - \exp\lbrack - \beta dose\rbrack \right)$

#### Constraints

$$0 \leq g < 1$$

$$0 < \ \beta < 18$$

#### Priors

$$logit(g)\sim\ Normal(0,\ 2)$$

$$\beta\sim\ Lognormal(0,\ 1)$$

#### Notes

The difference in priors between Quantal Linear and the following
Multistage model is by design. The objective is to emphasize the
higher-order terms in each model.

Quantal Linear is not the same as Multistage-1. This is important for
model averaging purposes. Multistage 1 uses a prior favoring shallow
dose-response relationships, while Quantal Linear uses a more diffuse
prior.

### Gamma

#### Model Form

$p(dose) = g + \frac{1 - g}{\Gamma(\alpha)}\int_{0}^{\beta dose}{t^{\alpha - 1}\exp( - t)dt\ }$

#### Constraints

$$0 \leq g < 1$$

$$0.2 < \alpha < 20$$

$$0 < \ \beta < 10,000$$

#### Priors

$$logit(g)\sim\ Normal(0,2)$$

$$\alpha\sim\ Lognormal(\ln(2),\ \sqrt{0.18})$$

$$\beta\sim\ Lognormal(0,\ 1)$$

#### Notes

The prior for α entails that there is only a 0.05 prior probability the
power parameter will be less than 1. This allows for models that are
supra linear; however, it requires a large amount of data for the α
parameter to go much below 1.

The α parameter is also constrained to be greater than 0.2, for
numerical reasons.

### Logistic

#### Model Form

$p(dose) = \frac{1}{1 + exp\lbrack - \alpha\  - \beta dose\rbrack}$

#### Constraints

$$- 20 < \alpha < 20$$

$$0 < \ \beta\  < 40$$

#### Priors

$$\alpha\ \sim\ Normal(0,\ 2)$$

$$\beta\sim\ Lognormal(0,2)$$

### Log-Logistic

#### Model Form

$p(dose) = g + \frac{1 - g}{1 + exp\lbrack - \alpha\  - \beta ln(dose)\rbrack}$

#### Constraints

$$0 \leq g < 1$$

$$- 40 < \alpha < 40$$

$$0 < \ \beta < 20$$

#### Priors

$$logit(g)\sim\ Normal(0,\ 2)$$

$$\alpha\ \sim\ Normal(0,\ 1)$$

$$\beta\sim\ Lognormal({ln}(2),\ 0.5)$$

### Probit

#### Model Form

$p(dose) = \ \Phi(\alpha + \ \beta dose)$

#### Constraints

$$- 20 < \alpha < 20$$

$$0 < \ \beta < 40$$

#### Priors

$$\alpha\ \sim\ Normal(0,\ 2)$$

$$\beta\sim\ Lognormal(0,\ 1)$$

#### Notes

$\Phi( \bullet )$ is the standard Normal cumulative density function.

### Log-Probit

#### Model Form

$p(dose) = g + (1 - g)\Phi\lbrack\alpha + \beta\ln(dose)\rbrack$

#### Constraints

$$0 \leq g < 1$$

$$- 40 < \alpha < 40$$

$$0 < \ \beta < 20$$

#### Priors

$$logit(g)\sim\ Normal(0,\ 2)$$

$$\alpha\ \sim\ Normal(0,\ 1)$$

$$\beta\sim\ Lognormal(\ln(2),\ 0.5)$$

#### Notes

$\Phi( \bullet )$ is the standard Normal cumulative density function

### Dichotomous Hill

#### Model Form

$p(dose) = g + \ \frac{\nu - v \times g}{1 + exp\lbrack - a - b\ln(dose)\rbrack}$

#### Constraints

$$0 \leq g < 1$$

$$- 40 < v \leq 40$$

$$- 40 < a < 40$$

$$0 < \ b < 40$$

#### Priors

$$logit(g)\sim\ Normal( - 1,\ 2)$$

$$a\ \sim\ Normal( - 3,\ 3.3)$$

$$b\ \sim\ Lognormal(\ln(2),\ 0.5)$$

$$logit(v)\sim\ Normal(0,\ 3)$$
