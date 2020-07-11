<template>
<div class="root">
  <h1 class="title">Player Select</h1>
  <div class="select-container" id="selectContainer">
  <startgame-character  v-for="id in member" v-bind:key=id :character-id=id v-on:character-click="characterClick" > </startgame-character>
   </div>
</div>
</template>

<script>
import startgameCharacter from './Character.vue'
export default {
  name: 'StartGame',
  components:{startgameCharacter},
  data:function(){
      return{
          member:["dailiange","xinai","abi","apan","caizige","dige","haizige","heimao","shuaiyang","xiaomi"],
          current_list:[]
      }
  },
  methods:{
    characterClick:function(id){
      console.log(this.current_list)
      var index = this.current_list.indexOf(id)
      index == -1 ? this.current_list.push(id):this.current_list.splice(index,1);
      console.log(this.current_list)
    }
  }

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



</style>
