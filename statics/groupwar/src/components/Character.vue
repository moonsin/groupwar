<template>
    <button class="character" :class="{'active':isActive}" :id=characterId @click="characterClick">
      <img class="character__img" :src=src>
      <p class="character__name">{{characterIdCh}}</p>
    </button>
</template>

<script>
export default {
  name: 'startgame-character',
  props:["characterId", "characterIdCh"],
  data:function(){
      return{
          src:"/static/avatar/" + this.characterId + ".jpg",
          isActive:false
      }
  },
  methods:{
    characterClick:function(e){
      this.isActive = !this.isActive 
      this.$emit('character-click',this.characterId)
    }
  } 
  
}
</script>

