from app import app

#==========Criando rotas simples=============================================
@app.route("/")
def index():
    return 'Pagina Inicial'

#=========Criando rotas com mais de uma URL e passando paramentros na URL=====
@app.route("/test/", defaults={'name': None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    return 'Olá Usuario'

#=============Mudando tipo do dado recebido================

@app.route('/post/<int:post_id>')
def show_post(post_id):
    print(type(post_id))
    return f'Post {post_id}'