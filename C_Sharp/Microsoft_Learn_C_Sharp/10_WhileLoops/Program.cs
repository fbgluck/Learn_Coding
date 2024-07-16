// Loops

Console.WriteLine("Loops - Repeating Statements");
/*
A loop is a set of statements that repeat 
 While loops will repeat a set of instructions
until the condition tests false.

Programming practice: DRY -- Don't Repeat Yourself

*/
Console.WriteLine("*** While Loop (Pt 10) ***");
int counter = 0;
while (counter < 5) // check condition. If true, will run block.
{
    Console.WriteLine($"While Loop: The value of counter is {counter}");
    /*
     ++ is an operator that increments its variable by 1
     It is a shortcut for counter = counter + 1
    */
    counter++;
}
Console.WriteLine($"We are done with the 'while loop'. The value of Counter is {counter}");
Console.WriteLine("");

Console.WriteLine("*** Do while loop ***");
counter = 0; // reset the counter
do
{
    Console.WriteLine($"Do While Loop: The value of counter is now {counter}");
    counter++;
}
while (counter < 5); // Condition tested at the end of the loop
Console.WriteLine($"We are done with the 'do while' loop. Counter is {counter}");
Console.WriteLine(" ");

Console.WriteLine("*** For Loop***");
// For loop (Pt 11)
counter = 0;
for (
    int i = 0; // initial state. i exists for the scope of the loop
    i < 5; // this this conditional each time
    i++ // increment
    )
// for (int i = 0; i < 5; i++) // preferred shortcut  notation
// type 'for' to show snippet and keyword from intellisense 

{
    Console.WriteLine($"For Loop: The value of i is now {i}");
    counter++;
}
// Console.WriteLine($"The final value of i is {i}"); // Try this an see what happens
Console.WriteLine($"For Loop: We are done with the 'for' loop. The final value of i is {counter}");

// *** Combined For loop and if ***
Console.WriteLine(); // just a blank line
Console.WriteLine("*** Combined For Loop and if ***");
for (int i = 0; i < 5; i++) 
{
    if (i==3)
        {
            Console.WriteLine($"Combined: The value of i is {i}");
        }
}