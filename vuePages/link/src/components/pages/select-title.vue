<template>
<div>
  <h1>请选择要筛选的表和条件：</h1>
  <p>注：生成的表的表头会按照选择【表头】的先后顺序排列</p>
  <div v-for="(item,index) in chooseTableValue" :key="item.id">
    <choose-table :options="options"
                  @tableValue="changeValue"
                  :id = item.id
                  @selfRemove="removeLine"
                  style="margin: 8px"
    ></choose-table>
  </div>
  <el-divider></el-divider>
  <el-button style="margin: 4px" @click="addChooseTable">添加新过滤器</el-button>
  <el-button style="margin: 4px" @click="PostSelection" type="success">发送请求并下载</el-button>
<!--  <el-button @click="showTable"></el-button>-->
</div>
</template>

<script>

import ChooseTable from '../basic/chose-table'
import { Base64 } from 'js-base64'
export default {
  name : "select-title",
  data(){
    return{
      chooseTableNumber : 0,
      chooseTableValue : [],
      options:[{
        value:'jxlb',
        label:'教学楼表'
      }]
    }
  },
  components:{
    ChooseTable

  },
  methods: {
    addChooseTable(){
      this.chooseTableValue.push({values:{},id: this.chooseTableNumber})
      this.chooseTableNumber ++
      console.log(this.chooseTableValue)
    },
    changeValue(res){
      for (let i = 0 ; i < this.chooseTableValue.length ; i++){
        if(this.chooseTableValue[i].id == res.id){
          this.chooseTableValue[i].values = res.value
          return
        }
      }
    },
    showTable(){
      console.log(this.chooseTableValue)
    },
    removeLine(id){
      for (let i = 0 ; i < this.chooseTableValue.length ; i++){
        if (this.chooseTableValue[i].id == id){
          this.chooseTableValue.splice(i,1)
          return
        }
      }
    },
    PostSelection(){
      let Base64 = require('js-base64').Base64
      console.log(this.chooseTableValue)
      this.$http({
        method: 'post',
        url: '/getExcel',
        data: this.chooseTableValue,
        responseType: 'blob',//服务器返回的数据类型
      }).then(
        res=> {
          let data = res.data
          let reader = new FileReader()
          let blob = new Blob([data])
          let url = window.URL.createObjectURL(blob);
          const a = document.createElement('a')
          a.style.display = 'none'
          a.download = '导出数据表_' + new Date().toLocaleDateString() +'__' + new Date().toLocaleTimeString()+'.xlsx'
          a.href  = url
          a.click()
        }
      )
    }
  },
  created () {
    this.$http("/fetchAllTableNames").then((res)=>{
      this.options = res.data
    })
  }
}
</script>

<style>

</style>
