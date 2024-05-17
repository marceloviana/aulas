var produtos = null

function renderProdutos () {

    for (let produto of produtos) {    
        let CARD = `<div class='produtos'> \
        <div class='card'>\
        <img src='${produto.imagem}' class='card-img-top' alt='...'>\
        <div class='card-body'>\
        <h5 class='card-title'>${produto.nome}</h5>\
        <p class='card-text'>${produto.descricao}</p>\
        <p class='card-text preco'>R$ ${produto.preco}</p>\
        <a href='#' class='btn btn-primary btn-primary-personally botao-abre-modal' data-id-produto='${produto.id}' data-bs-toggle='modal' data-bs-target='#exampleModal'>Adicionar no carrinho</a>\
        </div>\
        </div>\
        </div>`
        document.getElementById("produtos").innerHTML += CARD
    }

}


axios.get("http://localhost:8000/v1/produtos").then( response => {
    produtos = response.data
    renderProdutos()
    adicionarEventoCards()
})

