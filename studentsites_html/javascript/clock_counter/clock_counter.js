// This is the code to handle button press from the program

// Done when loaded
let intervalId; // make this variable global by declaring it

// Done when program is initialized
function initializeCounter() {
    counterValueText = 0;
// display starting value in field
counterValue.innerHTML = counterValueText;
}
// ---------------------------------------------------------------
// Done when either the +  or - button is pressed
// direction: 1 = increment counter, 0 = decrement counter
function doCounter(direction) {
    // Get current value from the screen
    let counterValueText = document.getElementById("counterValue").textContent;
    // Are we counting up or down?
    if (direction === 1) {  // counting up
        // convert the text from the field to a number
        counterValueNumber = Number(counterValueText) 
        // Increase the value by 1
        counterValueNumber++ 
        // Update the text in the field rewrite the inner HTML
        counterValue.innerHTML=counterValueNumber
}
else    // Direction is 0 which means decrement the counter
{       
        // Convert the text from the field to a number
        counterValueNumber = Number(counterValueText) 
        // Increase the value by 1
        if (counterValueNumber === 0) {
            // print an error message as an Alert -- can't decrement past 0
             window.alert("Can't Decrement Past 0");
        }
        else 
        {
            counterValueNumber-- 
            // rewrite the inner HTML
            // Update the text in the field
            counterValue.innerHTML=counterValueNumber
        }
    }
}
// ----------------------------------------------------------------
function startCountdown() {
    // Reference: https://developer.mozilla.org/en-US/docs/Web/API/setInterval
    // call countdown every 1000 ms
    intervalId = setInterval(countDown,1000);  // Just the name of the function, not calling the function itself
}

function countDown() {
    let displayValue = Number(document.getElementById("counterValue").textContent);
    if (displayValue !=0) {
        displayValue-- // decrement 1
        counterValue.innerHTML=displayValue;
    }
    else {
        clearInterval(intervalId);
        // release our intervalID from the variable
        intervalId = null;
    }
}