# Surfs_Up_Climate_Analysis

## Overview

The purpose of this analysis was to give the client information about temperature trends during the months of June and December in O'ahu, Hawaii in order to predict whether or not a surf and ice cream shop will be sustainable throughout the year.

## Resources

- Data Sources
    - Weather Data Set provided by University of Oregon: hawaii.sqlite

- Software
    - Jupyter Notebook 6.3.0
    - SQLAlchemy 1.4.7
    - Python 3.7.10
    
## Results

### Temperature Analysis

- There was a 200 count difference between the number of times the temperature was measured in June than in December (see table 1). The data for December temperatures was not collected in 2017, which may account for this difference; however, the 200 count difference was not significant enough to impact the results of the analysis.

- There was a slight but insignificant difference between the average temperature in the month of June versus the month of December (see table 1). June has an average temperature of 74.9°F with a mean of 75°F. December shows an average temperature of 71°F with the same mean. The temperatures in these months seem consistently high enough for a surf and ice cream .

*Table 1*

<img src="https://github.com/jisellejones/surfs_up/blob/main/Images/temp_table.png" width="200" height="200">

- The histograms show the frequency of temperatures in December and June. December had a greater range of temperatures, dipping into the 50° temperatures where most of the temperatures in June range between 73°F and 83°F. Although there are 

<img src="https://github.com/jisellejones/surfs_up/blob/main/Images/histogram_june_temps.png" width="300" height="200">      <img src="https://github.com/jisellejones/surfs_up/blob/main/Images/histogram_dec_temps.png" width="300" height="200">

### Precipitation Analysis

A secondary analysis was run on the precipitation amounts in the months of June and December by year to determine if there are any trends in the amount of rainfall that may influence the number of people who might need surf gear and/or may want an ice cream snack.

- The bar graphs show the average amount of rainfall in June for 2010 - 2017 and December for 2010 - 2016. Average rainfall across the years in both months is below 0.25 inches except in December in 2010. Research was conducted on the December 2010 rainfall data and has been summarized in the summary section.

<img src="https://github.com/jisellejones/surfs_up/blob/main/Images/bar_graph_june_prcp.png" width="300" height="200">      <img src="https://github.com/jisellejones/surfs_up/blob/main/Images/bar_graph_dec_prcp.png" width="300" height="200">

## Summary

Overall it seems that O'ahu is a good place for a surf and ice cream shop. While the data suggests that June may be a more ameable month for surfing and ice cream eating with most temperatures ranging between 73°F and 83°F, the bulk of days in December are 70°F or above. 

The precipitation analysis performed on the June and December rainfall amounts offers further evidence that a surf and shake shop has the potential to be successful as data suggests little rainfall during these months with the exception of rainfall amounts in the month of December.

There was a concerning increase in the amount of rainfall in 2010. Upon further investigation, we found that there was an unusual weather event causing heavy rainfall to hit the island of O'ahu in December of 2010. While this weather event was unusual for the island, it may be worth researching how frequently heavy rainfalls have occured on the island over the last 30 - 50 years. It may also be a good idea to run an analysis on the other months of the year to determine if there is a particular month or season where inclement weather often occurs and may not be ideal conditions for surfing or ice cream eating.