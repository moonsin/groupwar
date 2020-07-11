<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@font-face
{
font-family: bai;
src:url('./assets/HYShangWeiShouShuW.ttf');
}

body{
  height: 100%;
  background-image: url("http://pickorban.johnr.io/wp-content/themes/lolchampdb/img/primary-bg.jpg");
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
