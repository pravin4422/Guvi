function login() {
    let data = {
        email: $("#email").val(),
        password: $("#password").val()
    };

    $.ajax({
        url: "http://localhost:5000/api/login",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function (res) {
            // Save token in localStorage
            localStorage.setItem("token", res.token);

            alert("Login Successful!");
            window.location.href = "profile.html";
        },
        error: function () {
            alert("Invalid Credentials");
        }
    });
}