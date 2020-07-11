from flask import Flask,request
from scripts import Ranker
import json
import logging
from flask_cors import *
from flask_socketio import SocketIO, emit

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='./log',  
                    filemode='w')  

app = Flask(__name__)
CORS(app, supports_credentials=True)

ranker = Ranker.Ranker()
current_list = ["yue","dailiange"]
socketio = SocketIO(app)

name_dict ={
"dailiange":"代练哥",
"xinai":"西奈",
"abi":"阿比",
"apan":"阿攀",
"caizige":"菜子哥",
"dige":"弟哥",
"haizige":"孩子哥",
"heimao":"黑猫",
"shuaiyang":"帅扬",
"xiaomi":"小米",
"xueda":"雪大",
"dailianerge":"代练二哥",
"yue":"月",
"laowang":"老王",
"ruijie":"瑞姐",
"gunge":"棍哥"
}

def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data

'''
@app.route("/start_game",methods=['post','get'])
def start_game():
    data = request_parse(request)
    players = data['players']
    print(players)
    must_together = request.args.get('must_together')
    if not must_together:
        must_together = '[]'
    logging.info("start_game?players=%s&must_together=%s" % (players,must_together))
    return str(ranker.start_game(players.split(','),eval(must_together)))
'''
@app.route("/start_game",methods=['post','get'])
def start_game():
    logging.info("start_game?players=%s&must_together=%s" % (",".join(current_list),"[]"))
    player_list = [name_dict[item] for item in current_list]
    return str(ranker.start_game(player_list,[]))

@app.route("/show_list")
def show_list():
    return str(ranker.show_list())

@app.route("/update")
def update():
    winners = request.args.get('winners')
    losers = request.args.get('losers')
    logging.info("update?winners=%s&losers=%s" % (winners,losers))
    return ranker.update(winners.split(','),losers.split(','))

@app.route("/get_current_list")
def get_current_list():
    return ",".join(current_list)

@app.route("/update_current_list",methods=['post','get'])
def update_current_list():
    data = request_parse(request)
    print(data)
    new_id = data['id']
    active = data['active']
    if active and new_id not in current_list:
        current_list.append(new_id)
    elif not active and new_id in current_list:
        current_list.remove(new_id)
    return "success"

#@socketio.on('update_current_list', namespace='/current_list')
#def update_current_list(message):
#    emit('update_current_list', {'data': current_list})

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port=9527)
