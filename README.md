
---

## Gerenciamento de Biblioteca com Flask

Este projeto é uma aplicação Flask que fornece uma API RESTful para o gerenciamento de uma coleção de livros em uma biblioteca. Utilizando Flask, Flask-SQLAlchemy com SQLite como banco de dados, e Flask-HTTPAuth para autenticação, permite aos usuários realizar operações CRUD (criar, ler, atualizar e deletar livros) através de endpoints HTTP, com a exigência de autenticação para operações que alteram os dados.

### Funcionalidades

* **CRUD de Livros com Autenticação**: Crie, leia, atualize e delete livros usando a API REST. Operações de criação, atualização e exclusão exigem autenticação.
* **Autenticação de Usuários**: Acesso controlado às operações de manipulação de livros através de autenticação básica HTTP.
* **Armazenamento com SQLite**: Facilita o armazenamento e recuperação de dados de livros.
* **Feedback ao Usuário**: Fornece respostas claras e informativas para as ações do usuário.

### Tecnologias Utilizadas

* Flask
* Flask-SQLAlchemy
* SQLite
* Flask-HTTPAuth

### Como Configurar

#### Pré-Requisitos

* Python 3.6 ou superior
* pip

#### Instalação

1. Clone o repositório para sua máquina local:

```bash
git clone <URL do repositório>
```

2. Navegue até o diretório do projeto:

```bash
cd <nome do diretório do projeto>
```

3. Instale as dependências necessárias:

```bash
pip install flask flask_sqlalchemy flask_httpauth
```

### Como Executar

1. Antes de iniciar o servidor, defina os usuários e senhas para autenticação. **Nota: O exemplo no código utiliza um método simples para fins de demonstração. Em produção, utilize métodos mais seguros para gerenciar usuários e senhas.**

2. Inicie o servidor Flask executando:

```bash
python app.py
```

3. A aplicação agora estará rodando em http://localhost:5000/. Você pode acessar os endpoints definidos utilizando um cliente HTTP como Postman ou via curl, fornecendo as credenciais de usuário quando necessário.

### Endpoints da API

* **POST /livro** (Protegido): Adiciona um novo livro. Requer autenticação. Exemplo de corpo da requisição: `{"titulo": "Novo Livro", "autor": "Autor"}`.
* **GET /livros**: Retorna uma lista de todos os livros.
* **GET /livro/<id>**: Retorna detalhes de um livro específico.
* **PUT /livro/<id>** (Protegido): Atualiza um livro existente. Requer autenticação. Exemplo de corpo da requisição: `{"titulo": "Livro Atualizado", "autor": "Autor Atualizado"}`.
* **DELETE /livro/<id>** (Protegido): Deleta um livro específico. Requer autenticação.

### Testando Autenticação com Postman

Para testar endpoints protegidos com autenticação no Postman:

1. Abra o Postman e crie uma nova requisição.
2. Selecione o tipo de requisição (POST, PUT, DELETE) e insira o URL do endpoint.
3. Na aba "Authorization", selecione o tipo "Basic Auth" e insira as credenciais de usuário.
4. Configure o corpo da requisição conforme necessário e envie a requisição.

### Contribuindo

Contribuições são muito bem-vindas! Por favor, leia o CONTRIBUTING.md para mais detalhes sobre nosso código de conduta, e o processo para enviar pedidos de pull.

### Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.

---
