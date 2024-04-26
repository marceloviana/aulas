for (let botao of document.querySelectorAll(".btn-primary-personally")) {
    botao.addEventListener('click', function (data) {
        let produtoId = ~~data.target.getAttribute("data-id-produto") - 1
        // Adiciona o nome do produto ao corpo do modal
        document.getElementsByClassName("modal-body")[0].innerHTML = `${produtos[produtoId].nome} - <strong>R$ ${produtos[produtoId].preco}</strong>`

        // insere o ID do produto no data- do botão de "Adicionar" dentro do modal.
        // Isso permite saber qual produto será efetivamente adicionado ao carrinho
        document.getElementById("botaoAdicionarAoCarrinho").setAttribute("data-id-produto", produtoId)
    })
}


