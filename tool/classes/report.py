import os

import ujson

from tool.functions.suggest_reductions import suggest_reductions


class Report:
    def __init__(self, data):
        self.report_id = data["report_id"]
        self.timestamp = data["timestamp"]
        self.scope_1 = data["scope_1"]
        self.scope_2 = data["scope_2"]
        self.scope_3 = data["scope_3"]
        self.suggestions = suggest_reductions(data)

    def to_dict(self):
        return {
            "report_id": self.report_id,
            "timestamp": self.timestamp,
            "scope_1": {key: f"{value} kg of CO2e" for key, value in self.scope_1.items()},
            "scope_2": {key: f"{value} kg of CO2e" for key, value in self.scope_2.items()},
            "scope_3": {key: f"{value} kg of CO2e" for key, value in self.scope_3.items()},
            "suggestions": self.suggestions,
        }

    def save(self, data_dir):
        file_name = f"{self.timestamp}.json"
        file_path = os.path.join(data_dir, file_name)

        with open(file_path, "w", encoding="utf-8") as report_file:
            ujson.dump(self.to_dict(), report_file, indent=4)

        print(f"\nReport saved to {file_path}.")

    def display_suggestions(self):
        if self.suggestions:
            print("\nSuggestions for reducing your carbon footprint:")
            for scope, suggestion in self.suggestions.items():
                print(f"- {scope.capitalize().replace('_', ' ')}: {suggestion}")
        else:
            print("\nNo suggestions needed. Your carbon footprint is already within acceptable limits!")
