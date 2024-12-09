from tool.classes.monitor import CarbonFootprintMonitor

# Entry point of the program when running the script
if __name__ == "__main__":
    try:
        # Instantiate the CarbonFootprintMonitor and run the tool
        monitor = CarbonFootprintMonitor()
        monitor.run()

    except Exception as exception:
        # Handle any errors during the initialization or execution of the program
        print(f"Failed to initialize the Carbon Footprint Monitor: {exception}")
