from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('notas.html')

@app.route('/calculo', methods=['GET','POST'])
def calculo():
    dicionario = request.form.to_dict()#mostrando o valor do dicionario que foi levantado atraves do metodo request.form
    print(dicionario)

    valor = request.form.to_dict().values()#O método values() retorna um objeto de visualização. O objeto view contém os valores do dicionário, como uma lista.
    print(valor)

    total = sum(int(v) for v in request.form.to_dict().values())#codigo convertido para de 'str' para 'int' e somnado 'sum'
    print(total)
    resu = total / 2
    print(resu)
    

    return render_template('notas_calculo.html', resu=resu)

if __name__ == '__main__':
    app.run(debug=True)