# Bayesian Dichotomous Analysis, including Model Averaging

BMDS model averaging proceeds from the basis of Bayesian analyses, for
which the parameters of the models under consideration are updated using
the dataset of interest.

Priors for the parameters are defined in [Section
12.2](#bayesian-dichotomous-model-descriptions) for dichotomous
dose-response models. Only dichotomous model averaging is available in
BMDS Online.

For each model, $M$, there is a likelihood for the data,
$\mathcal{l}(D|M)$, based on the data generating mechanism (binomial
sampling in the case of the dichotomous endpoints; Normal or Lognormal
distributions for continuous data).

When one is interested in more than one model, model averaging is an
approach that should be seriously considered in lieu of model selection
(*e.g.*, basing inferences on one model deemed to be the "best").

Suppose for this development that we are considering K models
($M_{k},\ k\  = \ 1,\ \ldots,\ K)$).

For each model, BMDS approximates the posterior density for the BMD
using a Laplacian approximation; call that density
$g_{k}\left( BMD \middle| M_{k},D \right)$ for model k. If the parameter
vector for model k is denoted θ~k~, let ${\widehat{\theta}}_{k}$
designate the value of that vector that maximizes the posterior
likelihood (the maximum *a posteriori*, or MAP, estimate).

The posterior density of the model-averaged BMD is

$$g_{ma}\left( BMD|D \right) = \ \sum_{k = 1}^{K}{\pi_{k}\left( M_{k} \middle| D \right)g_{k}\left( BMD \middle| M_{k},D \right),}$$

where $\pi_{k}$ is the posterior probability of model $M_{k}$ given the
data.

Clearly, this approach requires estimation of the posterior
probabilities for each model considered. These are the weights for the
averaging process. Unlike approaches that have been used elsewhere, we
eschew the use of information-criteria-based weights (*e.g.*, those
based on Bayesian information criteria or Akaike information criteria).
Rather, BMDS generates weights using the Laplace approximation to the
marginal density of the data. That is, for model *M~k~*, 1 ≤ *k* ≤ K,
with parameter vector $\theta_{k}$ of length s, one approximates the
marginal density as

$$I_{k} = (2\pi)^{\frac{s}{2}}\left| {\widehat{\Sigma}}_{k} \right|^{\frac{1}{2}}\mathcal{l}\left( D \middle| {M_{k},\widehat{\theta}}_{k} \right)g\left( {\widehat{\theta}}_{k}|M_{k} \right)$$

where

${\widehat{\theta}}_{k}$ is the MAP estimate,

${\widehat{\Sigma}}_{k}\ $is the negative inverse Hessian matrix
evaluated at ${\widehat{\theta}}_{k}$,

$\mathcal{l}\left( D \middle| {M_{k},\ \widehat{\theta}}_{k} \right)\ $is
the likelihood of the data, for model k evaluated at the MAP, and

$g\left( {\widehat{\theta}}_{k} \middle| M_{k} \right)$ is the value of
the prior density for $M_{k}$ evaluated at the MAP parameter estimates.

To compute the posterior model probabilities for the $M_{k}$, one
calculates the MAP and then calculates *I~k~* using the preceding
equation. The posterior probability of the model is

$$\pi_{k}\left( M_{k} \middle| D \right) = \ \frac{w_{k}I_{k}}{\sum_{i = 1}^{K}{w_{k}I_{k}}},$$

where $w_{k}\ $is the prior probability of model $M_{k}$. In BMDS, the
user can specify those weights; the default is equal weight for each
model (all models being considered are equally probable *a priori*).

This approximation is similar to the Model Averaged Profile Likelihood
(MAPL) approach of Fletcher and Turek
([2012](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/4286986)).
However, while MAPL relies only on the likelihood, our approach
incorporates prior information in calculating the marginal profile
density of the BMD. In other words, both the likelihood and prior are
used. The model-specific density is defined by treating profile density
bounds as quantiles of a marginal posterior density for the parameter of
interest, and the relation to the present approach and the MAPL approach
is justified asymptotically.

This approach can be related to the MAPL framework by substituting the
posterior density for the likelihood in each of the steps. This method
approximates the marginal likelihood using the posterior MAP estimate
and Hessian of the log-posterior.

**Note** For the model average approach, the dichotomous Bayesian models
(described in Section 9.1) are available in the model average. For
dichotomous model averaging, the Multistage model is capped to a maximum
degree of 2. The reasoning for this follows upon the work of Nitcheva,
et al.
([2007](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/729569))
who show that higher-order polynomials are not necessary given the fact
that other models of the model averaging suite (*e.g.*, dichotomous
Hill) can provide increased curvature.

The BMDS model-averaged BMD point estimate is the weighted average of
BMD MAP estimates from individual models, weighted by posterior weights
$\pi_{k}\left( M_{k} \middle| D \right).$ This is equivalent to the
median of the approximate posterior density of θ. For the BMDL or BMDU
estimates, the equation defining $g_{ma}$ is integrated. A 100(*α*)%
BMDU estimate or 100(1 - *α*)% BMDL estimate is the value BMD~α~ such
that:

$$\alpha = \ \int_{- \infty}^{BMD_{\alpha}}{g_{ma}\left( BMD|D \right)\ dBMD,}$$

$$= \sum_{k = 1}^{K}{\pi_{k}\left( M_{k} \middle| D \right)\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}.}$$

The quantity
$\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}$
is approximated by,

$$\int_{- \infty}^{BMD_{\alpha}}{g_{k}\left( BMD \middle| M_{k},D \right)\ dBMD}$$

$$\approx {\frac{1}{2}\Pr}\left( \  - 2{\text{ log}\lbrack\widehat{g}}_{k}\left( \widehat{BMD} \middle| M_{k},D \right) \right\rbrack - 2{\ log\lbrack\widehat{g}}_{k}\left( BMD_{\alpha} \middle| M_{k},D \right)\rbrack < \ \chi_{1,\alpha\ }^{2}),$$

where${\ \widehat{g}}_{k}\left( x \middle| M_{k},D \right)$ is the
maximum value of the posterior evaluated at *x,* $\widehat{BMD}$ is the
MAP estimate of the BMD*,* and $\chi_{1,\alpha\ }^{2}$ is the *α*
quantile of a Chi-square random variable with one degree of freedom. The
above approximation assumes $BMD_{\alpha} < \widehat{BMD}$. When
$\widehat{BMD} < BMD_{\alpha}$ the right-hand side of this equation is
replaced by

$$\approx 1 - {\frac{1}{2}\Pr}\left( \  - 2{\ log\lbrack\widehat{g}}_{k}\left( \widehat{BMD} \middle| M_{k},D \right) \right\rbrack - 2{\ log\lbrack\widehat{g}}_{k}\left( BMD_{\gamma} \middle| M_{k},D \right)\rbrack < \ \chi_{1,\gamma\ }^{2}).$$

This approximation is like the profile-likelihood used when estimating
the BMDL and BMDU using the method of maximum likelihood, but in this
case ${\ \widehat{g}}_{k}\left( x \middle| M_{k},D \right)$ is the
posterior density, which incorporates both the likelihood and the prior.

## Results Specific to Bayesian Dichotomous Models

To compare the difference between any two Bayesian models, the
unnormalized Log Posterior Probability (LPP) is given, which allows the
computation of a Bayes factor (BF) to compare any two models. BF equals
the exponentiated difference between the two LPP. For example, if one
wishes to compare the Log-Logistic model (Model A) (yielding LPP~A~) to
the Multistage 2^nd^ degree model (Model B, with LPP~B~) one estimates
the BF as

$$BF = \exp\left( LPP_{A} - LPP_{B} \right),$$

This computation assumes that both models have equal probability *a
priori.* This value is then interpreted as the posterior odds one model
is more correct than the other model and is used in Bayesian hypothesis
testing. In the example above, if the Bayes Factor was 2.5, the
interpretation would be that the Log-logistic model is *a posteriori*
2.5 times more likely than the multistage model. When these values are
normalized into proper probabilities, they are equivalent to the
posterior model probabilities given in model averaging (again, assuming
equal model probability *a priori*). Table 13 is adapted from Jeffreys
([1998](https://www.epa.gov/bmds/benchmark-dose-software-bmds-version-27-materials?action=search.view&reference_id=4850043))
and is a common interpretation of Bayes Factors.

[]{#_Toc47700653 .anchor}**Figure 101.** Sample Bayesian dichotomous
results plot.

![Multiple model result curves plotted on single graph, with
legend](_static/img/image104.png){width="6.5in" height="3.161111111111111in"}


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

For BMDS, all LPP and corresponding posterior model probabilities are
computed using the Laplace approximation. This value is different from
the commonly used Bayesian Information Criterion (BIC), and the two
should not be confused based upon other model averaging approaches,
which use the BIC exclusively. Errors in the posterior probabilities
estimated from the BIC are $O(1)$ estimators. Errors in the posterior
probabilities estimated using the Laplace approximation are
$O(n^{- 1})$. This means the latter approximation goes to the true
posterior model probability with increasing data and the former, using
the BIC, may not go to the true value.

## Bayesian Dichotomous Model Descriptions

***Note*** At this time, EPA does not offer technical guidance on
Bayesian modeling or Bayesian model averaging.

From a Bayesian perspective, inference proceeds by defining a
data-generating mechanism, given a model, $M$, and its parameters. For
our purposes, $M$ would be one of the models listed in Table 8 that
determines the probability of response. For the dichotomous models, the
data generating mechanism would be the assumption that the observations
were obtained from binomial sampling, having the dose-dependent
probability of response defined by one of those models (with specific
values of the parameters in that model).

We can then relate that to the likelihood, here denoted
$\mathcal{l}(D|M)$, which shows explicitly that it is the likelihood of
the data, $D$, conditional on the model. The functional form of the log
of the likelihood is presented in Section 9.5.1, "Likelihood Function,"
on page [77](#likelihood-function-1).

The set of Bayesian dichotomous models used in BMDS 3 is identical to
the set of models used for maximum-likelihood estimation (MLE)
approaches (Table 8). In the following, let θ be the vector of
parameters that are required to define the any one of those models. So,
for example, for the Weibull model θ = (g, α, β). The additional
consideration incorporated into the Bayesian approach is the
specification of a prior distribution for θ. The Bayesian approach takes
the specified prior and updates it using the data under consideration to
obtain a posterior distribution for θ.

From a Bayesian perspective, functions of θ also have posterior
densities. So, using the equations (which express the BMD as function of
the model parameters) summarized in Table 9, one can derive a posterior
distribution for the BMD.

BMDS summarizes the posterior for the BMD as follows. The BMD is equated
to the value obtained (as in Table 9) by using the maximum *a
posteriori* (MAP) θ estimate. The MAP is the value of θ that maximizes
the posterior log-likelihood. The posterior density is itself
approximated using a Laplacian approximation. This approximation is also
used to estimate BMDL and BMDU values, which are the percentiles from
that density that correspond to the confidence level selected by the
user.

The priors for the BMDS dichotomous models are defined in Table 14.

**Note**

The priors for the parameters are based on scaled doses and scaled
responses; BMDS performs this scaling automatically.

**BMDS automatically scales the doses** by dividing by the maximum dose
in the dataset under consideration, *i.e.*, that the doses under
consideration range from 0 to 1 (inclusive). **BMDS automatically scales
the responses** by dividing by the mean response in the control (or
lowest dose) group.

The user does ***not*** need to scale anything beforehand. That means
that the parameter estimates, and BMD values returned by the program
have been adjusted back to the original scale of the doses and the
original scale of the responses specified in the input data file.

[]{#_Ref548672746 .anchor}Table 14. *Bayesian dichotomous models and
their respective parameter priors.*

+---------------------+-------+--------------+-------------------------+
| Model               | C     | Priors       | Notes                   |
|                     | onstr |              |                         |
|                     | aints |              |                         |
+=====================+=======+==============+=========================+
| Multistage          | $     | $$logit      | The prior over the β~1~ |
|                     | $0 \l | (g)\sim\ Nor | parameter reflects the  |
| $p(dose) = g + (1   | eq g  | mal(0,\ 2)$$ | belief that the linear  |
|  - g)\left( 1 - \ex | < 1$$ |              | term should be strictly |
| p\left\lbrack - \su |       | $$\beta_{    | positive if the         |
| m_{i = 1}^{N}{\beta | $$    | i}\sim\ Logn | quadratic term is       |
| _{i}{dose}^{i}} \ri | \beta | ormal(0,1),\ | positive in the two-hit |
| ght\rbrack \right)$ | _{i}  |  i \geq 2)$$ | model of                |
|                     | > 0$$ |              | carcinogenesis.         |
|                     |       |              |                         |
|                     | $$N\  |              | The difference in       |
|                     |   \ge |              | priors between          |
|                     | q 2$$ |              | Multistage and Quantal  |
|                     |       |              | Linear models is by     |
|                     |       |              | design. The objective   |
|                     |       |              | is to emphasize the     |
|                     |       |              | higher-order terms in   |
|                     |       |              | each model. Multistage  |
|                     |       |              | 1 uses a prior favoring |
|                     |       |              | shallow dose-response   |
|                     |       |              | relationships, while    |
|                     |       |              | Quantal Linear uses a   |
|                     |       |              | more diffuse prior.     |
|                     |       |              |                         |
|                     |       |              | For model averaging     |
|                     |       |              | purposes, N = 2.        |
+---------------------+-------+--------------+-------------------------+
| Weibull             | $     | $$logit      |                         |
|                     | $0 \l | (g)\sim\ Nor |                         |
| $p(dose) = g + (1 - | eq g  | mal(0,\ 2)$$ |                         |
|  g)\left( 1 - \exp\ | < 1$$ |              |                         |
| left\lbrack - \beta |       | $\alph       |                         |
| {dose}^{\alpha} \ri | $$0   | a\sim\ Logno |                         |
| ght\rbrack \right)$ | < \al | rmal(\sqrt{0 |                         |
|                     | pha < | .18},\ 0.5$) |                         |
|                     |  40$$ |              |                         |
|                     |       | $$\beta\s    |                         |
|                     | $$    | im\ Lognorma |                         |
|                     | 0 < \ | l(0,\ 1.5)$$ |                         |
|                     | beta  |              |                         |
|                     | < 10, |              |                         |
|                     | 000$$ |              |                         |
+---------------------+-------+--------------+-------------------------+
| Quantal Linear      | $     | $$logit      | The difference in       |
|                     | $0 \l | (g)\sim\ Nor | priors between Quantal  |
| $p(dose) = g + (    | eq g  | mal(0,\ 2)$$ | Linear and the          |
| 1 - g)\left( 1 - \e | < 1$$ |              | following Multistage    |
| xp\lbrack - \beta d |       | $$\beta      | model is by design. The |
| ose\rbrack \right)$ | $$0 < | \sim\ Lognor | objective is to         |
|                     |  \ \b | mal(0,\ 1)$$ | emphasize the           |
|                     | eta < |              | higher-order terms in   |
|                     |  18$$ |              | each model.             |
|                     |       |              |                         |
|                     |       |              | Quantal Linear is not   |
|                     |       |              | the same as             |
|                     |       |              | Multistage-1. This is   |
|                     |       |              | important for model     |
|                     |       |              | averaging purposes.     |
|                     |       |              | Multistage 1 uses a     |
|                     |       |              | prior favoring shallow  |
|                     |       |              | dose-response           |
|                     |       |              | relationships, while    |
|                     |       |              | Quantal Linear uses a   |
|                     |       |              | more diffuse prior.     |
+---------------------+-------+--------------+-------------------------+
| Gamma               | $     | $$log        | The prior for α entails |
|                     | $0 \l | it(g)\sim\ N | that there is only a    |
| $p(dose) = g + \fra | eq g  | ormal(0,2)$$ | 0.05 prior probability  |
| c{1 - g}{\Gamma(\al | < 1$$ |              | the power parameter     |
| pha)}\int_{0}^{\bet |       | $$\alpha\si  | will be less than 1.    |
| a dose}{t^{\alpha - | $     | m\ Lognormal | This allows for models  |
|  1}\exp( - t)dt\ }$ | $0.2  | (\ln(2),\ \s | that are supra linear;  |
|                     | < \al | qrt{0.18})$$ | however, it requires a  |
|                     | pha < |              | large amount of data    |
|                     |  20$$ | $$\beta      | for the α parameter to  |
|                     |       | \sim\ Lognor | go much below 1.        |
|                     | $$0   | mal(0,\ 1)$$ |                         |
|                     | < \ \ |              | The α parameter is also |
|                     | beta  |              | constrained to be       |
|                     | < 10, |              | greater than 0.2, for   |
|                     | 000$$ |              | numerical reasons.      |
+---------------------+-------+--------------+-------------------------+
| Logistic            | $$    | $$\alph      |                         |
|                     | - 20  | a\ \sim\ Nor |                         |
| $p(dose) =          | < \al | mal(0,\ 2)$$ |                         |
|  \frac{1}{1 + exp\l | pha < |              |                         |
| brack - \alpha\  -  |  20$$ | $$\be        |                         |
| \beta dose\rbrack}$ |       | ta\sim\ Logn |                         |
|                     | $$    | ormal(0,2)$$ |                         |
|                     | 0 < \ |              |                         |
|                     |  \bet |              |                         |
|                     | a\  < |              |                         |
|                     |  40$$ |              |                         |
+---------------------+-------+--------------+-------------------------+
| Log-Logistic        | $     | $$logit      |                         |
|                     | $0 \l | (g)\sim\ Nor |                         |
| $p(d                | eq g  | mal(0,\ 2)$$ |                         |
| dose) = g + \frac{1 | < 1$$ |              |                         |
|  - g}{1 + exp\lbrac |       | $$\alph      |                         |
| k - \alpha\  - \bet | $$    | a\ \sim\ Nor |                         |
| a\ln(dose)\rbrack}$ | - 40  | mal(0,\ 1)$$ |                         |
|                     | < \al |              |                         |
|                     | pha < | $$\          |                         |
|                     |  40$$ | beta\sim\ Lo |                         |
|                     |       | gnormal({ln} |                         |
|                     | $$0 < | (2),\ 0.5)$$ |                         |
|                     |  \ \b |              |                         |
|                     | eta < |              |                         |
|                     |  20$$ |              |                         |
+---------------------+-------+--------------+-------------------------+
| Probit              | $$    | $$\alph      | $\Phi( \bullet )$ is    |
|                     | - 20  | a\ \sim\ Nor | the standard Normal     |
| $p(                 | < \al | mal(0,\ 2)$$ | cumulative density      |
| dose) = \ \Phi(\alp | pha < |              | function                |
| ha + \ \beta dose)$ |  20$$ | $$\beta      |                         |
|                     |       | \sim\ Lognor |                         |
|                     | $$0 < | mal(0,\ 1)$$ |                         |
|                     |  \ \b |              |                         |
|                     | eta < |              |                         |
|                     |  40$$ |              |                         |
+---------------------+-------+--------------+-------------------------+
| Log-Probit          | $     | $$logit      | $\Phi( \bullet )$ is    |
|                     | $0 \l | (g)\sim\ Nor | the standard Normal     |
| $p(dose             | eq g  | mal(0,\ 2)$$ | cumulative density      |
| ) = g + (1 - g)\Phi | < 1$$ |              | function                |
| \lbrack\alpha + \be |       | $$\alph      |                         |
| ta\ln(dose)\rbrack$ | $$    | a\ \sim\ Nor |                         |
|                     | - 40  | mal(0,\ 1)$$ |                         |
|                     | < \al |              |                         |
|                     | pha < | $$           |                         |
|                     |  40$$ | \beta\sim\ L |                         |
|                     |       | ognormal(\ln |                         |
|                     | $$0 < | (2),\ 0.5)$$ |                         |
|                     |  \ \b |              |                         |
|                     | eta < |              |                         |
|                     |  20$$ |              |                         |
+---------------------+-------+--------------+-------------------------+
| Dichotomous Hill    | $     | $$logit(g)   |                         |
|                     | $0 \l | \sim\ Normal |                         |
| $p(do               | eq g  | ( - 1,\ 2)$$ |                         |
| se) = g + \ \frac{\ | < 1$$ |              |                         |
| nu - v \times g}{1  |       | $$a\ \s      |                         |
| + exp\lbrack - a -  | $$- 4 | im\ Normal(  |                         |
| b\ln(dose)\rbrack}$ | 0 < v | - 3,\ 3.3)$$ |                         |
|                     |  \leq |              |                         |
|                     |  40$$ | $$b\ \sim\ L |                         |
|                     |       | ognormal(\ln |                         |
|                     | $$    | (2),\ 0.5)$$ |                         |
|                     | - 40  |              |                         |
|                     | < a < | $$logit      |                         |
|                     |  40$$ | (v)\sim\ Nor |                         |
|                     |       | mal(0,\ 3)$$ |                         |
|                     | $     |              |                         |
|                     | $0 <  |              |                         |
|                     | \ b < |              |                         |
|                     |  40$$ |              |                         |
+---------------------+-------+--------------+-------------------------+

: The individual Bayesian dichotomous models and their respective
parameter priors. Table showing, for each Bayesian dichotomous model,
its equation, constraints, priors, and notes

**Notes:** $\text{logit}(g) = \ln\left( \frac{g}{1 - g} \right)$. Normal(x, y) denotes a Normal distribution with mean x and standard deviation y. Lognormal(w, z) denotes a Lognormal distribution with log-scale mean w and log-scale standard deviation z.

As the number of observations in a dataset increases, there should be less quantitative difference between the parameters and BMDs obtained from the Bayesian approach and from the maximum-likelihood estimation (MLE) approach.

When there are fewer data points, the priors will affect the Bayesian estimation. The impact may be most noticeable when the data suggest a "hockey-stick" shaped dose-response relationship, or when those data suggest strong supralinear behavior. In these cases, the priors specified above for the Bayesian approach will tend to "shrink back" parameter estimates to obtain smoother dose-response relationships where changes in the slope are more gradual.

***Note*** Table 14 presents the background parameter constraints on the logit scale, which is the form in which BMDS uses these constraints for calculation. The constraints are input into the software on the real number scale, with values of -18/18 for the MLE model and -20/20 for the Bayesian model minimum/maximum. The software then performs a logit transformation on these values. The background parameter values output by BMDS in the results will have a range of 0 to the maximum dose for each model.
