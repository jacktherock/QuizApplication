// Alert messages
setTimeout(() => {
    $(".ms").fadeToggle(1000);
}, 2000);

// jquery code
$(document).ready(function () {
    $("#b1").click(function () {
        $(".rb").show();
        $(".rb").attr("disabled", true);
    });
});

// javascript code
function getanswers() {
    document.getElementById("UserAnswers").innerHTML = "";
    var e = document.getElementsByTagName("input");
    for (i = 0; i <= e.length; i++) {
        if (e[i].type == "radio") {
            if (e[i].checked) {
                document.getElementById("UserAnswers").innerHTML += "Q." + e[i].name +
                    " Selected answer is : " + e[
                        i].value + "<br>";
            }
        }
    }
}