function setupPaginationLinks() {
  document.querySelectorAll('.pagination-link').forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const url = this.getAttribute('href');

      fetch(url, {
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        }
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao carregar página');
        }
        return response.json();
      })
      .then(data => {
        document.getElementById('posts-wrapper').innerHTML = data.html;
        setupPaginationLinks(); // Reaplica os eventos aos novos links
      })
      .catch(error => console.error('Erro ao paginar:', error));
    });
  });
}

document.addEventListener('DOMContentLoaded', setupPaginationLinks);
