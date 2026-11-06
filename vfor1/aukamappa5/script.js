const input = document.getElementById('nameInput')
const button = document.getElementById('greetButton')
const output = document.getElementById('output')

button.addEventListener('click', function () {
    const name = input.value;
    output.textContent = 'Halló ' + name + '!';
});