const studentname = "Sara";
let points = 32;
const maxPoints = 40;
let statuss = document.getElementById("status")
let studentnamee = document.getElementById("student")
percent = document.getElementById("percentage")

function percentage() {
    return (points / maxPoints) * 100;
}

console.log(percentage());

if (percentage() >= 60) {
    classlistadd.statuss = "passed";
}
else classlistadd.statuss = "failed";

studentnamee.textContent()
percent = percentage;