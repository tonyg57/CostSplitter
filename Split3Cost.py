# Split3Cost.py
# Updated 17-OCT-2024

import itertools

# Define the list of motel costs - Make sure these have unique names!
motel_costs = {
    "Santa Maria": 140,
    "Fresno": 136,
    "Oakhurst": 178,
    "Sonora": 167,
    "Visalia": 182,
    "Kernville": 143
}

# Calculate the total cost
total_cost = sum(motel_costs.values())

# Calculate the ideal split for three people
ideal_split = total_cost / 3

# Generate all combinations of motels to assign to three people (i.e. Gary, Bill, and Tony)
combinations = itertools.combinations(motel_costs.keys(), len(motel_costs) // 3)

# Initialize variables to keep track of the best solution
best_split = None
smallest_max_owed = float('inf')

# Iterate through all combinations
for combo in combinations:
    gary_motel_costs = sum(motel_costs[m] for m in combo)
    remaining_motels = set(motel_costs.keys()) - set(combo)
    remaining_combinations = itertools.combinations(remaining_motels, len(remaining_motels) // 2)
    
    for combo_bill in remaining_combinations:
        bill_motel_costs = sum(motel_costs[m] for m in combo_bill)
        tony_motel_costs = total_cost - gary_motel_costs - bill_motel_costs
        max_owed = max(gary_motel_costs, bill_motel_costs, tony_motel_costs)

        if max_owed < smallest_max_owed:
            smallest_max_owed = max_owed
            best_split = (combo, combo_bill, set(motel_costs.keys()) - set(combo) - set(combo_bill))

# Determine the costs for each person
gary_group, bill_group, tony_group = best_split
gary_cost = sum(motel_costs[m] for m in gary_group)
bill_cost = sum(motel_costs[m] for m in bill_group)
tony_cost = total_cost - gary_cost - bill_cost

# Print the results
print(f"Total lodging cost is ${total_cost:.2f} and the three-way split cost is ${ideal_split:.2f}")
print(f"Gary pays for the following motels in: {', '.join(gary_group)}")
print(f"Bill pays for the following motels in: {', '.join(bill_group)}")
print(f"Tony pays for the following motels in: {', '.join(tony_group)}")
print(f"Total amount Gary pays: ${gary_cost:.2f}")
print(f"Total amount Bill pays: ${bill_cost:.2f}")
print(f"Total amount Tony pays: ${tony_cost:.2f}")

# Calculate the amounts owed
amounts_owed = {
    "Gary": gary_cost - ideal_split,
    "Bill": bill_cost - ideal_split,
    "Tony": tony_cost - ideal_split,
}

# Determine who owes whom
for person, amount in amounts_owed.items():
    if amount < 0:  # This person owes money
        for creditor, creditor_amount in amounts_owed.items():
            if creditor != person and creditor_amount > 0:  # The creditor is owed money
                owed_amount = min(abs(amount), creditor_amount)
                print(f"{person} owes ${owed_amount:.2f} to {creditor}")
                amounts_owed[person] += owed_amount  # Adjust owed amounts
                amounts_owed[creditor] -= owed_amount  # Adjust creditor's owed amounts

exit_program = input('Press enter to quit... ')
if exit_program == "":
    exit()

