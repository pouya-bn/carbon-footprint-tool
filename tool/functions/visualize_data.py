import matplotlib.pyplot as plt


def visualize_report(report):
    """
    Visualizes the Carbon footprint data from a single report using a pie chart.

    This function takes a report containing Carbon footprint data for Scope 1, Scope 2, and Scope 3,
    calculates the total emissions for each scope, and visualizes the distribution of emissions across
    the three scopes using a pie chart. The chart shows the percentage contribution of each scope to
    the total Carbon footprint.
    """

    # Define the labels for the pie chart
    labels = ['Scope 1', 'Scope 2', 'Scope 3']

    # Calculate the total emissions for each scope
    sizes = [
        sum(report["scope_1"].values()),  # Total Scope 1 emissions
        sum(report["scope_2"].values()),  # Total Scope 2 emissions
        sum(report["scope_3"].values())  # Total Scope 3 emissions
    ]

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    # Set the title of the chart
    plt.title('Carbon Footprint Distribution by Scope')

    # Display the pie chart
    plt.show()


def visualize_summary(summary):
    """
    Visualizes the average Carbon footprint data by scope using a bar chart.

    This function takes a summary of Carbon footprint data, including the average emissions for Scope 1,
    Scope 2, and Scope 3, and displays a bar chart representing the average Carbon footprint for each scope.
    """

    # Define the labels for the bar chart (Scope 1, Scope 2, Scope 3)
    labels = ['Scope 1', 'Scope 2', 'Scope 3']

    # Extract the average emissions for each scope from the summary dictionary
    averages = [
        summary['avg_scope_1'],
        summary['avg_scope_2'],
        summary['avg_scope_3'],
    ]

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, averages, color=['blue', 'orange', 'green'])  # Different colors for each scope

    # Set the label for the y-axis
    ax.set_ylabel('Average CO2e (kg)')

    # Set the title for the bar chart
    ax.set_title('Average Carbon Footprint by Scope')

    # Display the bar chart
    plt.show()
