(() => {
  const particles = document.querySelectorAll('.particle');

  particles.forEach(particle => {
    function randomPosition() {
      const top = Math.random() * 80 + 10;
      const left = Math.random() * 80 + 10;
      particle.style.top = `${top}%`;
      particle.style.left = `${left}%`;
    }

    randomPosition();

    particle.addEventListener('animationiteration', () => {
      randomPosition();
    });
  });
})();
