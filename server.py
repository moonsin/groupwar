from flask import Flask,request
from scripts import Ranker
import json
import logging


logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='./log',  
                    filemode='w')  

app = Flask(__name__)

ranker = Ranker.Ranker()

@app.route("/start_game",methods=['post','get'])
def start_game():
    players = request.args.get('players')
    must_together = request.args.get('must_together')
    logging.info("start_game?players=%s&must_together=%s" % (players,must_together))
    return str(ranker.start_game(players.split(','),eval(must_together)))

@app.route("/show_list")
def show_list():
    return str(ranker.show_list())

@app.route("/update")
def update():
    winners = request.args.get('winners')
    losers = request.args.get('losers')
    logging.info("update?winners=%s&losers=%s" % (winners,losers))
    return ranker.update(winners.split(','),losers.split(','))


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=9527)
