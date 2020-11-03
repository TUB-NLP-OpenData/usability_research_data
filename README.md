# Overview

Usability of Research Data

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [jacebrowning/template-python](https://github.com/jacebrowning/template-python).

[![Unix Build Status](https://img.shields.io/travis/TUB-NLP-OpenData/usability_research_data/master.svg?label=unix)](https://travis-ci.org/TUB-NLP-OpenData/usability_research_data)
[![Windows Build Status](https://img.shields.io/appveyor/ci/TUB-NLP-OpenData/usability_research_data/master.svg?label=windows)](https://ci.appveyor.com/project/TUB-NLP-OpenData/usability_research_data)
[![Coverage Status](https://img.shields.io/coveralls/TUB-NLP-OpenData/usability_research_data/master.svg)](https://coveralls.io/r/TUB-NLP-OpenData/usability_research_data)
[![Scrutinizer Code Quality](https://img.shields.io/scrutinizer/g/TUB-NLP-OpenData/usability_research_data.svg)](https://scrutinizer-ci.com/g/TUB-NLP-OpenData/usability_research_data/?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/redu.svg)](https://pypi.org/project/redu)
[![PyPI License](https://img.shields.io/pypi/l/redu.svg)](https://pypi.org/project/redu)

# 1. Problem
Deducing from experience as well as observation we can state the hypothesis that digital research in the scholarly field of the humanities appears to perform not as effective and in accordance to the possibility and potential of digital research. We identify usability as a key factor and shortcomings of usability as a major hindrance. 

## Usability
The term usability refers to the extent to which a product can be used by specified users to achieve specific goals with effectiveness, efficiency, and satisfaction in a specified context of use. The term usability also refers to methods for improving ease-of-use during the design process. For instance, ISO 9241-151:2008 provides guidance on the human-centred design of software Web user interfaces with the aim of increasing its usability.

# 2. Goal
Create a connector that makes the bridge between data available on Research Data Repositories inside of a Data Science Tool (to be defined). This would avoid manual download and open up a few possibilities, e.g. preview of data, metadata exploration, data curation, etc. Moreover, translation of metadata (e.g. German->English) would be also a plus for the internationalization.

This documentation aims to help the user of our tool to get an understanding
of using the syntax of BOPi by using a short explanation and example step by
step.



# 3. Getting Started

## 3.1 Prerequisites

  ### Python 3
  Python 3 should be installed in your System.

## 3.2 Clone package from Git
    !git clone https://github.com/TUB-NLP-OpenData/usability_research_data
    
## 3.3 Install dependencies
    !pip install git+https://github.com/TUB-NLP-OpenData/usability_research_data 
**(restart the runtime after installation)*

## 3.4 Referencing to the parent of the current working directory
    import sys
    sys.path.append('/content/usability_research_data')

## 3.5 Import-Package
    from usability_research_data import bopi




# 4. Syntax Usage

Below is the explanation to search the data in DSpace repository and features to help
the researcher to read, preview, describe, and download the data that consists of 2
parts 4.1. And 4.2.
  
 
  * ##  4.1 Searching the data in the repository
    * ### 4.1.1 bopi.search(String | required, format = String | optional, tabular = Boolean | optional, translate_to = String | optional, max_e = Number |      optional,             detailed = Boolean | optional)
    
The search() method has 6 total parameters where the first parameter is required to find the data that the user is looking for and the other 5 parameters are optional such as format, tabular, translate_to, max_e,detailed. The table below will explain each parameter with its functionality:
  
Parameter | Functionality
------------ | -------------
"Required search string" | This first parameter must be filled with the String, e.g: “World”, “Food” or “Humidity”.
format =  "csv" &#124; "json" &#124; ""  | This optional parameter can be filled with the required data type in String type, e.g: “csv” or “json”.
tabular &#124; optional  | This optional parameter defines if the user is looking for tabular data or not by filling with boolean type True or False.
translate_to &#124; optional | This optional parameter is using to translate the data. E.g: “en” for English and “de” for germans
Max_e &#124; optional  | This optional parameter will give the number of the output.
detailed &#124; optional  |This optional parameter can be filled with True or False to give the user another form of the output in text. _Note: the default output is table dataframe_.



