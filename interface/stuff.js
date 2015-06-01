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
