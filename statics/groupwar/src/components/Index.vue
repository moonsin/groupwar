<template>
    <div class="root">
        <!--<img class="index_logo" src="../assets/logo2.jpeg"> --> 
        <div class="index_options">
          <h1 @click="startgame" class="opntion"> 开始游戏 </h1>
          <h1> 群友排名 </h1>
          <h1> 更新分数 </h1>
          <h1> 人员名单 </h1>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Index',
  methods:{
    startgame(){
      this.$router.push({path:'/startgame'})
    }
  }
}
</script>

<style>

.root {
  font-family: bai;
}

.index_logo{
  width: 300px;
}

.index_options{
  margin-top:240px;
  color:white;
}

.index_options h1{
  font-size: 40px;
}

.opntion{
  cursor: pointer;
}
</style>

