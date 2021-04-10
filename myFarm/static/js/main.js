jQuery(document).ready(function () {
    getFarmDetail()
    // toggleScheduleRelay()
    // pad()
    // endTime()
    // timeCal()
    // scheduleSet()
    enableButton()

});

function getFarmDetail() {
    console.log(localStorage.farmID)
    console.log(localStorage.tk)
}

function setModeRelay(relay, mode, farmCode) {
    // console.log('setModeRelay')
    // console.log(relay)
    // console.log(mode)
    // console.log(farmCode)
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
        "farmCode": localStorage.farmCode,
        "token": localStorage.tk,
        "method": "setMode",
        "detail": {"device": "Relay" + relay.toString(), "mode": mode}
    });
    // console.log(raw)
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
        // fetch("http://127.0.0.1:8000/setMode/", requestOptions)

    fetch("https://navitaiot.herokuapp.com/setMode2/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}

function controlRelay(relay, control, farmCode) {

    // var url = "http://127.0.0.1:8000/controlRelay/"

    var url = "https://navitaiot.herokuapp.com/controlRelay/"
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Cookie", "csrftoken=rEjFtI8SYft2HZ0JZJe02HuyzYjPv7VTqbsNnfbl1V0zHQVt7VsdwAhzhjVdVRsH");

    var raw = JSON.stringify({
        "farmCode": localStorage.farmCode,
        "token": localStorage.tk,
        "method": "control",
        "detail": {"device": "Relay" + relay.toString(), "control": control}
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch(url, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

}

function enableButton() {

    $('.sendButton11').attr('disabled', true);

    $('#timePeriod1R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton11').attr('disabled', false);
        } else {
            $('.sendButton11').attr('disabled', true);

        }
    })

    $('.sendButton12').attr('disabled', true);
    $('#timePeriod2R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton12').attr('disabled', false);
        } else {
            $('.sendButton12').attr('disabled', true);
        }
    })

    $('.sendButton13').attr('disabled', true);
    $('#timePeriod3R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton13').attr('disabled', false);
        } else {
            $('.sendButton13').attr('disabled', true);
        }
    })

    $('.sendButton14').attr('disabled', true);
    $('#timePeriod4R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton14').attr('disabled', false);
        } else {
            $('.sendButton14').attr('disabled', true);
        }
    })

    $('.sendButton15').attr('disabled', true);
    $('#timePeriod5R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton15').attr('disabled', false);
        } else {
            $('.sendButton15').attr('disabled', true);
        }
    })

    $('.sendButton16').attr('disabled', true);
    $('#timePeriod6R1Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton16').attr('disabled', false);
        } else {
            $('.sendButton16').attr('disabled', true);
        }
    })

    $('.sendButton21').attr('disabled', true);

    $('#timePeriod1R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton21').attr('disabled', false);
        } else {
            $('.sendButton21').attr('disabled', true);

        }
    })

    $('.sendButton22').attr('disabled', true);
    $('#timePeriod2R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton22').attr('disabled', false);
        } else {
            $('.sendButton22').attr('disabled', true);
        }
    })

    $('.sendButton23').attr('disabled', true);
    $('#timePeriod3R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton23').attr('disabled', false);
        } else {
            $('.sendButton23').attr('disabled', true);
        }
    })

    $('.sendButton24').attr('disabled', true);
    $('#timePeriod4R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton24').attr('disabled', false);
        } else {
            $('.sendButton24').attr('disabled', true);
        }
    })

    $('.sendButton25').attr('disabled', true);
    $('#timePeriod5R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton25').attr('disabled', false);
        } else {
            $('.sendButton25').attr('disabled', true);
        }
    })

    $('.sendButton26').attr('disabled', true);
    $('#timePeriod6R2Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton26').attr('disabled', false);
        } else {
            $('.sendButton26').attr('disabled', true);
        }
    })
    $('.sendButton31').attr('disabled', true);

    $('#timePeriod1R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton31').attr('disabled', false);
        } else {
            $('.sendButton31').attr('disabled', true);

        }
    })

    $('.sendButton32').attr('disabled', true);
    $('#timePeriod2R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton32').attr('disabled', false);
        } else {
            $('.sendButton32').attr('disabled', true);
        }
    })

    $('.sendButton33').attr('disabled', true);
    $('#timePeriod3R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton33').attr('disabled', false);
        } else {
            $('.sendButton33').attr('disabled', true);
        }
    })

    $('.sendButton34').attr('disabled', true);
    $('#timePeriod4R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton34').attr('disabled', false);
        } else {
            $('.sendButton34').attr('disabled', true);
        }
    })

    $('.sendButton35').attr('disabled', true);
    $('#timePeriod5R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton35').attr('disabled', false);
        } else {
            $('.sendButton35').attr('disabled', true);
        }
    })

    $('.sendButton36').attr('disabled', true);
    $('#timePeriod6R3Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton36').attr('disabled', false);
        } else {
            $('.sendButton36').attr('disabled', true);
        }
    })
    $('.sendButton41').attr('disabled', true);

    $('#timePeriod1R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton41').attr('disabled', false);
        } else {
            $('.sendButton41').attr('disabled', true);

        }
    })

    $('.sendButton42').attr('disabled', true);
    $('#timePeriod2R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton42').attr('disabled', false);
        } else {
            $('.sendButton42').attr('disabled', true);
        }
    })

    $('.sendButton43').attr('disabled', true);
    $('#timePeriod3R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton43').attr('disabled', false);
        } else {
            $('.sendButton43').attr('disabled', true);
        }
    })

    $('.sendButton44').attr('disabled', true);
    $('#timePeriod4R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton44').attr('disabled', false);
        } else {
            $('.sendButton44').attr('disabled', true);
        }
    })

    $('.sendButton45').attr('disabled', true);
    $('#timePeriod5R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton45').attr('disabled', false);
        } else {
            $('.sendButton45').attr('disabled', true);
        }
    })

    $('.sendButton46').attr('disabled', true);
    $('#timePeriod6R4Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton46').attr('disabled', false);
        } else {
            $('.sendButton46').attr('disabled', true);
        }
    })
    $('.sendButton51').attr('disabled', true);

    $('#timePeriod1R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton51').attr('disabled', false);
        } else {
            $('.sendButton51').attr('disabled', true);

        }
    })

    $('.sendButton52').attr('disabled', true);
    $('#timePeriod2R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton52').attr('disabled', false);
        } else {
            $('.sendButton52').attr('disabled', true);
        }
    })

    $('.sendButton53').attr('disabled', true);
    $('#timePeriod3R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton53').attr('disabled', false);
        } else {
            $('.sendButton53').attr('disabled', true);
        }
    })

    $('.sendButton54').attr('disabled', true);
    $('#timePeriod4R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton54').attr('disabled', false);
        } else {
            $('.sendButton54').attr('disabled', true);
        }
    })

    $('.sendButton55').attr('disabled', true);
    $('#timePeriod5R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton55').attr('disabled', false);
        } else {
            $('.sendButton55').attr('disabled', true);
        }
    })

    $('.sendButton56').attr('disabled', true);
    $('#timePeriod6R5Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton56').attr('disabled', false);
        } else {
            $('.sendButton56').attr('disabled', true);
        }
    })
    $('.sendButton61').attr('disabled', true);

    $('#timePeriod1R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton61').attr('disabled', false);
        } else {
            $('.sendButton61').attr('disabled', true);

        }
    })

    $('.sendButton62').attr('disabled', true);
    $('#timePeriod2R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton62').attr('disabled', false);
        } else {
            $('.sendButton62').attr('disabled', true);
        }
    })

    $('.sendButton63').attr('disabled', true);
    $('#timePeriod3R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton63').attr('disabled', false);
        } else {
            $('.sendButton63').attr('disabled', true);
        }
    })

    $('.sendButton64').attr('disabled', true);
    $('#timePeriod4R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton64').attr('disabled', false);
        } else {
            $('.sendButton64').attr('disabled', true);
        }
    })

    $('.sendButton65').attr('disabled', true);
    $('#timePeriod5R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton65').attr('disabled', false);
        } else {
            $('.sendButton65').attr('disabled', true);
        }
    })

    $('.sendButton66').attr('disabled', true);
    $('#timePeriod6R6Delay').keyup(function () {
        if ($(this).val().length != 0) {
            $('.sendButton66').attr('disabled', false);
        } else {
            $('.sendButton66').attr('disabled', true);
        }
    })


}

function toggleScheduleRelay(relay_num, period, farmCode) {
    start = $('#R' + relay_num + '_Sch' + period + '_on').text();
    end = $('#R' + relay_num + '_Sch' + period + '_off').text();
    duration = $('#R' + relay_num + '_Sch' + period + '_duration').text();
    var s = start.split(":")
    var e = end.split(":")


    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    if (relay_num == 1 && period == 1) {
        if (document.getElementById('chk11').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }

    } else if (relay_num == 1 && period == 2) {
        if (document.getElementById('chk12').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 1 && period == 3) {
        if (document.getElementById('chk13').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 1 && period == 4) {
        if (document.getElementById('chk14').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 1 && period == 5) {
        if (document.getElementById('chk15').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 1 && period == 6) {
        if (document.getElementById('chk16').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 1) {
        if (document.getElementById('chk21').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 2) {
        if (document.getElementById('chk22').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 3) {
        if (document.getElementById('chk23').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 4) {
        if (document.getElementById('chk24').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 5) {
        if (document.getElementById('chk25').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 2 && period == 6) {
        if (document.getElementById('chk26').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 1) {
        if (document.getElementById('chk31').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 2) {
        if (document.getElementById('chk32').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 3) {
        if (document.getElementById('chk33').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 4) {
        if (document.getElementById('chk34').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 5) {
        if (document.getElementById('chk35').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 3 && period == 6) {
        if (document.getElementById('chk36').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 1) {
        if (document.getElementById('chk41').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 2) {
        if (document.getElementById('chk42').checked) {
            var p = false
        } else {
            console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 3) {
        if (document.getElementById('chk43').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 4) {
        if (document.getElementById('chk44').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 5) {
        if (document.getElementById('chk45').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 4 && period == 6) {
        if (document.getElementById('chk46').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 1) {
        if (document.getElementById('chk51').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 2) {
        if (document.getElementById('chk52').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 3) {
        if (document.getElementById('chk53').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 4) {
        if (document.getElementById('chk54').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 5) {
        if (document.getElementById('chk55').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 5 && period == 6) {
        if (document.getElementById('chk56').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 1) {
        if (document.getElementById('chk61').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 2) {
        if (document.getElementById('chk62').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 3) {
        if (document.getElementById('chk63').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 4) {
        if (document.getElementById('chk64').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 5) {
        if (document.getElementById('chk65').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    } else if (relay_num == 6 && period == 6) {
        if (document.getElementById('chk66').checked) {
            var p = false
        } else {
            // console.log("button 1 Not Checked")
            var p = true
        }
    }


    var raw = JSON.stringify({
        "farmCode": farmCode,
        "token": localStorage.tk,
        "method": "scheduleSet",
        "detail": {
            "device": "relay" + relay_num,
            "period": period,
            "start_hour": s[0],
            "start_minute": s[1],
            // "start_second": s[2],
            "end_hour": e[0],
            "end_minute": e[1],
            // "end_second": e[2],
            "duration": duration,
            "pause": p
        },
        "dayOfWeek": "mon,tue,wed,thu,fri,sat,sun"
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // {#console.log(raw)#}
    //     fetch("http://10.90.14.133:8000/createJobSchedule/", requestOptions)
    // fetch("http://127.0.0.1:8000/createJobSchedule/", requestOptions)
    fetch("https://navitaiot.herokuapp.com/createJobSchedule/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}

function pad(num) {
    return ("0" + num).slice(-2);
}

function endTime(start, delay) {
    var s = start.split(":"), sMin = +s[1] + s[0] * 60
    end = sMin + Math.floor(delay);
    var h = Math.floor(end / 60), m = end % 60;
    return "" + pad(h) + ":" + pad(m);
}

function timeCal(relay_num, period) {
    document.getElementById('timePeriod' + period + 'R' + relay_num + 'Stop').value = endTime(
        document.getElementById('timePeriod' + period + 'R' + relay_num + 'Start').value,
        document.getElementById('timePeriod' + period + 'R' + relay_num + 'Delay').value)
}

function scheduleSet(relay_num, period, farmCode) {
    timeCal(relay_num, period);
    start = document.getElementById('timePeriod' + period + 'R' + relay_num + 'Start').value
    end = document.getElementById('timePeriod' + period + 'R' + relay_num + 'Stop').value
    duration = document.getElementById('timePeriod' + period + 'R' + relay_num + 'Delay').value
    var s = start.split(":")
    var e = end.split(":")
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    if (document.getElementById('chk' + relay_num + '' + period).checked) {
        var raw = JSON.stringify({
            "farmCode": farmCode,
            "token": localStorage.tk,
            "method": "scheduleSet",
            "detail": {
                "device": "relay" + relay_num,
                "period": period,
                "start_hour": s[0],
                "start_minute": s[1],
                // "start_second": s[2],
                "end_hour": e[0],
                "end_minute": e[1],
                // "end_second": e[2],
                "duration": duration,
                "pause": false
            },
            "dayOfWeek": "mon,tue,wed,thu,fri,sat,sun"
        });
    } else {
        var raw = JSON.stringify({
            "farmCode": farmCode,
            "token": localStorage.tk,
            "method": "scheduleSet",
            "detail": {
                "device": "relay" + relay_num,
                "period": period,
                "start_hour": s[0],
                "start_minute": s[1],
                // "start_second": s[2],
                "end_hour": e[0],
                "end_minute": e[1],
                // "end_second": e[2],
                "duration": duration,
                "pause": true
            },
            "dayOfWeek": "mon,tue,wed,thu,fri,sat,sun"
        });
    }
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    // fetch("http://10.90.14.133:8000/createJobSchedule/", requestOptions)

    // fetch("http://127.0.0.1:8000/createJobSchedule/", requestOptions)
    fetch("https://navitaiot.herokuapp.com/createJobSchedule/", requestOptions)
        .then(function (response) {
            console.log(response.status);
            if (response.status == "404") {
                alert('Unauthorization')
            }
        });
}



