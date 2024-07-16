// 14_SortingSearchingLists
/* Lots of Analysis on This -- Why aren't we getting
 the expected results?
 Hints: is F different than f? 
 Does sorting change the list?
 How does the modifying the output change the list?
 Copy this code to fix it!
*/ 

Console.WriteLine("Sorting And Searching Lists");
var ListOfNames = new List<string> // declare a variable that is a list object that contains strings
{ 
    "scott",
    "ana",
    "xavier",
    "helen",
    "paige",
    "filipe",
    "eric"
};
Console.WriteLine("**Before The Sort...");
foreach (var firstName in ListOfNames)  // iterate through the list
    {   // Make sure we have initial caps
        Console.WriteLine($"{char.ToUpper(firstName[0])+ firstName.Substring(1)}"); // output each item in Initial Caps
    };

Console.WriteLine($"I found Filipe at index {ListOfNames.IndexOf("Filipe")}");
Console.WriteLine($"I didn't find Fredric at index {ListOfNames.IndexOf("Fredric")}");

//Now Let's Sort The List 
Console.WriteLine();
Console.WriteLine("**After The Sort...");
ListOfNames.Sort();
foreach (var i in ListOfNames)  // iterate through the list
    {
        Console.WriteLine($"{i}!"); // output each item (no modifications)
    };

Console.WriteLine($"I found filipe at index {ListOfNames.IndexOf("filipe")}");
Console.WriteLine($"I didn't find fredric at index {ListOfNames.IndexOf("fredric")}");

