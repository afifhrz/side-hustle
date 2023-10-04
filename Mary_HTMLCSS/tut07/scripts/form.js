//single line comment
/*
multiple
line
comment
*/
// Array declarations.
var inputArray=document.getElementsByTagName("input");
var numInputs = inputArray.length;
alert("This is the Contact page.");

function formDetails(){
    // CUSTOMER INQUIRY OBJECT
    const contactObj = {
        firstName: document.getElementById('fname').value,
        surname: document.getElementById('surname').value,
        email: document.getElementById('email').value,
        contact: document.getElementById('contact').value,
        date: document.getElementById('date').value,
        media: document.getElementById('media').value,
        message: document.getElementById('message').value,
        showDetails: function() {
            var msgDetails = 'Thanks, <strong>' + this.firstName + 
            '</strong>. Please confirm if your details are correct:<br><br><strong>Email:</strong> ' + 
            this.email + '<br><br><strong>Message:</strong> <br>' + this.message;
            return msgDetails;
        }
    };
    // END OF contactObj
    const customer = Object.create(contactObj);
    if (customer.firstName != "" &&
        customer.email != "" &&
        customer.message != "") {
            document.getElementById("overlay").style.display = "block";
            document.getElementById("msgDetails").innerHTML = customer.showDetails();
    }

}
// END OF formDetails() FUNCTION

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

    
    // Outputting id and value of fname <input> element.
    // alert(inputArray[1].id + " = " + inputArray[1].value);
    // Outputting total number of <input> elements on the page.
    alert("This page has " + numInputs + " input elements.");
    
    for(var i=0; i<numInputs; i++){
        if (inputArray[i].type!="button"&&
            inputArray[i].type!="checkbox"&&
            inputArray[i].type!="submit"&&
            inputArray[i].type!="reset"){
                message = message + "\n" + inputArray[i].id + " = " + inputArray[i].value;
            }
    }
    alert(message);
    formDetails();
}

function closeOverlay() {
    document.getElementById("overlay").style.display = "none";
}

function validateForm() {
    var message = "Please enter the following details before submitting: \n";
    var errorMsg = "";
    for (var i = 0; i<numInputs; i++) {
        if (
            (inputArray[i].type!="button"||
            inputArray[i].type!="checkbox"||
            inputArray[i].type!="submit"||
            inputArray[i].type!="reset") && 
            inputArray[i].value=="" &&
            inputArray[i].id != ""
        ) {
            errorMsg = errorMsg + inputArray[i].id + "\n"
        }
    }

    if (errorMsg==""){
        document.getElementById("contactForm").submit();
    } else {
        message = message + errorMsg;
        alert(message);
        document.getElementById("overlay").style.display = "none";
    }
}