if (document.getElementById("select_restart_difficulty_end") != null) {
    document.getElementById("select_restart_difficulty_end").addEventListener("change", function (ev) {
    const difficulty = ev.target.value;
    enableRestartButton(difficulty, "restart_button_end")
})
}
document.getElementById("select_restart_difficulty").addEventListener("change", function (ev) {
    const difficulty = ev.target.value;
    enableRestartButton(difficulty, "restart_button")
})

function enableRestartButton(difficulty, button_id) {
    console.log(button_id)
    const button = document.getElementById(button_id);
    if (difficulty === "") {
        button.setAttribute("href", "");
        if (button.classList.contains("cursor-pointer")) {
            button.classList.remove("cursor-pointer");
            button.classList.add("cursor-not-allowed");
        }
        if (!button.classList.contains("grayscale-[75%]")) {
            button.classList.add("grayscale-[75%]")
        }
    } else {
        button.setAttribute("href",`/game/restart/${difficulty}`);
        if (button.classList.contains("cursor-not-allowed")) {
            button.classList.remove("cursor-not-allowed");
        button.classList.add("cursor-pointer");
        }
        if (button.classList.contains("grayscale-[75%]")) {
            button.classList.remove("grayscale-[75%]")
        }
    }
}