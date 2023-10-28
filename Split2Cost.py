# Cost splitting for two persons
# Modified from ChatGPT suggestion
# 21-SEP-2023

import itertools

# Define the list of motel costs - Make sure these have unique names!
motel_costs = {
    "Morro Bay": 101.29,
    "San Rafael": 123.19,
    "Fort Bragg": 76.26,
    "So. Lake Tahoe": 126.22,
    "June Lake": 144.48,
    "Sanger": 100.39,
    "Kernville": 76.55
}

# Calculate the total cost
total_cost = sum(motel_costs.values())

# Calculate the ideal split
ideal_split = total_cost / 2

# Generate all combinations of motels to assign to two people (i.e. Bill & Tony)
combinations = itertools.combinations(motel_costs.keys(), len(motel_costs) // 2)

# Initialize variables to keep track of the best solution
best_split = None
smallest_max_owed = float('inf')

# Iterate through all combinations
for combo in combinations:
    bill_motel_costs = sum(motel_costs[m] for m in combo)
    tony_motel_costs = total_cost - bill_motel_costs
    max_owed = max(bill_motel_costs, tony_motel_costs)

    if max_owed < smallest_max_owed:
        smallest_max_owed = max_owed
        best_split = (combo, set(motel_costs.keys()) - set(combo))

# Determine which person gets the more expensive cost group
bill_group, tony_group = best_split
bill_cost = sum(motel_costs[m] for m in bill_group)
tony_cost = total_cost - bill_cost

# Print the results (Names Bill & Tony can be globally replaced from this point down)
print(f"Total lodging cost is ${total_cost:.2f} and the even split cost is ${ideal_split:.2f}")
print(f"Bill pays for the following motels in: {', '.join(bill_group)}")
print(f"Tony pays for the following motels in: {', '.join(tony_group)}")
print(f"Total amount Bill pays: ${bill_cost:.2f}")
print(f"Total amount Tony pays: ${tony_cost:.2f}")
#print(f"Settlement amount (lesser payer owes to larger payer): ${smallest_max_owed - ideal_split:.2f}")
if bill_cost > tony_cost:
    print(f"Tony owes Bill: ${smallest_max_owed - ideal_split:.2f}")
elif tony_cost > bill_cost:
    print(f"Bill owes Tony: ${smallest_max_owed - ideal_split:.2f}")
elif bill_cost == tony_cost:
    print(f"The costs were evenly split!")

exit_program = input('Press enter to quit... ')
if exit_program == "":
    exit
