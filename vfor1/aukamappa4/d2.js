const button = document.getElementById('themeButton');
const card = document.getElementById('card');

function changeTheme() {
    card.classList.toggle('dark-card');
}

button.addEventListener('click', changeTheme);