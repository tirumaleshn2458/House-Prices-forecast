# Forecast of House Prices in Connecticut
## Aim:- Forecasting the median and average sale prices
### Models used:- Prophet, ARIMA, SARIMA
Note:- 
- ARIMA and SARIMA models doesn't fit for the data given due it's bad accuracy. 
  - You can view the files reagarding the accuracy in connecticut_ARIMA folder
- As an alternative, Prophet is used to fit data of every county. 
- The whole work-flow is based only on Prophet for training the data.

**Libraries used:**
- Pandas
  - Data manipulation
- prophet(from facebook)
  - Visualization
  - Model training
  - Model evaluation

**Data Collection**
Data is downlaoded from [here](https://catalog.data.gov/dataset/monthly-sale-price-of-single-family-homes-in-ct/)

**Data handling**
- The dataframe is categorized into different dataframes based on county name.
- The other county names in the dataframe are Fairfield, Hartford, Lichfield, Middlesex, New Haven, New London, Connecticut, Tolland, Windham.

**File handling**
- Each categorized dataframe is sent into new directory by creating a folder under the name of county.
- The workflow is done in 2 jupyter notebooks since we need to forecast the Median and Average Sale Price Independently in separate notebooks.
- In Median Sale Price file, we need to forecast the Median Sale Price.
- In Average Sale Price file, we need to forecast the Average Sale Price.

**The process is done for every individual county's dataframe separately.**

**Data Manipulation**
- The county name is removed since it is no longer required because of it's single value in entire column.
- The 'Date' column(feature) will be in str(string) format. So, we need to change that into datetime format using pandas.
- Dropping of features
  - To forecast the median sale price, we need to drop average sale price and proceed because we have to use only median sale price data in dataframe.
    - Extracting only two features such as 'Date' and 'Median Sale Price'.
  - To forecast the average sale price, we need to drop average sale price and proceed because we have to use only average sale price data in dataframe.
    - Extracting only two features such as 'Date' and 'Average Sale Price'.


Note:- *Values in 'Date' feature is same for both the Median and Average Sale Price*
**Model training**
- Once the dataframe is finalized we need to change the column names of the dataframe.
  - 'ds' for Date and 'y' for the data we need to forecast
- The model is initialized and got trained.
- And when we predict the values, a dataframe will be returned that contains all the values related to the model predictions.
- The forecasted values are visualized in various forms. You can see in the notebooks.
- At the end of the process, the trained model is saved for every county. 
    
   
       
