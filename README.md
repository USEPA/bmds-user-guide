# BMDS User Guide

TODO ...

## Installation

Requires [uv](https://docs.astral.sh/uv/) on your command line.

```bash
cd dev/
git clone https://github.com/USEPA/bmds-user-guide.git
cd bmds-user-guide/
uv venv --python=3.12
# on windows:
.venv\Scripts\activate
# on mac:
# .venv/bin/activate
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

### Converting the docx file:

The docx file was converted using the following command:

```batch
cd "C:\Users\ASHAPIRO\dev\bmds-user-guide"
"C:\Program Files\RStudio\resources\app\bin\quarto\bin\tools\pandoc.exe" guide.docx --extract-media=static -o guide.md
```

## Disclaimer

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use.  EPA has relinquished control of the information and no longer has responsibility to protect the integrity, confidentiality, or availability of the information.  Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA.  The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
