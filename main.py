from flask import Flask, json, request
import random

app = Flask(__name__)

quotes = [
    "Цель не должна быть просто отдыхом, но и возвышением жизни",
    "Любой человек может забрать у вас деньги, но только вы сами можете отнять у себя время",
    "Делайте то, что вы должны делать, и пусть мир делает свое дело",
    "Большинство людей проводят большую часть времени, но не делают ничего",
    "Только тот, кто двигается, может упасть",
    "Удача - это результат твердой работы",
    "Успех - это не ключ к счастью, счастье - это ключ к успеху",
    "Не стоит ждать, что кто-то другой сделает что-то для вас",
    "Поставьте свою цель так высоко, чтобы даже если вы упадете, вы все равно окажетесь на вершине горы",
]

@app.route('/quote', methods=['GET'])
def get_quote():
    random_quote = random.choice(quotes)
    response = {'quote': random_quote}
    return app.response_class(response=json.dumps(response, ensure_ascii=False), status=200, mimetype='application/json')

@app.route('/add_quote', methods=['POST'])
def add_quote():
    new_quote = request.json['quote']
    quotes.append(new_quote)
    response = {'message': 'Цитата успешно добавлена'}
    return app.response_class(response=json.dumps(response, ensure_ascii=False), status=201, mimetype='application/json')

@app.route('/delete_quote', methods=['DELETE'])
def delete_quote():
    quote_to_delete = request.json['quote']
    if quote_to_delete in quotes:
        quotes.remove(quote_to_delete)
        response = {'message': 'Цитата успешно удалена'}
        return app.response_class(response=json.dumps(response, ensure_ascii=False), status=200, mimetype='application/json')
    else:
        response = {'message': 'Цитата не найдена'}
        return app.response_class(response=json.dumps(response, ensure_ascii=False), status=404, mimetype='application/json')

if __name__ == '__main__':
    app.run()
