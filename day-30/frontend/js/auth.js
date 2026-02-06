// Authentication helpers

function isLoggedIn() {
    return localStorage.getItem('token') !== null;
}

function getToken() {
    return localStorage.getItem('token');
}

function setToken(token) {
    localStorage.setItem('token', token);
}

function removeToken() {
    localStorage.removeItem('token');
}

function logout() {
    removeToken();
    window.location.href = 'index.html';
}

// Update navigation based on auth status
function updateNavigation() {
    const loginLink = document.getElementById('loginLink');
    const registerLink = document.getElementById('registerLink');
    const createPostLink = document.getElementById('createPostLink');
    const logoutBtn = document.getElementById('logoutBtn');

    if (isLoggedIn()) {
        if (loginLink) loginLink.classList.add('hidden');
        if (registerLink) registerLink.classList.add('hidden');
        if (createPostLink) createPostLink.classList.remove('hidden');
        if (logoutBtn) {
            logoutBtn.classList.remove('hidden');
            logoutBtn.addEventListener('click', logout);
        }
    } else {
        if (loginLink) loginLink.classList.remove('hidden');
        if (registerLink) registerLink.classList.remove('hidden');
        if (createPostLink) createPostLink.classList.add('hidden');
        if (logoutBtn) logoutBtn.classList.add('hidden');
    }
}

// Check auth on page load
document.addEventListener('DOMContentLoaded', () => {
    updateNavigation();
});
