import pandas as pandas_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_csv("../../Datasets/bangalore_jan_weather_report.csv", parse_dates=["Date"])
date_series = df_object["Date"]
temperature_series = df_object["Temperature"]
windspeed_series = df_object["Windspeed"]
aqi_series = df_object["AQI"]

plot_package.title("Weather Report in Bangalore in January month")     # Set title of chart
plot_package.xlabel("Date")     # Set label for x-axis
plot_package.ylabel("Temperature")      # Set label for y-axis

# When used same x-axis data for multiple plots, all those plots will be in same chart with different line graphs.
# In such case, label attribute should be defined to each line plot to help legend to distinguish them.
plot_package.plot(date_series, temperature_series, label="Temperature")  # Plot line graph between date and temperature.
plot_package.plot(date_series, windspeed_series, label="Windspeed")  # Plot line graph between date and windspeed.
plot_package.plot(date_series, aqi_series, label="AQI")  # Plot line graph between date and AQI.
plot_package.legend()   # add legend only in case of multi-lines in single chart
plot_package.grid()     # adds grid lines as canvas in the background.
plot_package.show()     # Display line plot chart.

plot_package.legend(loc="upper right")  # sets legend location to be upper right

plot_package.legend(fontsize="large")  # sets fontsize of the labels in the legend to be large
