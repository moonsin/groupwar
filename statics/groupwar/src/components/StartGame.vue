<template>
<div class="root">
  <h1 class="title">内战</h1>
  <div class="select-container" id="selectContainer">
    <button class="character active" id="akuma">
      <img class="character__img" src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/813538/akuma.png">
      <p class="character__name">Akuma</p>
    </button>
  <startgame-character  v-for="id in member" v-bind:key=id :character-id=id v-on:character-click="test" > </startgame-character>
  <startgame-character character-id="xinai" class="active"> </startgame-character>
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
    test:()=>{
      cosnole.log('111')
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
  font-family: bai;
  color: #dac751;
  font-size:40px;
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
  animation: flash 300ms linear;
  filter: grayscale(0.84);
	width: 100%;
}

.character__img, .character__name {
    margin: 0;
    padding: 0;
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

</style>
