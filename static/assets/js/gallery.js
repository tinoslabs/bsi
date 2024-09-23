
// const sliderWrapper = document.querySelector('.slider-wrapper');
// const sliderItems = document.querySelectorAll('.gallery-item');
// const prevBtn = document.querySelector('.slider-nav.prev');
// const nextBtn = document.querySelector('.slider-nav.next');

// let currentIndex = 0;

// nextBtn.addEventListener('click', () => {
// if (currentIndex < sliderItems.length - 3) {
//     currentIndex++;
//     sliderWrapper.style.transform = `translateX(-${currentIndex * 33.33}%)`;
// }
// });

// prevBtn.addEventListener('click', () => {
// if (currentIndex > 0) {
//     currentIndex--;
//     sliderWrapper.style.transform = `translateX(-${currentIndex * 33.33}%)`;
// }
// });


// setInterval(() => {
// if (currentIndex < sliderItems.length - 3) {
//     currentIndex++;
// } else {
//     currentIndex = 0;
// }
// sliderWrapper.style.transform = `translateX(-${currentIndex * 33.33}%)`;
// }, 3000); 

const sliderWrapper = document.querySelector('.slider-wrapper');
const sliderItems = document.querySelectorAll('.gallery-item');
const prevBtn = document.querySelector('.slider-nav.prev');
const nextBtn = document.querySelector('.slider-nav.next');

let currentIndex = 0;
let imagesPerView = 3; // Default is 3 images per row

// Function to update slider based on screen size
function updateSlider() {
  const screenWidth = window.innerWidth;

  // Adjust the number of images displayed based on screen size
  if (screenWidth < 768) {
    imagesPerView = 1; // 1 image per view for small screens
  } else if (screenWidth < 1200) {
    imagesPerView = 2; // 2 images per view for medium screens
  } else {
    imagesPerView = 3; // 3 images per view for large screens
  }

  // Reset the slider position
  sliderWrapper.style.transform = `translateX(-${currentIndex * (100 / imagesPerView)}%)`;
}

// Add event listeners for navigation buttons
nextBtn.addEventListener('click', () => {
  if (currentIndex < sliderItems.length - imagesPerView) {
    currentIndex++;
    sliderWrapper.style.transform = `translateX(-${currentIndex * (100 / imagesPerView)}%)`;
  }
});

prevBtn.addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    sliderWrapper.style.transform = `translateX(-${currentIndex * (100 / imagesPerView)}%)`;
  }
});

// Automatically update slider on window resize
window.addEventListener('resize', updateSlider);

// Initial slider setup
updateSlider();

// Optional: Auto-slide feature (if desired)
setInterval(() => {
  if (currentIndex < sliderItems.length - imagesPerView) {
    currentIndex++;
  } else {
    currentIndex = 0;
  }
  sliderWrapper.style.transform = `translateX(-${currentIndex * (100 / imagesPerView)}%)`;
}, 3000);
