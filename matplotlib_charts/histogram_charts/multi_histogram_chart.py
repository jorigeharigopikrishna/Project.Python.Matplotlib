import pandas as pandas_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_csv("../../Datasets/employees_exp_details.csv")
employee_name_series = df_object["Employee Name"]
experience_series = df_object["Experience (in yrs)"]
before_companies_series = df_object["Number of companies before?"]

plot_package.title("Experience details of employees")

# Vertical bars
plot_package.xlabel("Experience (in years) including number of companies before")
plot_package.ylabel("Number of employees")
plot_package.hist([experience_series, before_companies_series], bins=10, rwidth=0.99, label=["Experience", "Companies before"])
plot_package.legend()
plot_package.show()

# Horizontal bars
plot_package.ylabel("Experience (in years) including number of companies before")
plot_package.xlabel("Number of employees")
plot_package.hist([experience_series, before_companies_series], orientation="horizontal", bins=10, rwidth=0.99, label=["Experience", "Companies before"])
plot_package.legend()
plot_package.show()
