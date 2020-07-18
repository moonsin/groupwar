<template>
<div class="root">
  <h1 class="title">Player Select</h1>
  <div class="select-container" id="selectContainer" v-if="show_all">
    <startgame-character  
      v-for="id in member" 
      v-bind:key=id 
      :character-id=id 
      :character-id-ch=name_dict[id] 
      v-on:character-click="characterClick" 
      :current-list=current_list> 
    </startgame-character>
   </div>

   <div class="show-team" >
    <startgame-character  
      v-for="id in team1" 
      v-bind:key=id 
      :character-id=id 
      :character-id-ch=name_dict[id] 
      :current-list=current_list> 
    </startgame-character>
   </div  >
   <h1 class="title" v-if="!show_all"> VS </h1>
    <div class="show-team">
    <startgame-character  
      v-for="id in team2" 
      v-bind:key=id 
      :character-id=id 
      :character-id-ch=name_dict[id] 
      :current-list=current_list> 
    </startgame-character>
   </div>

   <!-- <h1 id="result" class='title'>{{result_content}}</h1> -->
   <span class='start-btn' @click="startGame">START</span>
   <span class='reset-btn' @click="resetGame">RESET</span>

</div>
</template>

<script>
import startgameCharacter from './Character.vue'
import axios from 'axios'

export default {
  name: 'StartGame',
  components:{startgameCharacter},
  data:function(){
      return{
          member:["dailiange","xinai","abi","apan","caizige","dige","haizige","heimao","shuaiyang","xiaomi","xueda","dailianerge","yue","laowang","ruijie","gunge"],
          current_list:[],
          name_dict:{
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
          },
          result_content:"",    
          team1:[],
          team2:[],
          show_all:true,
          url:'http://104.160.45.150:9527'
      }
  },

  mounted (){
    this.getCurrentList() 
    this.getShowAll() 
  },

  methods:{

    getCurrentList: function(){
      let axiosUrl =this.url + "/get_current_list"
      let self=this
      axios.get(axiosUrl)
        .then(function(response){
          setTimeout(() =>{
            self.getCurrentList() 
          },50)
          self.current_list = response.data.split(',')
        })
      .catch(function(error){
          console.log(error);
        })
    },

    getShowAll:function(){
       let axiosUrl = this.url + "/get_show_all"
      let self=this
      axios.get(axiosUrl)
        .then(function(response){
          setTimeout(() =>{
            self.getShowAll() 
          },50)
          let result = eval(response.data)
          self.show_all = result[0]=="true"
          self.team1 = self.getIdList(result[1])
          self.team2 = self.getIdList(result[2])
        })
      .catch(function(error){
          console.log(error);
        })
    },

    initTest:function(){
      this.current_list.push('yue')
    },

    characterClick:function(data){
      let id=data['id']
      var index = this.current_list.indexOf(id)
      index == -1 ? this.current_list.push(id):this.current_list.splice(index,1);
      let axiosUrl = this.url + "/update_current_list"
      axios.post(axiosUrl,{
          id:id,
          active:data['isActive']
      })
      .then(function(response){
        console.log(response);
      })
        .catch(function(error){
          console.log(error);
        })
 
      console.log(this.current_list)
    },

    startGame:function(){
      self = this
      axios.get(this.url + '/start_game',{
      })
      .then(function(response){
        self.result_content = response.data
        console.log(self.result_content)
        let re = eval(self.result_content)
        self.team1 = self.getIdList(re[0])
        self.team2 = self.getIdList(re[1])
        self.show_all = false
        let axiosUrl = this.url + "/update_show_all"
        axios.post(axiosUrl,{
            show_all:"false",
        })
        .then(function(response){
          console.log(response);
        })
          .catch(function(error){
            console.log(error);
        })
   
      })
      .catch(function(error){
        console.log(error);
      })
    },

    resetGame:function(){
      let axiosUrl = this.url + "/reset_game"
      let self=this
      axios.get(axiosUrl)
        .then(function(response){})
      .catch(function(error){
          console.log(error);
        })
    
    },

    getIdList:function(nameList){
      var idList = []
       
      nameList.forEach(v=>{
        for(var key in this.name_dict){
          if(this.name_dict[key] == v){
            idList.push(key) 
            break;
          } 
        } 
      })
      return idList
    }

  },

}
</script>


<style>
body{
  height: 100%;
  background-image: url("");
  background-color: #0d0d3a;
}

.title {
    text-align: center;
    text-transform: uppercase;
    color: #dac751;
    letter-spacing: 0.1em;
    text-shadow: 0px 2px 2px rgba(255, 255, 255, 0.6);
}

.select-container {
  margin: 0 auto;
	display: grid;
	grid-template-columns: repeat(8, 100px);
	grid-column-gap: 8px;
	grid-row-gap: 8px;
  /*margin: 1em auto 3em;*/
	background: rgba(255, 255, 255, 0.5);
	padding: 4px 4px;
  width:856px;
}

.character {
	width: 100px;
	background: rgba(255, 255, 255, 0.5);
	cursor: pointer;
	position: relative;
	text-align: center;
	padding: 0;
	border: 0;
	margin: 0;
	display: inline-flex;
}

.character__img {
  filter: grayscale(0.84);
	width: 100%;
}

.character__img, .character__name {
    margin: 0;
    padding: 0;
}

.active {
		transform: scale(1.05);
		box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.2);
		z-index: 100;
}

.character__name {
    position: absolute;
    width: 100%;
    bottom: 0;
    display: none;
}

.character.active .character__name{
    display: block;
    width: 100%;
    background: #e3231e;
    color: white;
    opacity: 0.7;
    margin-top: 0.8em;
    font-size: 0.7em;
    text-transform: uppercase;
    font-weight: 700;
    padding: 0.3em 0;
}

.character.active .character__img{
  -webkit-filter: grayscale(0);
    filter: grayscale(0);
    outline: 4px solid white;
    -webkit-animation: flash 300ms linear;
    animation: flash 300ms linear;
}

@keyframes flash {
	0% {
		filter: brightness(100%);
	}
	20% {
		filter: brightness(150%);
	}
	40% {
		filter: brightness(100%);
	}
	60% {
		filter: brightness(150%);
	}
	80% {
		filter: brightness(100%);
	}
	100% {
		filter: brightness(150%);
	}
}


.video-game-button {
	text-shadow: 1px 1px pink, -1px -1px maroon;

	line-height: 1.5em;
	text-align: center;
	display: inline-block;
	width: 1.5em;
	-webkit-border-radius: .75em;
	-moz-border-radius: .75em;
	-o-border-radius: .75em;
		border-radius: .75em;
	background-color: red;
	-webkit-box-shadow:  0 .2em maroon;
	-moz-box-shadow:  0 .2em maroon;
	-o-box-shadow:  0 .2em maroon;
	box-shadow:  0 .2em maroon;
	color: red;
	margin: 5px;
	background-color: red;
	background-image: -o-linear-gradient(left top, pink 3%, red 22%, maroon 99%);
	background-image: -moz-linear-gradient(left top, pink 3%, red 22%, maroon 99%);
	background-image: -webkit-linear-gradient(left top, pink 3%, red 22%, maroon 99%);
	background-image: linear-gradient(left top, pink 3%, red 22%, maroon 99%);
	cursor: pointer;
  padding-left: 5px;
}

.start-btn{
  font-size:40px;
  text-align: center;
	display: inline-block;
	margin:330px auto;
    font-weight: bold;
    padding: 10px ;
    background-color: lightgray;
    text-shadow: -1px -1px black, 1px 1px white;
    color: gray;
    -webkit-border-radius: 7px;
	-moz-border-radius: 7px;
	-o-border-radius: 7px;
	border-radius: 7px;
    box-shadow: 0 .2em gray; 
    cursor: pointer;
}

.reset-btn{
  font-size:40px;
  text-align: center;
	display: inline-block;
	margin:330px 30px;
    font-weight: bold;
    padding: 10px ;
    background-color: lightgray;
    text-shadow: -1px -1px black, 1px 1px white;
    color: gray;
    -webkit-border-radius: 7px;
	-moz-border-radius: 7px;
	-o-border-radius: 7px;
	border-radius: 7px;
    box-shadow: 0 .2em gray; 
    cursor: pointer;
}

.video-game-button:active, .start-btn:active {
	box-shadow: none;
	position: relative;
	top: .2em;
}

.show-team{
  margin-top:30px;
}
</style>
