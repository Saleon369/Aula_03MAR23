from flask_migrate import Migrate
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SECRET_KEY'] = 'uma-chave-secreta'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    ano_publicacao = db.Column(db.Integer, nullable=False)
    genero = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Livro {self.titulo}>'

@app.route('/')
def index():
    livros = Livro.query.all()
    return render_template('index.html', livros=livros)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        ano_publicacao = request.form['ano_publicacao']
        genero = request.form['genero']
        novo_livro = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao, genero=genero)
        db.session.add(novo_livro)
        db.session.commit()
        flash('Livro adicionado com sucesso!')
        return redirect(url_for('index'))
    return render_template('adicionar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    livro = Livro.query.get_or_404(id)
    if request.method == 'POST':
        livro.titulo = request.form['titulo']
        livro.autor = request.form['autor']
        livro.ano_publicacao = request.form['ano_publicacao']
        livro.genero = request.form['genero']
        db.session.commit()
        flash('Livro atualizado com sucesso!')
        return redirect(url_for('index'))
    return render_template('editar.html', livro=livro)

@app.route('/deletar/<int:id>')
def deletar(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    flash('Livro deletado com sucesso!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)