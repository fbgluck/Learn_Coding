// This is a simple javascript program that starts with an
// empty HTML page and modifies the DOM to add two <p> nodes
// each of which contain text.
// Its sole purpose is to show how you can modify a DOM programatically
//
// ref: https://www.delftstack.com/howto/javascript/javascript-add-text/
console.clear()
console.log("Starting javascript in first_program.js")
// A text string we are going to dynamically insert
let today = "Today's date is: " + new Date();

// Build two <p> nodes we are going to add to the document

// create a <p> node to hold some fixed text
const ptag_1 = document.createElement("p");
// and set the ID attribute so we can select it later
ptag_1.setAttribute('id', "fixed_text");
//create some text to add to the node
var text = document.createTextNode("The following text was inserted by javascript");
// and append the text node to the DOM leaf we created  
ptag_1.appendChild(text);
// create another <p> node that will hold the date and time text
const ptag_2 = document.createElement("p");
ptag_2.setAttribute('id', 'time_text');
var timetext = document.createTextNode(today);
ptag_2.appendChild(timetext);
// now we append the <p> nodes with the child text to the wrapper div
const WrapperDiv = document.getElementById("wrapper");
WrapperDiv.appendChild(ptag_1);
WrapperDiv.appendChild(ptag_2);