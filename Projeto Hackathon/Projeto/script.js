console.log("Dentro da função")
async function enviar() {
    console.log("Olá Olá")
    form = document.getElementById("formulario")
    dados = new FormData(form)
    console.log(dados)
    resposta = await fetch(
        "http://127.0.0.1:8000/disciplinas/",
        {method: "POST", body: dados}
    )
}

async function criar_lista() {
    resposta = await fetch(
        "http://127.0.0.1:8000/disciplinas/",
    )
    dados = await resposta.json()
    console.log(dados)
    div = document.getElementById("div_disc_cadastros")
    div.innerHTML = null
    ul = document.createElement('ul')
    dados.forEach(d => {
        li = document.createElement('li')
        li.innerHTML = d[0] + " - " + d[1]
        ul.appendChild(li)
    });
    div.appendChild(ul)
    
}

window.addEventListener("load", criar_lista)