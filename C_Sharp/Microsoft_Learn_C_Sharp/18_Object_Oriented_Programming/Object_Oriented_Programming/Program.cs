// 18_Object_Oriented_Programming

/* 
Fact -- C# is an Object oriented language. That means that it interfaces
to the world through objects. Everything it does is done on an object. (The
program itself is an object that may contain other objects.)

Primitive Objects are types (objects) built in to C#. Examples
include string, int, float, bool

Sometimes, you want to make your own types of objects that 
have their own methods and properties (or states). You can change
the state of a object using its methods).

You create objects to model the world. An example might be creating an object
"book" that has properties like "date_published" or "authored_by"
and may have methods like "check_out" or "check_in". (Look at
Library of Congress CIP data for examples. You could make an object for each book using
the data in the CIP.)

Another example:  A C# string is an (primitive) object. It has a property (state)called length. length
can be manipulated by using the "trim" method.

As previously stated, at it's core, C# is an Object Oriented Language. Everything
in C# programs is an object. Up until now, we have allowed
the compiler to add code to make our programs into objects. (This convienent feature is
a relatively new one in C#.)

That's why a one line program like this this statement 

    Console.WriteLine("18_Object_Oriented_Programming");

is a complete program. Because the C# compiler is adding a lot of items behind the scene to
"object" it when you compile the program

Prior to this feature, a C# programmer would have to include code to create it's own
objects.

There are some cases where you want to do this manually instead of letting the compiler do it for us.
Mostly, we do this so we have more control.

Following is an example of how to do this:

*************************************************************************************** */

/* Have to tell the program where to find some core libraries it may need */
using System;
/* ---------------------------------------------------------
First, create a namespace 'container' so that objects
can be grouped together and differentiated from other objects that
may be part of the code. */
namespace oopDemo 
{   // curly brackets indicate the 'scope' (e.g. where it applies to)

    /*
    Now, create an object class called Person in this namespace. 
    This declares the object and its name (oopDemo.Person) and makes it public
    (as opposed to private) which declares that others can use it
    */
    public class famousPainter (string firstname, string lastname, DateOnly birthday)
    {
        /* This is the constructor for the object. When a Person object is instantiated (created)
        values are passed to the object and the properties are set */

        /* Defining the Member Fields of an object class 
        
        Now we define the member fields of the object class (firstname, lastname and birthday)  
        These properties (member fields) are marked private instead of public.
        
        As a best practice, instead of marking members as public you mark them as private so that these 
        states / properties are not exposed to the outside world. 

        (What's on the menu (the public face), is not necessarily what's in the kitchen.)
        */
        public string First {get; } = firstname;
        public string Last {get; } = lastname;
        public DateOnly Birthday {get; } = birthday;
        /* 
        {get;} means that I can only read this property and not change it
        {get; set;} is used if you want the property read and changed   
        */
        
    } // End of the definition for the object class Person
    
    /* Now define the object that contains the entry point to the program */
    public class MyApp 
    {
        /* Main is a special function that is the "entry point"
        for this class. 'void' says that the function is not going to return
        any values and is not expecting any arguments. All classes
        need and entrypoint function in this object called 'Main' */
        public static void Main()
        {
            /* And here's the code that is going to be executed
            when this class is called 
            */
            
            Console.WriteLine("18_Object_Oriented_Programming");
            /* We start by creating two new obects */
            var painter1 = new famousPainter ("Salvadore","Dali",new DateOnly(1860,1,1));
            var painter2 = new famousPainter ("VanGogh","Vincent",new DateOnly(1872,1,31));

            /* Now show how to access objects by placing them in a list */
            List<famousPainter>thePainter=[painter1,painter2];
            Console.WriteLine($"I know about {thePainter.Count} famous painters.");

            /* Now we show how to access the properties of these objects */
            Console.Write($"The painter: {painter1.First}");
            Console.Write($"{painter1.Last}");
            Console.WriteLine($" was born on: {painter1.Birthday}");
        } // end of Main method 
    } // End of the definition for the object class MyApp
} // end of namespace definition
