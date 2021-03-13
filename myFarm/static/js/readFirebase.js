jQuery(document).ready(function() {
    getRtdbData();
});
function getRtdbData(){
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




}

