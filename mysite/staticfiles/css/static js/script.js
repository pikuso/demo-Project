document.addEventListener("DOMContentLoaded", function() {
    const button = document.querySelector(".dropdown-btn");
    const menu = document.querySelector(".dropdown-menu");

    button.addEventListener("click", function() {
        menu.style.display = menu.style.display === "block" ? "none" : "block";
    });

    document.addEventListener("click", function(event) {
        if (!button.contains(event.target) && !menu.contains(event.target)) {
            menu.style.display = "none";
        }
    });
});
