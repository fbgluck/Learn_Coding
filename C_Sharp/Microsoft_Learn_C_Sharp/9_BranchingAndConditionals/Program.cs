// Branching, Ifs and Conditional Logic (Boolean)
Console.WriteLine("Branching, Ifs and Conditional Logic");
// Boolean

int a = 5;
int b = 6;

if ((a+b)>10) // Optional inner parens for order of operations (PEMDAS)
{   // Curley Braces or Mustaches
    Console.WriteLine("1. The answer is greater than 10. ");
}
// Define a variable of type Boolean and assign it a value (TRUE of FALSE)
int c = a + b;
bool mytest = c > 10;
if (mytest) // the testing condition
{
    Console.WriteLine("2. The answer is still greater than 10.");
}
b = 4; // Give a new value to b so we can show the else clause
c = a + b; // Recalculate since we gave a new value to b
mytest = c > 10;
// Else Clause
Console.WriteLine("** Else Clause **");
if (mytest)
{
    Console.WriteLine("3. The answer is still greater than 10."); // You can nest "if" statemets\
}
    else
{
    Console.WriteLine($"4. The answer is NOT greater than 10. c is now {c}");    
}
Console.WriteLine("** More Boolean Operations ** ");
int d = 5;
int e = 20;
bool f = d < e;
if ((d + e > 20) && (d > 4)) // Boolean AND comparison
{
    Console.WriteLine ("5. Both Conditions are TRUE");
}
else
{   
    Console.WriteLine ("6. Both conditions are not true");
}

if ((d + e > 20) && (d == 4)) // Boolean AND comparison. == is comparison. = is assignment
{
    Console.WriteLine ("7. Both Conditions are TRUE");
}
else
{   
    Console.WriteLine ("8. Both conditions are not true");
}

if ((d + e > 20) || (d == 4)) // Boolean OR comparison. == is comparison. = is assignment
{
    Console.WriteLine ("9. At least one of the conditions are TRUE");
}
else
{   
    Console.WriteLine ("10. Both of the conditions are FALSE");
}
// Other Boolean Operators in C#
// ....