using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Write_Your_First_And_Last_Name
{
    class Program
    {
        static void Main(string[] args)
        {
            string ageNow; // console input
            DateTime currentTime = DateTime.Now;  // A dateTime Object set to the current date and time
            int ageAsInt; // console input converted to integer
            bool doInputTest = true; // used to determine if console input met conditions
            double sqrtAnswer;

/* ************* Question 6  */
            Console.WriteLine(" My name is: Fredric Gluck");

/* *************  Question 7 */
            Console.WriteLine("Print a sequence of numbers ....");
            Console.WriteLine (1);
            Console.WriteLine(100);
            Console.WriteLine(1001);

/* *************  Question 8 */
            Console.WriteLine("It is now: " + currentTime);
            Console.WriteLine("In 10 years, it will be: " + currentTime.AddYears(10));

/* *************  Question 9 */
            sqrtAnswer = Math.Sqrt(12345);
            Console.WriteLine("The square root of 12345 is: " + sqrtAnswer);

/* ************* Question 10 */
            for (int i=2; i <= 102; i++)
            {
                // Check if our loop is dealing with an odd or even number
                if (i % 2 != 0) // Check to see if the number is even
                {
                    Console.WriteLine(-1 * i); // if so, write it's negagative equivalent
                }
                else
                {
                    Console.WriteLine(i); // otherwise, just write the number
                }
            } // end of for loop

/* ************* Question 11 Write a program that reads your age from the console and prints your age after 10 years */

            while (doInputTest) // We have not failed the input test
            { 
                Console.Write("What is your age now? ");                  // Read from the console to a variable
                ageNow = Console.ReadLine();
                if (int.TryParse(ageNow, out ageAsInt))                   // We try to convert the input from the console into an integer
                {
                    ageAsInt = ageAsInt + 10;
                    Console.WriteLine("You will be: " + ageAsInt + " in 10 years.");
                    doInputTest = false;

                }
                else            // conversion to integer failed
                {
                    Console.WriteLine("You did not enter an integer!");
                    doInputTest = true;
                }
            }
        }
    }
}
