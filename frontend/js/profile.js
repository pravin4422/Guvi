$(document).ready(function () {
    loadProfile();
});

function loadProfile() {
    let token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "login.html";
    }

    $.ajax({
        url: "http://localhost:5000/api/profile",
        type: "GET",
        headers: {
            "Authorization": token
        },
        success: function (res) {
            $("#age").val(res.age);
            $("#dob").val(res.dob);
            $("#contact").val(res.contact);
        },
        error: function () {
            alert("Session expired");
            window.location.href = "login.html";
        }
    });
}

function updateProfile() {
    let token = localStorage.getItem("token");

    let data = {
        age: $("#age").val(),
        dob: $("#dob").val(),
        contact: $("#contact").val()
    };

    $.ajax({
        url: "http://localhost:5000/api/profile",
        type: "PUT",
        contentType: "application/json",
        headers: {
            "Authorization": token
        },
        data: JSON.stringify(data),
        success: function () {
            alert("Profile Updated!");
        },
        error: function () {
            alert("Update Failed");
        }
    });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "login.html";
}