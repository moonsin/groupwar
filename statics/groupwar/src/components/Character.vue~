<template>
    <button class="character" :class="{'active':isActiveCharacter}" :id=characterId @click="characterClick">
      <img class="character__img" :src=src>
      <p class="character__name">{{characterIdCh}}</p>
    </button>
</template>

<script>
export default {
  name: 'startgame-character',
  props:["characterId", "characterIdCh","currentList"],
  data:function(){
      return{
          src:"/static/avatar/" + this.characterId + ".jpg",
      }
  },
  computed:{
      isActiveCharacter:function(){
        return this.currentList.indexOf(this.characterId) != -1 
      } 
  },
  methods:{
    characterClick:function(e){
      this.$emit('character-click',{"id":this.characterId,"isActive":!this.isActiveCharacter})
    }
  } 
  
}
</script>

