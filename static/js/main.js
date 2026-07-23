// Select de municípios

// Armazena os selects
const selectEstados = document.getElementById('estados');
const selectMunicipios = document.getElementById('cidades');

// Array vazio de cidades de cada estado
let cidadesPorEstado = {}

// Função assíncrona para carregar municipios.json
async function carregarDados() {
    try {
        const resposta = await fetch('/static/municipios.json');
        if (!resposta.ok) {
            throw new Error(`HTTP ${resposta.status}`);
        }
        cidadesPorEstado = await resposta.json();
        selectEstados.disabled = false;
    } catch (error) {
        console.error("Erro ao carregar os dados dos municípios: ", error);
        selectEstados.disabled = true;
    }
}

// Detecta o estado selecionado pelo usuário
selectEstados.addEventListener('change', function () {
    const estadoSelecionado = this.value;
    selectMunicipios.innerHTML = '<option value="" disabled selected>Selecione um município</option>';

    const municipios = cidadesPorEstado[estadoSelecionado];
    if (municipios && municipios.length > 0) {
        selectMunicipios.disabled = false;

        const fragment = document.createDocumentFragment();
        municipios.forEach(function (cidade) {
            const option = document.createElement('option');
            option.value = cidade;
            option.textContent = cidade;
            fragment.appendChild(option);
        })
        selectMunicipios.appendChild(fragment);
        
    } else selectMunicipios.disabled = true;
    
})

carregarDados();

/////////////////////// CRUD ///////////////////////

// 1. CREATE

async function criarRegistro(e){
    e.preventDefault();
    try {
        const form = e.target;
        const dados = new FormData(form);

        const resposta = await fetch("/registro", {
            method: "POST",
            body: dados
        });
        
        const html = await resposta.text();
        document.getElementById("resultado-cadastro").innerHTML = html;
        form.reset();
        
    } catch (error){
        console.error("Falha ao cadastrar", error);
        document.getElementById("resultado-cadastro").innerHTML = "<p>Algo deu errado :(</p>";
    };
    
};

form_cadastro = document.getElementById("cadastro");
if (form_cadastro) form_cadastro.addEventListener("submit", criarRegistro);

// 2. READ

async function buscarRegistro(e) {
    e.preventDefault();

    try{
     const id = document.getElementById("texto-id").value;

        const resposta = await fetch("/registro?texto-id=" + encodeURIComponent(id), {
            method: "GET"
        });

        if (!resposta.ok) {
            throw new Error(`Erro na busca: ${resposta.status}`);
        }

        const html = await resposta.text();
        document.getElementById("resultado-busca").innerHTML = html;

    } catch (error) {
        console.error("Falha ao buscar registro");
        document.getElementById("resultado-busca").innerHTML = "<p>Algo deu errado :(</p>"
    }
};

form_buscar = document.getElementById("buscar");
if (form_buscar) form_buscar.addEventListener("submit", buscarRegistro);

// 3. UPDATE

function editarRegistro(){
    const id = botao.dataset.id;
    
};

document.querySelectorAll(".btn-editar").forEach(botao =>{
    botao.addEventListener("click", editarRegistro());
});