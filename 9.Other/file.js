alert("5");

//function and class

var CheckObject = function(){};
CheckObject.prototype = {
        checkName: function(){
        return this;
    },
    checkEmail: function(){
        return this;
    },
    checkPassword: function(){
        alert(3);
        return this;
    }
}

CheckObject.prototype.addmethod = function(name,fn){
    this[name] = fn;
    return this;
}
var methods = new CheckObject();
methods.addmethod('checkGrade',function(){
    alert("checkGrade");
    return this;
});
methods.checkGrade();
//alert(typeof document.getElementById("purchases"));
//alert(document.getElementsByTagName("li").length);
var att = document.getElementById("kfc");
att.setAttribute("title","hahaha");
alert(att.getAttribute("title"));