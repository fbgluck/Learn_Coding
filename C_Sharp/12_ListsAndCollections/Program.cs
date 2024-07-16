// 12_ListsAndCollections
Console.WriteLine("12_Lists and Collections");
/*
Lists are for containing data
List<T> = Pronounced List of T (T means type)
List<T> class
**********************/
/*
 NEW INFO: type 'var' is a Local Variable Type Inference.
 This means that you are letting C# try to figure out what
 type the variable is based on its use on the right hand side).
 Right hand side MUST be explicit.
 
 Non var example:
List<string> ListofNames = new List<string>();
*/
var ListOfNames = new List<string> // declare a variable that is a list object that contains strings
{               // Add 3 strings to lists
    "Scott",
    "Ana",
    "Filipe",
};
// ... and iterate through the list
// We could iterate using a regular for loop and indexing into a list
Console.WriteLine("*** Iteration using a 'for' loop ***");
for (int i=0; i < ListOfNames.Count; i++)
    {
        Console.WriteLine($"1. Hello {ListOfNames[i].ToUpper()}!");
    }
// but the foreach loop is a bit easier
Console.WriteLine();
Console.WriteLine("*** Iteration using a 'foreach' loop ***");
//  foreach (var name in names)... tradition to have a singular name for var and plural name for list collection
foreach (var firstName in ListOfNames)  // iterate through the list
    {
        Console.WriteLine($"2. Hello {firstName.ToUpper()}!"); // output each item in UPPERCASE
        // strings are immutable so we are actually getting a new string when we convert to UPPER
    }
Console.WriteLine();
Console.WriteLine("*** More Methods to use with Lists ***");
// Lists are not immutable
ListOfNames.Add("Willie(added)"); // Add a name to the end of the list
ListOfNames.Add("Kayla(added)");
ListOfNames.Remove("Ana");
foreach (var firstName in ListOfNames)  // iterate through the list
    {
        Console.WriteLine($"3. Hello {firstName.ToUpper()}!"); // output each item in UPPERCASE
    }

