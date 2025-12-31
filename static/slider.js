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

// ===== КНОПКА "ПОКАЗАТИ ВСІ ВІДГУКИ" =====
const reviewsBtn = document.querySelector('.all-reviews-link');

if (reviewsBtn) {
    reviewsBtn.addEventListener('click', function (e) {
        e.preventDefault();

        const hiddenReviews = document.querySelectorAll(
            '.review-card[style*="display: none"]'
        );

        hiddenReviews.forEach(r => r.style.display = 'block');
        reviewsBtn.style.display = 'none';
    });
}


// ===== КНОПКА "ПОКАЗАТИ ВСІ МІСТА" =====
const citiesBtn = document.getElementById("showCitiesBtn");
const cities = document.querySelector(".cities-route");

if (citiesBtn && cities) {
    citiesBtn.addEventListener("click", () => {
        cities.style.maxHeight = "none";
        citiesBtn.style.display = "none";
    });
}

