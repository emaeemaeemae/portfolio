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

// Модальное окно

let writeButton = document.querySelector('.button-write'); // кнопка написать
let modalWindow = document.querySelector('.modal');
let modalForm = $('.modal_form');
let closeButtons = document.querySelectorAll('.modal_close');

modalWindow.addEventListener('click', () => {
    modalWindow.classList.remove('modal--active');  // закрытие модального окна при клике вне формы
})

for (let closeButton of closeButtons) {
    closeButton.addEventListener('click', () => {
        modalWindow.classList.remove('modal--active');  // закрытие модального окна при клике на X
    })
}

modalForm.click(function (event) { // приостанавливает закрытие модального окна при кликах на форму
    event.stopPropagation();
});


writeButton.addEventListener('click', () => {
    $('.success').removeClass('success_active');
    modalForm.removeClass('modal_hidden');
    modalWindow.classList.add('modal--active');
    document.querySelector('.modal_name-input-input').focus();
})

modalForm.submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: '/',
        type: 'POST',
        data: modalForm.serialize(),
        success: function () {
            $('.success').addClass('success_active'); // вывод сообщения об отправке
            modalForm.addClass('modal_hidden'); // скрытие формы
            modalForm[0].reset();
        }
    });
});