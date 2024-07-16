// Lists, Arrays and Indexing
Console.WriteLine("Lists, Arrays and Indexing");
// Define a list of names to work with
var ListOfNames = new List<string> // declare a variable that is a list object that contains strings
{ 
    "Scott",
    "Ana",
    "Filipe",
    "Helen",
    "Paige"
};
Console.WriteLine();
Console.WriteLine("Here is our list...");
foreach (var firstName in ListOfNames)  // iterate through the list
    {
        Console.WriteLine($"{firstName.ToUpper()}!"); // output each item in UPPERCASE
    }

Console.WriteLine();
Console.WriteLine($"1. Your list has {ListOfNames.Count} entries.");
/* Index - Position of an item in the list
NOTE that positions start with [0]
*/
Console.WriteLine();
Console.WriteLine(" *** Retrieving a Specific Item In The List ***");
Console.WriteLine($"2. The first item in the list is {ListOfNames[0]}");
Console.WriteLine($"2. The third item in the list is {ListOfNames[2]}");
// How to find the last name in the list if you don't know how long the list is
Console.WriteLine($"2. TIP: The last name is the list is {ListOfNames[ListOfNames.Count-1]}");
// Count from the back of the array (List) - Not Zero based
Console.WriteLine();
Console.WriteLine($"*** Count backwards in the array to find the index...");
Console.WriteLine($"3. The Second-To-Last Item in the Array is {ListOfNames[^2]}");
// Get Ranges of items in a list
Console.WriteLine();
Console.WriteLine($"*** Get Ranges of Items In A List");
foreach(var firstName in ListOfNames[2..4]) // Give me including 2 through before 4
{
    Console.WriteLine($"{firstName}");
}
/* Arrays (Compared to Lists)
 Arrays are also a collection of items 
 Arrays are a fixed length. You can't add to them
*/
Console.WriteLine();
Console.WriteLine(" ** Arrays -- another type of data structure");
var arrayNames = new string[] { "ArrayName1","ArrayName2","ArrayName3","ArrayName4"};
foreach (var name in arrayNames) {
    Console.WriteLine($"4. {name}");
}

Console.WriteLine();
Console.WriteLine("*** Adding an item to an array");
/* With Arrays, the only way to add an item is to create a new array,
copy the old items into it and then add one. Here is a new 
feature is C# 12.

Use arrays when you want fixed sizes (memory) otherwise use Lists
*/
// ..<name> is a way to say "copy the current items in <name>
arrayNames = [..arrayNames,"** AddedName"];
foreach (var name in arrayNames) {
    Console.WriteLine($"5. {name}");
}

/* 
    NOTE: *** Lists and arrays can be a collection of any data types
*/
var ListOfScores = new List<int> // declare a variable that is a list object that contains integers
{ 
    112,
    34,
    74566,
    20,
    399
};
// Using Synchronized lists
Console.WriteLine();
Console.WriteLine("*** List of Current Scores");
for (var i=0;
     i<ListOfScores.Count;
     i++
     )
{
    Console.WriteLine($"{ListOfNames[i]}: {ListOfScores[i]}");
}
