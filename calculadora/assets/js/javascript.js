const elementos = document.getElementsByTagName("li")
for (i in elementos) {

   if ( !isNaN(elementos[i].innerText) || elementos[i].innerText == "*" || elementos[i].innerText == "+" || elementos[i].innerText == "-") {
         
         elementos[i].addEventListener("click", function (data) {
            value = data.target.innerText
            document.getElementById("operacao").innerText += value
         })
      }

}

function somar() {
   document.getElementById("operacao").innerText = eval(document.getElementById("operacao").innerText)
}

function limpar() {
   document.getElementById("operacao").innerText = ""
}
