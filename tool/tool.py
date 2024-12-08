import ujson
import os
from datetime import datetime


def collect_data():
    print("Please enter your carbon footprint data.")
    print("\nScope 1 (Direct emissions)")
    fuel_combustion = float(input("Fuel combustion (kg of CO2e): "))
    company_vehicles = float(input("Company vehicles (kg of CO2e): "))
    other_direct_sources = float(input("Other direct emissions (kg of CO2e): "))

    print("\nScope 2 (Indirect emissions from purchased energy)")
    electricity = float(input("Electricity usage (kg of CO2e): "))
    heating = float(input("Heating (kg of CO2e): "))
    cooling = float(input("Cooling (kg of CO2e): "))

    print("\nScope 3 (Indirect value chain emissions)")
    supplier_emissions = float(input("Supplier-related emissions (kg of CO2e): "))
    transportation = float(input("Transportation and logistics (kg of CO2e): "))
    waste = float(input("Waste generated in operations (kg of CO2e): "))
    employee_commuting = float(input("Employee commuting (kg of CO2e): "))

    date = datetime.now().strftime("%Y-%m-%d")

    return {
        "date": date,
        "scope_1": {
            "fuel_combustion": fuel_combustion,
            "company_vehicles": company_vehicles,
            "other_direct_sources": other_direct_sources
        },
        "scope_2": {
            "electricity": electricity,
            "heating": heating,
            "cooling": cooling
        },
        "scope_3": {
            "supplier_emissions": supplier_emissions,
            "transportation": transportation,
            "waste": waste,
            "employee_commuting": employee_commuting
        }
    }


def suggest_reductions(data):
    suggestions = {}
    if sum(data["scope_1"].values()) > 10000:
        suggestions["scope_1"] = "Consider optimizing fuel usage, adopting electric vehicles, or upgrading equipment."
    if sum(data["scope_2"].values()) > 10000:
        suggestions["scope_2"] = "Switch to renewable energy sources or implement energy-efficient practices."
    if sum(data["scope_3"].values()) > 20000:
        suggestions["scope_3"] = "Engage suppliers on sustainability, improve waste management, and optimize logistics."
    return suggestions


def generate_report(data_dir, data):
    if not data:
        print("No data provided. Cannot generate a report.")
        return

    suggestions = suggest_reductions(data)
    report = {
        "date": data["date"],
        "scope_1": {key: f"{value} kg of CO2e" for key, value in data["scope_1"].items()},
        "scope_2": {key: f"{value} kg of CO2e" for key, value in data["scope_2"].items()},
        "scope_3": {key: f"{value} kg of CO2e" for key, value in data["scope_3"].items()},
        "suggestions": suggestions
    }

    file_path = os.path.join(data_dir, f"{data['date']}.json")
    with open(file_path, "w", encoding="utf-8") as report_file:
        ujson.dump(report, report_file, indent=4)

    print(f"Report saved to {file_path}.")
    print("\nSuggestions for reducing your carbon footprint:")
    for scope, suggestion in suggestions.items():
        print(f"- {scope.capitalize().replace("_", " ")}: {suggestion}")

class CarbonFootprintMonitor:
    def __init__(self, data_dir="reports"):
        parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.data_dir = os.path.join(parent_dir, data_dir)
        os.makedirs(self.data_dir, exist_ok=True)
        print(f"Reports will be saved in: {self.data_dir}")

    def run(self):
        print("Welcome to the Carbon Footprint Monitoring Tool!")
        data = collect_data()
        generate_report(self.data_dir, data)


if __name__ == "__main__":
    monitor = CarbonFootprintMonitor()
    monitor.run()
