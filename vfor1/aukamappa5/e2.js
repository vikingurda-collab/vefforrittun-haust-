const form = document.getElementById('signupForm');
const emailInput = document.getElementById('emailInput');
const output = document.getElementById('output');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    const email = emailInput.value;
    output.textContent = "Takk fyrir að skrá þig inn með netfangi: " + email;
});