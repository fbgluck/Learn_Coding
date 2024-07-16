// Working with Numbers
// How to ensure your math is precise and accurate!
// Ref: https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/tutorials/numbers-in-csharp-local
Console.WriteLine("Working With Numbers");
int a = 222222100; // declaring an variable to be of type integer
int b = 222222221; // What is the largest number represented by int?
/* other types in C#
int: max number = 2^32 (32-bit signed integer)
long: nax number = 2^64 (64-bit signed integer)
*/
long c = (long)a + (long)b; // compiler instructions. Do math as long.
Console.WriteLine ($"The result is: {c}");

// Why do we get this answer?
int d = (int)42.1;
int e = (int)11.2;
long f = checked(d+e);
Console.WriteLine ($"The value of f is {f}");

/* double and float
 double and float math is not exactly precise but a bit
squishy or imprise after the significant digits
*/
double  g = 42.1;  // the natural (assumed) type of g is double
float h = 38.2F; // the F forces it to a float
double i =  g + h;
Console.WriteLine ($"The value of i (double + float) is {i}");


// decimal -- the most accurate but takes up more space
decimal  j = 42.1M;  // M is an explicit type
decimal k = 38.2M; 
decimal m =  j + k;
Console.WriteLine ($"The value of m (decimal + decimal) is {m}");

