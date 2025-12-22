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
