const swiper = new Swiper(".mySwiper", {
    slidesPerView: "auto",
    centeredSlides: true,
    spaceBetween: 40,
    loop: true,
    grabCursor: true,
    speed: 600
});

document.querySelectorAll(".heroMosaicSwiper").forEach(swiperEl => {
    new Swiper(swiperEl, {
        slidesPerView: "auto",
        spaceBetween: 40,
        grabCursor: true,
        speed: 700,
        loop: true,
    });
});

document.querySelectorAll(".countryMosaicSwiper").forEach(swiperEl => {
    new Swiper(swiperEl, {
        slidesPerView: "auto",
        spaceBetween: 40,
        grabCursor: true,
        speed: 700,
        loop: true,
    });
});

const btn = document.querySelector('.all-reviews-link');
btn.addEventListener('click', function(e){
    e.preventDefault();
    const hiddenReviews = document.querySelectorAll('.review-card[style*="display: none"]');
    hiddenReviews.forEach(r => r.style.display = 'block');
    btn.style.display = 'none'; // ховаємо кнопку після натискання
});