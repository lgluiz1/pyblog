
const botaoComentario = document.querySelector('.botao-comentario-exibir');
const comentarioPost = document.querySelector('.comentario-post');
const loadingComents = document.querySelector('.typewriter');
const divEnviaComentario = document.querySelector('.comentario-enviar');
const divSemComentarios = document.querySelector('.sem-comentario');
const bottonAbrirComentario = document.querySelector('.botao-comentario-enviar');
const escerverComentario = document.querySelector('.comentario-box');


const botaoResponder = document.querySelector('.botao-comentario-responder');
const botaoDenunciar = document.querySelector('.botao-comentario-denunciar');
const responderComentario = document.querySelector('.comentario-box-resposta');
const divDenuncia = document.querySelector('.comentario-denuncia');


function abrirPopupGithub(event) {
    event.preventDefault();

    const largura = 600;
    const altura = 700;
    const left = (screen.width - largura) / 2;
    const top = (screen.height - altura) / 2;

    window.open(
        '/accounts/github/login/?process=login',
        'LoginGitHub',
        `width=${largura},height=${altura},top=${top},left=${left},resizable=yes,scrollbars=yes,status=no`
    );
}

document.addEventListener('click', function (e) {
    // Botão responder
    if (e.target.closest('.botao-comentario-responder')) {
        const comentarioBox = e.target.closest('.comentario-body');
        const responderComentario = comentarioBox.querySelector('.comentario-box-resposta');
        const denunciaBox = comentarioBox.querySelector('.comentario-denuncia');

        const estaVisivel = responderComentario.style.display === 'block';

        responderComentario.style.display = estaVisivel ? 'none' : 'block';
        denunciaBox.style.display = 'none';
    }

    // Botão denunciar
    if (e.target.closest('.botao-comentario-denunciar')) {
        const comentarioBox = e.target.closest('.comentario-body');
        const denunciaBox = comentarioBox.querySelector('.comentario-denuncia');
        const responderComentario = comentarioBox.querySelector('.comentario-box-resposta');

        const estaVisivel = denunciaBox.style.display === 'block';

        denunciaBox.style.display = estaVisivel ? 'none' : 'block';
        responderComentario.style.display = 'none';
    }
});





document.addEventListener('DOMContentLoaded', function () {
    const botaoAbrir = document.getElementById('botaoAbrirModalLogin');
    const modal = document.getElementById('modalLogin');
    const closeModal = document.querySelector('.close-modal');
    const githubBtn = document.getElementById('loginGithubBtn');

    botaoAbrir.addEventListener('click', () => modal.style.display = 'block');

    closeModal.addEventListener('click', () => modal.style.display = 'none');

    // Ouve mensagem do popup de login
    window.addEventListener('message', function (event) {
        if (event.origin !== window.location.origin) return;

        if (event.data === 'login_sucesso') {
            modal.style.display = 'none';
            location.reload(); // Ou atualize só parte da página
        }
    });

    githubBtn.addEventListener('click', (event) => {
        event.preventDefault();

        const width = 600, height = 600;
        const left = (screen.width / 2) - (width / 2);
        const top = (screen.height / 2) - (height / 2);

        window.open(
            '/accounts/github/login/?process=login',
            'Login GitHub',
            `width=${width},height=${height},top=${top},left=${left}`
        );
    });

    // Fecha modal se clicar fora do conteúdo
    window.addEventListener('click', (e) => {
        if (e.target == modal) modal.style.display = 'none';
    });
});



botaoComentario.addEventListener('click', function () {
    const iconeUp = botaoComentario.querySelector('.fa-angle-up');
    const iconeDown = botaoComentario.querySelector('.fa-angle-down');

    const estaFechado = comentarioPost.getAttribute('data-aberto') !== 'true';

    if (estaFechado) {
        // Garante que todos os comentários estejam visíveis para calcular a altura real
        comentarioPost.style.display = 'flex';
        comentarioPost.style.height = comentarioPost.scrollHeight + 'px';
        comentarioPost.style.padding = '10px';
        comentarioPost.setAttribute('data-aberto', 'true');

        comentarioPost.addEventListener('transitionend', function removerAltura() {
            comentarioPost.style.height = 'auto';
            comentarioPost.removeEventListener('transitionend', removerAltura);
        });

        iconeUp.style.display = 'flex';
        iconeDown.style.display = 'none';
    } else {
        // Recolher
        comentarioPost.style.height = comentarioPost.scrollHeight + 'px'; // define altura atual
        comentarioPost.offsetHeight; // força reflow
        comentarioPost.style.height = '0px';
        comentarioPost.style.padding = '0';
        comentarioPost.setAttribute('data-aberto', 'false');

        iconeUp.style.display = 'none';
        iconeDown.style.display = 'flex';
    }
});


const emojiButtons = document.querySelectorAll('.emoji-btn');
const emojiPicker = document.getElementById('emoji-picker');

let inputAtivo = null;

// Para cada botão .emoji-btn, adiciona o comportamento
emojiButtons.forEach(botao => {
  botao.addEventListener('click', (e) => {
    e.preventDefault();

    // Encontra o contêiner pai (.comentario-box ou .comentario-box-resposta)
    const container = botao.closest('.comentario-box, .comentario-box-resposta');
    inputAtivo = container.querySelector('textarea');

    // Posição do botão na tela
    const rect = botao.getBoundingClientRect();
    emojiPicker.style.top = `${rect.bottom + window.scrollY}px`;
    emojiPicker.style.left = `${rect.left + window.scrollX}px`;
    emojiPicker.style.display = 'block';
  });
});

// Quando o usuário seleciona um emoji
emojiPicker.addEventListener('emoji-click', (event) => {
  if (inputAtivo) {
    inputAtivo.value += event.detail.unicode;
    emojiPicker.style.display = 'none';
  }
});

// (Opcional) Fechar o picker ao clicar fora
document.addEventListener('click', (e) => {
  if (!emojiPicker.contains(e.target) && !e.target.closest('.emoji-btn')) {
    emojiPicker.style.display = 'none';
  }
});