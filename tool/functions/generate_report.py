from tool.classes.report import Report


def generate_report(data_dir, data):
    if not data:
        print("No data provided. Cannot generate a report.")
        return

    report = Report(data)
    report.save(data_dir)
    report.display_suggestions()
