from tool.classes.report import Report
from tool.functions.collect_data import collect_data
from tool.functions.visualize_data import visualize_report


def generate_report(data_dir):
    """
    This function acts as the entry point for generating a new Carbon footprint report. It prompts the user
    for input through the `collect_data` function, processes the data into a report object using the `Report` class,
    and stores the report in the specified directory. It also visualizes the report data for better insight.
    """
    try:
        # Collect the Carbon footprint data from the user
        data = collect_data()

        # If no data is collected, exit the function
        if not data:
            print("No data provided. Cannot generate a report.")
            return

        # Create a Report object using the collected data
        report = Report(data)

        # Save the generated report to the specified directory
        report.save(data_dir)

        # Display suggestions for reducing Carbon footprint
        report.display_suggestions()

        # Visualize the collected report data for better insights
        visualize_report(data)

    except FileNotFoundError as e:
        # Handle case where the specified directory does not exist
        print(f"Error: The directory '{data_dir}' does not exist. {e}")
    except PermissionError as e:
        # Handle case where the program doesn't have permission to write to the directory
        print(f"Error: Insufficient permissions to write to '{data_dir}'. {e}")
    except ValueError as e:
        # Handle case where there is invalid data, such as missing or incorrect input
        print(f"Error: Invalid data encountered. {e}")
    except Exception as e:
        # Catch all unexpected errors and print the error message
        print(f"An unexpected error occurred: {e}")
