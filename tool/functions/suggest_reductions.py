def suggest_reductions(data):
    """
    Analyzes the carbon footprint data provided for Scope 1, Scope 2, and Scope 3 emissions and
    provides suggestions for reducing carbon emissions based on thresholds for each scope.

    This function examines the total emissions in each scope and, if they exceed predefined
    thresholds, provides actionable suggestions for reducing emissions. If the data for any of
    the scopes is missing or invalid, an error is raised, and the function returns an empty dictionary.
    """
    try:
        suggestions = {}

        # Check Scope 1 emissions and suggest reductions if necessary
        if "scope_1" in data:
            if sum(data["scope_1"].values()) > 10000:
                suggestions[
                    "scope_1"] = "Consider optimizing fuel usage, adopting electric vehicles, or upgrading equipment."
        else:
            # Raised if scope 1 is missing from the input data
            raise ValueError("Missing or invalid 'scope_1' data.")

        # Check Scope 2 emissions and suggest reductions if necessary
        if "scope_2" in data:
            if sum(data["scope_2"].values()) > 10000:
                suggestions["scope_2"] = "Switch to renewable energy sources or implement energy-efficient practices."
        else:
            # Raised if scope 2 is missing from the input data
            raise ValueError("Missing or invalid 'scope_2' data.")

        # Check Scope 3 emissions and suggest reductions if necessary
        if "scope_3" in data:
            if sum(data["scope_3"].values()) > 20000:
                suggestions[
                    "scope_3"] = "Engage suppliers on sustainability, improve waste management, and optimize logistics."
        else:
            # Raised if scope 3 is missing from the input data
            raise ValueError("Missing or invalid 'scope_3' data.")

        return suggestions

    except (ValueError, TypeError) as e:
        # Handle invalid data and missing keys gracefully
        print(f"Error in suggest_reductions: {e}")
        return {}
