console.log ("Logical Ops");
// && - AND operator -  both sides need to be true
// || - OR operator - either side need to be true
// ! - NOT (reverses boolean value)

let isVerified =  false;
let isLoggedIn = true;
let hasPaymentToken = true;
let isGuest = true;


if (!isVerified && isLoggedIn && hasPaymentToken) {
    console.log ('Greeting message to user');
    console.log ('Grant access to course');
    console.log ('Enjoy Yourself!');
} else if (isVerified || isGuest) {
    console.log ('Allow free previews');
} else {
    console.log("MESSAGE: Please cotact admin");
}