// This is a comment in javascript
// This code processes the form and outputs a greeting after reading
// the values in the form field
console.log("Executing javascript");
// Build the reversed name
function reverseName() { // Executed when button is clicked   
    console.log("Executing reversename");
    // retrieve the value of the first name and last name field
    firstName = document.getElementById("firstName").value;
    console.log(firstName)
    lastName = document.getElementById("lastName").value;
    console.log(lastName)
    // Build a new string og the reversed name
    let reversedName = lastName.concat(", ", firstName);
    // create an object of the output field
    let outputParagraphField = document.getElementById('outputParagraph')
    //document.getElementById("outputParagraph").innerHTML = reversedName;
    // insert text into the paragraph and change the style
    outputParagraphField.innerHTML=reversedName
    outputParagraphField.style.backgroundColor = "yellow";
}

function reset() {  // Reset the form by clearing the fields
    document.getElementById("firstName").value = "";
    document.getElementById("lastName").value = ""; 
    document.getElementById('outputParagraph').innerHTML = "&nbsp;";  // clear the contents of the paragraph
    document.getElementById('outputParagraph').style.backgroundColor='unset';  //remove the color

}