import os

import ujson

from tool.functions.suggest_reductions import suggest_reductions


def generate_report(data_dir, data):
    if not data:
        print("No data provided. Cannot generate a report.")
        return

    suggestions = suggest_reductions(data)
    report = {
        "date": data["date"],
        "scope_1": {
            key: f"{value} kg of CO2e" for key, value in data["scope_1"].items()
        },
        "scope_2": {
            key: f"{value} kg of CO2e" for key, value in data["scope_2"].items()
        },
        "scope_3": {
            key: f"{value} kg of CO2e" for key, value in data["scope_3"].items()
        },
        "suggestions": suggestions,
    }

    file_path = os.path.join(data_dir, f"{data['date']}.json")
    with open(file_path, "w", encoding="utf-8") as report_file:
        ujson.dump(report, report_file, indent=4)

    print(f"Report saved to {file_path}.")
    print("\nSuggestions for reducing your carbon footprint:")
    for scope, suggestion in suggestions.items():
        print(f"- {scope.capitalize().replace("_", " ")}: {suggestion}")
