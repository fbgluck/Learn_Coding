// See https://aka.ms/new-console-template for more information
// Read name from console
Console.WriteLine("What is your name?");
var name = Console.ReadLine();
// Get current date and time
var currentDate = DateTime.Now;
Console.WriteLine("Hello, World!");
Console.WriteLine($"{Environment.NewLine}Hello, {name}. Today is {currentDate:d}");