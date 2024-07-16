// Demonstrates methods that can be used with arrays
const numbers =['One','Two','Three','Four','Five', 'Six'];
// Replace an individual value in the array
console.log("The length of the array is: " + `${numbers.length}`);
numbers[1] = 'SOMETHING';
console.log("The value replaced now makes the array: " + numbers);
// Array Methods: 

console.log(" =========== SHIFT Method ============");
// drops and returns the first element of array and changes the length. Returns the number that was dropped
console.log("The element that was dropped is: " + `${numbers.shift()}`);
console.log("The result of shift is: " + numbers);
console.log("The length of the array is now: " + `${numbers.length}`);

console.log(" =========== UNSHIFT Method ============");
// .unshift - adds to the first position of the array
numbers.unshift("ADDED");
console.log('After the UNSHIFT, the array now looks like: ' + numbers);
console.log ("The length of the array is now: " + `${numbers.length}`);

console.log(" =========== POP Method ============");
// .pop -- removes and returns the last value of the array
console.log ("The length of the array is: " + `${numbers.length}`);
console.log ("The element to be removed from the end by the .pop method is: " + numbers.pop());
console.log ("The length of the array is now: " + `${numbers.length}`);

console.log("============ PUSH METHOD =================== ");
// .push adds an element to the end of the array
console.log ("The length of the array is: " + `${numbers.length}`);
console.log ("The new length of the array is now: " + `${numbers.push('SEVEN')}`); // adds the element and returns the new length
console.log ("The array is now " + numbers);

console.log("==========  MIDDLE (SPLICING) ========================");
// start after position 2 and delete 1 element and then place an element in the array
numbers.splice(2,1,"SPLICED");
console.log ("The Spliced array now looks like: " + numbers);



