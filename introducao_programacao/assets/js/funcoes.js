var itensCarrinho = []

function adicionarItemCarrinho (id) {
    itensCarrinho.push(produtos[id])

    // Configure total itens:
    document.getElementById("contador").innerText = itensCarrinho.length

    // Configure itens no dropdown:
    
    const initialValue = 0;
    document.getElementById("dropdownItens").innerHTML = `Total: R$ ${itensCarrinho.reduce((accumulator, currentValue) => accumulator + ~~currentValue.preco, initialValue)}`;
    for (let item of itensCarrinho) {
        document.getElementById("dropdownItens").innerHTML += `<li>${item.nome} - R$ ${item.preco}</li>`
    }    
}

function removeItenCarrinho (indice) {
    document.getElementById("dropdownItens").innerHTML = ""

    itensCarrinho.splice(indice, 1)
    for (let item of itensCarrinho) {
        document.getElementById("dropdownItens").innerHTML += `<li>${item.nome} - R$ ${item.preco}</li>`
    }    
}