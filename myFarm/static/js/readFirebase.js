jQuery(document).ready(function () {
    getRtdbData();

});

function getRtdbData() {
    var firebaseConfig = {
        apiKey: localStorage.APIkey,
        authDomain: "navitaiot.firebaseapp.com",
        databaseURL: "https://navitaiot.firebaseio.com",
        projectId: "navitaiot",
        storageBucket: "navitaiot.appspot.com",
        messagingSenderId: "840926440731",
        appId: "1:840926440731:web:9e7d0a635d9e89ff0db7be",
        measurementId: "G-5FY5JL3YN1"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    firebase.analytics();

    var relay1Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period1");
    relay1Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            // document.getElementById("R1_Sch1").style.color = "#000000";
            document.getElementById("R1_Sch1").style.color = "#000000";

        } else {
            // document.getElementById("R1_Sch1").style.color = "#999999";
            document.getElementById("R1_Sch1").style.color = "#999999";

        }
    });

    var relay1Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period2");
    relay1Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R1_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R1_Sch2").style.color = "#999999";
        }
    });

    var relay1Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period3");
    relay1Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R1_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R1_Sch3").style.color = "#999999";
        }
    });

    var relay1Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period4");
    relay1Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R1_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R1_Sch4").style.color = "#999999";
        }
    });

    var relay1Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period5");
    relay1Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R1_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R1_Sch5").style.color = "#999999";
        }
    });

    var relay1Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay1/Schedule/Period6");
    relay1Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R1_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R1_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R1_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R1_Sch6").style.color = "#000000";
        } else {
            document.getElementById("R1_Sch6").style.color = "#999999";
        }
    });


    var relay2Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period1");
    relay2Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch1").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch1").style.color = "#999999";
        }
    });
    var relay2Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period2");
    relay2Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch2").style.color = "#999999";
        }
    });
    var relay2Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period3");
    relay2Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch3").style.color = "#999999";
        }
    });
    var relay2Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period4");
    relay2Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch4").style.color = "#999999";
        }
    });
    var relay2Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period5");
    relay2Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch5").style.color = "#999999";
        }
    });
    var relay2Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay2/Schedule/Period6");
    relay2Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R2_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R2_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R2_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R2_Sch6").style.color = "#000000";
        } else {
            document.getElementById("R2_Sch6").style.color = "#999999";
        }
    });

    var relay3Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period1");
    relay3Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch1").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch1").style.color = "#999999";
        }
    });
    var relay3Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period2");
    relay3Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch2").style.color = "#999999";
        }
    });
    var relay3Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period3");
    relay3Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch3").style.color = "#999999";
        }
    });
    var relay3Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period4");
    relay3Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch4").style.color = "#999999";
        }
    });
    var relay3Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period5");
    relay3Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch5").style.color = "#999999";
        }
    });
    var relay3Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay3/Schedule/Period6");
    relay3Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R3_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R3_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R3_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R3_Sch6").style.color = "#000000";
        } else {
            document.getElementById("R3_Sch6").style.color = "#999999";
        }
    });

    var relay4Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period1");
    relay4Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch1").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch1").style.color = "#999999";
        }
    });
    var relay4Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period2");
    relay4Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch2").style.color = "#999999";
        }
    });
    var relay4Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period3");
    relay4Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch3").style.color = "#999999";
        }
    });
    var relay4Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period4");
    relay4Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch4").style.color = "#999999";
        }
    });
    var relay4Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period5");
    relay4Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch5").style.color = "#999999";
        }
    });
    var relay4Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay4/Schedule/Period6");
    relay4Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R4_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R4_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R4_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R4_Sch6").style.color = "#000000";
        } else {
            document.getElementById("R4_Sch6").style.color = "#999999";
        }
    });


    var relay5Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period1");
    relay5Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch1").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch1").style.color = "#999999";
        }
    });
    var relay5Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period2");
    relay5Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch2").style.color = "#999999";
        }
    });
    var relay5Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period3");
    relay5Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch3").style.color = "#999999";
        }
    });
    var relay5Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period4");
    relay5Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch4").style.color = "#999999";
        }
    });
    var relay5Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period5");
    relay5Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch5").style.color = "#999999";
        }
    });
    var relay5Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay5/Schedule/Period6");
    relay5Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R5_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R5_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R5_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R5_Sch6").style.color = "#000000";
        } else {
            document.getElementById("R5_Sch6").style.color = "#999999";
        }
    });


    var relay6Period1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period1");
    relay6Period1Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch1_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch1_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch1_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch1").style.color = "#000000";
        } else {
            document.getElementById("R6_Sch1").style.color = "#999999";
        }
    });
    var relay6Period2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period2");
    relay6Period2Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch2_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch2_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch2_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch2").style.color = "#000000";
        } else {
            document.getElementById("R6_Sch2").style.color = "#999999";
        }
    });
    var relay6Period3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period3");
    relay6Period3Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch3_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch3_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch3_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch3").style.color = "#000000";
        } else {
            document.getElementById("R6_Sch3").style.color = "#999999";
        }
    });
    var relay6Period4Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period4");
    relay6Period4Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch4_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch4_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch4_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch4").style.color = "#000000";
        } else {
            document.getElementById("R6_Sch4").style.color = "#999999";
        }
    });
    var relay6Period5Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period5");
    relay6Period5Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch5_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch5_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch5_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch5").style.color = "#000000";
        } else {
            document.getElementById("R6_Sch5").style.color = "#999999";
        }
    });
    var relay6Period6Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/Relay6/Schedule/Period6");
    relay6Period6Ref.on('value', function (snapshot) {
        var arr = snapshot.val();
        document.getElementById("R6_Sch6_on").innerHTML = arr['sch_on'];
        document.getElementById("R6_Sch6_off").innerHTML = arr['sch_off'];
        document.getElementById("R6_Sch6_duration").innerHTML = arr['sch_duration'];
        if (arr['pause'] == false) {
            document.getElementById("R6_Sch6").style.color = "#000000";

        } else {
            document.getElementById("R6_Sch6").style.color = "#999999";
        }
    });


    var farmRef = firebase.database().ref("farmCode/" + localStorage.farmCode);
    farmRef.on('value', function (snapshot) {
        var arr = snapshot.val();
        // console.log(arr)

        //relay 1
        if (arr['Relay1']['manual'] == true) {
            document.getElementById("Relay1_mode").innerHTML = "manual";
            document.getElementById("setRelay1Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay1Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay1']['manual'] == false) {
            document.getElementById("Relay1_mode").innerHTML = "schedule";
            document.getElementById("setRelay1Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay1Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay1']['cur_status'] == true) {
            document.getElementById("Relay1_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay1On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay1Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay1']['cur_status'] == false) {
            document.getElementById("Relay1_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay1On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay1Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay1']['sch_status'] == true) {
            document.getElementById("Relay1_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay1']['sch_status'] == false) {
            document.getElementById("Relay1_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay1_sch_status").innerHTML = "N/A";
        }

        //relay 2
        if (arr['Relay2']['manual'] == true) {
            document.getElementById("Relay2_mode").innerHTML = "manual";
            document.getElementById("setRelay2Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay2Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay2']['manual'] == false) {
            document.getElementById("Relay2_mode").innerHTML = "schedule";
            document.getElementById("setRelay2Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay2Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay2']['cur_status'] == true) {
            document.getElementById("Relay2_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay2On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay2Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay2']['cur_status'] == false) {
            document.getElementById("Relay2_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay2On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay2Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay2']['sch_status'] == true) {
            document.getElementById("Relay2_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay2']['sch_status'] == false) {
            document.getElementById("Relay2_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay2_sch_status").innerHTML = "N/A";
        }

        //relay 3
        if (arr['Relay3']['manual'] == true) {
            document.getElementById("Relay3_mode").innerHTML = "manual";
            document.getElementById("setRelay3Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay3Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay3']['manual'] == false) {
            document.getElementById("Relay3_mode").innerHTML = "schedule";
            document.getElementById("setRelay3Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay3Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay3']['cur_status'] == true) {
            document.getElementById("Relay3_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay3On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay3Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay3']['cur_status'] == false) {
            document.getElementById("Relay3_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay3On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay3Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay3']['sch_status'] == true) {
            document.getElementById("Relay3_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay3']['sch_status'] == false) {
            document.getElementById("Relay3_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay3_sch_status").innerHTML = "N/A";
        }


        //relay 4
        if (arr['Relay4']['manual'] == true) {
            document.getElementById("Relay4_mode").innerHTML = "manual";
            document.getElementById("setRelay4Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay4Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay4']['manual'] == false) {
            document.getElementById("Relay4_mode").innerHTML = "schedule";
            document.getElementById("setRelay4Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay4Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay4']['cur_status'] == true) {
            document.getElementById("Relay4_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay4On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay4Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay4']['cur_status'] == false) {
            document.getElementById("Relay4_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay4On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay4Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay4']['sch_status'] == true) {
            document.getElementById("Relay4_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay4']['sch_status'] == false) {
            document.getElementById("Relay4_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay4_sch_status").innerHTML = "N/A";
        }
        //relay 5
        if (arr['Relay5']['manual'] == true) {
            document.getElementById("Relay5_mode").innerHTML = "manual";
            document.getElementById("setRelay5Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay5Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay5']['manual'] == false) {
            document.getElementById("Relay5_mode").innerHTML = "schedule";
            document.getElementById("setRelay5Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay5Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay5']['cur_status'] == true) {
            document.getElementById("Relay5_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay5On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay5Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay5']['cur_status'] == false) {
            document.getElementById("Relay5_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay5On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay5Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay5']['sch_status'] == true) {
            document.getElementById("Relay5_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay5']['sch_status'] == false) {
            document.getElementById("Relay5_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay5_sch_status").innerHTML = "N/A";
        }
        //relay 6
        if (arr['Relay6']['manual'] == true) {
            document.getElementById("Relay6_mode").innerHTML = "manual";
            document.getElementById("setRelay6Manual").className = "btn btn-warning btn-block btn-lg";
            document.getElementById("setRelay6Schedule").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay6']['manual'] == false) {
            document.getElementById("Relay6_mode").innerHTML = "schedule";
            document.getElementById("setRelay6Manual").className = "btn btn-light btn-block btn-lg";
            document.getElementById("setRelay6Schedule").className = "btn btn-info btn-block btn-lg";
        }
        if (arr['Relay6']['cur_status'] == true) {
            document.getElementById("Relay6_cur_status").innerHTML = "เปิด";
            document.getElementById("controlRelay6On").className = "btn btn-success btn-block btn-lg";
            document.getElementById("controlRelay6Off").className = "btn btn-light btn-block btn-lg";
        } else if (arr['Relay6']['cur_status'] == false) {
            document.getElementById("Relay6_cur_status").innerHTML = "ปิด";
            document.getElementById("controlRelay6On").className = "btn btn-light btn-block btn-lg";
            document.getElementById("controlRelay6Off").className = "btn btn-danger btn-block btn-lg";
        }
        if (arr['Relay6']['sch_status'] == true) {
            document.getElementById("Relay6_sch_status").innerHTML = "เปิด";
        } else if (arr['Relay6']['sch_status'] == false) {
            document.getElementById("Relay6_sch_status").innerHTML = "ปิด";
        } else {
            document.getElementById("Relay6_sch_status").innerHTML = "N/A";
        }
    });


    var lastTimeRef = firebase.database().ref("farmCode/" + localStorage.farmCode + '/last_time');
    lastTimeRef.on('value', function (snapshot) {
            var arr = snapshot.val()
            // console.log(arr)
            var date = new Date(arr * 1000);
// Hours part from the timestamp
            var day = date.getDate();
            var year = date.getFullYear()
            var month = date.getMonth() + 1;
            var hours = date.getHours();
// Minutes part from the timestamp
            var minutes = "0" + date.getMinutes();
// Seconds part from the timestamp
            var seconds = "0" + date.getSeconds();

// Will display time in 10:30:23 format
            var formattedTime = day + '-' + month + '-' + year + ' ' + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);

            // console.log(formattedTime);
            document.getElementById("last_Time").innerHTML = formattedTime;
        }
    );

    var sensorAirTempRef = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/airTemp");
    sensorAirTempRef.on('value', function (snapshot) {
            var arr = snapshot.val();
            // console.log(arr)
            document.getElementById("sensorAirTemp").innerHTML = arr['v'];

        }
    );

        var sensorAirHumidRef = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/airHumid");
    sensorAirHumidRef.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorAirHumid").innerHTML = arr['v'];
        }
    );


    var sensorBoardHumidRef = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/boardHumi");
    sensorBoardHumidRef.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorBoardHumid").innerHTML = arr['v'];
        }
    );


        var sensorBoardTempRef = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/boardTemp");
    sensorBoardTempRef.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorBoardTemp").innerHTML = arr['v'];
        }
    );


    var sensorBoardTempRef = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/boardTemp");
    sensorBoardTempRef.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorBoardTemp").innerHTML = arr['v'];
        }
    );


        var sensorSoil1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/soil1A");
    sensorSoil1Ref.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorSoil1").innerHTML = arr['v'];
        }
    );
        var sensorSoil2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/soil2A");
    sensorSoil2Ref.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorSoil2").innerHTML = arr['v'];
        }
    );
        var sensorSoil3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/soil3A");
    sensorSoil3Ref.on('value', function (snapshot) {
            var arr = snapshot.val();
            document.getElementById("sensorSoil3").innerHTML = arr['v'];
        }
    );

            var sensorFlow1Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/flowSen1");
    sensorFlow1Ref.on('value', function (snapshot) {
            var arr = snapshot.val();
            if (arr['v']=="0"){
                document.getElementById("sensorFlow1").innerHTML = "Off";
            }else{
                                document.getElementById("sensorFlow1").innerHTML = "On";

            }

        }
    );
        var sensorFlow2Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/flowSen2");
    sensorFlow2Ref.on('value', function (snapshot) {
            var arr = snapshot.val();

            if (arr['v']=="0"){
                document.getElementById("sensorFlow2").innerHTML = "Off";
            }else{
                                document.getElementById("sensorFlow2").innerHTML = "On";

            }        }
    );
        var sensorFlow3Ref = firebase.database().ref("farmCode/" + localStorage.farmCode + "/sensors/flowSen3");
    sensorFlow3Ref.on('value', function (snapshot) {
            var arr = snapshot.val();

            if (arr['v']=="0"){
                document.getElementById("sensorFlow3").innerHTML = "Off";
            }else{
                                document.getElementById("sensorFlow3").innerHTML = "On";

            }        }
    );

}

