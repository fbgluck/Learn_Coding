// Kings territory problem. Illustrates scope!
// If it can't find a local definition in a block, it will look to the parent block for a definition
let king = "Global King"
if (true) {
    let king = "Level1 King";
    if (true) {
        // let king = "Level2 King";
        console.log ("The King is: " + king);
    }
    console.log ("The King is: " + king);
}
console.log ("The King is: " + king);