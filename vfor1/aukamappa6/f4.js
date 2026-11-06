const games = ["Team Fortress 2", "Minecraft", "Five nights at Freddy's", "Deltarune", "Undertale"];
const list = document.getElementById("gamelist");

if (list) {
    for (const game of games) {
        const item = document.createElement("li");
        item.textContent = game;
        list.appendChild(item);
    }
}