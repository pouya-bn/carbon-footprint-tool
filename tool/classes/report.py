import os

import ujson

from tool.functions.suggest_reductions import suggest_reductions


class Report:
    """
    A class to represent a Carbon footprint report. This class is responsible for storing
    the collected Carbon footprint data, converting it to a dictionary, saving it to a file,
    and displaying suggestions for reducing Carbon emissions.
    """

    def __init__(self, data):
        """
        Initializes the Report object with the provided Carbon footprint data.

        Parameters:
            - "client_name" (str): Name of the client.
            - "report_id" (str): Unique identifier for the report.
            - "timestamp" (int): Timestamp when the report was created.
            - "unit" (str): Unit of measurement (e.g., "kg of CO2e").
            - "scope_1" (dict): Direct emissions data (Scope 1).
            - "scope_2" (dict): Indirect emissions data from purchased energy (Scope 2).
            - "scope_3" (dict): Indirect value chain emissions data (Scope 3).
        """
        try:
            self.client_name = data["client_name"]
            self.report_id = data["report_id"]
            self.timestamp = data["timestamp"]
            self.unit = data["unit"]
            self.scope_1 = data["scope_1"]
            self.scope_2 = data["scope_2"]
            self.scope_3 = data["scope_3"]
            self.suggestions = suggest_reductions(data)

        except KeyError as e:
            # Raised if any of the expected keys are missing in the data
            raise ValueError(f"Missing key in data: {e}")
        except Exception as e:
            # Raised for any other errors during initialization
            raise ValueError(f"An error occurred during initialization: {e}")

    def to_dict(self):
        """
        Converts the Report object to a dictionary format.
        """
        try:
            return {
                "client_name": self.client_name,
                "report_id": self.report_id,
                "timestamp": self.timestamp,
                "unit": self.unit,
                "scope_1": {key: value for key, value in self.scope_1.items()},
                "scope_2": {key: value for key, value in self.scope_2.items()},
                "scope_3": {key: value for key, value in self.scope_3.items()},
                "suggestions": self.suggestions,
            }

        except Exception as e:
            # Raised if an error occurs while converting the object to a dictionary
            raise ValueError(f"An error occurred while converting to dictionary: {e}")

    def save(self, data_dir):
        """
        Saves the report data to a JSON file in the specified directory.
        """
        try:
            file_name = f"{self.report_id}.json"
            file_path = os.path.join(data_dir, file_name)

            # Create the directory if it doesn't exist
            os.makedirs(data_dir, exist_ok=True)

            with open(file_path, "w", encoding="utf-8") as report_file:
                ujson.dump(self.to_dict(), report_file, indent=4)  # type: ignore

            print(f"\nReport saved to {file_path}.")

        except OSError as e:
            # Raised if there is a problem with the file system (e.g., insufficient permissions)
            print(f"File system error: {e}")
        except Exception as e:
            # Raised for any other errors that occur during the save operation
            print(f"An unexpected error occurred while saving the report: {e}")

    def display_suggestions(self):
        """
        Displays suggestions for reducing Carbon emissions based on the data in the report.

        This method prints out suggestions for Scope 1, Scope 2, and Scope 3 based on the
        amount of emissions. If no suggestions are needed (i.e., emissions are within acceptable limits),
        it will inform the user.
        """
        try:
            if self.suggestions:
                print("\nSuggestions for reducing your Carbon footprint:")
                for scope, suggestion in self.suggestions.items():
                    print(f"- {scope.capitalize().replace('_', ' ')}: {suggestion}")
            else:
                print("\nYour Carbon footprint is within acceptable limits!")

        except Exception as e:
            # Raised if an error occurs while displaying the suggestions
            print(f"An error occurred while displaying suggestions: {e}")
