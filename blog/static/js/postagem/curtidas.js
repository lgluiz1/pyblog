function handleLikeDislike(url, button, countClass) {
    fetch(url)
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;  // redireciona para login
                return;
            }
            return response.json();
        })
        .then(data => {
            if (data) {
                button.querySelector(countClass).textContent = data.likes || data.dislikes;
            }
        });
}

document.querySelectorAll('.like-button-post').forEach(button => {
    button.addEventListener('click', () => {
        const postId = button.getAttribute('data-id');
        handleLikeDislike(`/like/${postId}/`, button, '.like-count');
    });
});

document.querySelectorAll('.dislike-button-post').forEach(button => {
    button.addEventListener('click', () => {
        const postId = button.getAttribute('data-id');
        handleLikeDislike(`/dislike/${postId}/`, button, '.dislike-count');
    });
});
