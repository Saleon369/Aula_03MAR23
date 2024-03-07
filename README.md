# Gerenciamento de Biblioteca com Flask

Este projeto é uma aplicação web Flask que permite o gerenciamento de uma coleção de livros. Os usuários podem adicionar, consultar, editar e deletar livros da biblioteca. A aplicação usa SQLite como banco de dados e inclui uma interface de usuário com templates HTML para interação fácil.

## Estrutura do Projeto

O projeto inclui os seguintes arquivos e diretórios principais:

- `app.py`: O arquivo principal da aplicação Flask que define rotas e lógica.
- `templates/`: Diretório que contém os templates HTML para as páginas da aplicação.
  - `adicionar.html`: Template para adicionar novos livros.
  - `consultar.html`: Template para visualizar a lista de livros.
  - `editar.html`: Template para editar os detalhes de um livro existente.
  - `index.html`: Template que serve como a página inicial e lista todos os livros.
- `instance/`: Diretório que contém o banco de dados SQLite da aplicação.
- `venv/`: Diretório do ambiente virtual Python para o projeto.
- `requirements.txt`: Lista todas as dependências necessárias para o projeto.
- `Pipfile` e `Pipfile.lock`: Arquivos usados pelo Pipenv para gerenciar dependências.

## Funcionalidades

- **CRUD de Livros**: Crie, leia, atualize e delete informações de livros.
- **Interface Amigável**: Utilize templates HTML para interagir com a aplicação.
- **Armazenamento com SQLite**: Use SQLite para armazenar dados de livros de forma persistente.

## Tecnologias Utilizadas

- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- HTML
- SQLite

## Configuração e Execução

### Pré-Requisitos

- Python 3.6 ou superior
- Pipenv para a gestão de dependências

### Instalação

1. Clone o repositório:

    ```bash
    git clone <URL do repositório>
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd ProjetoBiblioteca
    ```

3. Instale as dependências usando Pipenv:

    ```bash
    pipenv install
    ```

### Como Executar

1. Ative o ambiente virtual:

    ```bash
    pipenv shell
    ```

2. Inicie o aplicativo Flask:

    ```bash
    flask run
    ```

3. Acesse a aplicação em `http://localhost:5000/`.

## API Endpoints

- **POST /adicionar**: Adiciona um novo livro.
- **GET /consultar**: Lista todos os livros.
- **GET /editar/<id>**: Mostra o formulário de edição para um livro.
- **POST /editar/<id>**: Submete as alterações de um livro.
- **GET /deletar/<id>**: Deleta um livro.

## Contribuição

Contribuições são bem-vindas! Consulte `CONTRIBUTING.md` para obter diretrizes sobre como contribuir para o projeto.

## Licença

Este projeto é distribuído sob a Licença MIT, conforme detalhado no arquivo `LICENSE.md`.
