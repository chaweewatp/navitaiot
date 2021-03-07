function login() {
    var username = $("#username").val();
    var password = $("#password").val();

    console.log(username)
    console.log(password)
    console.log("onclick clicked")


    var settings = {
        "url": "http://127.0.0.1:8000/test",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({"username": username, "password": password}),
    };
    console.log(settings)

    $.ajax(settings).done((response) => {
        console.log(response)
    }).fail((response) => {
        console.log(response)
    });
}