// This file makes use of the pre .NET 6 template.  
// Post .NET uses recent C# features that simplify the code you need to write for a program and replaces it
// compiler features that generate Namespace, internal class statement and the Main Method. For additional info, 
// see  https://learn.microsoft.com/en-us/dotnet/core/tutorials/top-level-templates or generate a new project using
// the .NET Console template and see the URL in that template.
using System.Runtime.CompilerServices;
// a namespace is a way to collect related programs together so we can organize them into logical groups.
namespace RectangleAreaCalculator
{
    
/*
C# is an Object Oriented Programming Language
Everything we do in C# is a class. 
A class is a template used to create objects.
A class is a data structure in memory that contains fields (also called variables or attributes), properties, methods, and events
An object is an instance of the structure created from using a class as a blueprint.

This defines a class called Program. 
Internal means that it is not available outside of an object that is created from this class) of the class.
NOTE: This example is a basic but not an ideal illustration of an OOP because we are not using all the features of Classes and objects. 
*/
    internal class Program 
    {
/*
Inside of classes are methods (functions). Methods are pieces of a class that do something (as opposed to a Properties of a class that has a value).

In C#, each class has to have a Method called "Main". "Main" is the entry point for the class.
static means: the method belongs to this class not an instance of the class
void means: that it is not going to return (give back) anything
Main is the name of the method
() means that no arguments are passed to this method
*/
        static void Main ()
        {
            // Declare Variables
            double length; // length of the rectangle as type double
            double width; // width of the rectangle as type double
            double area; // the area of the rectangle as type double

            // Introduction and instructions to the user
            Console.WriteLine ("This program calcuates the area of a rectangle from user input of length and width.");
            // get user input from console and convert it from a string to a type of Double
            Console.Write("Input the length of the rectangle: "); // Console.Write will not put a newline after the output
            length = Convert.ToDouble (Console.ReadLine());
            Console.Write("Input the width of the rectangle: ");
            width = Convert.ToDouble (Console.ReadLine());
            // Call the Method to do the calculation
            area = CalculateRectangleArea(length, width);

            Console.WriteLine ($"The area of the rectangle is: {area}");
            Console.WriteLine ("Program complete....");
        } 
/*
This is another method called CalculateRectangleArea
static means: the method belongs to this class not an instance of the class
double means: that it will return a value of type double
CalculateRectangleArea is the name of the method
double side1 means: the first argument passed to it is type double and inside the method it is known as side1
double side2 meaans: the second argument passed to it is type double and inside the method it is known as side2
*/
        static double CalculateRectangleArea (double side1, double side2)
        {
            return (side1 * side2);
        }   
    }
}