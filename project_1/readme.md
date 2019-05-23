# Project 1: SAT & ACT Analysis
Syamil M.

## Problem Statement

In 2016, the College Board released a new SAT format to reflect changing trends in college education and to better prepare students for college [<sup>1</sup>](#fn1). While test preferences differ from state to state, SAT participation rates in 2018 saw a 25% increase from 2017 with 2018 having the largest number of SAT test takers since the inception of the SAT [<sup>2</sup>](#fn2). 

At the same time, the colleges throughout America are dropping standardised tests such as the ACT and SAT in favour of more streamlined admissions assessment policies [<sup>3<sup>](#fn4). Clearly, this poses a challenge for the future of standardised testing in which the SAT has an intrinsic stake. 


## Executive Summary

In light of this challenge, aggregated data from the 2017 and 2018 cohort for the SAT and ACT assessments across the 51 United States Districts have been used in this report to better understand key trends in participation rates as well as provide new ways to look into further improving SAT participation rates. From the analysis, lowering barriers towards participation via SAT School Days on top of enabling easy access to fee waivers had a clear impact in a number of states towards improving SAT participation. In some cases, we see a ten-fold increase in SAT participation for one particular state, Illinois, that made the SAT its state-wide college entrance exam.


### Contents:

- [2017 Data Import & Cleaning](#Data-Import-and-Cleaning)
- [2018 Data Import and Cleaning](#2018-Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Visualization](#Visualize-the-data)
- [Descriptive and Inferential Statistics](#Descriptive-and-Inferential-Statistics)
- [Outside Research](#Outside-Research)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)
- [References](#References)


## Data Dictionary

#### SAT/ACT 2017 data dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**State_sat2017 / State_act2017**|*object (category)*|SAT/ACT 2017|Name of US State| 
|**Participation_sat2017 / Participation_act2017**|*integer*|SAT/ACT 2017|Participation rate of students in percentages| 
|**Evidence-Based_Reading_and_Writing_sat2017**|*integer*|SAT 2017|Score for Evidenced Based Reading and Writing Component of SAT (maximum is 800)| 
|**Math_sat2017**|*integer*|SAT 2017|Score for Math Component of SAT (maximum is 800)| 
|**Total_sat2017**|*integer*|SAT 2017|Total Score computed as a sum of Evidence-Based Reading and Writing and Math (maximum is 1600)| 
|**English_act2017**|*float*|ACT 2017|Score for English Component (Scaled between 1 and 36)|
|**Math_act2017**|*float*|ACT 2017|Score for Math Component (Scaled between 1 and 36)|
|**Reading_act2017**|*float*|ACT 2017|Score for Reading Component (Scaled between 1 and 36)|
|**Science_act2017**|*float*|ACT 2017|Score for Science Component (Scaled between 1 and 36)|
|**Composite_act2017**|*float*|ACT 2017|Average Score of English/Math/Reading/Science Components (Scaled between 1 and 36)|


## References


