# 1D-Multi Dataset

### General Notes
- From the readme notes, the data has one Proposed method and 9 baseline methods
- From the exploration in the data-exploration notebook (see notebooks folder), each method has 10 measurements
- No outliers in each method, but the methods have quite different ranges, so this should stand out in the visualization

### Data Viz
- Swarmplot should be a good choice to make sure all data is shown since the measurement count for each method is small
- The idea is to have all baseline methods with the same color and the proposed method with a unique color to implement the preattentive attribute