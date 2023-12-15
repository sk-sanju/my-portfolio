function showAlert() {
    // Get the alert element
    var alert = document.getElementById("myAlert");

    // Display the alert
    alert.style.display = "block";

    // Hide the alert after 3 seconds (3000 milliseconds)
    setTimeout(function(){
        alert.style.display = "none";
    }, 3000);
}