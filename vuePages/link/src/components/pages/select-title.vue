<template>
<div>
  <h1>请选择要筛选的表和条件：</h1>
  <div v-for="(item,index) in chooseTableValue" :key="item.id">
    <choose-table :options="options"
                  @tableValue="changeValue"
                  :id = item.id
                  @selfRemove="removeLine"
    ></choose-table>
  </div>
  <el-button style="margin: 4px" @click="addChooseTable">添加新过滤器</el-button>
  <el-button @click="showTable"></el-button>
</div>
</template>

<script>

import ChooseTable from '../basic/chose-table'
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
      this.chooseTableValue.push({value:"",id: this.chooseTableNumber})
      this.chooseTableNumber ++
      console.log(this.chooseTableValue)
    },
    changeValue(res){
      for (let i = 0 ; i < this.chooseTableValue.length ; i++){
        if(this.chooseTableValue[i].id == res.id){
          this.chooseTableValue[i].value = res.value[0]
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
