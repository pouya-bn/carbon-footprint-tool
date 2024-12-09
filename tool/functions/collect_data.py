import uuid
from datetime import datetime


def collect_data():
    """
    Collects carbon footprint data from the user.

    The data is organized into three scopes:
        - Scope 1: Direct emissions (e.g., fuel combustion, company vehicles)
        - Scope 2: Indirect emissions from purchased energy (e.g., electricity, heating, cooling)
        - Scope 3: Indirect emissions from the value chain (e.g., supplier emissions, transportation)

    This function prompts the user to enter data for relevant information, and it validates the input to
    ensure all data entered is numeric. The collected data is returned as a dictionary with unique
    report ID and timestamp for record-keeping, as well as the unit of measurement.
    """
    try:
        # Prompt for the client name
        client_name = input("Please enter the name of the client: ")

        print("Please enter your Carbon footprint data.")

        # Collect Scope 1 data (Direct emissions)
        while True:
            print("\nScope 1 (Direct emissions)")
            try:
                fuel_combustion = float(input("Fuel combustion (kg of CO2e): "))
                company_vehicles = float(input("Company vehicles (kg of CO2e): "))
                other_direct_sources = float(input("Other direct emissions (kg of CO2e): "))
                break  # Exit loop once valid data is entered
            except ValueError:
                # Raised if the user enters invalid data (non-numeric values)
                print("Invalid input! Please enter numerical values for Scope 1 emissions. Let's try again.")

        # Collect Scope 2 data (Indirect emissions from purchased energy)
        while True:
            print("\nScope 2 (Indirect emissions from purchased energy)")
            try:
                electricity = float(input("Electricity usage (kg of CO2e): "))
                heating = float(input("Heating (kg of CO2e): "))
                cooling = float(input("Cooling (kg of CO2e): "))
                break  # Exit loop once valid data is entered
            except ValueError:
                # Raised if the user enters invalid data (non-numeric values)
                print("Invalid input! Please enter numerical values for Scope 2 emissions. Let's try again.")

        # Collect Scope 3 data (Indirect value chain emissions)
        while True:
            print("\nScope 3 (Indirect value chain emissions)")
            try:
                supplier_emissions = float(input("Supplier-related emissions (kg of CO2e): "))
                transportation = float(input("Transportation and logistics (kg of CO2e): "))
                waste = float(input("Waste generated in operations (kg of CO2e): "))
                employee_commuting = float(input("Employee commuting (kg of CO2e): "))
                break  # Exit loop once valid data is entered
            except ValueError:
                # Raised if the user enters invalid data (non-numeric values)
                print("Invalid input! Please enter numerical values for Scope 3 emissions. Let's try again.")

        # Generate a unique report ID and timestamp for the report
        report_id = str(uuid.uuid4())

        # Get the current timestamp (seconds since epoch)
        timestamp = int(datetime.now().timestamp())

        # Return the collected data as a dictionary
        return {
            "client_name": client_name,
            "report_id": report_id,
            "timestamp": timestamp,
            "unit": "kg of CO2e",
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

    except KeyboardInterrupt:
        # Raised if the user interrupts data entry
        print("\nData collection interrupted by the user. Exiting...")
        return
    except Exception as e:
        # Handle any unexpected errors and print the error message
        print(f"An unexpected error occurred: {e}")
        return
