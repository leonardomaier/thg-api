def extract_population_by_year(data):
    state_populations = {}
    for entry in data:
        year = entry["Year"]
        population = entry["Population"]
        state = entry["Geography"]

        if state not in state_populations:
            state_populations[state] = []

        state_populations[state].append((year, population))

    for state, populations in state_populations.items():
        state_populations[state] = sorted(populations)

    return state_populations