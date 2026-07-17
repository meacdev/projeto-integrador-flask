// Select de municípios

const selectEstados = document.getElementById('estados')
const selectMunicipios = document.getElementById('cidades')
let cidadesPorEstado = {}

async function carregarDados() {
    try {
        const resposta = await fetch('municipios.json')
        if (!resposta.ok) {
            throw new Error(`HTTP ${resposta.status}`)
        }
        cidadesPorEstado = await resposta.json()
        selectEstados.disabled = false
    } catch (error) {
        console.error("Erro ao carregar os dados dos municípios: ", error)
        selectEstados.disabled = true
    }
}

selectEstados.addEventListener('change', function () {
    const estadoSelecionado = this.value
    selectMunicipios.innerHTML = '<option value="" disabled selected>Selecione um município</option>'

    const municipios = cidadesPorEstado[estadoSelecionado]
    if (municipios && municipios.length > 0) {
        selectMunicipios.disabled = false

        const fragment = document.createDocumentFragment()
        municipios.forEach(function (cidade) {
            const option = document.createElement('option')
            option.value = cidade
            option.textContent = cidade
            fragment.appendChild(option)
        })
        selectMunicipios.appendChild(fragment)
    } else {
        selectMunicipios.disabled = true
    }
})

carregarDados()