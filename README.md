# Carbon Footprint Monitoring Tool

A Carbon Footprint Monitoring Tool that enables organizations to input client data,
calculate and visualize their carbon emissions, and generate detailed reports with suggestions for reduction,
covering all three recognized emission scopes:

- **Scope 1** emissions are direct emissions from owned or controlled sources.
- **Scope 2** emissions are indirect emissions from the generation of purchased energy.
- **Scope 3** emissions are all indirect emissions (not included in scope 2) that occur in the value chain of the
  reporting company, including both upstream and downstream emissions.

## Features

- **Data Collection**: Prompt users to input client information and emissions data for each scope.
- **Report Generation**: Create and store structured reports as JSON files, each containing a unique report ID,
  timestamp, and emission details.
- **Summaries and Insights**: Combine data from multiple reports to calculate average emissions, identify common
  suggestions, and highlight trends.
- **Visualizations**: Present data as pie charts (for single reports) and bar charts (for summaries) to simplify
  interpretation and highlight key areas for improvement.
- **Suggestions for Reduction**: Suggest actions when emissions exceed predefined thresholds, encouraging users to
  optimize operations and adopt cleaner practices.
- **Error Handling**: Handle invalid input or file-related issues and provide clear feedback to the user.

## Project Structure

```
carbon-footprint-tool/
│
├── tool/
│   ├── classes/
│   │   ├── monitor.py
│   │   └── report.py
│   │
│   ├── functions/
│   │   ├── collect_data.py      
│   │   ├── generate_report.py   
│   │   ├── generate_summary.py  
│   │   ├── suggest_reductions.py
│   │   └── visualize_data.py    
│   │
│   ├── reports/
│   │   └── ... (report files)   
│   │
│   └── carbon_footprint_tool.py
│
├── requirements.txt
└── README.md
```

The project is structured into several modules and functions, each responsible for a specific aspect of the carbon
footprint monitoring process. Here is an overview of its organization:

1. **tool**: This directory contains the core functionality of the tool, including the following:
    - _classes_: Contains the classes used by the tool.
    - _functions_: Contains several Python modules that implement different functionalities.
    - _carbon_footprint_tool.py_: The main entry point for the tool.
2. **reports**: This directory contains several JSON files, each representing a carbon footprint report.
3. **README.md**: The project's README file, which contains instructions and documentation for the tool.
4. **requirements.txt**: Contains a list of Python packages and their versions which are used by the tool and are
   required to run it.

## Installation

The project is created using Python `3.13.0`. Follow these steps in order to install the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/pouya-bn/carbon-footprint-tool.git
   cd carbon-footprint-tool
   ```

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the tool**:
   ```bash
   python tool/carbon_footprint_tool.py
   ```

2. **Select an option from the menu**:
    - **Option 1**: Add new Carbon footprint data  
      Enter the client name and emissions data as prompted. The tool will validate inputs and save a new report file in
      `tool/reports/`.
    - **Option 2**: Generate summary of all reports  
      The tool will aggregate data from all JSON files in `tool/reports/`, calculate averages, identify common
      suggestions, and display both text-based summaries and visualizations.
    - **Option 3**: Exit  
      Ends the program gracefully.

## Viewing Reports and Summaries

- **Reports** are saved as JSON files in the `tool/reports` directory. Each file contains detailed emission data, a
  unique report ID, and suggestions.
- **Visualizations** open in a new window using `matplotlib`. Pie charts show the distribution of emissions for a single
  report, while bar charts represent average emissions across all reports, making it easy to spot trends and prioritize
  reduction efforts.

## Troubleshooting

- **FileNotFoundError or PermissionError**: Ensure that the `reports` directory exists and that you have the necessary
  write permissions.
- **Invalid Input**: If non-numeric values are entered where numbers are expected, the tool prompts you to try again.
- **Missing Data**: If mandatory fields are not provided, the tool either requests the input again or exits with an
  error message.
