import uuid
from datetime import datetime


def collect_data():
    print("Please enter your carbon footprint data.")

    while True:
        print("\nScope 1 (Direct emissions)")
        try:
            fuel_combustion = float(input("Fuel combustion (kg of CO2e): "))
            company_vehicles = float(input("Company vehicles (kg of CO2e): "))
            other_direct_sources = float(input("Other direct emissions (kg of CO2e): "))
            break
        except ValueError:
            print("Invalid input! Please enter numerical values for Scope 1 emissions. Let's try again.")

    while True:
        print("\nScope 2 (Indirect emissions from purchased energy)")
        try:
            electricity = float(input("Electricity usage (kg of CO2e): "))
            heating = float(input("Heating (kg of CO2e): "))
            cooling = float(input("Cooling (kg of CO2e): "))
            break
        except ValueError:
            print("Invalid input! Please enter numerical values for Scope 2 emissions. Let's try again.")

    while True:
        print("\nScope 3 (Indirect value chain emissions)")
        try:
            supplier_emissions = float(input("Supplier-related emissions (kg of CO2e): "))
            transportation = float(input("Transportation and logistics (kg of CO2e): "))
            waste = float(input("Waste generated in operations (kg of CO2e): "))
            employee_commuting = float(input("Employee commuting (kg of CO2e): "))
            break
        except ValueError:
            print("Invalid input! Please enter numerical values for Scope 3 emissions. Let's try again.")

    report_id = str(uuid.uuid4())
    timestamp = int(datetime.now().timestamp())

    return {
        "report_id": report_id,
        "timestamp": timestamp,
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
