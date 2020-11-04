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
    * ### 4.1.1 bopi.search
      ```
      bopi.search(String | required, format = String | optional, tabular = Boolean | optional, translate_to = String | optional, max_e = Number | optional, detailed = Boolean | optional) 
      ```
    The search() method has 6 total parameters where the first parameter is required to find the data that the user is looking for and the other 5 parameters are optional such as format, tabular, translate_to, max_e,detailed. The table below will explain each parameter with its functionality:

    Parameter | Functionality
    ------------ | -------------
    "Required search string" (REQUIRED) | This first parameter must be filled with the String, e.g: “World”, “Food” or “Humidity”.
    format =  "csv" &#124; "json" &#124; "" (OPTIONAL) | This optional parameter can be filled with the required data type in String type, e.g: “csv” or “json”.
    tabular = True &#124; False (OPTIONAL)  | This optional parameter defines if the user is looking for tabular data or not by filling with boolean type True or False.
    translate_to = "en" &#124; "de" (OPTIONAL) | This optional parameter is using to translate the data. E.g: “en” for English and “de” for germans
    Max_e = number (OPTIONAL)  | This optional parameter will give the number of the output.
    detailed = True &#124; False (OPTIONAL)  |This optional parameter can be filled with True or False to give the user another form of the output in text. _Note: the default output is table dataframe_.
    
    * ### 4.1.2 Example of bopi.search()  
  
    To get a better explanation, some examples will be given below:
       ```
        from usability_research_data import bopi
        bopi.search("Temperature")    
       ```
       _**Output:**_ :

      _The example of input search only_

       ![image](https://drive.google.com/uc?export=view&id=1aIE2mwFE_wOxsEQNz9mnI-vPv_R1-zQS)   
       
       ---
       
       ```
        from usability_research_data import bopi
        bopi.search("Temperature",detailed = True)    
       ```
       _**Output:**_

       _The example by adding detailed = True as parameterr, so that we get another form of result._

       ![image](https://drive.google.com/uc?export=view&id=1w9d6VRX7m4OohHFetEyq_yFJOGgpK_kb)
       
       ---
       
       ```
        from usability_research_data import bopi
        bopi.search("Temperature",format = “csv”)   
       ```
       _**Output:**_

       _The example by adding format ="csv". so that the user can get repositories that only have csv dataset.

       ![image](https://drive.google.com/uc?export=view&id=1804W8twZ03csW7qtsZryeqaUvIi4K3Fq)
       
       ---
   
       ```diff
       - IMPORTANT: As you can see in the result, the output holds an important keys, which are “ID” and “Files” to be used later to read the data, preview, describe, and download the data.
       ```
       
       
       
       
       
  * ##  4.2 Feature to read the data, preview, describe, and download bopi.repository()
    After we get the result from our search, we want obviously to check the content of each title. It can be performed by using the main function which is  ***repository(“ID”)*** that has parameter ID that we get from the result of the search (See Important note above) in String data type.
    
    * ### 4.2.1. Listing and download all of the data
        However, The ***repository(“ID”)*** itself contains some 2 methods, which are _***datasets()***_ and  _***download()***_, where:
    _***datasets()***_  method will be used to list the files inside one title and _***download()***_ method is used to download the entire file in one title.
    
    _***<ins>bopi.repository("ID").datasets()</ins>***_
    
    ***EXAMPLES:***
    
    As the example we can take the output of the search above which is "temperature" and we are going to get the list of dataset inside of the data.
    
    ![image](https://drive.google.com/uc?export=view&id=1L0AMUI5cys09pBXneQWBupzodrFJklKb)
    
    From the ***ID*** column from the search result above, we can use the method .datasets() to list all the data inside that title.
    
    ```
    import bopi
    bopi.repository("11303/10989.2").datasets()
    ```    
    
     _**Output:**_
    
    The list of datasets inside 1 repository
    
    ![image](https://drive.google.com/uc?export=view&id=1SHV7c7yvw9LGpGImq5ZsrO8f89BEp_cb)
    
    ```diff
    - IMPORTANT NOTE: The list of the files above will be used late to fill the parameter inside the method get(“name of file”).
    ```
    
    ---
    
    _***<ins>bopi.repository("ID").download()</ins>***_
    
    The next is an example to download “all” data inside one repository:
    
    ```
    import bopi
    bopi.repository("11303/10989.2").download(“path”)
    ```    

    * ### 4.2.2. Preview, describe, and download certain data
         After we list the dataset through the method 
         
         ```
         bopi.repository("11303/10989.2").datasets()
         
         ```
         We can continue to preview, download, and profiling datasets, but to access the single datasets we need the String the name of the file that we need to input inside the parameter of _***.get(“name of the file”)***_ method. Of course, the name of the file must exact with the name that we see in the list above.
         
         _***<ins>bopi.repository("ID").datasets().get("name of file")</ins>***_
         
         Download the single dataset by using .get(“name of file”);
         ```
          import bopi
          bopi.repository("11303/10989.2").datasets().get(‘Xb.csv’)
         ```
         
         ---
         
         _***<ins>bopi.repository("ID").datasets().get("name of file").preview(tail = True | random = True)</ins>***_
         
         Preview the single dataset by using _***.get(“name of file”).preview()***_.The user has no parameter means that the dataset will be previewed from the top of the file, otherwise, the user can fill the parameter with parameter tail = True to preview the file from the bottom of random = True to let get the insight of random rows.  
         
         ```
          import bopi
          bopi.repository("11303/10989.2").datasets().get(‘Xb.csv’).preview()
         ```
         _**Output:**_
         
         To preview data rows of data from head of file and end of file:
         
         ![image](https://drive.google.com/uc?export=view&id=1mxtr-3fD0w2hzZRft7ZGIh_srvPZdCB4)
         
         ---
         
         _***<ins>bopi.repository("ID").datasets().get("name of file").describe()</ins>***_
         
         Profiling the single dataset _***.get(“name of file”).describe()***_:
         
         ```
          import bopi
          bopi.repository("11303/10989.2").datasets().get(‘Xb.csv’).describe()
         ```
         _**Output:**_
         
         To profile data rows of data from one file:
         
         ![image](https://drive.google.com/uc?export=view&id=13U_bF0k3WZrEf8HuVLcIB8enRCtEMqtI)
         
         ![image](https://drive.google.com/uc?export=view&id=1GOR1kzzimKaz48Yap3lv_l2NHY2muYc8)
         
         ---
         
         
    * ### 4.2.3. Another feature to transform the data
    Another feature that can help the user to transform the data to csv or json type by adding method to_csv() or to_json() behind .get() method and can store the value in a variable.
    
    ```
    import bopi
    bopi.repository("11303/10989.2").datasets().get(‘Xb.csv’).to_json()
    bopi.repository("11303/10989.2").datasets().get(‘Xb.csv’).to_csv()
    ```
    
    ---
    
     * ### 4.2.4. Video and structure of function.
     
     ![image](https://drive.google.com/uc?export=view&id=1PjPOL2AyIO-nUwxdFMtPC64_wlkOqEHm)
     
     
     ---
     
     
     # VIDEO
      [VIDEO EXAMPLE](https://youtu.be/m8__tHsJopE)
   
