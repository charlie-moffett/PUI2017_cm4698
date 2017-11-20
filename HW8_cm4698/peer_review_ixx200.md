# Overview
This is a peer review of YuKun's visualization submission provided by Ian Xiao (ixx200). This review includes the following:
- CLARITY: is the plot easy to read? is it clear or confusing, are the quantities being visualized ambiguous?
- ESTHETIC: beautiful is a subjective judgment: you should not judge the plot on the basis of whether you think it is "beautiful", but you should judge whether its esthetic is functional to what it is meant to communicate. Are the colors chosen appropriately? Are the graphical elements used appropriate to represent the quantities being visualized? Are the graphical choices allowing you to focus on the right elements or are they distracting you?
- HONESTY: is the plot honestly reproducing the data or is it deforming it, perhaps to emphasize a point?

# Original Visualization

![Alt text](./1800pop.PNG?raw=true)

# Clarity
The plot is clear at first glance and the insight is very interesting. Here are a few considerations to provide more context to support the key message of "1 in 8 American lives in the city in 1800":
- label each sample with the name of the State
- provide summary stats, such as the coefficient and R2, of the regression line in the caption; the coefficient should be around 8 so that it supports the key message
- use an bar plot instead; this may avoid a perception of "projecting", which can lead to a message of "10k people live in the urban area when the population is 100K; so there will be ~100k people when there are 1M people" (see details below)

# Esthetic
I think Charlie chose good graphical elements to support his key messsage. Alternatively, Charlie can considering using a side-by-side bar chart, such as this: 

![Alt text](./sample_barchart.png?raw=true)

Each bar can represent a State. Percentage breakdown is by city dweller vs. people who live in the suburban area (totpop - urb800). The absolute population count by states should also be included so that readers knows the actual population if they want to know more. 

This view may avoid the perception of "projecting" when scatter plot and regression line are used. It still speaks direclty to the message Charlie wanted to present.  

# Honesty
Charlie's data processing approach is reasonable and maintain the data integrity of the dataset. He removed States with zero popoulation, which may be due to data availability. This is sufficient to support the regression analysis Charlie intended to perform.  
