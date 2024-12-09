import os

from tool.functions.generate_report import generate_report
from tool.functions.generate_summary import generate_summary


class CarbonFootprintMonitor:
    """
    A class to monitor and manage carbon footprint reports and summaries.

    This tool allows users to add new carbon footprint data, generate summaries
    based on existing data, and provides a user-friendly interface to interact
    with the tool.
    """

    def __init__(self, data_dir="reports"):
        """
        Initializes the CarbonFootprintMonitor instance, setting up the directory
        to save reports.
        """
        try:
            # Get the current working directory and append the data directory to it
            project_dir = os.getcwd()
            self.data_dir = os.path.join(project_dir, data_dir)

            # Create the data directory if it doesn't exist
            os.makedirs(self.data_dir, exist_ok=True)

        except OSError as e:
            print(f"Error: Could not create the reports directory '{data_dir}'. {e}")
            raise

    def run(self):
        """
        Runs the interactive loop for the CarbonFootprintMonitor.

        This method displays a menu for the user to choose between adding new carbon
        footprint data, generating a summary, or exiting the tool.

        It uses the `generate_report` and `generate_summary` functions to generate
        reports and summaries based on the user's choice.

        The loop continues until the user chooses to exit or interrupts the program.
        """
        print("\nWelcome to the Carbon Footprint Monitoring Tool!\n")
        print(f"Reports will be saved in: {self.data_dir}\n")

        while True:
            try:
                # Display menu options to the user
                print("\nPlease choose an option:")
                print("1. Add new Carbon footprint data")
                print("2. Generate summary of all reports")
                print("3. Exit")

                # Get the user's choice
                choice = input("\nEnter your choice (1/2/3): ")

                if choice == "1":
                    # Option 1: Generate a new report
                    generate_report(self.data_dir)

                elif choice == "2":
                    # Option 2: Generate a summary of existing reports
                    generate_summary(self.data_dir)

                elif choice == "3":
                    # Option 3: Exit the program
                    print("\nExiting the Carbon Footprint Monitoring Tool.")
                    break  # Exit the loop

                else:
                    # Invalid option handling
                    print("\nInvalid choice. Please enter 1, 2, or 3.")

            except KeyboardInterrupt:
                # Handle program interruption by the user
                print("\n\nProgram interrupted by user. Exiting...")
                break
            except Exception as e:
                # Handle any unexpected errors during runtime
                print(f"\nAn unexpected error occurred: {e}")
