import os

from functions.collect_data import collect_data
from functions.generate_report import generate_report


class CarbonFootprintMonitor:
    def __init__(self, data_dir="reports"):
        project_dir = os.getcwd()
        self.data_dir = os.path.join(project_dir, data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        print(f"Reports will be saved in: {self.data_dir}")

    def run(self):
        print("Welcome to the Carbon Footprint Monitoring Tool!")
        data = collect_data()
        generate_report(self.data_dir, data)


if __name__ == "__main__":
    monitor = CarbonFootprintMonitor()
    monitor.run()
