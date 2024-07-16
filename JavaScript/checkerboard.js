let gridSize = 10;
let oddRow = "";
let evenRow = "";
// build odd or even row string with the correct number of columns
// something is odd or even depending on modulo 2 result
for (colCount = 1; colCount <= gridSize; colCount++) {
    if (colCount%2 !== 0) {  // oddCol
        oddRow = oddRow + ".";
        evenRow = evenRow + "#";
    } else {    // not odd, so it's even
        oddRow = oddRow + "#";
        evenRow = evenRow + ".";
    }
}
// output each row
for (rowCount = 1; rowCount <= gridSize; rowCount++) {
    if (rowCount%2 !== 0) {  // output odd row
        console.log("(Row" + rowCount + ") " + oddRow + "\n");
    } else { // not odd so it's even row
        console.log("(Row" + rowCount + ") "+ evenRow + "\n");
    }
}    
