# a. verify that their Null and alternative hypotheses are formulated correctly

Based on her idea that customers are less likely than subscribers to choose biking for commuting, Yu formulated her Null hypothesis incorrectly. Instead of "the ratio of Subscriber biking on weekends over Subscriber biking on weekdays" being "the same or higher than the ratio of Customer biking over weekends to Customer biking on weekdays", her Null Hypothesis should have stated that the Subscriber ratio is the same or lower than that of the Customer ratio.

# b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

The data was has the appropriate features to answer the question user type and date) but the data wasn't properly pre-processed to extract the needed values. Her null hypothesis describes a ratio of users biking on weekends to weekdays, but I am not seeing any such transformation in her notebook.

# c. chose an appropriate test to test H0 given the type of data, and the question asked.

This is a test of proprotions. Since we are dealing with categorical data (weekends vs. weekdays). If we were dealing with numerical data, it would be important to decide if they follow the parameters of the normal distribution curve (Gaussian curve), in which case parametric tests should be applied applied. In this case, however, I would choose a Chi-Squared test for heterogeneity because we're working with we're asking whether the data match an expected RATIO, with a priori expectations, working on one variable (rider count) and two samples (Customer and Subscriber). Per Professor Bianco's Hard-to-Employ example from class, you should apply Pearson's Chi-Squared test when the data is non-parametric!
