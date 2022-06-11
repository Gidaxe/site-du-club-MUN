const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.button-right');
const prevButton = document.querySelector('.button-left');
const dotsNav = document.querySelector('.carousel__nav');
const dots = Array.from(dotsNav.children);
const slideWidth = slides[0].getBoundingClientRect().width;


const setSlidePosition = (slide, index) => {
    slide.style.left = slideWidth * index + 'px';
};
slides.forEach(setSlidePosition);

const updateDots = (currentDot, targetDot) => {
    currentDot.classList.remove('current__slide');
    targetDot.classList.add('current__slide');
}

const moveToSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = 'translateX(-' + targetSlide.style.left +')';
    currentSlide.classList.remove('current__slide');
    targetSlide.classList.add('current__slide');
}


prevButton.addEventListener('click', e => {
    const currentSlide = track.querySelector('.current__slide');
    const prevSlide = currentSlide.previousElementSibling;
    const currentDot = dotsNav.querySelector('.current__slide');
    const prevDot = currentDot.previousElementSibling;
    
    moveToSlide(track, currentSlide, prevSlide);
    updateDots(currentDot, prevDot)

});


nextButton.addEventListener('click', e => {
    const currentSlide = track.querySelector('.current__slide');
    const nextSlide = currentSlide.nextElementSibling;
    const currentDot = dotsNav.querySelector('.current__slide');
    const nextDot = currentDot.nextElementSibling;
    
    moveToSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, nextDot)

});

dotsNav.addEventListener ('click', e => {
    const targetDot = e.target.closest('button');
     
    if (!targetDot) return;

    const currentSlide = track.querySelector('.current__slide');
    const currentDot = dotsNav.querySelector('.current__slide');
    const targetIndex = dots.findIndex(dot => dot === targetDot);
    const targetSlide = slides[targetIndex];

    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentDot, targetDot)
})