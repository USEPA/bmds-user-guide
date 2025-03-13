# Benchmark Dose Models Included in BMDS

Most of the models in the following tables were developed by U.S. EPA
and are available in BMDS, unless otherwise noted.

Some models are flagged as available only in BMDS 2.7. The [BMDS
2.7](https://www.epa.gov/bmds/benchmark-dose-software-bmds-version-27-materials)
and [BMDS 3.3](https://www.epa.gov/bmds/download-bmds/) software
packages are available for download but are no longer supported or
updated by EPA.

```{csv-table} List of Maximum-Likelihood Estimation (MLE) Continuous Models
:header: Model,BMDS 2.7,BMDS 3.3,BMDS Online/Desktop/pybmds
:widths: 40, 20, 20, 30

Exponential,Yes,Yes,Yes
Hill,Yes,Yes,Yes
Linear,Yes,Yes,Yes
Polynomial,Yes,Yes,Yes
Power,Yes,Yes,Yes
```

```{csv-table} List of MLE Dichotomous Models
:header: Model,BMDS 2.7,BMDS 3.3,BMDS Online/Desktop/pybmds
:widths: 40, 20, 20, 30

Gamma,Yes,Yes,Yes
Logistic,Yes,Yes,Yes
Log-Logistic,Yes,Yes,Yes
Log-Probit,Yes,Yes,Yes
Multistage,Yes,Yes,Yes
Probit,Yes,Yes,Yes
Weibull,Yes,Yes,Yes
Quantal Linear,Yes,Yes,Yes
Dichotomous Hill,Yes,Yes,Yes
```

```{csv-table} List of Nested Dichotomous Models
:header: Model,BMDS 2.7,BMDS 3.3,BMDS Online/Desktop/pybmds
:widths: 40, 20, 20, 30

Nested Logistic,Yes,Yes,Yes
National Center for Toxicological Research (NCTR),Yes,No,Yes
"Rai and Van Ryzin (No longer supported)",Yes,No,No
```

```{csv-table} List of Specialized Models
:header: Model,BMDS 2.7,BMDS 3.3,BMDS Online/Desktop/pybmds
:widths: 40, 20, 20, 30

Bayesian Model Averaging (Dichotomous),No,Yes,Yes
Multistage Cancer/Multitumor,Yes,Yes,Yes
```

## Models Not Included in BMDS Online

BMDS Online contains all the models and features that were available in
BMDS 2.7 except for:

-   Dichotomous background-dose models, which were rarely used.

-   Rai and Van Ryzin nested dichotomous model, which was not included
    in BMDS due to the planned inclusion, and increased reliability, of
    the Nested Logistic and NCTR models.

-   [ToxicoDiffusion
    model](https://www.epa.gov/bmds/external-review-draft-toxicodiffusion-model-development-2008)---also
    known as Repeated Response Measures--- was not included because it
    required R to be installed on the target computer.

-   [Ten Berge Concentration x Time
    model](https://www.epa.gov/bmds/external-review-concentration-x-time-ten-berge-model-2008),
    which was superseded by [EPA's categorical regression software
    CatReg](https://www.epa.gov/bmds/catreg). CatReg has
    the same functionality but with added features and options.

-   NCTR (National Center for Toxicological Research) nested dichotomous
    model, which is slated for inclusion in a future BMDS release.

All these models --- excluding CatReg --- can be accessed in BMDS 2.7,
[which is available from the BMDS
website](https://www.epa.gov/bmds/benchmark-dose-software-bmds-version-27-materials).

