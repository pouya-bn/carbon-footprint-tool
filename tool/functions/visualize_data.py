import matplotlib.pyplot as plt


def visualize_report(report):
    labels = ['Scope 1', 'Scope 2', 'Scope 3']
    sizes = [
        sum(report["scope_1"].values()),
        sum(report["scope_2"].values()),
        sum(report["scope_3"].values())
    ]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    plt.title('Carbon Footprint Distribution by Scope')
    plt.show()


def visualize_summary(summary):
    labels = ['Scope 1', 'Scope 2', 'Scope 3']
    averages = [summary['avg_scope_1'], summary['avg_scope_2'], summary['avg_scope_3']]

    fig, ax = plt.subplots()
    ax.bar(labels, averages, color=['blue', 'orange', 'green'])
    ax.set_ylabel('Average CO2e (kg)')
    ax.set_title('Average Carbon Footprint by Scope')

    plt.show()
