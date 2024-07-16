// Language Integrated Query (LINQ) and IEnumerable [Pt 15]
// Produces an object (IEnumerable) that contains items meeting a query
// It's a more efficient way than iterating and testing each element
Console.WriteLine("Language Integrated Query (LINQ) and IEnumerable [Pt 15]");
//  Define the Data Source - A List of integers called Scores
// Could be the scores from a test

List<int> scores = [12,31,20,60,103,90,21,30];

// Define the query expression 
IEnumerable<int> scoreQuery =  // the resultant object contains int but can by other type
    from score in scores // as it iterates and tests, each item in the collection is called score
    where score > 50  // the criteria (condition)
    select score;  // the action / answer. If it meets criteria, add it to object
foreach (var i in scoreQuery) // now iterate throug the result object
    Console.WriteLine($"1. Found a score over 50: {i}");

// You can do a conversion from an IEnumberable to a List for further processing

Console.WriteLine();
Console.WriteLine("*** Convert from IEnumberable to a List *** ");
var ListOfScores =scoreQuery.ToList(); // Convert IE to new list
int listIndex = 0;
foreach (var theScore in ListOfScores) // Iterate through the list
{
    Console.WriteLine($"2. List Index {listIndex}: {theScore}");
    listIndex++; 
}

// LINQ - Query Expression Basics

List<int> scores1 = [12,31,20,60,103,90,21,30];

// Define the query expression 
IEnumerable<int> descendingScoreQuery =  // the resultant object contains int but can by other type
    from score1 in scores1 // as it iterates and tests, each item in the collection is called score1
    where score1 > 50  // the criteria (condition)
    orderby score1 descending // sort the results highest to lowest
    select score1;  // the action. If it meets criteria, add it to object
Console.WriteLine();
Console.WriteLine("Sorting the Result");
foreach (var i in descendingScoreQuery) // now iterate through the result object
    Console.WriteLine($"3. Found a sorted score over 50: {i}");

// IE as type string changes the foreach
Console.WriteLine();
Console.WriteLine("*** Changing the query output in the loop");

List<int> scores2 = [12,31,20,60,103,90,21,30,95,80,71];

IEnumerable<string> stringQuery =  // the resultant object contains strings
    from score2 in scores2 // as it iterates and tests, each item in the collection is called score1
    where score2 > 50  // the criteria (condition)
    orderby score2 descending // sort the results highest to lowest
    select $"4. Found a sorted score of {score2}";  // the action. If it meets criteria, add it to object
Console.WriteLine();
Console.WriteLine($"Found {stringQuery.Count()} scores > 50: ");
 // now iterate through the result object
foreach (string s in stringQuery)
{
     Console.WriteLine(s); // wrote the result of the select
}

// LINQ as Functions (an alternate way to write the query)
Console.WriteLine();
Console.WriteLine("*** A Method based way to do queries");

List<int> scores3 = [12,31,20,60,103,90,21,30,95,80,71,99];
// Uses Lambda expression => read as "such that".
// s is the parameter (arg) passed to the function 
var scoreQuery3 = scores3.Where(s => s > 50).OrderByDescending(s => s);
foreach (int s in scoreQuery3)
{
     Console.WriteLine($"5. Found a sorted score of {s}"); // wrote the result of the select
}