var buttonOpen = document.getElementById("open");
var buttonClose = document.getElementById("close");


buttonOpen.onclick = function(){

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/open_lock");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "true" }));
};

buttonClose.onclick = function() {

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/open_lock");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify({ status: "false" }));
};
