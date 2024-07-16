// Fizz Buzz (from page 38)
let fizzString ="";
let buzzString="";
for (let counter=1; counter<=100; counter++) {
    if (counter % 3==0) {
        fizzString= "fizz";
    }
    if (counter % 5==0) {
        buzzString="buzz";
    }
        if (fizzString.length + buzzString.length == 0) { // neither fizz nor buzz
        console.log(counter);   // just output the counter value
    }
    else {
        console.log(fizzString+buzzString + " " + counter); // it's one or the other
        fizzString =""; // reset for the next round
        buzzString="";
    }
}