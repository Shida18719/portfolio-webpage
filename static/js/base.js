// Load saved theme on page load
function loadTheme() {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
}

// Save theme preference
function saveTheme(theme) {
    localStorage.setItem('theme', theme);
}

// Toggle theme function
function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-bs-theme', newTheme);
    saveTheme(newTheme);
}

// Load theme immediately when script runs
loadTheme();


// Add event listeners
document.addEventListener('DOMContentLoaded', function() {
    const mainBtn = document.getElementById("btnSwitch-main");
    const canvasBtn = document.getElementById("btnSwitch-canvas");
    
    if (mainBtn) {
        mainBtn.addEventListener("click", toggleTheme);
    }
    
    if (canvasBtn) {
        canvasBtn.addEventListener("click", toggleTheme);
    }
});


// Message Alert
document.addEventListener("DOMContentLoaded", function() {

  // Dismisses messages alert after 10 seconds

    $('.alert').delay(10000).fadeOut(1000);
});



// Set footer with the current year
  const year = document.querySelector('#current-year');
  year.innerHTML = new Date().getFullYear();
