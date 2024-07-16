// Working With Strings
// See https://aka.ms/new-console-template for more information
Console.WriteLine("Working With Strings");
// Declare a string - extra spaces are for demonstration
string firstName = "            Fredric";
string lastName = "Gluck           ";
string fullName;
string jobTitle = " Senior Instructor   ";
// Methods for String Objects

// Removing spaces at start, end and both
Console.WriteLine("*** Trim Method for Strings ***");
firstName = firstName.TrimStart(); // trim spaces at start
lastName = lastName.TrimEnd(); // trim spaces at end
Console.WriteLine("*** String Interpolation ***");
// $ specifies to use string interpolation where the value
// of variables betweeb {} is substituted in the string.
Console.WriteLine($"Your Name is: {firstName} {lastName}");
jobTitle = jobTitle.TrimStart();
Console.WriteLine($"Your Current Job Title is: {jobTitle}");
// String Concatination using the + operator
fullName = firstName + " " + lastName;
// Searching strings (substrings)
Console.WriteLine("*** Searching Strings***");
// Replace (and other methods)
// Type string name followed by . to show available methods for the object
// to be listed. Most likely items have a star.
jobTitle.Replace("Senior","Distinguished"); // This does not change the value of jobTitle but returns a new string.
// Strings in .NET are immutable -- they (not the variable they are assigned to)
// can not be changed.
Console.Write($"Congratulations {fullName}, you have been promoted to {jobTitle.Trim().Replace("Senior","Distinguished")}");
Console.WriteLine($" from your previous position as {jobTitle.TrimEnd()}.");
