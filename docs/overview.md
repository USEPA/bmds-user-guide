# Overview

The U.S. Environmental Protection Agency (EPA) Benchmark Dose Software
(BMDS) was developed as a tool to facilitate the application of
benchmark dose (BMD) methods to EPA hazardous pollutant risk
assessments.

This user guide provides instruction on how to use BMDS but is not
intended to address or replace EPA BMD guidance. However, every attempt
has been made to make this software consistent with EPA guidance,
including the Risk Assessment Forum's (RAF) [Benchmark Dose Technical
Guidance
Document](https://www.epa.gov/risk/benchmark-dose-technical-guidance).
([U.S. EPA,
2012](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=1239433)).

## BMDS for Dose-Response Modeling

BMDS facilitates dose-response modeling. BMDS models are currently
accessible primarily via an online browser-based web application.

### Dose-Response Modeling

Dose-response modeling is a technique, often used in toxicology and risk
assessment, for quantitatively relating exposure (the dose) to a
biological outcome (the response). It may be thought of as an elaborate
form of regression, which is the statistical technique used to explore
or represent the relationship(s) between two (or more) variables.

In the dose-response context, the dose term (*e.g.*, mg of chemical per
kg body weight per day) is most often viewed as the "cause" of the
response (*e.g.*, presence of a tumor or other manifestation of disease
or a measure of the weight of some organ that might be susceptible to
the toxic effects of the exposure).

[]{#_Toc185445177 .anchor}**Figure 1.** The dose-response relationship:
A benchmark dose (BMD) is the dose amount estimated to produce a
response (BMR) of a specific magnitude in the test subject. The BMD's
lower confidence limit (BMDL) is a dose where the observable physical
effect is less than the predetermined BMR.

![Sample graph showing the predetermined BMR line, and its intersection
with the BMDL and
BMD](_static/img/image7.jpeg){width="4.775807086614173in"
height="2.298611111111111in"}



---

EXAMPLE


```{figure} _static/img/image7.jpeg
:alt: Sample graph showing the predetermined BMR line, and its intersection with the BMDL and BMD
:name: z1

The dose-response relationship:
A benchmark dose (BMD) is the dose amount estimated to produce a
response (BMR) of a specific magnitude in the test subject. The BMD's
lower confidence limit (BMDL) is a dose where the observable physical
effect is less than the predetermined BMR.

```

```{figure} _static/img/image7.jpeg
:alt: Sample graph showing the predetermined BMR line, and its intersection with the BMDL and BMD
:name: z2

The dose-response relationship:
A benchmark dose (BMD) is the dose amount estimated to produce a
response (BMR) of a specific magnitude in the test subject. The BMD's
lower confidence limit (BMDL) is a dose where the observable physical
effect is less than the predetermined BMR.

```


```{figure} _static/img/image7.jpeg
:alt: Sample graph showing the predetermined BMR line, and its intersection with the BMDL and BMD
:name: z3

The dose-response relationship:
A benchmark dose (BMD) is the dose amount estimated to produce a
response (BMR) of a specific magnitude in the test subject. The BMD's
lower confidence limit (BMDL) is a dose where the observable physical
effect is less than the predetermined BMR.
```

* Link to [Figure 1.](#z1)
* Link to [Figure 2.](#z2)
* Link to [Figure 3.](#z3)

---


EPA's Benchmark Dose Software (BMDS) provides easy access to numerous
dose-response models that help risk assessors estimate the quantitative
relationship between a chemical ***dose*** and the test
subject's ***response***. The user can select from and/or compare the
models to make predictions about the quantitative relationship between
dose and response. One specific focus of this software is the estimation
of a statistical benchmark dose (BMD), including bounds (*e.g.*, 95%
confidence intervals) on such estimates.

The BMD is a dose estimated to produce a response level of a defined
(benchmark) magnitude. The [online BMDS
Glossary](https://sor.epa.gov/sor_internet/registry/termreg/searchandretrieve/glossariesandkeywordlists/search.do?details=&vocabName=BMDS%20Glossary&uid=1821254&taxonomyName=BMDS%20Glossaryhttp://ofmpub.epa.gov/sor_internet/registry/termreg/searchandretrieve/glossariesandkeywordlists/search.do?details=&vocabName=BMDS%20Glossary&uid=1821254&taxonomyName=BMDS%20Glossary)
defines BMD as follows:

*An exposure due to a dose of a substance associated with a specified
low incidence of risk, generally in the range of 1% to 10%, of a health
effect; or the dose associated with a specified measure or change of a
biological effect.*

The BMD is a range, rather than a fixed number. For example, the
benchmark dose lower confidence limit (BMDL) can be regarded as a dose
where the observable physical effect is *less* than the predetermined
benchmark response (BMR).

### Types of Responses Modeled

Another key aspect of dose-response modeling is that the models,
statistical assumptions, and techniques that it uses depend on the type
of response under consideration.

For BMDS, as reflected many times over in this user guide, the
distinctions that are made (*i.e.*, for which separate and distinct
modeling approaches are applied) can be categorized with respect to the
following three types of response: continuous endpoints, dichotomous
endpoints, and nested dichotomous endpoints. (Nested continuous
endpoints will be added to a future release.)

The key features of those response (endpoint) types are as follows:

-   **Continuous Endpoint**: the response is measured on a continuous
    scale, so its valid values are real numbers (often restricted to
    positive values, but not always). Organ weight, body weight,
    concentration levels of biological markers --- these are all
    examples of continuous endpoints whose values might be affected by
    exposure to the compound under consideration.

-   **Dichotomous Endpoint**: the response here is the presence or
    absence of a disease state or other "counter" of system malfunction.
    In this case, each experimental unit will either have the response
    or not. Dichotomous dose-response models predict the proportion of
    such units that have the response. Tumor responses are a subcategory
    of dichotomous endpoints with cancer-specific model selection
    considerations that are automated in the BMDS Multitumor model; for
    more information, see Section 11.0, "Multiple Tumor Analysis," on
    page [94](#multiple-tumor-analysis).

-   **Nested Dichotomous Endpoint:** as for Dichotomous endpoints, the
    presence or absence of a disease state or counter is the response.
    However, in this case each experimental unit may have more than one
    such count (*i.e.*, the counts are nested within an experimental
    unit). The most common example of such an endpoint is with
    developmental toxicity experiments in which the experimental unit is
    the pregnant dam and the fetuses or offspring from each dam's litter
    are examined for the presence or absence of an effect (*e.g.*,
    malformation).

Collectively, the application of the methods for fitting mathematical
models to data is referred to as BMD modeling or the BMD approach. BMDS
facilitates these operations by providing simple data-management tools
and an easy-to-use interface to run multiple models on one or more
dose-response datasets.

### Presentation of Model Results

BMDS presents model results in text and graphic outputs that can be
printed or saved and incorporated into other documents. Results from all
models include:

-   Model-run options chosen by the user

-   Goodness-of-fit information

-   BMD

-   Estimates of the bounds (*e.g.*, confidence limits) on the BMD
    (notated BMDL and BMDU for the lower bound and upper bound,
    respectively)

[]{#_Toc185445178 .anchor}**Figure 2.** BMDS results for a dichotomous
endpoint, presented using graph and tables.

![Cursor hovers over Log-logistic row, with corresponding plot
displayed](_static/img/image8.png){width="6.476848206474191in"
height="2.2419870953630796in"}

## How EPA Uses BMD Methods

EPA uses BMD methods to derive reference doses estimates (such as
reference doses (RfDs), reference concentrations (RfCs), and slope
factors,[^1] which are used along with other scientific information to
set standards for human health effects.

[^1]: With few exceptions, RfD/RfC values are noncancer benchmarks and slope factors are generally cancer benchmarks derived in accordance with [EPA cancer guidelines](https://www.epa.gov/sites/production/files/2013-09/documents/cancer_guidelines_final_3-25-05.pdf).

Prior to the availability of tools such as BMDS, noncancer risk
assessment benchmarks such as RfDs and RfCs were determined from
no-observed-adverse-effect levels (NOAELs), which represent the highest
experimental dose for which no statistically or biologically significant
increase in an adverse health effect has been documented.

However, using the NOAEL in determining RfDs and RfCs has long been
recognized as having limitations:

-   It is limited to one of the doses in the study and is dependent on
    study design.

-   It does not account for variability in the estimate of the
    dose-response.

-   It does not account for the slope of the dose-response curve.

-   It cannot be applied when there is no NOAEL, except through the
    application of an uncertainty factor ([Kimmel and Gaylor,
    1988](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=4250);
    [Crump,
    1984](https://hero.epa.gov/hero/index.cfm?action=search.view&reference_id=66651)).

*A goal of the BMD approach is to define a starting point of departure
(POD) for the computation of a reference value (RfD or RfC) or slope
factor that is more independent of study design.* The EPA Risk
Assessment Forum has published [technical
guidance](https://www.epa.gov/risk/benchmark-dose-technical-guidance)
for the application of the BMD approach in cancer and non-cancer
dose-response assessments ([U.S. EPA,
2012](https://www.epa.gov/risk/benchmark-dose-technical-guidance?action=search.view&reference_id=1239433)).

## BMDS Development History

Research into model development for BMDS started in 1995 and the first
BMDS prototype was internally reviewed by EPA in 1997. After external
and public reviews in 1998-1999, and extensive Quality Assurance testing
in 1999-2000, the first public version of BMDS, version 1.2, was
released in April 2000. Since that time, BMDS has been transformed from
a standalone Windows application to an Excel-based application in 2018,
and then to a browser-based web application in 2022.

The 2018 release of BMDS 3.0 included Bayesian versions of all
maximum-likelihood estimation (MLE) dichotomous models, and Bayesian
model averaging using all or weighted dichotomous models.

The [BMDS application
history](https://www.epa.gov/bmds/about-benchmark-dose-tools#history) is
documented on the BMDS website.

## What's New: BMDS Online is EPA's Primary Dose-Response Modeling Platform

[BMDS Online](https://bmdsonline.epa.gov/) is the U.S. EPA's primary
application for benchmark dose-response modeling.

BMDS Online leverages aspects of the familiar BMDS 3.x Excel interface
yet delivers faster performance and enables greater accessibility for
users. Now, instead of downloading and installing an Excel macro-based
application, users only need an internet connection to run a BMD
analysis.

There is also the added flexibility of offline processing with the
simultaneous releases of BMDS Desktop and pybmds. For more information
on these programs, refer to "BMDS Desktop and pybmds" on page
[7](./bmds-desktop-pybmds.md).

Learn more about BMDS Online on the [BMDS
website](https://www.epa.gov/bmds).

### Privacy is Respected

The BMDS Online application does not track personal information about
users of the software.

### Results Saved for Three Years

BMDS Online will save datasets and analyses for three years; users can
rerun or delete the analyses at any time, and they can optionally
"renew" an analysis to continue saving for another three years.

If data sensitivity is an issue, BMDS Desktop or pybmds should be used
for offline analysis.

## What's New: Work Offline with BMDS Desktop and pybmds

The 2024 BMDS Online upgrade includes the release of two new
applications:

-   **BMDS Desktop** is a Python-based version of BMDS Online that runs
    offline in a web browser and replaces the Excel-based BMDS 3.3. It
    is intended for users with increased data privacy or sensitivity
    concerns that prevent them from being able to run BMD analyses on
    EPA infrastructure.

-   **pybmds** enables users to run dose-response analyses in a
    scripting environment, along with running high-throughput or batch
    analyses of thousands of individual datasets. pybmds is a
    command-line application and is intended for the advanced user with
    some development experience.

For more information, refer to Section 2.0, "BMDS Desktop and pybmds,"
on page [7](./bmds-desktop-pybmds.md).

## What's New: Active Development Stopped on BMDS 3.3

Active development has stopped on the Excel-based BMDS 3.3 application,
which was first introduced in 2018. While the Excel framework for the
application was modern and familiar to users at the time, several issues
hampered innovation and maintenance:

-   Excel incompatibilities across different versions of Microsoft
    Office

-   Limitations to the design of the user interface both functionally
    and aesthetically

-   Slow performance when writing to Excel workbooks and Word reports

-   Limitations in Excel's Visual Basic for Applications (VBA)
    programming language hindered BMDS development and complicated its
    maintenance

-   BMDS Excel's macro-based nature occasionally triggered workplace
    security restrictions that stalled or prevented uptake of BMDS
    within some organizations

BMDS Online is now the primary application where new development and
innovation will occur. BMDS Online also offers an easier introduction to
BMD analysis for new users.

BMDS 3.3 will remain
[downloadable](https://www.epa.gov/bmds/download-bmds/) but will receive
no further updates.

## What's New: Key Improvements and Enhancements

All improvements and enhancements listed below are available in BMDS
Online, BMDS Desktop, and pybmds:

-   Addition of Multistage Cancer/Multitumor model, along with a [poly-k
    trend test](./multiple-tumor-analysis.md#poly-k-adjustment)

-   Addition of the Nested Logistic nested dichotomous model for
    developmental toxicity data

-   Enhancements and under-the-hood fixes to improve efficiency, error
    handling, and stability for future development

For a complete list of what's new or changed in the current release,
refer to the BMDS website's [Release History
page](https://www.epa.gov/bmds/bmds-online-release-history).

## BMDS Resources

### BMDS Website

The [BMDS website](https://www.epa.gov/bmds) contains the most
up-to-date information and updates pertaining to BMDS.

In addition to the latest downloadable version of BMDS, the site
includes links to [troubleshooting and usage
tips](https://www.epa.gov/node/277054), [BMDS Online Release
History](https://www.epa.gov/bmds/bmds-online-release-history), links to
technical guidance, links to [external and peer-review
information](https://www.epa.gov/node/266953#eapr) on models used in
BMDS, and opportunities to participate in the development of the next
generation of BMDS models.

### BMDS Mailing List

The BMDS mailing list is the best way to stay current with software
development, training opportunities, and other information relevant to
your work with BMDS.

The BMDS mailing list is low traffic; members receive about 2-4
announcements per year.

To join the mailing list, please [sign up on the BMDS
website](https://www.epa.gov/bmds/how-subscribe-bmds-bulletin-email-list).

### BMDS Glossary

For definitions of terms used in this guide, please refer to the [online
BMDS
Glossary](https://sor.epa.gov/sor_internet/registry/termreg/searchandretrieve/glossariesandkeywordlists/search.do?details=&vocabName=BMDS%20Glossary&uid=1821254&taxonomyName=BMDS%20Glossaryhttp://ofmpub.epa.gov/sor_internet/registry/termreg/searchandretrieve/glossariesandkeywordlists/search.do?details=&vocabName=BMDS%20Glossary&uid=1821254&taxonomyName=BMDS%20Glossary).
The glossary items can be exported to other formats, such as PDF or
Excel.

Another good source of dose-response terminology is the [Integrated Risk
Information System (IRIS)
Glossary](https://sor.epa.gov/sor_internet/registry/termreg/searchandretrieve/glossariesandkeywordlists/search.do?details=&vocabName=IRIS%20Glossary).

### BMDS Source Code

The BMDS source code is available from the following GitHub sites:

-   pybmds and BMDS core code: <https://github.com/USEPA/bmds>

-   BMDS Desktop and BMDS Online: <https://github.com/USEPA/bmds-ui>

Python packages to install pybmds and BMDS Desktop are available from
the Python package inventory (pypi) at:

-   <https://pypi.org/project/pybmds/>

-   <https://pypi.org/project/bmds-ui/>

The documentation for BMDS Desktop and pybmds are at
<https://usepa.github.io/BMDS/>.

### BMDS Support

The [BMDS Contact Us
page](https://www.epa.gov/bmds/forms/contact-us-about-benchmark-dose-tools)
serves as the online Help Desk for all BMDS applications. Use the page
to post questions, concerns, comments, or suggestions on any aspect of
the software or its usage.

