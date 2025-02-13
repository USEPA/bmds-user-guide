# Results Output Common to MLE Models

BMDS results provide the user with goodness-of-fit criteria and model
results to aid in determining the appropriateness of the Model and
Option Set to the benchmark dose derivation.

BMDS Online displays summary results for the analysis for the Model and
Option Set in the Output tab. From the Output tab, the user can then
select an individual model's detailed results and statistics. Individual
model results open in their own window when the model name is selected.

## All Models: Output Tab

The Output tab displays several tables of results and calculations
depending on the type of endpoint.

-   Dataset and Option Set tables: Reproduces the dataset and option set
    selections for the analysis.

-   Maximum Likelihood Approach Model Results table, for both Restricted
    and Unrestricted models. The table includes key fit statistics with
    BMDS recommendations for best-fitting model.

-   Graph of the dataset; hover the pointer over a model name to display
    the curve.

-   Model Selection block where the user can document the best-fitting
    model.

-   Bayesian Model Results table (Dichotomous only) and graph.

The following wireframe diagrams provide a simple overview of the tables
and plots shown on the Output tab for each endpoint type.

[]{#_Toc185445223 .anchor}**Figure 47.** Continuous Results Output tab
layout.

![Simplified and labeled layout of continuous results output
page](_static/img/image52.JPG){width="5.2625in"
height="2.4625798337707785in"}

[]{#_Toc185445224 .anchor}**Figure 48.** Dichotomous Results Output tab
layout.

![Simplified and labeled layout of dichotomous results output
page](_static/img/image53.JPG){width="5.424459755030621in"
height="3.8666666666666667in"}

[]{#_Toc185445225 .anchor}**Figure 49.** Nested Dichotomous Results
Output tab layout.

![Simplified and labeled layout of nested dichotomous results output
page](_static/img/image54.png){width="5.382653105861768in"
height="2.3782163167104113in"}

[]{#_Toc185445226 .anchor}**Figure 50.** Multistage Multitumor Results
Output tab layout.

![Simplified and labeled layout of multistage multitumor results output
page](_static/img/image55.png){width="4.684178696412949in"
height="2.298051181102362in"}

## Individual Model Results

From the Output tab's Maximum Likelihood Approach Model Results table,
select any model link () to display a popup window thoroughly detailing
that model's stats results ().

[]{#_Ref183108349 .anchor}**Figure 51.** Select a model name in the
results table \...

![Callout box drawn around model name in summary results
table](_static/img/image56.png){width="1.2428893263342082in"
height="2.166155949256343in"}

[]{#_Ref183108350 .anchor}**Figure 52.** \... to display a window
showing all results for that model.

s![Pop-up window with model results overlaying the Output
tab.](_static/img/image43.png){width="5.152244094488189in"
height="2.371353893263342in"}

### Individual Model Result Window Layouts

The individual model results window layout differs based on the type of
endpoint: continuous, dichotomous, and nested dichotomous. The following
wireframe diagrams illustrate the results displayed by BMDS for each
model type.

[]{#_Toc185445229 .anchor}**Figure 53.** Continuous model result window
layout.

![Simplified and labelled diagram of continuous model result window
layout](_static/img/image57.png){width="4.54in" height="3.4in"}

[]{#_Toc185445230 .anchor}**Figure 54.** Dichotomous model result window
layout.

![Simplified and labelled diagram of individual dichotomous model result
window layout](_static/img/image58.png){width="4.51in" height="3.38in"}

[]{#_Toc185445231 .anchor}**Figure 55.** Nested Dichotomous model
results window layout.

![Simplified and labelled diagram of nested dichotomous model result
window layout](_static/img/image59.png){width="4.373811242344707in"
height="3.397836832895888in"}

[]{#_Toc185445232 .anchor}**Figure 56.** Multistage Multitumor model
results window layout.

![Simplified and labelled diagram of multistage multitumor model result
window layout](_static/img/image60.png){width="4.37731627296588in"
height="3.346120953630796in"}

### Summary Table of Key Fit Statistics (All Endpoints)

A model result window's Modeling Summary table for the Model-Option set
contains---depending on the endpoint type---the BMD, BMDL, and BMDU
estimates, AIC, Log Likelihood, the overall goodness-of-fit test
p-value, and degrees of freedom (d.f.).

[]{#_Toc185445233 .anchor}**Figure 57.** Example Modeling Summary table
for a dichotomous model.

![Model Summary table from result
output](_static/img/image61.png){width="2.496596675415573in"
height="2.03159886264217in"}

#### AIC

The Akaike Information Criterion (AIC) ([Akaike,
1973](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=591))
value is calculated as follows:

$$AIC\  = \  - 2 \times LL\  + \ 2 \times p$$

where LL is the log-likelihood at the maximum likelihood estimates for
the parameters, and p is the number of model parameters estimated (and
not on a restriction boundary).[^1]

The AIC can be used to compare different models fit (using the same
fitting method, *e.g.*, least squares or maximum likelihood) to the same
dataset. Smaller values of the AIC indicate better fit. Although AIC
comparisons are not exact (they rely on rules of thumb for interpreting
AIC differences), they can provide useful guidance in model selection.

Model-type specific details on the AIC are discussed in the following
sections:

-   For continuous endpoints, refer to Section 8.6.4 on page
    [65](./continuous.md#aic-and-model-comparisons).

-   For dichotomous endpoints, refer to Section 9.5.2 on page
    [77](./dichotomous.md#aic-and-model-comparisons).


[^1]: For the dichotomous and nested dichotomous models, an additivity
    constant is not included in the LL calculations.

#### P-value

The goodness-of-fit p-value is computed based on the degrees of freedom
and the Chi^2^ value (Chi^2^ is assumed to be distributed as a
Chi-square distribution having degrees of freedom equal to degrees of
freedom). The p-value measures the "closeness" of the model predictions
to the observed data. If the overall p-value is larger than some
predetermined critical p-value, then the user might infer that the model
appropriately describes the observed dose-response pattern. The critical
p-value used by EPA is generally 0.1 but is sometimes relaxed to 0.05
for the Multistage model when it is applied to cancer data ([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

### Model Parameters Table (All Endpoints)

[]{#_Toc47700637 .anchor}**Figure 58.** Model Parameters table for
Exponential 3 (Continuous), with popup description of bounded variable.

![Popup help panel text displayed for Exponential 3
model](_static/img/image62.png){width="5.257245188101487in"
height="1.9506846019247595in"}

The Model Parameters table includes the estimates for the parameter
values that "optimize" the model fit.

Parameter estimates are checked to see if they fall within a given
tolerance (1.0e^-6^) of parameter boundaries. If so, they are marked as
*On Bound*. This tolerance value applies to all parameters.

### Cumulative Distribution Function (CDF) Table (All Endpoints)

CDF stands for *cumulative distribution function*, in this case for the
BMD estimate. It lists the percentiles associated with the CDF for the
BMD being estimated ().

Note that the BMD value associated with the CDF value of 0.5 is the MLE
of the BMD (and matches the value reported for the BMD in the Summary
table discussed above).

The CDF block may also correspond to the Summary table in terms of the
BMDL and BMDU values reported in the latter. Recall that the confidence
level specified by the user in the options is a one-sided confidence
level. So, if that confidence level is related to one of the cumulative
percentiles in the CDF block, the BMD values will match.

As an example, if the confidence level specified by the user is 0.95
(95% one-sided confidence limits requested), then the BMDU from the
Benchmark Dose table will match the BMD value listed for 0.95 in the CDF
block. And the BMDL will match the BMD value listed for 0.05 in the CDF
block.

[]{#_Ref177727762 .anchor}**Figure 59.** CDF table and graph.

![CDF table with accompanying graph
](_static/img/image63.png){width="5.282240813648294in"
height="2.1066885389326333in"}

### Graphs/Plots (All Endpoints)

Graphical outputs (plots) are displayed on both the Output tab and on
the individual model result window.

[]{#_Toc47700638 .anchor}**Figure 60**. Results plot for the Multistage
2 model.

![Results plot for an individual model illustrating various plot
components](_static/img/image64.png){width="3.1683125546806647in"
height="2.890197944006999in"}

The results plot shows the dose-response curve estimated by the model.

-   Data points are shown as blue dots with their individual group
    confidence intervals.

-   The horizontal bar is centered on the y-axis at the modeled BMR.

-   The diamond symbol inside the horizontal bar is the BMD.

-   The horizontal bar's left edge is the BMDL, the right is the BMDU.

Error bar calculations for the data points differ slightly based on the
endpoint:

-   For continuous endpoints, refer to Section 8.5.4, "Plot and Error
    Bar Calculation," on page [61](./continuous.md#plot-and-error-bar-calculation).

-   For dichotomous endpoints, refer to Section 9.4.3, "Plot and Error
    Bar Calculation," on page [72](./dichotomous.md#plot-and-error-bar-calculation).

-   For nested endpoints, refer to Section 10.5.3, "Plot and Error Bar
    Calculation," on page [93](./nested-dichotomous.md#plot-and-error-bar-calculation).

