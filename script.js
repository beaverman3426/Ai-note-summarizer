const summarizedparagrah=document.querySelector("#summaroutput")
const summaryButton=document.querySelector("#summarize")
const inputField = document.querySelector("#input");

summaryButton.addEventListener("click", bartCall)

async function bartCall() {
    const userInput=inputField.value;
    const response= await fetch("http://127.0.0.1:8000/summarize", {
        method : "POST",
        headers:{
            "Content-type": "application/json",
        },
        body: JSON.stringify({text: userInput}),
    });
    if (response.ok) {
        const data = await response.json(); 
        summarizedparagrah.textContent = data.summary; 
    } else {
        summarizedparagrah.textContent = "Error summarizing text.";
    }
}
     
