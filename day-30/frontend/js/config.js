// API Configuration
const API_BASE_URL = 'http://localhost:8000';

const API = {
    AUTH: {
        REGISTER: `${API_BASE_URL}/api/auth/register`,
        LOGIN: `${API_BASE_URL}/api/auth/login`,
        ME: `${API_BASE_URL}/api/auth/me`
    },
    POSTS: {
        LIST: `${API_BASE_URL}/api/posts/`,
        CREATE: `${API_BASE_URL}/api/posts/`,
        GET: (id) => `${API_BASE_URL}/api/posts/${id}`,
        UPDATE: (id) => `${API_BASE_URL}/api/posts/${id}`,
        DELETE: (id) => `${API_BASE_URL}/api/posts/${id}`
    },
    COMMENTS: {
        LIST: (postId) => `${API_BASE_URL}/api/comments/post/${postId}`,
        CREATE: `${API_BASE_URL}/api/comments/`,
        DELETE: (id) => `${API_BASE_URL}/api/comments/${id}`
    }
};

// Helper function to get auth headers
function getAuthHeaders() {
    const token = localStorage.getItem('token');
    return {
        'Content-Type': 'application/json',
        'Authorization': token ? `Bearer ${token}` : ''
    };
}

// Helper function to format date
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

// Helper function to show error
function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        element.classList.remove('hidden');
        element.querySelector('span').textContent = message;
    }
}

// Helper function to hide error
function hideError(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.classList.add('hidden');
    }
}
