## Fizz Buzz Test - 
loop_counter = 0
while loop_counter <= 99:
  loop_counter += 1
  if loop_counter % 15 == 0:
      print("fizzBuzz")
      continue
  elif loop_counter % 3 == 0:
      print("fizz")
      continue
  elif loop_counter % 5 == 0:
      print("buzz")
      continue
  else:
    print(loop_counter)


