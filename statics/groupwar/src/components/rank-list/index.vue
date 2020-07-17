<template>
    <div>
      <div class="title">
        <span>带 恶 人 排 行 榜</span>
      </div>
      <div class="table">
        <table>
          <thead>
            <tr>
              <th width="65">
                <span>排名</span>
              </th>
              <th width="300">
                <span>姓名</span>
              </th>
              <th width="65">
                <span>分数</span>
              </th>
            </tr>
          </thead>
          <tbody>
            <template v-if="diaoMaoList && diaoMaoList.length > 0">
              <tr v-for="diaomao in diaoMaoList">
                <td>
                  <span>{{ diaomao.rank }}</span>
                </td>
                <td>
                  <div class="avatar">
                    <img :src="`/static/avatar/${diaomao.id}.jpg`">
                  </div>
                  <div style="float:left;">
                    <span>{{ diaomao.name }}</span> 
                  </div>
                </td>
                <td>
                  <span>{{ diaomao.score }}</span>
                </td>
              </tr>
            </template>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>

<script>
export default {
  name: 'rankList',
  data() {
    return {
      diaoMaoList: []
    }
  },
  computed: {},
  watch: {},
  created() { 
    this.init()
  },
  mounted() { },
  methods: {
    init() {
      this.initDiaoMaoList()
    },
    initDiaoMaoList() {
      let res = [
        { rank: 1, id: 'dailiange', name: '一枪人', score: '110' },
        { rank: 2, id: 'yue', name: '小月人', score: '100' },
        { rank: 3, id: 'laowang',name: '老王人', score: '99' },
        { rank: 3, id: 'ruijie',name: '小瑞人', score: '98' },
      ]
      this.diaoMaoList = res
    },
  },
}
</script>

<style rel="stylesheet/scss" type="text/scss" scoped>
span {
  -webkit-user-select: none; /* for Chrome */
  -moz-user-select: none; /* for Firefox */
}
img {
  -webkit-user-select: none; /* for Chrome */
  -moz-user-select: none; /* for Firefox */
}
.title {
  text-align: center;
  text-transform: uppercase;
  color: #dac751;
  letter-spacing: 0.1em;
  text-shadow: 0px 2px 2px rgba(255, 255, 255, 0.6);
  font-family: bai;
  font-size: 50px;
  margin-bottom: 20px;
}
.table {
  width: 450px;
  margin: 0 auto;
  font-family: bai;
  font-weight: lighter;
}
.table th {
  color: white;
  font-size: 30px;
  font-weight:300;
  margin-right: 30px;
}
.table td {
  color: white;
  font-size: 26px;
}
.avatar {
  display: inline-block;
  float: left;
  margin-left: 90px;
  margin-right: 10px;
  text-align: center;
}
.avatar img{
  border:0px solid;
  border-radius: 50%;
  overflow: hidden;
  width: 30px;
  height: 30px;
}
</style>