import copy

class Ranker:
    player_dict = {}
    best_track = []
    best_rate_diff_abs = 10000
    
    def __init__(self):
        self.reload_player()


    def reload_player(self):
        self.player_dict = {}
        with open('./data/data.txt','r') as f:
            line = f.readline()
            while line:
                ll = line.strip().split('\t')
                self.player_dict[ll[0]] = {
                        "game_num": ll[1],
                        "win_rate": ll[2]
                    }
                line = f.readline()

    
    #传入的玩家列表可以少于10人，默认有10-n个路人玩家，胜率默认50%
    #可以传入必须在一起的人
    def start_game(self,player_list, must_together_list=[]):
        self.best_track = []
        self.best_rate_diff_abs = 10000

        one_side_min_size = len(player_list) - 5 if len(player_list) >= 5 else 0
        track = [player_list[0]]
        self.backtrack(player_list, track,one_side_min_size, must_together_list) 
        return self.best_track, self.get_second_side(player_list,self.best_track),self.best_rate_diff_abs

    def backtrack(self,player_list, track,one_side_min_size,must_together_list):
        if len(track) > 5 :
            return 
        print(track)
        if len(track) >= one_side_min_size and self.cal_legal(player_list, track,must_together_list):
            rate_a = self.calcul_one_side_win_rate(track)
            rate_b = self.calcul_one_side_win_rate(self.get_second_side(player_list,track))
            rate_diff = abs(rate_a - rate_b)
            if rate_diff < self.best_rate_diff_abs:
                self.best_rate_diff_abs = rate_diff
                self.best_track = copy.deepcopy(track)

        for i in range(len(player_list)):
            if player_list[i] in track:
                continue;
            
            track.append(player_list[i])
            self.backtrack(player_list, track,one_side_min_size,must_together_list)
            track.pop()

    def cal_legal(self,player_list, track,must_together_list):
        for item in must_together_list:
            if len(set(item) - set(track)) != 0 and len(set(item) - set(self.get_second_side(player_list,track)))!=0:
                return False
        return True

    def get_second_side(self,player_list, track):
        return list(set(player_list) - set(track))


    def calcul_one_side_win_rate(self,player_list):
        total_rate = 0
        for i in range(5):
            total_rate +=  float(self.player_dict[player_list[i]]["win_rate"]) if i<= len(player_list)-1 else 0.5
        return total_rate/5

    def update(self,win_list,lose_list):
        with open("./data/data.txt",'r') as f:
            lines = f.readlines()
        with open("./data/data.txt",'w') as f:
            for line in lines:
                ll = line.strip().split('\t')
                if ll[0] in win_list:
                    games = int(ll[1]) + 1
                    rate = (int(ll[1]) * float(ll[2]) + 1 ) / games
                    f.write("%s\t%s\t%s\n" % (ll[0],games,rate))
                elif ll[0] in lose_list:
                    games = int(ll[1]) + 1
                    rate = (int(ll[1]) * float(ll[2])) / games
                    f.write("%s\t%s\t%s\n" % (ll[0],games,rate))
                else:
                    f.write(line)
        return "sucess"

    def show_list(self):
        player_map = {
                "has_score":{},
                "no_score":{},
                "intro":"目前没有做排名"
                }
        
        with open("./data/data.txt",'r') as f:
            line = f.readline()
            while line:
                ll = line.strip().split('\t')
                if int(ll[1]) != 0:
                    player_map["has_score"][ll[0]] = {
                            "game":ll[1], 
                            "rate":ll[2]
                            }
                else:
                    player_map["no_score"][ll[0]] = {
                            "game":ll[1], 
                            "rate":0.5,
                            }
                line = f.readline()
        return player_map

if __name__ == "__main__":
    ranker = Ranker()
    print(ranker.start_game(["西奈","瑞姐","代练哥","月"],[["瑞姐","代练哥"]]))
    ranker.update(["月"],["西奈"])
    print(ranker.show_list())


    

