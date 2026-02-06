const urlParams = new URLSearchParams(window.location.search);
const postId = urlParams.get('id');

if (!postId) {
    window.location.href = 'index.html';
}

async function loadPost() {
    const loading = document.getElementById('loading');
    const postContent = document.getElementById('postContent');
    const commentsSection = document.getElementById('commentsSection');
    
    try {
        const response = await fetch(API.POSTS.GET(postId));
        const post = await response.json();
        
        if (response.ok) {
            loading.classList.add('hidden');
            postContent.classList.remove('hidden');
            commentsSection.classList.remove('hidden');
            
            // Display post
            document.getElementById('postTitle').textContent = post.title;
            document.getElementById('postAuthor').textContent = `By ${post.author.username}`;
            document.getElementById('postDate').textContent = formatDate(post.created_at);
            document.getElementById('postBody').textContent = post.content;
            
            // Load comments
            displayComments(post.comments || []);
            
            // Show comment form if logged in
            if (isLoggedIn()) {
                document.getElementById('commentForm').classList.remove('hidden');
                document.getElementById('loginPrompt').classList.add('hidden');
            }
        } else {
            alert('Post not found');
            window.location.href = 'index.html';
        }
    } catch (error) {
        console.error('Error loading post:', error);
        alert('Error loading post');
        window.location.href = 'index.html';
    }
}

function displayComments(comments) {
    const commentsList = document.getElementById('commentsList');
    const noComments = document.getElementById('noComments');
    
    if (comments.length === 0) {
        noComments.classList.remove('hidden');
        commentsList.innerHTML = '';
    } else {
        noComments.classList.add('hidden');
        commentsList.innerHTML = comments.map(comment => `
            <div class="bg-gray-50 rounded-lg p-4">
                <div class="flex items-center justify-between mb-2">
                    <span class="font-medium text-gray-900">${escapeHtml(comment.author.username)}</span>
                    <span class="text-sm text-gray-500">${formatDate(comment.created_at)}</span>
                </div>
                <p class="text-gray-700">${escapeHtml(comment.content)}</p>
            </div>
        `).join('');
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Handle comment submission
const commentForm = document.getElementById('commentForm');
if (commentForm) {
    commentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const content = document.getElementById('commentContent').value;
        
        try {
            const response = await fetch(API.COMMENTS.CREATE, {
                method: 'POST',
                headers: getAuthHeaders(),
                body: JSON.stringify({
                    content,
                    post_id: parseInt(postId)
                })
            });
            
            if (response.ok) {
                document.getElementById('commentContent').value = '';
                // Reload the post to show new comment
                loadPost();
            } else {
                const data = await response.json();
                alert(data.detail || 'Failed to post comment');
            }
        } catch (error) {
            console.error('Error posting comment:', error);
            alert('Error posting comment');
        }
    });
}

// Load post on page load
document.addEventListener('DOMContentLoaded', loadPost);
