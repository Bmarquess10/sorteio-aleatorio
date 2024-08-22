# Sorteio Aleatório

Este é um projeto simples de sorteio aleatório desenvolvido com Flask, Python e JavaScript. O aplicativo permite que você insira um número total de opções e a quantidade de números a serem sorteados, e então retorna os números sorteados aleatoriamente.

## Como Usar

### 1. Clonar o Repositório

Primeiro, clone o repositório para a sua máquina local:
git clone https://github.com/seu-usuario/sorteio-aleatorio.git

2. Navegar até o Diretório do Projeto
cd sorteio-aleatorio

4. Criar e Ativar um Ambiente Virtual
python -m venv .venv

No Windows:
.venv\Scripts\activate
No macOS/Linux:
source .venv/bin/activate

4. Instalar Dependências
Instale as dependências necessárias com o seguinte comando:
pip install -r requirements.txt

6. Executar a Aplicação Localmente
Após instalar as dependências, execute o servidor Flask:
python app.py
O servidor Flask deve iniciar em http://127.0.0.1:5000/. Visite esse endereço no seu navegador para acessar a aplicação.

Como Funciona
Entrada de Dados: O usuário insere o número total de opções e a quantidade de números a serem sorteados.
Geração de Números Aleatórios: A aplicação usa a função random.sample do Python para selecionar os números sorteados.
Resultado: Os números sorteados são exibidos na tela.

Requisitos
Python 3.x
Flask

Tecnologias Usadas
Flask - Framework de microserviços para Python.
JavaScript - Para a manipulação de eventos no frontend.
HTML/CSS - Interface básica para a aplicação.

Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs, ou novas funcionalidades! Faça um fork deste repositório e envie um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Exemplo de Uso

Ao acessar a aplicação, você verá um formulário onde pode inserir os dados do sorteio e clicar em "Sortear" para gerar os números aleatórios.
