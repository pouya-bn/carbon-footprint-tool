import os

from functions.collect_data import collect_data
from functions.generate_report import generate_report


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
        try:
            print("Welcome to the Carbon Footprint Monitoring Tool!")
            print(f"Reports will be saved in: {self.data_dir}\n")

            data = collect_data()
            generate_report(self.data_dir, data)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        monitor = CarbonFootprintMonitor()
        monitor.run()

    except Exception as exception:
        print(f"Failed to initialize the Carbon Footprint Monitor: {exception}")
