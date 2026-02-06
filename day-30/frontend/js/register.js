document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const email = document.getElementById('email').value;
    const username = document.getElementById('username').value;
    const full_name = document.getElementById('full_name').value;
    const password = document.getElementById('password').value;
    
    hideError('errorMessage');
    hideError('successMessage');
    
    try {
        const response = await fetch(API.AUTH.REGISTER, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                username,
                full_name: full_name || null,
                password
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            const successMsg = document.getElementById('successMessage');
            successMsg.classList.remove('hidden');
            successMsg.querySelector('span').textContent = 'Registration successful! Redirecting to login...';
            
            setTimeout(() => {
                window.location.href = 'login.html';
            }, 2000);
        } else {
            showError('errorMessage', data.detail || 'Registration failed');
        }
    } catch (error) {
        console.error('Registration error:', error);
        showError('errorMessage', 'An error occurred. Please try again.');
    }
});
