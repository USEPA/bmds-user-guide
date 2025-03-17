# Model Recommendations and Decision Logic

BMDS analyzes modeling results and automatically recommends model
selections that are consistent with the 2012 EPA Benchmark Dose
Technical Guidance ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

BMDS Online displays the logic tests relevant to the model type selected
on the Settings tab: Continuous, Dichotomous, or Nested.
Multitumor/Multistage Dichotomous does not have its own set of logic
rules because [it is a special instance of Dichotomous
modeling](#multiple-tumor-analysis).

On the Logic tab, users can enable or disable specific decision logic
settings and even alter specific test criteria. ***However, it is highly
recommended that new users leave the logic settings as-is; logic
settings should only be changed under the guidance of experienced
modelers.***

## About the Logic Tab

The purpose of the Logic tab and its settings in BMDS are to assist
users in performing BMD analyses in accordance with EPA Benchmark Dose
Technical Guidance ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

The logic settings can be overridden but are set to default values and
options that are most consistent with EPA's BMD guidance.

Models that meet all logic criteria are considered viable. If a modeling
result fails any of the criteria listed in [**Unusable**](#unusable-bin) or [**Questionable**](#questionable-bin), its
results are placed in those respective bins,
and are not classed as [**Viable**](#viable) for recommendation.

For the criteria listed in [**Warnings**](#warnings), failure of the criteria only
results in a warning.

The recommended model is chosen from the Viable models, as described in
[**Viable**](#viable). If the range of BMDL estimates from all Viable models is
less than a user-specified "Maximum BMDL range deemed sufficiently
close" (set to 3-fold by default), the Viable model with the lowest BMDL
is chosen. Otherwise, the Viable model with the lowest AIC is chosen.

## How BMDS Recommends a Model

BMDS places each model into one of three different bins:

-   **Unusable**---required outputs such as BMD or BMDL are not
    estimated.

-   **Questionable**---some serious deficiencies with model based on
    user-defined decision logic.

-   **Viable**---highest quality model, no serious deficiencies found
    based on user-defined logic but may contain warnings.

The default settings for factors (tests) that determine bin placement
are consistent with EPA Benchmark Dose Technical Guidance ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

### Unusable Bin

If ***any*** of the following tests are true, then the results are
classed as Unusable:

-   BMD not estimated or invalid

-   BMDL not estimated or invalid

-   AIC not estimated or invalid

These tests apply to all datasets.

### Questionable Bin

If ***any*** of the tests described in this section are true, then the
results are classed as Questionable.

The following default settings that can cause test failure, and thereby
affect bin placement, are not explicitly given in the EPA BMD guidance.
These settings have been assigned based on general EPA practice and are,
therefore, more open to user discretion:

-   BMDL range default fail: \> 3-fold (all dataset types)

-   Constant and non-constant variance p-value default fail: \<
    0.05 (continuous only)[^1]

[^1]: Examples given in EPA BMD guidance ([U.S. EPA, 2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)) suggest a criteria of p-value \> 0.1 for variance models, but this has since been relaxed in practice. Future EPA guidance will reflect this change.

-   Ratio of BMD/BMDL (serious) default fail: \> 20 (all dataset types)

-   BMD lower than lowest dose (serious) default fail: \> 10 (all
    dataset types)

-   BMDL lower than lowest dose (serious) default fail: \> 10 (all
    dataset types)

Other tests that will classify a result as Questionable include:

-   Absolute value of scaled residual of interest \> 2 (all dataset
    types)

-   Goodness-of-fit p-test \< 0.05 (dichotomous, multistage cancer
    model only)

-   Goodness-of-fit p-test \< 0.1 (all other models for continuous and
    dichotomous datasets)

### Warnings

If ***any*** of the tests described in this section are true, then BMDS
displays a warning in the Results table. However, the results are still
classed as Viable.

For all dataset types, the tests are:

-   BMD/BMDL ratio \> 5

-   BMDS result included a warning

-   BMD or BMDL higher than highest dose

-   BMD or BMDL 3x lower than lowest non-zero dose

-   BMDU not estimated

For continuous datasets only, the test is:

-   Modeled response standard deviation is \> 1.5x actual response
    standard deviation of control

### Viable

All models start as Viable before the logic tests are applied.

After all models of the same Option Set (*i.e.*, same model run settings
such as BMR Type, BMRF, etc.) have been placed into one of the three
quality bins, a best-fitting model is recommended from the Viable bin.

The model recommendation criteria are based on BMDL or AIC criteria
defined in the 2012 EPA Benchmark Dose Technical Guidance ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433))
and the following criteria:

-   If the range of BMDLs from models remaining in the Viable bin
    is \< 3, then recommend the BMDL from the model with the lowest AIC

-   Otherwise, recommend the lowest BMDL from models remaining in the
    Viable bin.

## Changing the Decision and Recommendation Logic

***Note*** When changing the decision logic; an experienced user or
statistician should be consulted to ensure the criteria selections are
reasonable.\
\
Any changes to the BMDS default logic should be noted in any results or
reports.

For all selections in the Decision Logic and Model Recommendation and
Bin Placement Logic tables, the user can:

-   Select the check boxes to enable or disable a setting or test.

-   Change the bin placement based on the threshold value.

-   Change numeric values to alter the BMDL range (Decision Logic) or
    threshold test range (Model/Bin logic).

-   Select the **Reset to Default Logic** button to revert all changes.

Logic settings are saved with the Settings and Results of a run; loading
a previously run analysis will restore any customized logic settings.

```{figure} _static/img/image65.png
:alt: BMDS Online Decision Logic table
:scale: 50%
:name: f61

Decision Logic settings.
```
The BMDS Decision Logic settings are:

-   Enable model recommendation logic testing. Default is selected.

-   Recommend model in viable bin. Default is selected.

-   Recommend model in questionable bin. Default is unselected. Enable
    this only to be more lenient on which models the logic could
    recommend.

-   Maximum BMDL range deemed "sufficiently close" to use lowest AIC
    instead of lowest BMDL in viable models. Default is 3. Allowable
    range is from zero (0) to 10,000.

-   A value of zero would ensure the lowest BMDL is used for model
    recommendation.

-   A value of 10,000 would almost certainly ensure that the lowest AIC
    is used for model recommendation, meaning that consideration of
    model uncertainty is relaxed (*i.e*., a greater range of BMDLs would
    be necessary for the lowest BMDL to be used as the selection
    criterion).

```{figure} _static/img/image66.png
:alt: Model Recommendation and Bin Placement Logic table with picklist displayed for alternative bin placement
:scale: 60%
:name: f62

Users can change the bin placement logic for a test.
```

The *Notes to Show* column text cannot be edited. BMDS automatically
updates a note to reflect any changed threshold values.

## Documenting Recommendations in the Word Report

Based on the decision logic entered by the user, BMDS will attempt to
select a recommended, best-fitting model. A user must ultimately select
a model and may choose to disagree with the BMDS auto-determination. If
so, the user should document that disagreement in the Word Report.

Any changes made by the user to the BMDS default logic also should be
noted in any results or reports.

BMDS automatically generates suggested text for the *BMDS
Recommendation* and *BMDS Recommendation Notes* columns of the Results
Workbook summary tables and the Word Report File tables.

The Word Report's tables can be modified extensively, and the user is
encouraged to take advantage of this flexibility to change and/or expand
on the table headers and the justification provided for why a model was
selected.

The Word Report's plots are images. Changes to the plot formatting
(*e.g.*, title and axis labels) must be made in BMDS prior to generating
the Word Report.

