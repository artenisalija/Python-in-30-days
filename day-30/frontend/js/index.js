async function loadPosts() {
    const loading = document.getElementById('loading');
    const postsContainer = document.getElementById('postsContainer');
    const emptyState = document.getElementById('emptyState');
    
    try {
        const response = await fetch(API.POSTS.LIST);
        const posts = await response.json();
        
        loading.classList.add('hidden');
        
        if (posts.length === 0) {
            emptyState.classList.remove('hidden');
        } else {
            postsContainer.classList.remove('hidden');
            postsContainer.innerHTML = posts.map(post => createPostCard(post)).join('');
        }
    } catch (error) {
        console.error('Error loading posts:', error);
        loading.classList.add('hidden');
        emptyState.classList.remove('hidden');
    }
}

function createPostCard(post) {
    return `
        <div class="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow">
            <div class="p-6">
                <h3 class="text-xl font-semibold text-gray-900 mb-2 hover:text-blue-600">
                    <a href="post.html?id=${post.id}">${escapeHtml(post.title)}</a>
                </h3>
                <p class="text-gray-600 mb-4 line-clamp-3">${escapeHtml(post.content.substring(0, 150))}...</p>
                <div class="flex items-center justify-between text-sm text-gray-500">
                    <span>By ${escapeHtml(post.author.username)}</span>
                    <span>${formatDate(post.created_at)}</span>
                </div>
            </div>
            <div class="bg-gray-50 px-6 py-3">
                <a href="post.html?id=${post.id}" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                    Read more →
                </a>
            </div>
        </div>
    `;
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Load posts on page load
document.addEventListener('DOMContentLoaded', loadPosts);
