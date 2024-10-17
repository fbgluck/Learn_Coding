## Fizz Buzz Test - 
loop_counter = 0
while loop_counter <= 99:
  loop_counter += 1
  if loop_counter % 15 == 0:
      print(f"{loop_counter} : fizzBuzz (5 and 3)")
      continue
  elif loop_counter % 3 == 0:
      print(f"{loop_counter} : fizz (3)")
      continue
  elif loop_counter % 5 == 0:
      print(f"{loop_counter} : buzz(5)")
      continue
  else:
    print(f"{loop_counter} : neither fizz nor buzz")


