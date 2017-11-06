# Comments on Charlie's Citibike Project

## 1. Null and Alternative Hypothesis
- Null and Alternative Hypothesis both stated
- Confidence level of 0.05 is stated. I would suggest this be replaced with a significance level of 0.05 instead, with a corresponding confidence level of 95%
- The idea of the project is interesting, but the hypothesis limits the scope of the study to only midnight. It may be more valuable to study the ridership for male and female comparing between day and night. 
- Suggested H0: the ratio of female night riders over total female riders is more than or equal to the ratio of male night riders over total male riders. 
- Suggested H1: the ratio of female night riders over total female riders is less than the ratio of male night riders over total male riders

## 2. Data Features
- The data is wrangled and only relevant data is selected. 
- Intiial analysis in the histogram shows the frequency of male and female riders over time (per hour). While this shows the distribution of riders over the course of a day, the scope of the project hypothesis means that only a small fraction of the data will be used. 
- For the suggested hypothesis, an additional step is required to reassign the time to day and night (0 and 1s). 

## 3. Suggested Statistical Tests 
- Using the table from CSUN. Since the male and female variables are unpaired and categorical, the Chi Square test which measures the differences between groups should be used. 

# FBB good
