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
              <th width="280">
                <span>姓名</span>
              </th>
              <th width="65">
                <span>局数</span>
              </th>
              <th width="100">
                <span>胜率</span>
              </th>
              <th width="100">
                <span>总得分</span>
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
                  <span>{{ diaomao.games }}</span>
                </td>
                <td>
                  <span>{{ diaomao.rate }}</span>
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
import axios from 'axios'
export default {
  name: 'rankList',
  data() {
    return {
      diaoMaoList: [],
      url:'http://104.160.45.150:9527',
      name_dict:{
          "代练哥":"dailiange",
          "西奈":"xinai",
          "阿比":"abi",
          "阿攀":"apan",
          "菜子哥":"caizige",
          "弟哥":"dige",
          "孩子哥":"haizige",
          "黑猫":"heimao",
          "帅扬":"shuaiyang",
          "小米":"xiaomi",
          "雪大":"xueda",
          "代练二哥":"dailianerge",
          "月":"yue",
          "老王":"laowang",
          "瑞姐":"ruijie",
          "棍哥":"gunge"
        },
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
      let result = {}
      let axiosUrl = this.url + "/show_list"
      let self = this
      axios.get(axiosUrl)
        .then(function(response){
          result = response.data
          var has_score = result['has_score']
          self.handle_data_list(has_score)
        })
      .catch(function(error){
          console.log(error);
        })
    },
    handle_data_list: function(result){
      for(var key in result){
        var item = result[key]
        result[key]['score'] = item['rate'] / (parseFloat(item['game']) + 1)  * 100
      }
      var sdic=Object.keys(result).sort(function(a,b){return result[b]['score']-result[a]['score']});
      console.log(sdic)
      let res= []
      let rank = 0
      let score = 10000
      for(var key in sdic){
        if(score > result[sdic[key]]['score']){
          score =  result[sdic[key]]['score']
          rank += 1
        } 

        res.push({
          rank:rank,
          id:this.name_dict[sdic[key]],
          name:sdic[key],
          score:score,
          games:result[sdic[key]]['game'],
          rate:result[sdic[key]]['rate']
        })
      }
      this.diaoMaoList = res
    }
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
  width: 650px;
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
