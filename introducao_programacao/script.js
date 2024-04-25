const produtos = [
    {
        id: 1,
        nome: "As 24 Horas da Paixão de Nosso Senhor Jesus Cristo",
        descricao: "Descrição livro - As 24 Horas da Paixão de Nosso Senhor Jesus Cristo",
        preco: "25",
        imagem: "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/as-24-horas-da-paixao_2020-05-14_09-08-17_0.jpg"
    },
    {
        id: 2,
        nome: "A Cura como Expressão da Misericórdia de Deus",
        descricao: "Descrição livro - A Cura como Expressão da Misericórdia de Deus",
        preco: "20",
        imagem: "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-cura-como-expressao-da-misericordia-de-deus_2022-03-23_15-13-56_0_321.jpg"
    },
    {
        id: 3,
        nome: "5 Passos para Ser Vencedor na Guerra Espiritual Atual",
        descricao: "Descrição livro - 5 Passos para Ser Vencedor na Guerra Espiritual Atual",
        preco: "30",
        imagem: "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/livro-5-passos-para-ser-vencedor-na-guerra-atual_2020-05-13_15-11-19_0.jpg"
    },
    {
        id: 4,
        nome: "A Fé de Ratzinger - A Teologia do Papa Bento XVI",
        descricao: "Descrição livro - A Fé de Ratzinger - A Teologia do Papa Bento XVI",
        preco: "20",
        imagem: "https://www.galaxcommerce.com.br/sistema/upload/2086/produtos/a-paixao-de-nosso-senhor-jesus-cristo_2023-06-20_09-13-09_0_367.jpg"
    }
]

var itensCarrinho = []

for (let produto of produtos) {    
    let CARD = `<div class='produtos'> \
    <div class='card'>\
    <img src='${produto.imagem}' class='card-img-top' alt='...'>\
    <div class='card-body'>\
    <h5 class='card-title'>${produto.nome}</h5>\
    <p class='card-text'>${produto.descricao}</p>\
    <p class='card-text preco'>R$ ${produto.preco}</p>\
    <a href='#' class='btn btn-primary btn-primary-personally' data-nome-produto='${produto.id}' data-bs-toggle='modal' data-bs-target='#exampleModal'>Adicionar no carrinho</a>\
    </div\
    ></div>\
    </div>`
    document.getElementById("produtos").innerHTML += CARD
}


var botoes = document.querySelectorAll(".btn-primary-personally")

for (let botao of botoes) {
    botao.addEventListener('click', function (data) {
        let nomeproduto = data.target
        document.getElementsByClassName("modal-body")[0].innerHTML = nomeproduto.getAttribute("data-nome-produto")
    })
}


document.getElementById("adicionarCarrinho").addEventListener('click', function () {
    let nome = document.getElementsByClassName("modal-body")[0].innerText
    itensCarrinho.push(nome)
    document.getElementById("contador").innerText = itensCarrinho.length
    console.log(itensCarrinho)

    
    document.getElementById("dropdownItens").innerHTML = ""
    for (let item of itensCarrinho) {
        console.log(item)
        document.getElementById("dropdownItens").innerHTML += `<li>${item} - R$0000</li>`
    }
    document.getElementById("dropdown").innerHTML += "<button type=button class=btn>Finalizar</button>"

})


document.getElementById("grupoCarrinho").addEventListener('click', function () {

    displayAtual = document.getElementById("dropdown").style.display
    
    if (displayAtual == "none") {
        document.getElementById("dropdown").style.display = "block"
    } else {
        document.getElementById("dropdown").style.display = "none"
    }

})
