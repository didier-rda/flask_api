from flask import Flask

app = Flask(__name__)

@app.route('/compras')
def compras():
    dict_ = {"arroz":"12","presunto":"14"}    
    return dict_
