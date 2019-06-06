# Project 2 : Ames Housing Data and Kaggle Challenge

_Syamil M._


## Problem Statement

Given a set of information about a house, we want to be able to predict its expected price.

## Executive Summary



### Contents:

- [Data Cleaning](#Data-Import-and-Cleaning)
- [2018 Data Import and Cleaning](#2018-Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Visualization](#Visualize-the-data)
- [Descriptive and Inferential Statistics](#Descriptive-and-Inferential-Statistics)
- [Outside Research](#Outside-Research)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
- [References](#References)


## Data Dictionary

#### AMES data dictionary

Original Data Dictionary [here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**house_score**|*float*|modified_train/transformed_train|Name of US State| 
|**Participation_satYYYY / Participation_actYYYY**|*integer*|SAT/ACT 2017|Participation rate of students in percentages| 
|**Evidence-Based_Reading_and_Writing_satY**|*integer*|SAT 2017|Score for Evidenced Based Reading and Writing Component of SAT (maximum is 800)| 
|**Math_satYYYY**|*integer*|SAT 2017|Score for Math Component of SAT (maximum is 800)| 
|**Total_satYYYY**|*integer*|SAT 2017|Total Score computed as a sum of Evidence-Based Reading and Writing and Math (maximum is 1600)| 
|**English_actYYYY**|*float*|ACT 2017|Score for English Component (Scaled between 1 and 36)|
|**Math_actYYYY**|*float*|ACT 2017|Score for Math Component (Scaled between 1 and 36)|
|**Reading_actYYYY**|*float*|ACT 2017|Score for Reading Component (Scaled between 1 and 36)|
|**Science_actYYYY**|*float*|ACT 2017|Score for Science Component (Scaled between 1 and 36)|
|**Composite_actYYYY**|*float*|ACT 2017|Average Score of English/Math/Reading/Science Components (Scaled between 1 and 36)|

### Key Takeaways

<img src="./img/illinois.png" style="float: left; margin: 50px; height: 50px"/>

Lowering the barriers to accessibility for the SAT has shown a marked improvement in SAT participation rates for states that previously did not have it. The waiving of SAT fees is one such example of increasing participation. Furthermore coupled with SAT school days where tests are administered during curriculum time as part of schools' assessment schedules, participation also improved.

Intervention via enhancing PSAT (Preliminary SAT) participation for prospective test takers or reducing barriers to entry. Access to SAT training/practice tests before the graduating year can be largely discounted for students living in areas that live in ACT-dominant states. 

For example, if a student has taken a PSAT or discounted test within the last year of the SAT test date - their actual SAT test can be discounted as well. This has a twofold objective of firstly improving visibility of SAT as an option for high-schoolers looking for alternative college readiness tests and secondly reducing the uncertainty and stress that comes with taking a national-level test.

## References

