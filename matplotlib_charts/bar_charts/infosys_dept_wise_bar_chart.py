import pandas as pandas_package
import numpy as numpy_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_excel("../../Datasets/companies_departments_data.xlsx", sheet_name="Infosys")
department_series = df_object["Department"]
employees_count_series = df_object["Employees Count"]

plot_package.title("Count of employees in various departments in Infosys")

# Vertical bars
# Use of bar() function to draw vertical bars
plot_package.xlabel("Department")
plot_package.ylabel("Number of employees")

# Without legend
plot_package.bar(department_series, employees_count_series)
plot_package.show()
# With legend
plot_package.bar(department_series, employees_count_series, label="Employees Count")    # Use of label for legend
plot_package.legend()   # Adds legend
plot_package.show()

# Horizontal bars
# Use of barh() function to draw horizontal bars
plot_package.ylabel("Department")
plot_package.xlabel("Number of employees")
# Without legend
plot_package.barh(department_series, employees_count_series)
plot_package.show()

# Vertical bars
# Suppose x-data-points are list of integers instead of list of strings, you want to display strings instead of integers, then use xticks() as below:
# Without legend
x_data_int_array = numpy_package.arange(len(department_series))
x_data_str_array = department_series
plot_package.xticks(x_data_int_array, x_data_str_array)
plot_package.bar(x_data_int_array, employees_count_series)
plot_package.show()

# Horizontal bars
# Suppose y-data-points are list of integers instead of list of strings, you want to display strings instead of integers, then use yticks() as below:
# With legend
y_data_int_array = numpy_package.arange(len(department_series))
y_data_str_array = department_series
plot_package.ylabel("Department")
plot_package.xlabel("Number of employees")
plot_package.yticks(y_data_int_array, y_data_str_array)
plot_package.barh(y_data_int_array, employees_count_series, label="Employees Count")
plot_package.legend()
plot_package.show()
