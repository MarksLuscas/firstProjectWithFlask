from html.entities import html5
from flask import Flask, render_template, request #, redirect
from vsearch import buscarLetras

app = Flask(__name__)

# def hello() -> '302':
#     return redirect('/entry') redireciona para a url /entry -> nao vamos mais redirecionar e sim usar duas urls diferentes para a mesma função

@app.route('/buscaLetras', methods=['POST'])
def do_search() -> 'html5':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results'
    results = str(buscarLetras(phrase,letters))

    return render_template('results.html', 
                              the_phrase = phrase, 
                              the_letters = letters,
                              the_title = title,
                              the_results = results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html5':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

if(__name__ == '__main__'):
 app.run(debug=True) #reinicia o codigo automaticamente apos fazer uma alteração no mesmo