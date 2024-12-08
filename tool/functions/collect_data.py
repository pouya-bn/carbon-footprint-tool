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