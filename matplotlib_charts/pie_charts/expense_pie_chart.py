import pandas as pandas_package
import matplotlib.pyplot as plot_package

df_object = pandas_package.read_csv("../../Datasets/expense_tracker.csv")
expense_series = df_object["Expense"]
amount_series = df_object["Amount spent"]

plot_package.title("Expenses in a month")
plot_package.pie(amount_series, labels=expense_series, autopct="%0.2f%%", shadow=True,
                 explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])  # Creates a pie chart
plot_package.show()

plot_package.pie(amount_series, labels=expense_series, radius=2)  # Modify the radius of pie chart

plot_package.pie(amount_series, labels=expense_series, autopct="%0.2f%%")  # Sets the format of percentage and display it in each pie
                                                                           # Two decimal places float format

plot_package.pie(amount_series, labels=expense_series, shadow=True)  # Adds some shadow to each pie

plot_package.pie(amount_series, labels=expense_series, explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])  # Explode pies whose value is more than 0.

plot_package.pie(amount_series, labels=expense_series, startangle=45)  # Pie creation starts at 45 degrees
