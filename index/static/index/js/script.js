let mainMenu = document.querySelector(".header_list");
let mainHamburger = document.querySelector(".hamburger");

mainHamburger.addEventListener('click', () => {
    mainMenu.classList.toggle("header_list--active");
    mainHamburger.classList.toggle("hamburger--active");
});


// Плавный скролл

let menuLinks = document.querySelectorAll('.header_link, .footer_link');

for (let menuLink of menuLinks) {
    menuLink.addEventListener('click', (event) => {
        event.preventDefault();
        let scrollToElem = menuLink.getAttribute('href');
        let coordinates = document.querySelector(scrollToElem).offsetTop;
        window.scrollTo({
            top: coordinates - 100,
            behavior: "smooth"
        });
        mainMenu.classList.remove("header_list--active");
        mainHamburger.classList.remove("hamburger--active");
    })
    
}


// Мигающая рамка
// setInterval(function() {
//     if (document.querySelector('.portfolio_item-img').style.boxShadow == 'rgba(130, 130, 130, 0.75) 0px 0px 4px') {
//         document.querySelector('.portfolio_item-img').style.boxShadow = 'rgba(0, 0, 0, 0.75) 0px 0px 4px';
//     } else {
//         document.querySelector('.portfolio_item-img').style.boxShadow = 'rgba(130, 130, 130, 0.75) 0px 0px 4px'
//     }
//   }, 2000);



// Первый слайдер
$('#vk_group_parser-slider').slick({
    centerMode: true,
    centerPadding: '0px',
    slidesToShow: 3,
    // dots: true,
    speed: 1200,

    prevArrow: $('#prev_arrow-vk_parser'),
    nextArrow: $('#next_arrow-vk_parser')
    // responsive: [
    //   {
    //     breakpoint: 768,
    //     settings: {
    //       arrows: false,
    //       centerMode: true,
    //       centerPadding: '40px',
    //       slidesToShow: 3
    //     }
    //   }
    // ]
  });

  // Модальное окно

let writeButton = document.querySelector('.button-write'); // кнопка написать
let modalWindow = document.querySelector('.modal');
let closeButton = document.querySelector('.modal_close');

modalWindow.addEventListener('click', () => {
    modalWindow.classList.remove('modal--active');  // закрытие модального окна при клике вне формы
})

closeButton.addEventListener('click', () => {
    modalWindow.classList.remove('modal--active');  // закрытие модального окна при клике на X
})

$(".modal_form").click(function(event) { // приостанавливает закрытие модального окна при кликах на форму
    event.stopPropagation();
});

writeButton.addEventListener('click', (clickButton) => {
    modalWindow.classList.add('modal--active');
    document.querySelector('.modal_name-input-input').focus();
})