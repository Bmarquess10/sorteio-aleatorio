from flask import Flask, render_template, request, jsonify # type: ignore
import random

app = Flask(__name__)

def sorteio_aleatorio(total_numeros, numeros_sorteados):
    if numeros_sorteados > total_numeros:
        raise ValueError("O número de sorteios não pode ser maior que o número total de números.")
    return random.sample(range(1, total_numeros + 1), numeros_sorteados)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sortear', methods=['POST'])
def sortear():
    try:
        total_numeros = int(request.form['total_numeros'])
        numeros_sorteados = int(request.form['numeros_sorteados'])
        resultado = sorteio_aleatorio(total_numeros, numeros_sorteados)
        return jsonify({'resultado': resultado})
    except ValueError as e:
        return jsonify({'erro': str(e)})
    except Exception as e:
        print(e)
        return jsonify({'erro': 'Por favor, insira valores válidos.'})

if __name__ == '__main__':
    app.run(debug=True)
