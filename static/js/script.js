async function sendMessage(){

let input=document.getElementById("userInput");

let message=input.value;

if(message==="") return;

let chat=document.getElementById("chatBox");

chat.innerHTML+=`
<div class="message user">
${message}
</div>
`;

const response=await fetch("/chat",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

message:message

})

});

const data=await response.json();

chat.innerHTML+=`
<div class="message bot">
${data.answer}
</div>
`;

input.value="";

chat.scrollTop=chat.scrollHeight;

}

document.getElementById("userInput").addEventListener("keypress",function(e){

if(e.key==="Enter"){

sendMessage();

}

});