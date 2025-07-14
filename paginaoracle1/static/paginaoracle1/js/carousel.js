document.addEventListener('DOMContentLoaded', function () {
  const carousel = document.getElementById('carousel');
  const carouselContainer = document.querySelector('.carousel-container');
  const dotsContainer = document.getElementById('carousel-dots');
  const items = carousel.querySelectorAll('.carousel-item');
  let currentIndex = 0;
  let autoSlide;

  window.moverCarousel = function (direction) {
    if (direction !== 0) {
      currentIndex += direction;
      if (currentIndex < 0) currentIndex = items.length - 1;
      else if (currentIndex >= items.length) currentIndex = 0;
    }
    const itemWidth = items[0].offsetWidth + 30; 
    carousel.style.transform = `translateX(${-itemWidth * currentIndex}px)`;
    actualizarDots();
  };

  items.forEach((_, i) => {
    const dot = document.createElement('span');
    dot.classList.add('dot');
    dot.addEventListener('click', () => {
      currentIndex = i;
      moverCarousel(0);
    });
    dotsContainer.appendChild(dot);
  });

  function actualizarDots() {
    const dots = dotsContainer.querySelectorAll('.dot');
    dots.forEach(dot => dot.classList.remove('active'));
    if (dots[currentIndex]) {
      dots[currentIndex].classList.add('active');
    }
  }

  function startAutoSlide() {
    autoSlide = setInterval(() => {
      moverCarousel(1);
    }, 3000);
  }
  function stopAutoSlide() {
    clearInterval(autoSlide);
  }

  carouselContainer.addEventListener('mouseenter', stopAutoSlide);
  carouselContainer.addEventListener('mouseleave', startAutoSlide);

  moverCarousel(0);
  startAutoSlide();
});
