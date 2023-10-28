import itertools

# Define the list of motel costs
motel_costs = {
    "Morro Bay": 202.58,
    "San Rafael": 246.38,
    "Fort Bragg": 152.52,
    "So. Lake Tahoe": 252.44,
    "June Lake": 288.96,
    "Sanger": 200.78,
    "Kernville": 153.10
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

if gary_cost > bill_cost and gary_cost > tony_cost:
    if bill_cost - ideal_split < 0:
        print(f"Bill owes ${abs(bill_cost - ideal_split):.2f} to Gary")
    else:
        print(f"Gary owes ${bill_cost - ideal_split:.2f} to Bill")
    
    if tony_cost - ideal_split < 0:
        print(f"Tony owes ${abs(tony_cost - ideal_split):.2f} to Gary")
    else:
        print(f"Gary owes ${tony_cost - ideal_split:.2f} to Tony")

elif bill_cost > gary_cost and bill_cost > tony_cost:
    if gary_cost - ideal_split < 0:
        print(f"Gary owes ${abs(gary_cost - ideal_split):.2f} to Bill")
    else:
        print(f"Bill owes ${gary_cost - ideal_split:.2f} to Gary")
    
    if tony_cost - ideal_split < 0:
        print(f"Tony owes ${abs(tony_cost - ideal_split):.2f} to Bill")
    else:
        print(f"Bill owes ${tony_cost - ideal_split:.2f} to Tony")

elif tony_cost > gary_cost and tony_cost > bill_cost:
    if gary_cost - ideal_split < 0:
        print(f"Gary owes ${abs(gary_cost - ideal_split):.2f} to Tony")
    else:
        print(f"Tony owes ${gary_cost - ideal_split:.2f} to Gary")
    
    if bill_cost - ideal_split < 0:
        print(f"Bill owes ${abs(bill_cost - ideal_split):.2f} to Tony")
    else:
        print(f"Tony owes ${bill_cost - ideal_split:.2f} to Bill")

else:
    print(f"The costs were evenly split!")

exit_program = input('Press enter to quit... ')
if exit_program == "":
    exit()
