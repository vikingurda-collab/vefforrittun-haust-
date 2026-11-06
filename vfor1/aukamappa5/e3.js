const form = document.getElementById('signupForm');
const emailInput = document.getElementById('emailInput');
const output = document.getElementById('output');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    
    const age = Number(ageInput.value);
    
    if (age > 17) {
        output.textContent = "Þú ert nákvæmlega 18 ára eða eldri.";
    } else {
        output.textContent = "Þú ert ekki 18 ára en þú getur skráð þig.";
    }
});