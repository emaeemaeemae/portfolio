// Положение меню

let head = document.querySelector('.header');
let footer = document.querySelector('.footer_wrap');

head.style.left = getComputedStyle(footer).marginLeft;

window.onresize = function() {
    head.style.left = getComputedStyle(footer).marginLeft;
}

// Инициализация слайдера
$('.customers_main-slider').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    prevArrow: $('.customers_arrows-prev'),
    nextArrow: $('.customers_arrows-next'),

    responsive: [
        {
          breakpoint: 1240,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
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

        let correction = 100
        if (menuLink.href.includes('#catalog')) {
            correction = 200;
        }
        else if (menuLink.href.includes('#customers')) {
            correction = -10;
        }

        window.scrollTo({
            top: coordinates - correction,
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
            let name = item.querySelector('.catalog_item-name'); // название
            name.setAttribute('style', 'text-transform: capitalize');
            orderType.value = name.innerText;
            document.querySelector('.modal_name-input-input').focus();
            // $(orderType).val(name.innerText);
    })
}


// Кнопка Читать далее

let read_more_buttons = document.getElementsByClassName('read_more')
let container = document.querySelector('.customers_container'); // общий контейнер отзыва
// alert(container.offsetHeight);

for (let read_more of read_more_buttons) {

    let item = read_more.closest('.customers_slider-item-div'); // отзыв клиента
    let area = item.querySelector('.customer_review'); // отзыв
    let area_text = area.querySelector('.customer_review-text');

    if (area.offsetHeight >= area_text.offsetHeight) {
        // alert(area_text.style.height);
        read_more.style.display = 'none'
    }

    read_more.addEventListener('click', () => {     
        area.style.height = 'auto';
        container.style.height = 'auto';
        read_more.style.color = 'white';
    })
}