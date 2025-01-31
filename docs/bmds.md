# Benchmark Dose Models Included in BMDS

Most of the models in the following tables were developed by U.S. EPA
and are available in BMDS, unless otherwise noted.

Some models are flagged as available only in BMDS 2.7. The [BMDS
2.7](https://www.epa.gov/bmds/benchmark-dose-software-bmds-version-27-materials)
and [BMDS 3.3](https://www.epa.gov/bmds/download-bmds/) software
packages are available for download but are no longer supported or
updated by EPA.

[]{#_Toc77956652 .anchor}Table 1. *List of Maximum-Likelihood Estimation
(MLE) Continuous Models*

| Model | BMDS 2.7 | BMDS 3.3 | BMDS Online |
|---|---|---|---|
| Exponential | Yes | Yes | Yes |
| Hill | Yes | Yes | Yes |
| Linear | Yes | Yes | Yes |
| Polynomial | Yes | Yes | Yes |
| Power | Yes | Yes | Yes |

This table identifies which BMDS products contain the MLE continuous models

[]{#_Toc77956653 .anchor}Table 2. *List of MLE Dichotomous Models*

  ------------------------------------------------------------------------
  Model                  BMDS 2.7       BMDS 3.3       BMDS Online
  ---------------------- -------------- -------------- -------------------
  Gamma                  Yes            Yes            Yes

  Logistic               Yes            Yes            Yes

  Log-Logistic           Yes            Yes            Yes

  Log-Probit             Yes            Yes            Yes

  Multistage             Yes            Yes            Yes

  Probit                 Yes            Yes            Yes

  Weibull                Yes            Yes            Yes

  Quantal Linear         Yes            Yes            Yes

  Dichotomous Hill       Yes            Yes            Yes
  ------------------------------------------------------------------------

  : This table identifies which BMDS products contain the MLE
  dichotomous models

[]{#_Toc77956654 .anchor}Table 3. *List of Nested Dichotomous Models*

  -------------------------------------------------------------------------
  Model                                 BMDS 2.7   BMDS 3.3   BMDS Online
  ------------------------------------- ---------- ---------- -------------
  Nested Logistic                       Yes        Yes        Yes

  National Center for Toxicological     Yes        No         No
  Research (NCTR)

  Rai and Van Ryzin\                    Yes        No         No
  (No longer supported)
  -------------------------------------------------------------------------

  : This table identifies which BMDS products contain the nested
  dichotomous models

[]{#_Toc77956655 .anchor}Table 4. *List of Specialized Models*

  -------------------------------------------------------------------------
  Model                                 BMDS 2.7   BMDS 3.3   BMDS Online
  ------------------------------------- ---------- ---------- -------------
  Bayesian model averaging              No         Yes        Yes
  (dichotomous)

  Multistage Cancer/Multitumor          Yes        Yes        Yes
  -------------------------------------------------------------------------

  : This table identifies which BMDS products contain the Bayesian model
  averaging and Multstage Cance/Multitumor models

## Models Not Included in BMDS Online

BMDS Online contains all the models and features that were available in
BMDS 2.7 except for:

-   Dichotomous background-dose models, which were rarely used.

-   Rai and Van Ryzin nested dichotomous model, which was not included
    in BMDS due to the planned inclusion, and increased reliability, of
    the Nested Logistic and NCTR models.

-   [ToxicoDiffusion
    model](https://cfpub.epa.gov/ncea/bmds/recordisplay.cfm?deid=308355)---also
    known as Repeated Response Measures--- was not included because it
    required R to be installed on the target computer.

-   [[Ten Berge Concentration x Time
    model]{.underline}](https://cfpub.epa.gov/ncea/bmds/recordisplay.cfm?deid=308352),
    which was superseded by [[EPA's categorical regression software
    CatReg](https://www.epa.gov/bmds/catreg).]{.underline} CatReg has
    the same functionality but with added features and options.

-   NCTR (National Center for Toxicological Research) nested dichotomous
    model, which is slated for inclusion in a future BMDS release.

All these models --- excluding CatReg --- can be accessed in BMDS 2.7,
[which is available from the BMDS
website](https://www.epa.gov/bmds/benchmark-dose-software-bmds-version-27-materials).

