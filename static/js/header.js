window.onscroll = function(){
    myFunction()
}

console.log(window.pageYOffset)
var header = document.getElementById("navbar")
//console.log(header)

var sticky = header.offsetTop;
console.log(sticky)

function myFunction(){
    if(window.pageYOffset > sticky){
        header.classList.add("sticky")
    }else{
        header.classList.remove("sticky")
    }
}
