import os

from functions.generate_report import generate_report
from functions.generate_summary import generate_summary


class CarbonFootprintMonitor:
    def __init__(self, data_dir="reports"):
        try:
            project_dir = os.getcwd()
            self.data_dir = os.path.join(project_dir, data_dir)
            os.makedirs(self.data_dir, exist_ok=True)
        except OSError as e:
            print(f"Error: Could not create the reports directory '{data_dir}'. {e}")
            raise

    def run(self):
        print("\nWelcome to the Carbon Footprint Monitoring Tool!")
        print(f"Reports will be saved in: {self.data_dir}\n")

        while True:
            try:
                print("\nPlease choose an option:")
                print("1. Add new Carbon footprint data")
                print("2. Generate summary of all reports")
                print("3. Exit")

                choice = input("\nEnter your choice (1/2/3): ")

                if choice == "1":
                    generate_report(self.data_dir)

                elif choice == "2":
                    generate_summary(self.data_dir)

                elif choice == "3":
                    print("\nExiting the Carbon Footprint Monitoring Tool.")
                    break

                else:
                    print("\nInvalid choice. Please enter 1, 2, or 3.")

            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        monitor = CarbonFootprintMonitor()
        monitor.run()

    except Exception as exception:
        print(f"Failed to initialize the Carbon Footprint Monitor: {exception}")
