import os

import ujson

from tool.functions.visualize_data import visualize_summary


def parse_reports(data_dir):
    reports_data = []

    for file_name in os.listdir(data_dir):
        if file_name.endswith(".json"):
            file_path = os.path.join(data_dir, file_name)
            try:
                with open(file_path, "r", encoding="utf-8") as report_file:
                    report = ujson.load(report_file)
                    reports_data.append(report)
            except Exception as e:
                print(f"Error reading {file_name}: {e}")

    return reports_data


def summarize_reports(reports_data):
    total_scope_1 = total_scope_2 = total_scope_3 = 0
    count_scope_1 = count_scope_2 = count_scope_3 = 0
    all_suggestions = {}

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

    avg_scope_1 = round(total_scope_1 / count_scope_1, 4) if count_scope_1 > 0 else 0
    avg_scope_2 = round(total_scope_2 / count_scope_2, 4) if count_scope_2 > 0 else 0
    avg_scope_3 = round(total_scope_3 / count_scope_3, 4) if count_scope_3 > 0 else 0

    most_common_suggestions = sorted(
        all_suggestions.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    return {
        "avg_scope_1": avg_scope_1,
        "avg_scope_2": avg_scope_2,
        "avg_scope_3": avg_scope_3,
        "most_common_suggestions": most_common_suggestions
    }


def generate_summary(data_dir):
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

        visualize_summary(summary)

    else:
        print("No reports found to summarize.")
