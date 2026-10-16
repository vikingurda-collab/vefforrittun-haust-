let likes = 0

const likars = document.getElementById("likes")
const button = document.getElementById("likebutton")

button.addEventListener("click", function () {
    likes++;
    likars.textContent = likes;
});