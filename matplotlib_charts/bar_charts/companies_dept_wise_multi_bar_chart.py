import pandas as pandas_package
import numpy as numpy_package
import matplotlib.pyplot as plot_package

infosys_df_object = pandas_package.read_excel("../../Datasets/companies_departments_data.xlsx", sheet_name="Infosys")
dept_series = infosys_df_object["Department"]
infosys_emp_count_series = infosys_df_object["Employees Count"]
tcs_df_object = pandas_package.read_excel("../../Datasets/companies_departments_data.xlsx", sheet_name="TCS")
tcs_emp_count_series = tcs_df_object["Employees Count"]
accenture_df_object = pandas_package.read_excel("../../Datasets/companies_departments_data.xlsx", sheet_name="Accenture")
accenture_emp_count_series = accenture_df_object["Employees Count"]
mphasis_df_object = pandas_package.read_excel("../../Datasets/companies_departments_data.xlsx", sheet_name="Mphasis")
mphasis_emp_count_series = mphasis_df_object["Employees Count"]

x_data_int_array = numpy_package.arange(len(dept_series))
x_data_str_array = dept_series
plot_package.title("Employees in various departments")

# Vertical bars
# Use of bar() function to draw vertical bars
# With legend
plot_package.xlabel("Department")
plot_package.ylabel("Number of employees")
plot_package.xticks(x_data_int_array, x_data_str_array) # Use of xticks to manually modify labels instead of integers along x-axis
plot_package.bar(x_data_int_array - 0.1, infosys_emp_count_series, width=0.1, label="Infosys")
plot_package.bar(x_data_int_array - 0.2, tcs_emp_count_series, width=0.1, label="TCS")
plot_package.bar(x_data_int_array + 0.1, accenture_emp_count_series, width=0.1, label="Accenture")
plot_package.bar(x_data_int_array + 0.2, mphasis_emp_count_series, width=0.1, label="Mphasis")
plot_package.legend()
plot_package.show()

y_data_int_array = numpy_package.arange(len(dept_series))
y_data_str_array = dept_series

# Horizontal bars
# Use of barh() function to draw horizontal bars
# With legend
plot_package.ylabel("Department")
plot_package.xlabel("Number of employees")
plot_package.yticks(y_data_int_array, y_data_str_array) # Use of yticks to manually modify labels instead of integers along y-axis
plot_package.barh(y_data_int_array - 0.1, infosys_emp_count_series, label="Infosys", height=0.1)
plot_package.barh(y_data_int_array - 0.2, tcs_emp_count_series, label="TCS", height=0.1)
plot_package.barh(y_data_int_array + 0.1, accenture_emp_count_series, label="Accenture", height=0.1)
plot_package.barh(y_data_int_array + 0.2, mphasis_emp_count_series, label="Mphasis", height=0.1)
plot_package.legend()
plot_package.show()
