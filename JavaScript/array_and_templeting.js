// Array datatypes
// One variable with multiple values and types. Use const to define fixed arrays
const superHeros = ['Iron Man', 'Spider Man','Captain America',1,true];
console.log (superHeros);
console.log("The first element in superHeros is: "+ superHeros[0]); // first element in array
let arrayLength = superHeros.length;
console.log("The length of superHeros is: " + arrayLength);
console.log("The Last Element is the array is: " + superHeros[arrayLength-1]); // the first element is 0
// templeting. Items in ${ and } are evaluated as javascript. Using backquotes is required for templating
// if we use "" or '', it is treated as a literal, not a template
console.log (`We have ${superHeros.length} superheros...`); 


