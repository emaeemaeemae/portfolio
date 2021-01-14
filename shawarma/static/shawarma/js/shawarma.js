// Инициализация слайдера
$('.customers_main-slider').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow: $('.customers_arrows-prev'),
    nextArrow: $('.customers_arrows-next'),

    responsive: [
        {
          breakpoint: 1240,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
    ]
});

// Меню
let mainMenu = document.querySelector(".header_list");
let mainHamburger = document.querySelector(".hamburger");


mainHamburger.addEventListener('click', () => {
    mainMenu.classList.toggle("header_list--active");
    mainHamburger.classList.toggle("hamburger--active");
});

// Плавный скролл

let menuLinks = document.querySelectorAll('.header_link, .footer_link, .primary_button-link');

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

// Модальное окно

let orderButtons = document.querySelectorAll('.catalog_item-offer-button'); // кнопки заказа
let modalWindow = document.querySelector('.modal');
let orderType = document.querySelector('.modal_type-input-input'); // окно ввода вида шаурмы
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

for (let orderButton of orderButtons) {
        orderButton.addEventListener('click', (clickButton) => {
        modalWindow.classList.add('modal--active');
        // поиск названия выбранной шаурмы через родительскую карточку
        let item = clickButton.target.closest('.catalog_item'); // карточка шаурмы 
        let name = item.querySelector('.catalog_item-name').innerHTML.toString(); // название
        orderType.value = name.trim();
        document.querySelector('.modal_name-input-input').focus();
        // $(orderType).val(name.innerText);
    })
}


