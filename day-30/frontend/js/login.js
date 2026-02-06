document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    hideError('errorMessage');
    
    try {
        // OAuth2 expects form data
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);
        
        const response = await fetch(API.AUTH.LOGIN, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            setToken(data.access_token);
            window.location.href = 'index.html';
        } else {
            showError('errorMessage', data.detail || 'Login failed');
        }
    } catch (error) {
        console.error('Login error:', error);
        showError('errorMessage', 'An error occurred. Please try again.');
    }
});
