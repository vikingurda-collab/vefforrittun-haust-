const games = ["Team Fortress 2", "Minecraft", "Mario Kart"];
const output = document.getElementById("output");

let text = "";

for (const game of games) {
    text += game + " / ";
}

output.textContent = text;