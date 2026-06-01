# DigimonDex

## Sobre o Projeto

O DigimonDex é uma aplicação Full Stack desenvolvida para a disciplina de Linguagem de Desenvolvimento Web.

O sistema permite consultar e cadastrar Digimons através de uma API REST construída com Flask. Os dados são consumidos por uma interface desktop desenvolvida com Flet. Além disso, o projeto possui uma Landing Page criada com HTML, CSS e Tailwind CSS para apresentação da aplicação.

---

## Tecnologias Utilizadas

### Backend

* Python
* Flask
* Flask Blueprints
* Flasgger (Swagger)
* Pydantic

### Frontend

* Flet
* Requests

### Landing Page

* HTML5
* CSS3
* Tailwind CSS

---

## Estrutura do Projeto

```text
DigimonDex
│
├── backend
│   ├── app.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── digimons.py
│   └── schemas
│       ├── __init__.py
│       └── digimon_schema.py
│
├── frontend
│   └── app.py
│
├── landing-page
│   ├── index.html
│   └── style.css
│
└── README.md
```

---

## Funcionalidades

* Listar Digimons cadastrados
* Buscar Digimon por ID
* Cadastrar novos Digimons
* Validação de dados utilizando Pydantic
* Documentação Swagger integrada
* Interface desktop desenvolvida com Flet

---

## Endpoints da API

### Listar todos os Digimons

```http
GET /digimons
```

### Buscar Digimon por ID

```http
GET /digimons/{id}
```

### Cadastrar novo Digimon

```http
POST /digimons
```

Exemplo de JSON:

```json
{
  "nome": "Patamon",
  "nivel": "Rookie"
}
```

---

## Pré-requisitos

Antes de iniciar o projeto, é necessário ter instalado:

* Python 3.10 ou superior
* Pip

Verifique a instalação com:

```bash
python --version
```

---

## Instalação das Dependências

Na pasta raiz do projeto execute:

```bash
python -m pip install flask
python -m pip install flasgger
python -m pip install pydantic
python -m pip install flet
python -m pip install requests
```

Ou:

```bash
python -m pip install flask flasgger pydantic flet requests
```

---

## Executando o Backend

Abra um terminal na pasta backend:

```bash
cd backend
python app.py
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

---

## Acessando a Documentação Swagger

Com o backend em execução, abra no navegador:

```text
http://127.0.0.1:5000/apidocs
```

A documentação permite testar todos os endpoints diretamente pela interface web.

---

## Executando o Frontend

Abra um novo terminal:

```bash
cd frontend
python app.py
```

A interface Flet será aberta automaticamente.

---

## Executando a Landing Page

Abra o arquivo:

```text
landing-page/index.html
```

em qualquer navegador moderno.

---

## Fluxo de Utilização

1. Inicie o backend Flask.
2. Acesse o Swagger para visualizar a documentação.
3. Execute o frontend Flet.
4. Visualize os Digimons cadastrados.
5. Cadastre novos Digimons através do formulário.
6. Verifique a atualização da lista na interface.

---

## Objetivo Acadêmico

Este projeto foi desenvolvido com o objetivo de demonstrar:

* Criação de APIs REST utilizando Flask
* Organização de rotas com Blueprints
* Validação de dados com Pydantic
* Documentação de APIs utilizando Swagger
* Consumo de APIs em aplicações desktop com Flet
* Desenvolvimento de Landing Pages com Tailwind CSS
* Integração entre frontend e backend

---

