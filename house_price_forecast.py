#import libraries
import streamlit as st
import pandas as pd
from prophet import Prophet
import warnings
from prophet.diagnostics import cross_validation
from prophet.plot import plot_plotly, plot_components_plotly
from prophet.diagnostics import performance_metrics
from prophet.plot import plot_cross_validation_metric
#defining the function
def work_flow(to_forecast,county):
    #to_forecast is the feature name and county is the name of County
    #extracting the data of a particular county name.
    data=data_frame[['County']==county]
    #dropping the County name after extracting as it is no longer required.
    data=data.drop(['County'],axis=1)
    #converting the 'Date' from str(string) format to 'Date' format.
    data['Date']=pd.to_datetime(data['Date'],format='%Y/%m/%d')
    #if to_forecast is 'Median Sale Price' then 'Average Sale Price' gets dropped.
    if to_forecast=='Median Sale Price':
        new_data=data_frame.drop(['Average Sale Price'],axis=1)
    #if to_forecast is 'Average Sale Price' then 'Median Sale Price' gets dropped.
    if to_forecast=='Average Sale Price':
        new_data=data_frame.drop(['Median Sale Price'],axis=1)
    #renaming the columns
    new_data.columns=['ds','y']
    #Initializing the Prophet model as m
    m = Prophet()
    #Fitting the model
    m.fit(median_data)
    #creating the data frame with the next 24 months in 'ds'(Date)
    future = m.make_future_dataframe(periods=24,freq='M')
    #predicting the values with future dataframe.
    forecast = m.predict(future)
    #plotting the forecast data.
    fig1 = m.plot(forecast)
    #plotting the components of forecast
    fig2 = m.plot_components(forecast)
    from prophet.plot import plot_plotly, plot_components_plotly
    #plotting the final figure
    fig3=plot_plotly(m, forecast)
    #plotting the trend and yearly data
    fig4=plot_components_plotly(m, forecast)
    #to check the accuracy of the forecasted values.
    from prophet.diagnostics import cross_validation
    #performing cross validation
    df_cv = cross_validation(m, initial='730 days', period='180 days', horizon = '365 days')
    #to get the dataframe that contains all kinds of metrics to evaluate the model.
    df_p = performance_metrics(df_cv)
    #plotting the 'mape' metrics
    fig = plot_cross_validation_metric(df_cv, metric='mape')


#reading the dataframe
data_frame=pd.read_csv('Monthly_Sale_Price_of_Single_Family_Homes_in_CT.csv')
#taking the county name and feature name to forecast
county_name=input('Please enter the County name: [Connecticut, Litchfield, Fairfield, Hartford, Middlesex, New Havon, New London, Tolland, Windham]')
if county_name in data_frame['County'].unique():
    feature_name=input('Please enter the feature name to forecast: [Median Sale Price,Average Sale Price]')
    if (feature_name=='Median Sale Price')|(feature_name=='Average Sale Price'):
        #calling the work_flow function
        work_flow(feature_name,county_name)
    else:
        print('Please enter the feature name correctly')
else:
    print('County not found, please enter the County name correctly')
