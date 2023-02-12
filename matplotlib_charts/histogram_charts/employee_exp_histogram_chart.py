import pandas as pandas_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_csv("../../Datasets/employees_exp_details.csv")
employee_name_series = df_object["Employee Name"]
experience_series = df_object["Experience (in yrs)"]

plot_package.xlabel("Experience (in years)")
plot_package.ylabel("Number of employees")
plot_package.title("Experience details of employees")

# Vertical bar Without legend
plot_package.hist(experience_series, rwidth=0.95)
plot_package.show()

# Horizontal bar Without legend
plot_package.hist(experience_series, rwidth=0.95, orientation="horizontal")
plot_package.show()

# Vertical bar With legend
plot_package.hist(experience_series, rwidth=0.95, label="Number of employees", color="red")
plot_package.legend()
plot_package.show()

# With Custom range
plot_package.hist(experience_series, bins=[0, 3, 6, 10], rwidth=0.95, label="Number of employees", color="orange")
plot_package.legend()
plot_package.show()

# With step histogram type
plot_package.hist(experience_series, bins=[0, 3, 6, 10], rwidth=0.95, label="Number of employees", color="orange", histtype="step")
plot_package.legend()
plot_package.show()

plot_package.hist(experience_series, orientation="horizontal")   # Bars will be horizontal
plot_package.hist(experience_series, bins=10)   # Integer value - Define the number of bars to be formed in histogram.
plot_package.hist(experience_series, bins=[0, 3, 6, 10])   # Array of ranges - bars of 0-3, 3-6, 6-10 ranges will be formed.
plot_package.hist(experience_series, rwidth=0.95)   # Define the relative width between bars. Value will be 0-1.
plot_package.hist(experience_series, histtype="step")   # Change the style of bars in histogram. step style produces steps like bars in histogram.
plot_package.hist(experience_series, color="green")   # Bars color is green
