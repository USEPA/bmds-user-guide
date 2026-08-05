# Results Output Common to MLE and Bayesian Models

BMDS results provide the user with goodness-of-fit criteria and model results for MLE models to aid in determining the appropriateness of the Model and Option Set to the BMD derivation.

BMDS Online displays analysis summary results for the Model and Option Set in the Output tab. From the Output tab, the user can then select an individual model's detailed results and statistics. Individual model results open in their own window when the model name is selected.

## Output Tab

The **Output** tab displays several tables of results and calculations depending on the type of endpoint and modeling method.

-   Dataset and Option Set tables that recapitulate the dataset and option set selections for the analysis.

-   Maximum Likelihood Approach Model Results table for both Restricted and Unrestricted models. The table includes key fit statistics with BMDS recommendations for best-fitting model.

-   Graph of the dataset, hovering the pointer over a model name  displays the curve.

-   Model Selection block where the user can document the best-fitting model.

-   Bayesian Model Averaging Results table and graph.

The following wireframe diagrams provide a simple overview of the tables and plots shown on the Output tab for each endpoint type.

```{figure} _static/img/cont_output_layout.png
:alt: Simplified and labeled layout of continuous results output page
:scale: 25%
:name: f47

Continuous Results Output tab layout.
```

```{figure} _static/img/dichot_output_layout.png
:alt: Simplified and labeled layout of dichotomous results output page
:scale: 25%
:name: f48

Dichotomous Results Output tab layout.
```

```{figure} _static/img/nest_dichot_output_layout.png
:alt: Simplified and labeled layout of nested dichotomous results output page
:scale: 25%
:name: f49

Nested Dichotomous Results Output tab layout.
```

```{figure} _static/img/multitumor_output_layout.png
:alt: Simplified and labeled layout of multistage multitumor results output page
:scale: 25%
:name: f50

Multistage Multitumor Results Output tab layout.
```
## Individual Model Results

From the **Output** tab's Maximum Likelihood Approach Model Results table, select any model link {numref}`f51` to display a popup window thoroughly detailing that model's stats results {numref}`f52`.

```{figure} _static/img/model_in_summary_table.png
:alt: Callout box drawn around model name in summary results table
:scale: 100%
:name: f51

Select a model name in the results table ...
```

```{figure} _static/img/individual_model_results_window.png
:alt: Pop-up window with model results overlaying the Output tab.
:scale: 60%
:name: f52

... to display a window showing all results for that model.
```

### Individual Model Result Window Layouts

The individual model results window layout differs based on the type of endpoint: continuous, dichotomous, and nested dichotomous. The following wireframe diagrams illustrate the results displayed by BMDS for each model type.

```{figure} _static/img/results_layout_MLE_C.png
:alt: Simplified and labelled diagram of continuous model result window layout - MLE
:scale: 25%
:name: f53

Continuous model result window layout - MLE.
```

```{figure} _static/img/results_layout_LOUD_C.png
:alt: Simplified and labelled diagram of continuous model result window layout - LOUD
:scale: 25%
:name: f54

Continuous model result window layout - LOUD Model Averaging.
```

```{figure} _static/img/results_layout_MLE_ToxicR_D.png
:alt: Simplified and labelled diagram of individual dichotomous model result window layout - MLE and ToxicR
:scale: 25%
:name: f55

Dichotomous model result window layout - MLE and ToxicR Model Averaging.
```

```{figure} _static/img/results_layout_LOUD_D.png
:alt: Simplified and labelled diagram of individual dichotomous model result window layout - LOUD
:scale: 25%
:name: f56

Dichotomous model result window layout - LOUD Model Averaging.
```

```{figure} _static/img/results_layout_MLE_NstD.png
:alt: Simplified and labelled diagram of nested dichotomous model result window layout
:scale: 25%
:name: f57

Nested Dichotomous model results window layout - MLE.
```

```{figure} _static/img/results_layout_MLE_MTumor.png
:alt: Simplified and labelled diagram of multistage multitumor model result window layout
:scale: 25%
:name: f58

Multistage Multitumor model results window layout - MLE.
```

### Summary Table of Key Fit Statistics (All Data Types)

A model result window's Modeling Summary table for the Model-Option set contains---depending on the endpoint type---the BMD, BMDL, and BMDU estimates, AIC, Log Likelihood, the overall goodness-of-fit test p-value, and degrees of freedom (d.f.).

```{figure} _static/img/BMD_summary_table_MLE.png
:alt: Model Summary table from result output
:scale: 100%
:name: f59

Example Modeling Summary table for a MLE continuous model.
```

```{figure} _static/img/BMD_summary_table_LOUD.png
:alt: Model Summary table from result output
:scale: 100%
:name: f60

Example Modeling Summary table for a LOUD continuous model.
```

#### AIC

The Akaike Information Criterion (AIC) ([Akaike, 1973](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=591)) value is calculated as follows:

$$AIC\  = \  - 2 \times LL\  + \ 2 \times p$$

where $LL$ is the log-likelihood at the maximum likelihood estimates for the parameters, and $p$ is the number of model parameters estimated (and not on a restriction boundary).

:::{important}
For the dichotomous and nested dichotomous models, an additivity constant is not included in the LL calculations.
:::

The AIC can be used to compare different models fit (using the same fitting method, *e.g.*, least squares or maximum likelihood) to the same dataset. Smaller values of the AIC indicate better fit. Although AIC comparisons are not exact (they rely on rules of thumb for interpreting AIC differences), they can provide useful guidance in model selection.

Model-type specific details on the AIC are discussed in the following sections:

-   [**AIC and Model Comparisons for Continuous Endpoints**](./continuous-mle.md#aic-and-model-comparisons).

-   [**AIC and Model Comparisons for Dichotomous Endpoints**](./dichotomous-mle.md#aic-and-model-comparisons).

#### WAIC
The Watanabe-Akaike information criterion (WAIC) ([Vehtari, et al. (2016)](https://hero.epa.gov/reference/13243404)) value is calculated as follows:


$$WAIC(y,\theta) = -2\left(lppd-\sum_i Var_\theta \log p(y_i|\theta)\right)$$

where $y$ are model predicted responses, $\theta$ are the model parameters, $s$ are the samples of the posterior distribution, $i$ is the observed data, and $lppd$ is the log pointwise posterior predicitve density:  

$$lppd(y,\theta)=\sum_i \log \frac{1}{S} \sum_s p(y_i|\theta_s)$$ 

The $\sum_i Var_\theta \log p(y_i|\theta)$ term is a correction for the effective number of parameters to adjust for overfitting ([Gelman, 2013](https://hero.epa.gov/reference/13243402)). As for the AIC, smaller values of the WAIC indicate better fit. For LOUD Bayesian model averaging, the WAIC is used for model weights, where the individual model weight is computed by normalizing the inverse of the WAIC for that model:

$$w_k=\frac{exp(-\frac{1}{2}WAIC_k)}{\sum^K_{k=1}exp(-\frac{1}{2}WAIC_k)}$$

#### P-value

The goodness-of-fit p-value for MLE models is computed based on the degrees of freedom and the Chi-square, $\chi^{2}$, value. The $\chi^{2}$ value is assumed to be distributed as a Chi-square distribution having degrees of freedom equal to the number of dose groups minus the number of model parameters estimated off a boundary.

The p-value measures the "closeness" of the model predictions to the observed data. If the overall p-value is larger than some predetermined critical p-value, then the user might infer that the model appropriately describes the observed dose-response pattern. The critical p-value used by EPA is generally 0.1 but is sometimes relaxed to 0.05 for the Multistage model when it is applied to cancer data ([U.S. EPA, 2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

For LOUD continuous and dichotomous models, the p-value is calculated based on comparing the values of pivotal discrepancy measures, computed from the output of the MCMC sampling, to known reference distributions ([Yuan and Johnson, 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3276744/)).  In general, $p < 0.05$ is strong evidence of model inadequacy, $0.05 < p < 0.25$ is some evidence of model inadequacy, and $p > 0.25$ indicates no evidence of model inadequcy. The individual model p-values are less important for LOUD model averaging as poorly fitting models receive proportionally lower posterior model weights; in the model averaging framework, individual model p-values can be checked to ensure that at least one individual model provides adequate fit to the observed data.

### Model Parameters Table (All Endpoints)

```{figure} _static/img/model_parameters_table_MLE.png
:alt: Popup help panel text displayed for Exponential 3 model
:scale: 75%
:name: f61

Model Parameters table for MLE Exponential 3 model, with popup description of bounded variable.
```

For MLE models, the **Model Parameters** table includes the estimates for the parameter values that "optimize" the model fit.  Parameter estimates are checked to see if they fall within a given tolerance ($1.0e^{-6}$) of parameter boundaries. If so, they are marked as *On Bound*. This tolerance value applies to all parameters. There are no hard boundaries for parameters for LOUD models.

### Cumulative Distribution Function (CDF) Table (All Data Types)

CDF stands for *cumulative distribution function*, in this case for the BMD estimate. The CDF table lists the percentiles associated with the CDF for the BMD being estimated ({numref}`f59`).

Note that the BMD value associated with the CDF value of 0.5 is the MLE of the BMD (and matches the value reported for the BMD in the Summary table discussed above).

The CDF table may also correspond to the Summary table in terms of the BMDL and BMDU values reported in the latter. Recall that the confidence level specified by the user in the options is a one-sided confidence level. Therefore, if that confidence level is related to one of the cumulative percentiles in the CDF block, the BMD values will match.

As an example, if the confidence level specified by the user is 0.95 (95% one-sided confidence limits requested), then the BMDU from the
Benchmark Dose table will match the BMD value listed for 0.95 in the CDF table. Similarly, the BMDL will match the BMD value listed for 0.05 in the CDF table.

```{figure} _static/img/BMD_CDF_plot.png
:alt: CDF table with accompanying graph
:scale: 65%
:name: f62

CDF table and graph.
```
:::{important}
**Why is BMDS reporting different cumulative distribution function values for different confidence levels?**<br>
BMDS may report different CDF percentile values when different user-specified confidence levels (alphas) are chosen. **These differences are not a bug in BMDS**. Rather, these CDF ranges — and any differences in CDFs based on different confidence levels — are calculated by the underlying Gnu Scientific Library's methods, not by BMDS. Differences in CDFs should not affect repeatability or reliability of results. However, users should use discretion when comparing CDF values to BMDL/BMDU values calculated from different confidence levels. For example, if a user inputs a 90% confidence level (alpha = 0.1), the BMDU is not guaranteed to match the 90% percentile from the CDF when using a 95% confidence level (alpha = 0.5).
:::

### Graphs/Plots (All Endpoints)

Graphical outputs (plots) are displayed on both the Output tab and on the individual model result window.

```{figure} _static/img/individual_model_plot.png
:alt: Results plot for an individual model illustrating various plot components
:scale: 75%
:name: f63

Results plot for the Multistage 2 model.
```

The results plot shows the dose-response curve estimated by the model.

-   Data points are shown as blue dots with their individual group confidence intervals.

-   The horizontal bar is centered on the y-axis at the modeled BMR.

-   The diamond symbol inside the horizontal bar is the BMD.

-   The horizontal bar's left edge is the BMDL, and the right is the BMDU.

Error bar calculations for the data points differ slightly based on the endpoint (see details in the subsections linked below):

-   [**For continuous endpoints**](./continuous-mle.md#plot-and-error-bar-calculation).

-   [**For dichotomous endpoints**](./dichotomous-mle.md#plot-and-error-bar-calculation).

-   [**For nested endpoints**](./nested-dichotomous.md#plot-and-error-bar-calculation).

