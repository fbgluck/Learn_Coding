using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ch2_Primitive_Types_and_Variables
{
    class Program
    {
        static void Main(string[] args)
        {
            /* Q1: ;;Declare Variables */
            ushort var1 = 52130;
            sbyte var2 = -115;
            uint var3 = 4825932;
            byte var4 = 97;
            short var5 = -10000;
            ushort var6 = 20000;
            byte var7 = 224;
            uint var8 = 970700000;
            byte var9 = 112;
            sbyte var10 = -44;
            int var11 = -1000000;
            ushort var12 = 1990;
            ulong var13 = 123456789123456789;

            /* Q3: Write a program that compares correctly two real numbers with an accuracy of 0.000001 */
            float side1 = 1.234567f; // floating type 
            float side2 = 1.234568f;
            float accuracy = 0.000001f;
            float sideDifference = Math.Abs(side1 - side2);
            bool equal = Math.Abs(sideDifference) < accuracy;
            Console.WriteLine("Value of side1 is: " + side1);
            Console.WriteLine("Value of side2 is: " + side2);
            if (equal)
            {
                Console.WriteLine(side1 + " and " + side2 + " are equal since their difference is less than " + accuracy + " (.000001). Their difference is: " + sideDifference);
            }
            else
            {
                Console.WriteLine(side1 + " and " + side2 + "are not equal. Their difference is " + sideDifference);
            }
            /* Q4 Initialize an integer variable in hex format */
            int var14InHex = 0x100;
            Console.WriteLine("The value or 0x100 as an decimal integer is: " + var14InHex);
            /* Q5 Assign a variable of type char as Unicode 72 */
            char var15Char = '\u0072';
            Console.WriteLine("The character with the unicode value of  Unicode 0072 is: " + var15Char);
            /* Q6: Declare a bool type */
            bool isMale = true;
            if (isMale)
            {
                Console.WriteLine("I am a male because the value of isMale is: " + isMale);
            }
            else
            { 
                Console.WriteLine("I am not a male because the value of isMale is: " + isMale);
            }
            /* Q7: Declare String Variables */
            string strHello = "Hello";
            string strWorld = "World";
            object objHelloWorld = strHello + " " + strWorld;
            Console.WriteLine("Here's What I Got To Say: " + objHelloWorld);
            /* Q8: Assigning a value to type Object. Use Typecasting */
            string concatedObject = (string)objHelloWorld;
            Console.WriteLine("The typecasted result is: " + concatedObject);
            /* Q9: Use of quotations */
            string strVar15 = "The \"use\" of quotations causes difficulties";
            string strVar16 = "The \u0022use\u0022 of quotations causes difficulties";
            Console.WriteLine("Here I used the escaping character for the double quote: " + strVar15);
            Console.WriteLine("Here I used Unicode character for the double quotes: " + strVar16);



        }
    }
}
