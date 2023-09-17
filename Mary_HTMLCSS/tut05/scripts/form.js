//single line comment
/*
multiple
line
comment
*/
alert("This is the Contact page.");

function test(){
    var message = "Your contact details are: \n";
    var firstName = document.getElementById('fname').value;
    message = message + firstName + "\n";
    alert(message);
}