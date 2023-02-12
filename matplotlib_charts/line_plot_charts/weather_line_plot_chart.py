import pandas as pandas_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_csv("../../Datasets/bangalore_jan_weather_report.csv", parse_dates=["Date"])
date_series = df_object["Date"]
temperature_series = df_object["Temperature"]
windspeed_series = df_object["Windspeed"]

plot_package.title("Temperature in Bangalore in January month")     # Set title of chart
plot_package.xlabel("Date")     # Set label for x-axis
plot_package.ylabel("Temperature")      # Set label for y-axis
plot_package.plot(date_series, temperature_series)  # Plot line graph between date and temperature.
plot_package.show()     # Display the line plot chart

# For multi-line charts, Setting label for line will be useful only for applying legend in line plot chart.
plot_package.plot(date_series, temperature_series, label="temperature")
plot_package.legend()   # Adds legend to line plot chart
plot_package.grid()     # adds grid lines as canvas in the background.
plot_package.show()

plot_package.plot(date_series, temperature_series, alpha=0.3)  # Controls the transparency / brightness of the line / markers in graph.

plot_package.plot(date_series, temperature_series, marker="+")  # Display data points in graph with + symbol

plot_package.plot(date_series, temperature_series, color="green")   # Line color is green

plot_package.plot(date_series, temperature_series, linewidth=6)     # Width of the line is 6

plot_package.plot(date_series, temperature_series, linestyle="dashed")  # Style of line is dashed

plot_package.plot(date_series, temperature_series, linestyle="dotted")  # Style of line is dotted
