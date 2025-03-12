# Rao-Scott Transformation for Modeling Summary Dichotomous Developmental Data

The Rao-Scott transformation is an approach, described in [Fox et al., 2017](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/3392386), to model dichotomous developmental data when only summary level dose-response data is available.  The transformation works by scaling dose-level incidence and sample size data by a variable called the design effect in order to approximate the intralitter correlation that occurs due to the clustered study design of developmental toxicity studies.

For dose-response analyses of dichotomous developmental toxicity studies, the proper approach is to model individual animal data (i.e., litter data for individual dams) in order to account for the tendency of pups from one litter to respond more alike one another than pups from other litters.  This behavior is commonly termed the *litter effect* or *intralitter correlation*. However, it is frequently the case that dose-response modelers will be modeling data reported in the peer-reviewed literature and it is rarely the case that individual litter data is reported in peer-reviewed articles or provided as supplemental materials.  Instead, peer-reviewed articles typically report the dose-level summary data: the total number of fetuses and the number of fetuses responding to treatment per dose group, irrespective of litter membership. 

:::{note}
If individual-level developmental toxicity data are available for modeling, see [Nested Dichotomous Endpoints](./nested-dichotomous.md#nested-dichotomous-endpoints) for details on the usage of the nested dichotomous models available in BMDS Online.
::: 

As reported in [Fox et al., 2017](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/3392386), multiple statistical studies have researched the concept of the design effect, $D$, as a strategy to reduce overdispersion arising from clustered study design via a simple dose-response transformation. The core concept is that correlated data can be transformed via scaling and then modeled with standard dichotomous models as if they were not correlated.  

In order to apply the Rao-Scott transformation, both the numerator and denominator of a dose-level proportion are divided by $D$.  This results in what can be described as the *effective* sample size $\left({N_{f}}_{RS} = \frac{N_{f}}{D}\right)$ and the *effective* affected fetuses $\left({A_{f}}_{RS} = \frac{A_{f}}{D}\right)$. 

In order to provide BMDS users an approach to approximate $D$ for summary data, [Fox et al., 2017](https://hero.epa.gov/hero/index.cfm/reference/details/reference_id/3392386) conducted an analysis of 55 developmental toxicity studies for which individual level data were available and used the regression equation $\ln(D) = a + b \times\ln(P_{f})$ to establish the relationship between $D$ and $P_{f}$ for studies that used either rats, mice, or rabbits as their test species.  This analysis used both least-squres and orthogonal regression.  The table below reports the species-specific regression coefficients for the established relationship between $D$ and $P_{f}$.

```{csv-table} Linear Least Squares (LS) and Orthogonal Regression (OR) Estimates by Species
:header: > 
: "Species", "Method", "$n$, Studies", "$n$, Dose Groups", "$a$", "$b$", "$\sigma_{res}^{2}$"
:widths: 10 10 10 10 10 10 10

"Mice", "LS", "21", "88", "1.5938", "0.2866", "0.2078"
"Mice", "OR", "21", "88", "1.6943", "0.3132", "0.1863"
"Rats", "LS", "25", "101", "1.6852", "0.3310", "0.1248"
"Rats", "OR", "25", "101", "1.8327", "0.3690", "0.1090"
"Rabbits", "LS", "10", "43", "1.0582", "0.2397", "0.1452"
"Rabbits", "OR", "10", "43", "1.1477", "0.2739", "0.1299"
```

From these regression coefficients, the design effect can be calculated as $D = e^{\left\lbrack a + b \times \ln(P_{f})+0.5\sigma_{res}^{2} \right\rbrack}$. Given there is no strong methodological preference using the design effect calculated using linear least squares regression ($D_{LS}$) vs the design effect calculated using orthogonal regression ($D_{OR}$), by practice the design effect estimated using these two regression approaches is averaged to generate the average design effect ($D_{average}$) actually used in the scaling of $N_{f}$ and $A_{f}$. 

For modeling the transformed data in BMDS, scaled ${N_{f}}_{RS}$ and ${A_{f}}_{RS}$ values would be entered as the modeling inputs. 

The ultimate consequence of the Rao-Scott transformation will be the estimation of wider confidence intervals for the BMD, and thus lower BMDLs. This is the consequence of the transformation that is most important as the lower BMDLs of the Rao-Scott transformed fetal incidence data approximate the BMDLs that would be estimated had individual-level data been modeled with a nested dichotomous model.  

## The inputs for this tool are:

The dataset used for the Rao-Scott transformation should have the same structure as regular dichotomous data and should have the following columns in this sequence:

1. **Dose** - the numeric value of the dose group

2. **N** - the numeric value for the number of fetuses (irrespective of litter membership) per dose group

3. **Incidence** - the numeric value for the number of affected fetuses (irrespective of litter membership) per dose group

Additionally, users will need to select the species that corresponds to their dose-response data; currently options for species are limited to rat, mouse, and rabbit.

## The outputs from this tool are:

1. A summary table of the original and adjusted data 

2. Plots of the original and adjusted values for both the total number of fetuses and number of affected fetuses per dose group

The **Copy Data for BMDS Modeling** link copies the summary table data to the clipboard.  From there, the user can return to their Dichotomous analysis, return to the data tab, select the **Load dataset from Excel**
button, and paste the clipboard contents to create a new dataset. 

## References