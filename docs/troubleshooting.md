# Troubleshooting

## Gamma model fails with BMR = 0.05 extra risk

Occasionally, when modeling dichotomous data with a shallow dose-response and a BMR = 0.05 extra risk, the MLE Gamma model will fail to execute. In such cases, BMDS will not properly execute and no results for any model will be returned. This is due to a failure in the model optimization routines in the C++ gsl library.
  
```{figure} _static/img/gam_fail_dataset.png
:alt: Example of a shallow dose response relationship
:name: f128

Example of a shallow dose-response relationship.
```
When users observe that BMDS fails to complete and return results when modeling shallow dose-response relationships with a BMR = 0.05, they should do the following:

1. First, unselect the Gamma model and re-run the analysis. In most cases, BMDS will return results.

In this example, BMDS returns results and automatically recommends the Hill model as the best model based on lowest BMDL

```{figure} _static/img/gam_fail_table_no_gamma.png
:alt: Example of dichotomous modeling results when the Gamma model is excluded
:name: f129

Modeling results when Gamma model is excluded
```

2. Re-run the analysis including the Gamma model but now using a BMR = 0.05000001. This small offset to the BMR allows the model optimization for the Gamma model to complete.

```{figure} _static/img/gam_fail_bmr_0.05000001.png
:alt: Example of dichotomous modeling when Gamma model is included and a BMR = 0.0500001 is used
:name: f130

Modeling results when Gamma model is included and BMR = 0.05000001 is used
```
The results of the two analyses are practically identical (i.e., numerical modeling results identical to at least the third decimal place). If users decide using the results from Step 2 is appropriate, they should make a note in their modeling results that a BMR = 0.05000001 was used and the reason for that value.