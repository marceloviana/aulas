var itensCarrinho = []

function adicionarItemCarrinho (id) {
    
    if (id) {
        itensCarrinho.push(produtos[id])
    }
    
    // Configure total itens:
    document.getElementById("contador").innerText = itensCarrinho.length

    // Configure itens no dropdown:
    
    const initialValue = 0;
    document.getElementById("dropdownItens").innerHTML = `Total: R$ ${itensCarrinho.reduce((accumulator, currentValue) => accumulator + ~~currentValue.preco, initialValue)}`;
    for (let item of itensCarrinho) {
        document.getElementById("dropdownItens").innerHTML += `<li>${item.nome} - R$ ${item.preco} <button onclick=removeItenCarrinho(${item.id})>remover</button></li>`
    }    
}

function removeItenCarrinho (idItemCarrinho) {
    
    itensCarrinho = itensCarrinho.filter((item) => item.id != idItemCarrinho)
    
    adicionarItemCarrinho(null)
}

function adicionarEventoCards () {

    for (let botao of document.querySelectorAll(".botao-abre-modal")) {
        botao.addEventListener('click', function (data) {
            let produtoId = ~~data.target.getAttribute("data-id-produto") - 1

            // Adiciona o nome do produto ao corpo do modal
            document.getElementsByClassName("modal-body")[0].innerHTML = `${produtos[produtoId].nome} - <strong>R$ ${produtos[produtoId].preco}</strong>`
    
            // insere o ID do produto no data- do botão de "Adicionar" dentro do modal.
            // Isso permite saber qual produto será efetivamente adicionado ao carrinho
            document.getElementById("botaoAdicionarAoCarrinho").setAttribute("data-id-produto", produtoId)
        })

    }    
}

function finalizarCompra() {

    if (!itensCarrinho.length) {
        alert("Não há itens no carrinho!")
        return
    }
    
    axios.post("http://localhost:8000/v1/finalizar_compra", {itensCarrinho, id_usuario: 1}).then(response => {
        alert(response.data)
        window.location.reload()
    })

}


