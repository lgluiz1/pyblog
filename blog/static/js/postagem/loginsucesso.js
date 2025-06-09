    // Escuta mensagem do popup após login
    window.addEventListener("message", function (event) {
        if (event.origin !== window.location.origin) return;

        if (event.data.tipo === "login_sucesso") {
            // Aqui você pode atualizar o estado da UI após login
            console.log("Login concluído via popup.");

            // Recarrega a página para atualizar o estado do usuário logado
            location.reload();
        }
    });