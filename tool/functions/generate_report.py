from tool.classes.report import Report
from tool.functions.collect_data import collect_data
from tool.functions.visualize_data import visualize_report


def generate_report(data_dir):
    try:
        data = collect_data()

        if not data:
            print("No data provided. Cannot generate a report.")
            return

        report = Report(data)
        report.save(data_dir)

        report.display_suggestions()
        visualize_report(data)

    except FileNotFoundError as e:
        print(f"Error: The directory '{data_dir}' does not exist. {e}")
    except PermissionError as e:
        print(f"Error: Insufficient permissions to write to '{data_dir}'. {e}")
    except ValueError as e:
        print(f"Error: Invalid data encountered. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
