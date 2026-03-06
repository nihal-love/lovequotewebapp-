let start=new Date("June 5, 2022")

function loveTimer(){

let now=new Date()

let diff=now-start

let days=Math.floor(diff/(1000*60*60*24))

let years=Math.floor(days/365)

let months=Math.floor((days%365)/30)

let remaining=days%30

document.getElementById("timer").innerHTML=

years+" Years "+
months+" Months "+
remaining+" Days ❤️"

}

setInterval(loveTimer,1000)
function loveVoice(){

let msg=new SpeechSynthesisUtterance(

"I Love You Shahu"

)

speechSynthesis.speak(msg)

}
function darkTheme(){

document.body.style.background="#000"

document.body.style.color="white"

}

function pinkTheme(){

document.body.style.background="#ff4d6d"

}
function shareLove(){

navigator.share({

title:"Shahu Love App",

text:"Our Love Story ❤️",

url:window.location.href

})

}