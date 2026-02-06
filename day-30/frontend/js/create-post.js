// Protect page - require login
if (!isLoggedIn()) {
    window.location.href = 'login.html';
}

document.getElementById('createPostForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const title = document.getElementById('title').value;
    const content = document.getElementById('content').value;
    
    hideError('errorMessage');
    
    try {
        const response = await fetch(API.POSTS.CREATE, {
            method: 'POST',
            headers: getAuthHeaders(),
            body: JSON.stringify({ title, content })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            window.location.href = `post.html?id=${data.id}`;
        } else {
            showError('errorMessage', data.detail || 'Failed to create post');
        }
    } catch (error) {
        console.error('Error creating post:', error);
        showError('errorMessage', 'An error occurred. Please try again.');
    }
});

// Setup logout button
document.getElementById('logoutBtn').addEventListener('click', logout);
