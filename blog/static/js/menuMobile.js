const hamburge = document.getElementById('menu-icon');
const menuMobile = document.querySelector('.menu-mobile');
const dropdown = document.querySelector('.dropdown-menu');
const menu = document.querySelector('.menu');
const menumobileitems = document.querySelector('.menu-mobile-items');


const navbar = document.querySelector('.navbar');
const navbarOffset = navbar.offsetTop;

let menuAberto = false;

menuMobile.addEventListener('click', () => {
    dropdown.classList.toggle('active');
    hamburge.classList.toggle('fa-xmark');

    if (!menuAberto) {
        menumobileitems.style.right = '0';
        menuMobile.style.backgroundColor = '#25252536';
    } else {
        menumobileitems.style.right = '-250px';
        menuMobile.style.backgroundColor = 'transparent';
    }

    menuAberto = !menuAberto; // alterna o estado do menu
});

function ajustarMenu() {
    if (window.innerWidth <= 768) {
        menu.classList.add('desativar-menu'); // Adiciona a classe desativar-menu
        hamburge.classList.remove('fa-xmark'); // Remove a classe fa-xmark
        hamburge.classList.add('fa-bars'); // Adiciona a classe fa-bars

        if (menuMobile.classList.contains('desativar-menu')) { // Verifica se a classe desativar-menu está presente
            menuMobile.classList.remove('desativar-menu'); // Remove a classe desativar-menu
        }
    } else {
        menu.classList.remove('desativar-menu'); // Remove a classe desativar-menu
        menuMobile.classList.add('desativar-menu'); // Adiciona a classe desativar-menu
    }
}

window.addEventListener('load', () => {
    ajustarMenu();

    // Ajusta o padding do main logo no carregamento
    const main = document.querySelector('main');
    const navbarHeight = navbar.offsetHeight;

    if (window.scrollY >= navbarOffset) {
        navbar.classList.add('fixed');
        main.style.paddingTop = navbarHeight + 'px';
    } else {
        navbar.classList.remove('fixed');
        main.style.paddingTop = '0px';
    }
});


// Executa no carregamento da página
window.addEventListener('load', ajustarMenu);

// Executa sempre que redimensionar a tela
window.addEventListener('resize', ajustarMenu);