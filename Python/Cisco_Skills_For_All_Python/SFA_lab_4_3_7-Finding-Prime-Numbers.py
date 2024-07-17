# SFA_lab_4_3_7-Finding-Prime-Numbers
# A prime number is a number that is only evenly divisible by
# 1 and itself. (That means that the remainder of
# every other result will not be 0)

def find_prime(target):
    # Start at target + 1, end at target -1
    for i in range(2, target):  # test entire range EXCEPT for 1 and the number
        # if any result in the range is 0 (evenly divisible)
        # print(f"Testing: {target}/{i} -- Result is {target/i}.")
        if target % i == 0:
            print(f"\n> The first factor of {target} is {i}")
            return (False)
   # We know this number is not prime so no more loop
    return (True)


def all_factors(target):
    # Start at target + 1, end at target -1
    num_factors = 0
    for i in range(2, target):  # test entire range EXCEPT for 1 and the number
        # if any result in the range is not evenly divisible

        if target % i != 0:
            print(f"A factor of {target} is {i}")  # it is a factor
            num_factors = num_factors + 1  # and we add one to the counter

    if num_factors != 0:  # We found at least one proof the number is not prime
        return (num_factors)
    else:
        return (0)


# PROGRAM STARTS HERE

test_result = all_factors(45)  # Returns number of factors
if test_result != 0:
    print(f"Number is not prime. Found {test_result} factors.")
else:
    print(f"Number is prime")
input("return to continue")
# Ask user for a number to test
item_to_test = int(input("What is the upper limit to test? >>> "))
for counter in range(1, item_to_test+1):
    if find_prime(counter):  # Number was determined to be prime
        print(f'\n** The number {counter} is prime **')
    else:
        print(f'The number {counter} is not prime')
