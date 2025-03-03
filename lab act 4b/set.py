# Define the sets based on the provided figure
A = {'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o'}
B = {'b', 'h', 'c', 'a', 'c', 'k', 'g', 'd', 'f', 'j', 'i'}
C = {'c', 'd', 'f', 'l', 'm', 'o'}

# a. How many elements are there in set A and B
num_elements_A = len(A)
num_elements_B = len(B)
print(f"a. Number of elements in set A: {num_elements_A}")
print(f"   Number of elements in set B: {num_elements_B}")

# b. How many elements are there in B that is not part of A and C
elements_B_not_in_A_and_C = B - (A | C)
num_elements_B_not_in_A_and_C = len(elements_B_not_in_A_and_C)
print(f"b. Number of elements in B that are not part of A and C: {num_elements_B_not_in_A_and_C}")

# c. Show the following using set operations
result_sets = {
    'i': {'h', 'i', 'j', 'k'},
    'ii': {'c', 'd', 'f'},
    'iii': {'b', 'c', 'h'},
    'iv': {'d', 'f'},
    'v': {'c'},
    'vi': {'l', 'm', 'o'}
}

print("c.")
for key, value in result_sets.items():
    print(f"{key}. {value}")