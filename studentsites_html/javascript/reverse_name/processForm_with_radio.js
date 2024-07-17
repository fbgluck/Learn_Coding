// This is a comment in javascript
// This code contains functions executed when buttons are pushed
// console.log("Executing javascript");

// FUNCTION: Retrieves the value of the radio button group
function getRadioValue() {   
    var colorBtnGroup = document.getElementsByName('colorChoice'); // creates an array of the value of the buttons

    for (i = 0; i < colorBtnGroup.length; i++) { // 1st statement , condition, executed every time
        // DEBUG: console.log(colorBtnGroup[i].value);
        if (colorBtnGroup[i].checked) {       // is the radio button checked?
            reverseName(colorBtnGroup[i].value); // if so, call this procedure with the color that the background will be
        }
    }
}

// FUNCTION: Build the reversed name
function reverseName(setColor) { // Executed when button is clicked   
    // retrieve the value of the first name and last name field
    firstName = document.getElementById("firstName").value;
    lastName = document.getElementById("lastName").value;
    // Build a new string og the reversed name
    let reversedName = lastName.concat(", ", firstName);
    // create an object of the output field
    let outputParagraphField = document.getElementById('outputParagraph')
    //document.getElementById("outputParagraph").innerHTML = reversedName;
    // insert text into the paragraph and change the style
    outputParagraphField.innerHTML=reversedName
    outputParagraphField.style.backgroundColor = setColor; // set to the color passed to the function
 }

// FUNCTION: Reset the form for the next trial 
function reset() {  // Reset the form by clearing the fields
    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = ""; 
    document.getElementById('outputParagraph').innerHTML = "&nbsp;";  // clear the contents of the paragraph
    document.getElementById('outputParagraph').style.backgroundColor='unset';  //remove the color
// reset radio buttons to default value
    radioBtnDefault = document.getElementById("unset");
    radioBtnDefault.checked = true;
}

