# Demonstration for Debugger
for i in range(1, 5):  # outer loop
    print(f"** {i} - in outer loop")
    for j in range(1, 3):   # inner loop
        print(f"    in inner loop i={i} -- j =={j}")
        if j % 2 == 0:
            print(f"      {j} is an even number ")
        else:
            print(f"     {j} is an odd number")
            print(f"Final values: i = {i}, j= {j}")
print(30*"-")
