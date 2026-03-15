# 1D Dataset

### General Notes
From the exploration in the data-exploration notebook (see notebooks folder), the 1d-data only has 20 rows of data:
 - 20 rows for the 10 subjects as noted in the project readme
 - 2 columns: value, group (which is either "control" or "cases")
 - the summary stats showed the data has some outliers as the `value` range goes from 4.564090 to 35764.919601, and there's the wide gap between the 25th and 75th percentiles
 - the only formatting that might needed will be roudning the decimal places


### Data Viz
- Since it's a small dataset and to ensure all points are shown including the outliers observed from the exploration checks, I will use the swarm plot from the [lecture notes](https://skojaku.github.io/applied-soft-comp/m02-visualization/1d-data.html#swarm-plots-beeswarm-plots)