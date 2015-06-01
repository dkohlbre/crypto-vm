function blocktoggle(thing) {
    if (document.getElementById(thing).style.display == 'block') {
        document.getElementById(thing).style.display = 'none';
        document.getElementById('show'+thing).value="Show";
    }
    else {
        document.getElementById(thing).style.display = 'block';
        document.getElementById('show'+thing).value="Hide";
    }
}


function flagcheck(flag){
    usrinput = document.getElementById('guess').value
    if (flag === usrinput) {
        document.getElementById("success").innerHTML="<font color=\"green\">Good job!</font>"
    }
    else {
        document.getElementById("success").innerHTML="<font color=\"red\">Try again :(</font>"
    }
}
