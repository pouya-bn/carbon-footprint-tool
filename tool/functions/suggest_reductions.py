def suggest_reductions(data):
    suggestions = {}
    if sum(data["scope_1"].values()) > 10000:
        suggestions["scope_1"] = "Consider optimizing fuel usage, adopting electric vehicles, or upgrading equipment."
    if sum(data["scope_2"].values()) > 10000:
        suggestions["scope_2"] = "Switch to renewable energy sources or implement energy-efficient practices."
    if sum(data["scope_3"].values()) > 20000:
        suggestions["scope_3"] = "Engage suppliers on sustainability, improve waste management, and optimize logistics."
    return suggestions