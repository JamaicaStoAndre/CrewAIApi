
document.addEventListener("DOMContentLoaded", () => {
    // Load the sidebar dynamically
    const sidebarPlaceholder = document.createElement("div");
    fetch("sidebar.html")
        .then(response => response.text())
        .then(data => {
            sidebarPlaceholder.innerHTML = data;
            document.body.prepend(sidebarPlaceholder);

            // Highlight the active menu item
            const currentPath = window.location.pathname.split("/").pop(); // Get current file name
            const menuItems = sidebarPlaceholder.querySelectorAll(".menu-item");
            menuItems.forEach(item => {
                if (item.getAttribute("href") === currentPath) {
                    item.classList.add("active");
                } else {
                    item.classList.remove("active"); // Remove highlight from others
                }
            });
        });
});

// Function to toggle submenu visibility
function toggleSubmenu(element) {
    element.classList.toggle("expanded");
}
