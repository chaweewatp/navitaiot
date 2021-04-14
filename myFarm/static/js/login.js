function login() {
    var username = $("#username").val();
    var password = $("#password").val();
    var settings = {
        // "url": "http://127.0.0.1:8000/login",
        //         "url": "http://10.90.14.133:8000/login",
        "url": "https://navitaiot.herokuapp.com/login",

        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({"username": username, "password": password}),
    };
    $.ajax(settings).done((response) => {
        localStorage.setItem('tk',response.token)
        localStorage.setItem('farmCode',response.farmCode)
        localStorage.setItem('APIkey',response.APIkey)
        window.location = "/farmlist/" + localStorage.tk;
    }).fail((response) => {
        alert("Incorrect username or password")
    });
}