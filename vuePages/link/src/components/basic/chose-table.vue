<template>
<div>
  <el-cascader
    style="margin: 4px;width:30%"
    placeholder="输入表名快速筛选：如“教学楼表”"
    :options = options
    v-model="value"
    filterable></el-cascader>
  <el-select style="width: 30%" v-if="haveTable" v-model="titleValue" multiple placeholder="请选择">
    <el-option
      v-for="item in currentTableOptions"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  <el-button type="primary">添加时间限定</el-button>
  <el-button @click="selfRemove" type="danger">移除条件</el-button>
</div>
</template>

<script>
export default {
  name:"chooseTable",
  props:['options','id'],
  data(){
    return {
      value :"",
      identify: this.id,
      currentTableOptions : {},
      titleValue:[],
      haveTable : false
      // options:[{
      //   value:'jxlb',
      //   label:'教学楼表'
      // }]
    }
  },
  watch:{
    value : function (val){
      this.$emit('tableValue', {'id':this.identify,'value': val})
      this.$http.get('/getTitles', {
        params:{
          tablename:this.value[0]
        }
      } ).then((res)=>{
        this.currentTableOptions = res.data
        console.log(this.currentTableOptions)
        this.haveTable = true
        this.titleValue = []
      }).catch((err) => {
          console.log(err)
      })
    }
  },
  methods:{
    selfRemove(){
      this.$emit('selfRemove', this.id)
    }
  }
}
</script>

<style></style>
