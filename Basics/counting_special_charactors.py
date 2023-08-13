string = '''Hello! Forecasting values in Power BI can provide valuable insights into future trends and help with decision-making. 
To forecast values in Power BI, you can follow these general steps: Data Preparation: Ensure your data is organized and clean. 
Load your data into Power BI and structure it appropriately, with a time-based column for forecasting, and the target variable you want to forecast. 
Visualizations: Create a visual representation of your data using line charts, time series charts, or other appropriate visuals. 
This will give you a clear understanding of the historical data and patterns. 
Time Intelligence: Power BI has built-in time intelligence functions that allow you to work with time-based data. Use functions like DATEADD, SAMEPERIODLASTYEAR, etc., to calculate time-based metrics. Forecasting Techniques: Power BI has a feature called "Forecast" which uses exponential smoothing to automatically generate forecasts. To use this: Select the visual you want to forecast. In the "Analytics" pane, choose the "Forecast" option. Configure the forecast options such as forecast period and confidence intervals. Advanced  orecasting: For more advanced forecasting, you can use Power Query to preprocess and transform data before creating visualizations. Additionally, you can use DAX formulas to create custom forecasting calculations. Custom DAX Forecasting: To perform custom forecasting, you might create measures or columns using DAX functions such as AVERAGEX, SUMX, or even external forecasting libraries. External Tools: You can also use external tools and libraries like R or Python within Power BI to perform more sophisticated forecasting techniques. Power BI allows integration with these languages to enhance the forecasting capabilities. Evaluate and Refine: Once you've generated forecasts, evaluate their accuracy against historical data and adjust parameters or techniques as needed. Visualizations for Forecasts: Create visuals that display historical data alongside forecasted values. This can help stakeholders understand the predicted trends more effectively. Dashboard Creation: Combine the forecasted visuals with other relevant data visuals to create insightful dashboards that can aid in decision-making. Remember, the effectiveness of your forecasts depends on the quality of your data, the chosen forecasting method, and the accuracy of your parameters. Experiment with different techniques and evaluate the results to find the best approach for your specific dataset and business needs.'''


st = ''
lio = '!-:,."'
special_char = ''
special_char_count = 0
count = 0

for i in string:
    if i == 'a':
        st += i
        count += 1
    elif i in lio:
        special_char += i
        special_char_count += 1
    else:
        pass
print(st)
print(count)
print(special_char)
print(special_char_count)
