from flask import Flask,request
from scripts import Ranker
import json

app = Flask(__name__)

ranker = Ranker.Ranker()

@app.route("/start_game",methods=['post','get'])
def start_game():
    players = request.args.get('players')
    must_together = request.args.get('must_together')
    print(players)
    print(must_together)
    return str(ranker.start_game(players.split(','),eval(must_together)))

@app.route("/show_list")
def show_list():
    return str(ranker.show_list())

@app.route("/update")
def update():
    winners = request.args.get('winners')
    losers = request.args.get('losers')
    print(ranker.update(winners.split(','),losers.split(',')))
    return ranker.update(winners.split(','),losers.split(','))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=9527)
