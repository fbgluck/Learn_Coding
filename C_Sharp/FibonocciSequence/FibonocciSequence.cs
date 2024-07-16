// See https://aka.ms/new-console-template for more information
// This program generates a Fibonocci Sequence from two consecutive numbers.
// A Fibonocci sequence is three numbers where the next number is the sum of the two previous numbers
Console.WriteLine("Fibonocci Sequence");
// Variables
int firstSequence;
int secondSequence;
int nextSequence;
Console.Write("Input the Starting Number of the sequence: "); // Console.Write will not put a newline after the output
firstSequence = Convert.ToInt32(Console.ReadLine()); // first number
secondSequence = firstSequence + 1; // next consecutive number
Console.WriteLine(firstSequence);
Console.WriteLine(secondSequence);

for (int i = 0; i < 10; i++)
{
    nextSequence = firstSequence + secondSequence; // calculate the next number in the sequence
    Console.WriteLine(nextSequence); // Output the next number in the sequence
    firstSequence = secondSequence; // reset for the next round
    secondSequence = nextSequence;
}

Console.WriteLine("Program complete....");