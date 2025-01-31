# Special Considerations

## Test for Combining Two Datasets for the Same Endpoint

BMDS does not include a formal test for similarity of dose response
across covariate values (*e.g.*, across class variables like species or
sex). [EPA's categorical regression software,
CatReg](https://www.epa.gov/bmds/about-catreg), has that capability.

However, the following procedure can be used in BMDS if there are
dose-response data for two experiments that the user is considering
combining (*e.g.*, for the two sexes within a species, or two species,
etc.).

1\. Choose a single model to consider for both datasets.

2\. Model the two datasets separately. For each run, record the
following:

-   Maximum log-likelihood for each dataset. Add the two log-likelihoods
    (one from each dataset) to get the ***summed*** log-likelihood.

-   The number of unconstrained parameters for each dataset. Add those
    numbers from each run to get the ***summed*** unconstrained
    parameters.

3\. Combine the data from the two experiments and model them together.
Record the following:

-   The maximum log-likelihood for the combined dataset. This will be
    the ***combined*** log-likelihood. The fitted model log-likelihoods
    are reported in the Analysis of Deviance (dichotomous endpoints) or
    Likelihoods of Interest (continuous endpoints) tables.

-   The number of unconstrained parameters for the combined dataset.
    This will be the ***combined*** unconstrained parameters.

4\. Subtract the combined log-likelihood from the summed log-likelihood.
Then, multiply the difference by 2.

5\. Compare the value from Step 4 to a Chi-square distribution. The
degrees of freedom for that Chi-square distribution will be the
difference between the summed unconstrained parameters (Step 2) and the
combined unconstrained parameters (Step 3).\
\
If the value from Step 4 is in the tail (say, greater than the 95th
percentile) of the Chi-square distribution in question, then reject the
null hypothesis that the two sets have the same dose-response
relationship. If rejection occurs, then infer that it is not proper to
combine the two datasets.
