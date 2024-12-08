import os

import ujson

from tool.functions.suggest_reductions import suggest_reductions


class Report:
    def __init__(self, data):
        try:
            self.report_id = data["report_id"]
            self.timestamp = data["timestamp"]
            self.scope_1 = data["scope_1"]
            self.scope_2 = data["scope_2"]
            self.scope_3 = data["scope_3"]
            self.suggestions = suggest_reductions(data)
            
        except KeyError as e:
            raise ValueError(f"Missing key in data: {e}")
        except Exception as e:
            raise ValueError(f"An error occurred during initialization: {e}")

    def to_dict(self):
        try:
            return {
                "report_id": self.report_id,
                "timestamp": self.timestamp,
                "scope_1": {key: f"{value} kg of CO2e" for key, value in self.scope_1.items()},
                "scope_2": {key: f"{value} kg of CO2e" for key, value in self.scope_2.items()},
                "scope_3": {key: f"{value} kg of CO2e" for key, value in self.scope_3.items()},
                "suggestions": self.suggestions,
            }

        except Exception as e:
            raise ValueError(f"An error occurred while converting to dictionary: {e}")

    def save(self, data_dir):
        try:
            file_name = f"{self.timestamp}.json"
            file_path = os.path.join(data_dir, file_name)
            os.makedirs(data_dir, exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as report_file:
                ujson.dump(self.to_dict(), report_file, indent=4)

            print(f"\nReport saved to {file_path}.")

        except OSError as e:
            print(f"File system error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while saving the report: {e}")

    def display_suggestions(self):
        try:
            if self.suggestions:
                print("\nSuggestions for reducing your carbon footprint:")
                for scope, suggestion in self.suggestions.items():
                    print(f"- {scope.capitalize().replace('_', ' ')}: {suggestion}")
            else:
                print("\nYour carbon footprint is within acceptable limits!")

        except Exception as e:
            print(f"An error occurred while displaying suggestions: {e}")
