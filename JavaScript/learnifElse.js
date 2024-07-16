 if (true) {
    console.log("I am true inside IF block");
    console.log("I am still inside IF block");
 } else if (false) {
        console.log("I am true inside the ELSE block");
    } else {   
    console.log("I am false inside the ELSE block");
 }

console.log('=================');

 var whoIsHere='';

 if (whoIsHere === 'user') { // EXACTLY equal
    console.log("You are a: " + whoIsHere);
    console.log('MESSAGE: Greeting message for all user');
    console.log('Allow access to view all courses');
 } 
 else if(whoIsHere==='teacher'){
    console.log("You are a: " + whoIsHere);
    console.log('MESSAGE: Greeting message for TEACHER');
    console.log('Allow access to his courses');
 } else {
    console.log("I don't know who you are.") 
    console.log('MESSAGE: please verify your email');
    console.log ('send user an email for verification');
 }
console.log("===============");
 // GRADE PROBLEM
 // Student Marks
 // 10 - Amazing
 // 5 - Good
 // 3 - Poor
 // 0 - Poor

 let yourMark = 0;
 if (yourMark== 10) {
     console.log ("Your Mark was " + yourMark + ". That is Amazing");
 }
 else if (yourMark== 5){
    console.log ("Your Mark was " + yourMark + ". That is Good");
 }
 else if (yourMark== 3){
    console.log ("Your Mark was " + yourMark + ". That is Poor");
 } else {
    console.log ("Your Mark was " + yourMark + ". You Failed");
 }
