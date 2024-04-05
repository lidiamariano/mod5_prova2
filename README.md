# Módulo 5 - Prova 2
## Processo para inicializar a aplicação:
**0) Ativar ambiente virtual:**
É indicado a utilização de um ambiente virtual para rodar esta aplicação. Para isso deve-se criar dentro da pasta flask-htmx o venv, por meio do seguinte comando, no powershell:
`python -m venv venv`. Depois será necessário ativar esse ambiente, pelo seguinte comando: `cd venv\Scripts`, em seguida: `.\Activate`.</br>

**1) Instalando depedências:**
Para instalar as depedências devemos utilizar o seguinte comando: `pip install -r requirements.txt`.</br>

**2) Navegar até a pasta src**
Dentro da página flask-htmx vá até a pasta src: `cd src`, e depois execute o programa pelo seguinte comando: `python main.py`</br>

## Como utilizar a aplicação:

Na rota principal há uma lista de todas as possíveis rotas a serem acessadas essas são:</br>
**-Dash:**</br>
Essa rota irá guardar todos os dados dos logs de acesso, que são "endereço", "metodo", "hora".
**-Echo:**</br>
Essa rota retorna um formulário em que os dados são coletados e guardados em um banco .json que é retornado na função
**-Info:**</br>
Essa rota retorna todas as informações de logs feitos.






