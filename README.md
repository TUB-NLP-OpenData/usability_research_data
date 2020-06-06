# Overview

Usability of Research Data

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/TUB-NLP-OpenData/usability_research_data/master.svg?label=unix)](https://travis-ci.org/TUB-NLP-OpenData/usability_research_data)
[![Windows Build Status](https://img.shields.io/appveyor/ci/TUB-NLP-OpenData/usability_research_data/master.svg?label=windows)](https://ci.appveyor.com/project/TUB-NLP-OpenData/usability_research_data)
[![Coverage Status](https://img.shields.io/coveralls/TUB-NLP-OpenData/usability_research_data/master.svg)](https://coveralls.io/r/TUB-NLP-OpenData/usability_research_data)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/TUB-NLP-OpenData/usability_research_data.svg)](https://scrutinizer-ci.com/g/TUB-NLP-OpenData/usability_research_data/?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/redu.svg)](https://pypi.org/project/redu)
[![PyPI License](https://img.shields.io/pypi/l/redu.svg)](https://pypi.org/project/redu)

# Problem
Deducing from experience as well as observation we can state the hypothesis that digital research in the scholarly field of the humanities appears to perform not as effective and in accordance to the possibility and potential of digital research. We identify usability as a key factor and shortcomings of usability as a major hindrance. 

# Usability
The term usability refers to the extent to which a product can be used by specified users to achieve specific goals with effectiveness, efficiency, and satisfaction in a specified context of use. The term usability also refers to methods for improving ease-of-use during the design process. For instance, ISO 9241-151:2008 provides guidance on the human-centred design of software Web user interfaces with the aim of increasing its usability.

# Goal
Create a connector that makes the bridge between data available on Research Data Repositories inside of a Data Science Tool (to be defined). This would avoid manual download and open up a few possibilities, e.g. preview of data, metadata exploration, data curation, etc. Moreover, translation of metadata (e.g. German->English) would be also a plus for the internationalization.



# Setup

## Requirements

* Python 1.8+

## Installation

Install it directly into an activated virtual environment:

```text
$ pip install redu
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add redu
```

# Usage

After installation, the package can imported:

```text
$ python
>>> import redu
>>> redu.__version__
```

