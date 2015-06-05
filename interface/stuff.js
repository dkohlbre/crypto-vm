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
        document.getElementById("success").innerHTML='<div class="alert alert-success" role="alert">'+
        '<strong>Well done!</strong> You got the flag =)'+
      '</div>'
    }
    else {
        document.getElementById("success").innerHTML='<div class="alert alert-danger" role="alert">'+
        '<strong>Oh snap!</strong> Change a few things up and try submitting again.'+
      '</div>'
    }
}
