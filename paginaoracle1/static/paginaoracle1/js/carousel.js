const carousel = document.getElementById('carousel');
let currentIndex = 0;

function moverCarousel(direction) {
  const items = carousel.querySelectorAll('.carousel-item');
  const itemWidth = items[0].offsetWidth + 30; // ancho + margen

  currentIndex += direction;

  // Si pasas del último, vuelve al primero
  if (currentIndex > items.length - 1) {
    currentIndex = 0;
  }

  // Si pasas antes del primero, vuelve al último
  if (currentIndex < 0) {
    currentIndex = items.length - 1;
  }

  carousel.style.transform = `translateX(${-itemWidth * currentIndex}px)`;
}
