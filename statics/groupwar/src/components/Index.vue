<template>
    <div class="root">
        <div class="index_options">
          <template v-if="menuList && menuList.length > 0">
            <div v-for="menu in menuList">
              <span @click="jump(menu.routerParams)">{{menu.name}}</span>
            </div>
          </template>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      menuList: []
    }
  },
  created() {
    this.init()
  },
  methods:{
    jump(params) {
      if(params && params.name) {
        this.$router.push(params)
      }
    },
    init() {
      this.initMenuList()
    },
    initMenuList() {
      let res = [
        { name: '开始游戏', routerParams: { name: 'StartGame'} },
        { name: '群友排名', routerParams: { name: 'RankList'} },
        { name: '更新分数', routerParams: { name: 'Index'} },
        { name: '人员名单', routerParams: { name: 'Index'} },
      ]
      this.menuList = res
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

.index_options span{
  display: block;
  font-size: 40px;
  cursor: pointer;
}
</style>

