# Project 1: SAT & ACT Analysis

## Problem Statement

The new format for the SAT was released in March 2016. As an employee of the College Board 
the organization that administers the SAT - you are a part of a team that tracks statewide
participation and recommends where money is best spent to improve SAT participation rates.
Your presentation and report should be geared toward non-technical executives with the College Board 
and you will use the provided data and outside research to make recommendations about how the College Board 
might work to increase the participation rate in a state of your choice.

## Executive Summary

### Contents:

- [2017 Data Import & Cleaning](#Data-Import-and-Cleaning)
- [2018 Data Import and Cleaning](#2018-Data-Import-and-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [Data Visualization](#Visualize-the-data)
- [Descriptive and Inferential Statistics](#Descriptive-and-Inferential-Statistics)
- [Outside Research](#Outside-Research)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)

## Data Dictionary

#### SAT 2017 data dictionary

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

