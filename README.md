
```markdown
## Gerenciamento de Biblioteca com Flask

Este projeto é uma aplicação Flask que fornece uma API RESTful para o gerenciamento de uma coleção de livros em uma biblioteca. Utilizando Flask, Flask-SQLAlchemy com SQLite como banco de dados, e Flask-HTTPAuth para autenticação, permite aos usuários realizar operações CRUD (criar, ler, atualizar e deletar livros) através de endpoints HTTP, com a exigência de autenticação para operações que alteram os dados.

### Funcionalidades

* **CRUD de Livros com Autenticação**: Crie, leia, atualize e delete livros usando a API REST. Operações de criação, atualização e exclusão exigem autenticação.
* **Pesquisa Avançada**: Pesquise livros por título, autor, ano de publicação e gênero.
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
* **GET /pesquisar**: Pesquise livros fornecendo parâmetros opcionais como `titulo`, `autor`, `ano_publicacao` e `genero`. Exemplo: `GET /pesquisar?titulo=O Nome da Rosa&autor=Umberto Eco`.


### Testando a Funcionalidade de Pesquisa Avançada com Postman

A funcionalidade de pesquisa avançada permite que você encontre livros com base em múltiplos critérios como título, autor, ano de publicação e gênero. Siga os passos abaixo para testar esta funcionalidade usando o Postman:

1. Abra o Postman e selecione o método de requisição para `GET`.
2. Na barra de endereços do Postman, insira a URL do seu servidor local seguida pelo endpoint de pesquisa. Por exemplo: `http://localhost:5000/pesquisar`.
3. Abaixo da barra de endereços, localize a seção `Params`. Aqui, você pode adicionar os parâmetros de consulta que deseja usar para filtrar sua pesquisa. Clique no botão `Add Param` e insira os detalhes:
   - Em `KEY`, digite o campo pelo qual você deseja pesquisar (por exemplo, `titulo`, `autor`, `ano_publicacao`, `genero`).
   - Em `VALUE`, digite o valor específico que você está buscando (por exemplo, `1984` para `titulo`, `George Orwell` para `autor`).
4. Você pode adicionar múltiplos parâmetros de pesquisa clicando repetidamente em `Add Param` e preenchendo as chaves e valores correspondentes.
5. Uma vez que todos os parâmetros estejam definidos, clique no botão `Send` para realizar a requisição.
6. O Postman enviará a requisição ao seu servidor Flask, que processará a pesquisa com os critérios fornecidos. Os resultados filtrados serão exibidos no painel de resposta do Postman.
7. Se nenhum livro corresponder aos critérios de pesquisa, você receberá uma lista vazia como resposta. Se houver correspondências, você verá os detalhes dos livros que atendem aos critérios especificados.

**Exemplo de Uso:**

Para pesquisar um livro com o título "1984" e autor "George Orwell", seus parâmetros no Postman ficarão assim:

- **KEY**: `titulo` **VALUE**: `1984`
- **KEY**: `autor` **VALUE**: `George Orwell`

A URL final no Postman parecerá com isso: `http://localhost:5000/pesquisar?titulo=1984&autor=George Orwell`

Após configurar, clique em `Send` e analise os livros retornados que correspondem aos seus parâmetros de pesquisa no painel de resposta do Postman.


### Contribuindo

Contribuições são muito bem-vindas! Por favor, leia o CONTRIBUTING.md para mais detalhes sobre nosso código de conduta, e o processo para enviar pedidos de pull.

### Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE.md para detalhes.

---
```
