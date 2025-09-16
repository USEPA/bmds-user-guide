# BMDS User Guide

[![Docs Badge](https://img.shields.io/badge/Latest-online-brightgreen)](https://usepa.github.io/bmds-user-guide)
![GitHub Commit Activity](https://img.shields.io/github/commit-activity/y/USEPA/bmds-user-guide)

Benchmark Dose Modeling Software (BMDS) User Guide. The User Guide is available online at https://usepa.github.io/bmds-user-guide. For edits or recommendations, please submit GitHub issues or GitHub pull-requests in this repository.

## Installation

The guide is written using [Sphinx](https://www.sphinx-doc.org/en/master/) and is compiled into a static website. To develop and edit locally, use [uv](https://docs.astral.sh/uv/) for Python environment management.

```bash
# clone the repository and change directories to the repo root
git clone https://github.com/USEPA/bmds-user-guide.git
cd bmds-user-guide/

# create a new python virtual environment
uv venv --python=3.13

# activate the environment
# on windows:
.venv\Scripts\activate
# on mac:
# .venv/bin/activate

# install python dependencies
uv pip install -e .
```

Then, build the docs:

```bash
poe docs
```

To build and edit the docs in real-time:

```bash
poe docs-serve
```

The documentation is deployed automatically whenever a commit is pushed to the `main` branch of the GitHub repository.

## Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use.  EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information.  Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA.  The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
