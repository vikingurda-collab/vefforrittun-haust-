const fruits = ["epli", "banani", "appelsína"];
const list = document.getElementById("fruitlist");

if (list) {
    for (const fruit of fruits) {
        const item = document.createElement("li");
        item.textContent = fruit;
        list.appendChild(item);
    }
}