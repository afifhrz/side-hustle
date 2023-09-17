//single line comment
/*
multiple
line
comment
*/
alert("This is the Contact page.");

function test(){
    var message = "Your contact details are: \n";
    // var firstName = document.getElementById('fname').value;
    var email = document.contactForm.email;    
    // message = message + firstName + "\n";
    // alert(email);   
    // alert(message);

    // This decision structure will do the following:
    // 1) Check: is the email’s value property NOT empty?
    // 2) if true, remove empty-field-message.
    // 3) if false, display empty-field-message &
    // change empty-field-message text color to red.
    if(email.value!=""){
        // remove empty-field-message
        document.getElementsByClassName("empty-field-message")[0].style.display = "none";
    }else{
        // display empty-field-message
        document.getElementsByClassName("empty-field-message")[0].style.display = "inline";
        document.getElementsByClassName("empty-field-message")[0].style.color = "red";
    }

    // Array declarations.
    var inputArray=document.getElementsByTagName("input");
    var numInputs = inputArray.length;
    // Outputting id and value of fname <input> element.
    // alert(inputArray[1].id + " = " + inputArray[1].value);
    // Outputting total number of <input> elements on the page.
    alert("This page has " + numInputs + " input elements.");
    
    for(var i=0; i<numInputs; i++){
        if (inputArray[i].type!="checkbox"&&
            inputArray[i].type!="submit"&&
            inputArray[i].type!="reset"){
                message = message + "\n" + inputArray[i].id + " = " + inputArray[i].value;
            }
    }
    alert(message);
}