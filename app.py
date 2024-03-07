from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Usuários (Para exemplo, em produção use um método mais seguro!)
users = {
    "admin": generate_password_hash("secret")
}

# Função de verificação de senha
@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

# Definição do modelo de dados
class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

# Rotas CRUD protegidas
@app.route('/livro', methods=['POST'])
@auth.login_required
def adicionar_livro():
    dados = request.json
    novo_livro = Livro(titulo=dados['titulo'], autor=dados['autor'])
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({'mensagem': 'Livro adicionado com sucesso!'}), 201

@app.route('/livro/<int:id>', methods=['PUT'])
@auth.login_required
def atualizar_livro(id):
    livro = Livro.query.get_or_404(id)
    dados = request.json
    livro.titulo = dados.get('titulo', livro.titulo)
    livro.autor = dados.get('autor', livro.autor)
    db.session.commit()
    return jsonify({'mensagem': 'Livro atualizado com sucesso!'})

@app.route('/livro/<int:id>', methods=['DELETE'])
@auth.login_required
def deletar_livro(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return jsonify({'mensagem': 'Livro deletado com sucesso!'})

# Rotas públicas
@app.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor} for livro in livros])

@app.route('/livro/<int:id>', methods=['GET'])
def pegar_livro(id):
    livro = Livro.query.get_or_404(id)
    return jsonify({'id': livro.id, 'titulo': livro.titulo, 'autor': livro.autor})

# Executar o aplicativo
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria o banco de dados e as tabelas
    app.run(debug=True)
