from itertools import combinations

def solution(num_buns, num_required):
    # Generate all combinations of bunnies that could be given a particular key,
    # such that each combination has 'num_buns - (num_required - 1)' bunnies.
    # This ensures that any group of 'num_required' bunnies will have the key.
    key_combinations = list(combinations(range(num_buns), num_buns - (num_required - 1)))

    # Initialize a list to hold the keys each bunny will receive.
    bunnies_keys = [[] for _ in range(num_buns)]

    # Assign keys to the bunnies based on the combinations calculated.
    # Each key (represented by its index in 'key_combinations') is assigned to the bunnies
    # in that combination. This loop iterates through all the keys.
    for key_index, bunnies_with_key in enumerate(key_combinations):
        for bunny in bunnies_with_key:
            bunnies_keys[bunny].append(key_index)

    return bunnies_keys

print(solution(3, 1))
print(solution(2, 2))
print(solution(3, 2))
print(solution(4, 4))
print(solution(5, 3))