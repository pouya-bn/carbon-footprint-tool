def suggest_reductions(data):
    try:
        suggestions = {}

        if "scope_1" in data:
            if sum(data["scope_1"].values()) > 10000:
                suggestions[
                    "scope_1"] = "Consider optimizing fuel usage, adopting electric vehicles, or upgrading equipment."
        else:
            raise ValueError("Missing or invalid 'scope_1' data.")

        if "scope_2" in data:
            if sum(data["scope_2"].values()) > 10000:
                suggestions["scope_2"] = "Switch to renewable energy sources or implement energy-efficient practices."
        else:
            raise ValueError("Missing or invalid 'scope_2' data.")

        if "scope_3" in data:
            if sum(data["scope_3"].values()) > 20000:
                suggestions[
                    "scope_3"] = "Engage suppliers on sustainability, improve waste management, and optimize logistics."
        else:
            raise ValueError("Missing or invalid 'scope_3' data.")

        return suggestions

    except (ValueError, TypeError) as e:
        print(f"Error in suggest_reductions: {e}")
        return {}
