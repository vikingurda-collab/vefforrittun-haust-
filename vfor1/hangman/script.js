let words = ["banana", "computer", "minecraft", "hangman", "guitar"];

let word = words[Math.floor(Math.random() * words.length)];

let guessedLetters = [];
let wrongGuesses = 0;

let guessInput = document.getElementById("guessInput");
let guessButton = document.getElementById("guessButton");
let wordDisplay = document.getElementById("word");

function updateDisplay() {
    let display = "";

    for (let letter of word) {
        if (guessedLetters.includes(letter)) {
            display += letter + " ";
        } else {
            display += "_ ";
        }
    }

    wordDisplay.textContent = display;
}

function updateHangman() {
    if (wrongGuesses >= 1) {
        document.getElementById("head").style.visibility = "visible";
    }

    if (wrongGuesses >= 2) {
        document.getElementById("body").style.visibility = "visible";
    }

    if (wrongGuesses >= 3) {
        document.getElementById("leftArm").style.visibility = "visible";
    }

    if (wrongGuesses >= 4) {
        document.getElementById("rightArm").style.visibility = "visible";
    }

    if (wrongGuesses >= 5) {
        document.getElementById("leftLeg").style.visibility = "visible";
    }

    if (wrongGuesses >= 6) {
        document.getElementById("rightLeg").style.visibility = "visible";
    }
}

updateDisplay();
function updateHangman() {
    if (wrongGuesses === 1) {
        document.getElementById("head").style.display = "none";
    }

    if (wrongGuesses === 2) {
        document.getElementById("body").style.display = "none";
    }

    if (wrongGuesses === 3) {
        document.getElementById("leftArm").style.display = "none";
    }

    if (wrongGuesses === 4) {
        document.getElementById("rightArm").style.display = "none";
    }

    if (wrongGuesses === 5) {
        document.getElementById("leftLeg").style.display = "none";
    }

    if (wrongGuesses === 6) {
        document.getElementById("rightLeg").style.display = "none";
    }
}
guessButton.addEventListener("click", function() {
    let guess = guessInput.value.toLowerCase();

    if (guess.length === 1) {

        if (guessedLetters.includes(guess)) {
            wrongGuesses++;
            document.getElementById("wrong").textContent = wrongGuesses;
            updateHangman();
        } 
        else {
            guessedLetters.push(guess);

            if (word.includes(guess)) {
                updateDisplay();
            } 
            else {
                wrongGuesses++;
                document.getElementById("wrong").textContent = wrongGuesses;
                updateHangman();
            }
        }
    }

    guessInput.value = "";
});