

function showPic(pic){
    var source = pic.getAttribute("href");
    var placeholder = document.getElementById("placeholder");
    placeholder.setAttribute("src",source);
    var text = pic.getAttribute("title");
    var description = document.getElementById("description");
    description.firstChild.nodeValue = text;
}

var body_elem = document.getElementsByTagName("body")[0];

//alert(body_elem.childNodes.length);