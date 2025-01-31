# BMDS Modeling Methods

BMDS employs two general modeling approaches: Bayesian for dichotomous
endpoints only, and non-Bayesian methods (such as maximum likelihood)
for all endpoints including dichotomous.

Both Bayesian and non-Bayesian methods estimate parameters of a
statistical model based on observed data. Both approaches use the
likelihood function, which measures how well the model explains the
observed data and provides key statistics such as point estimates (BMD)
and bounds (BMDL). However, the precise way the likelihood is used
differs somewhat between the two approaches.

## Maximum Likelihood and Related Non-Bayesian Methods

The BMDS non-Bayesian methods are maximum likelihood estimation (MLE)
and statistics that rely on optimized likelihood values, particularly
profile likelihood bounds and the Akaike Information Criterion (AIC) for
model-selection. In this documentation, the term *MLE method* is used
for the group of methods associated with likelihood maximization,
recognizing that the term may be considered to apply most specifically
to point estimation.[^3]

The MLE approach is based on finding the parameter values that maximize
the likelihood function. In simpler terms, it chooses the parameters
that make the observed data most probable. Models fit by these methods
report associated bounds determined by profile likelihood
approaches.[^4]

Models not labeled as Bayesian are, by default, MLE.

Specifics on the MLE model equations are presented in the following
sections:

-   Section 8.6, "Mathematical Details for Models for Continuous
    Endpoints in Simple Designs," on page
    [61](#mathematical-details-for-models-for-continuous-endpoints-in-simple-designs)

-   Section 9.5, "Mathematical Details for Models for Dichotomous
    Endpoints in Simple Designs," on page
    [73](#mathematical-details-for-models-for-dichotomous-endpoints-in-simple-designs)

-   Section 10.5, "Mathematical Details for Models for Nested
    Dichotomous Endpoints," on page
    [88](#mathematical-details-for-models-for-nested-dichotomous-endpoints)

## Bayesian

Bayesian methods combine prior information about parameters with the
observed data to update the probability of an event of interest, as more
evidence becomes available. Bayesian analysis can be more
computationally intensive than MLE methodology but offers a richer view
of parameter uncertainty.

Following the Bayesian approach, distributions describing the *a priori*
uncertainty in the parameter values (the so-called prior distributions)
are updated using the data under consideration to yield *a posteriori*
distributions (the so-called posterior distributions). A quantile of the
posterior BMD distribution, for example the 5th percentile, may be used
for a Bayesian BMDL.[^5] A Bayesian point estimation procedure analogous
to maximum likelihood is *maximum* *a posteriori probability* *(MAP)*
estimation.[^6]

The likelihood function plays a critical, formal role in Bayesian
inference, different from its role in maximum likelihood.

***Note*** At this time, EPA does not offer technical guidance on
Bayesian modeling or Bayesian model averaging.

See the following table where the priors and model constraints are
presented:

-   Table 14: Bayesian dichotomous models and their respective parameter
    priors on page [109](#_Ref548672746)

To see how model parameter estimates are reported in the BMDS results,
refer to Section 6.2.3, "Model Parameters," on page
[42](#model-parameters-table-all-endpoints).

Bayesian analysis is described in more detail in Section 12.0, "Bayesian
Dichotomous Analysis, including Model Averaging," on page
[105](#bayesian-dichotomous-analysis-including-model-averaging).

## Optimization Algorithms Used in BMDS

BMDS uses the NLopt optimization library for MLE analyses and some
Bayesian computations. Somewhat differently constrained optimization
methods are involved for BMD and BMDL computations (Bayesian or MLE).

Several optimization algorithms available in the library are used to
ensure reliability of the estimation:

-   For global optimization involving the maximum likelihood or maximum
    *a posteriori* estimation subject to bounds on parameters (which are
    inequality constraints), the L-BFGS[^7] method is attempted first.
    If it fails to converge, gradient-free algorithms (subplex and
    BOBYQA[^8]) are then attempted. Note that the parameter bounds will
    be carried forward into the calculations that follow.

-   The Bayesian BMDL in BMDS, as well as profile likelihood, involves
    *profiling*, wherein parameters are optimized with the BMD fixed at
    specific values, in addition to the inequality constraints on the
    individual parameters. Fixing the BMD will add a linear or nonlinear
    equality constraint.

-   For equality-constrained optimizations, the augmented Lagrangian
    algorithm is used and either the L-BFGS, BOBYQA, or subplex
    algorithm is used in the local optimization step. When two
    approaches produce different results, the values producing the
    larger optimum are used.

-   For optimizations involving ***only*** inequality constraints, the
    COBYLA[^9] and MMA[^10] approaches are used and compared. In the
    case the methods return different optimum, the values producing the
    larger of the two are used.

NLopt 2.4.1 was used when developing the BMDS model code. This version
is available for download from the [NLopt GitHub
site](https://github.com/stevengj/nlopt/releases). For more information
regarding the algorithms, refer to the [NLopt documentation
site](https://nlopt.readthedocs.io/en/latest/).

