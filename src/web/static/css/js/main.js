// main.js

document.addEventListener('DOMContentLoaded', () => {
    // Ripple on pixel-buttons
    document.querySelectorAll('.pixel-button').forEach(btn => {
      btn.addEventListener('click', () => {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        btn.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
      });
    });
  
    // Article hover lifts
    document.querySelectorAll('.article-card').forEach(article => {
      article.addEventListener('mouseenter', () => {
        article.style.transform = 'translateY(-5px)';
      });
      article.addEventListener('mouseleave', () => {
        article.style.transform = 'translateY(0)';
      });
    });
  
    // Random star twinkle on body
    setInterval(() => {
      if (Math.random() > 0.9) {
        document.body.style.boxShadow =
          `0 0 ${Math.random() * 5 + 2}px #00CCFF`;
      }
    }, 300);
  });
  