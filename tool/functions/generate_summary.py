import os

import ujson

from tool.functions.visualize_data import visualize_summary


def parse_reports(data_dir):
    """
    Parses all JSON files in the given directory and returns the parsed report data.

    This function reads all files in the specified directory (`data_dir`) that have a `.json` extension,
    loads the content of each file using `ujson.load()`, and appends the parsed data to a list. The function
    returns a list of reports as dictionaries.
    """
    reports_data = []

    for file_name in os.listdir(data_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as report_file:
                    report = ujson.load(report_file)
                    reports_data.append(report)
            except Exception as e:
                # Raised if an error occurs while reading any of the report files
                print(f"Error reading {file_name}: {e}")

    return reports_data


def summarize_reports(reports_data):
    """
    Summarizes the Carbon footprint reports by calculating averages and identifying the most common suggestions.

    This function returns a dictionary containing the summarized data:
        - `avg_scope_1`: The average Carbon footprint for Scope 1 (direct emissions).
        - `avg_scope_2`: The average Carbon footprint for Scope 2 (indirect emissions from energy use).
        - `avg_scope_3`: The average Carbon footprint for Scope 3 (indirect emissions from the value chain).
        - `most_common_suggestions`: A sorted list of the most common suggestions and their counts.
    """
    total_scope_1 = total_scope_2 = total_scope_3 = 0
    count_scope_1 = count_scope_2 = count_scope_3 = 0
    all_suggestions = {}

    # Iterate through all reports and aggregate the data
    for report in reports_data:
        for key, value in report["scope_1"].items():
            total_scope_1 += value
            count_scope_1 += 1
        for key, value in report["scope_2"].items():
            total_scope_2 += value
            count_scope_2 += 1
        for key, value in report["scope_3"].items():
            total_scope_3 += value
            count_scope_3 += 1

        if report["suggestions"]:
            for scope, suggestion in report["suggestions"].items():
                if suggestion not in all_suggestions:
                    all_suggestions[suggestion] = 1
                else:
                    all_suggestions[suggestion] += 1

    # Calculate averages for Scope 1, Scope 2, and Scope 3
    avg_scope_1 = round(total_scope_1 / count_scope_1, 4) if count_scope_1 > 0 else 0
    avg_scope_2 = round(total_scope_2 / count_scope_2, 4) if count_scope_2 > 0 else 0
    avg_scope_3 = round(total_scope_3 / count_scope_3, 4) if count_scope_3 > 0 else 0

    # Sort suggestions by frequency
    most_common_suggestions = sorted(
        all_suggestions.items(),  # Convert the dictionary to a list of key-value tuples
        key=lambda x: x[1],  # Sort by the frequency count (the second element in each tuple)
        reverse=True,  # Sort in descending order (most frequent suggestions first)
    )

    return {
        "avg_scope_1": avg_scope_1,
        "avg_scope_2": avg_scope_2,
        "avg_scope_3": avg_scope_3,
        "most_common_suggestions": most_common_suggestions
    }


def generate_summary(data_dir):
    """
    Generates and displays a summary of Carbon footprint reports, including average emissions and
    the most common suggestions for reducing emissions.

    This function loads all the report data from the specified directory, summarizes the emissions data
    (averages for Scope 1, Scope 2, and Scope 3), and identifies the most common suggestions for reducing emissions.
    After computing the summary, it prints the results and visualizes the summary data.
    """
    reports_data = parse_reports(data_dir)
    if reports_data:
        summary = summarize_reports(reports_data)
        print("\nSummary of Reports:\n")
        print(f"Average Scope 1: {summary['avg_scope_1']} kg of CO2e")
        print(f"Average Scope 2: {summary['avg_scope_2']} kg of CO2e")
        print(f"Average Scope 3: {summary['avg_scope_3']} kg of CO2e")
        print("\nMost Common Suggestions:")
        for suggestion, count in summary["most_common_suggestions"]:
            print(f"- {suggestion} (appeared {count} times)")

        # Visualize the summary data
        visualize_summary(summary)

    else:
        print("No reports found to summarize.")
