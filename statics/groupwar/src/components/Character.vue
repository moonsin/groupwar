<template>
    <button class="character" :id=characterId @click="$emit('character-click')">
      <img class="character__img" :src=src>
      <p class="character__name">{{characterId}}</p>
    </button>
</template>

<script>
export default {
  name: 'startgame-character',
  props:["characterId"],
  data:function(){
      return{
          src:"/static/avatar/" + this.characterId + ".jpg"
      }
  },
}
</script>

