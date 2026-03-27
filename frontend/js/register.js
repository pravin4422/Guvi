function register() {
    let data = {
        name: $("#name").val(),
        email: $("#email").val(),
        password: $("#password").val()
    };

    $.ajax({
        url: "http://localhost:5000/api/register",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {
            alert("Registered Successfully!");
            window.location.href = "login.html";
        },
        error: function () {
            alert("Registration Failed");
        }
    });
}