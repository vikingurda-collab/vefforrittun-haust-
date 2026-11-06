const priceform = document.getElementById("priceForm");
const priceinput = document.getElementById("priceInput");
const output = document.getElementById("output");
const countinput = document.getElementById("countInput");

priceform.addEventListener('submit', function(event) { 
    event.preventDefault(); 
    const verd = Number(priceinput.value); 
    const fjoldi = Number(countinput.value); 
    const samtals = verd * fjoldi; 
    output.textContent = "Samtals: " + samtals + " kr."; 
});