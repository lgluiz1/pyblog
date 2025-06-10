(() => {
  const apiKey = 'AIzaSyAYAUsw1rEW-qhfc0_iFjhNEsLuJMXNToo';  
  const keywords = ['python oque e python', 'python tutorial', 'python flask', 'python pandas', 'python django', 'python rest framworks' , 'django nija', 'python orientaçao a objeto'];
  const randomKeyword = keywords[Math.floor(Math.random() * keywords.length)];
  const query = encodeURIComponent(randomKeyword);
  const maxResults = 6;

  fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=${maxResults}&q=${query}&type=video&key=${apiKey}`)
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('videos');
      data.items.forEach(item => {
        const videoId = item.id.videoId;
        const iframe = document.createElement('iframe');
        iframe.src = `https://www.youtube.com/embed/${videoId}`;
        iframe.width = '300';
        iframe.height = '200';
        iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
        iframe.allowFullscreen = true;
        container.appendChild(iframe);
      });
    });
})();
