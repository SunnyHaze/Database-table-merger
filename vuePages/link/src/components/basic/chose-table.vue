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
  <el-button @click="switchTime" type="primary">{{timeButtonStr}}</el-button>
  <el-button @click="selfRemove" type="danger">移除条件</el-button>
  <br>
  <el-date-picker v-if="selectTimeActivate"
    v-model="timeValue"
    type="daterange"
    range-separator="至"
    start-placeholder="开始日期"
    end-placeholder="结束日期"
    value-format="yyyy-MM-dd">
  </el-date-picker>
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
      selectTimeActivate: false,
      currentTableOptions : {},
      titleValue:[],
      haveTable : false,
      timeValue :[],
      // 发送到父组件的信息
      dataToParent:{
        targetTable:"",
        targetTitle:[],
        selectTimeActivate : false,
        targetTimeRange :[]
      }
    }
  },
  watch:{
    deep : true,
    value : function (val){
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
      this.dataToParent.targetTable = val[0]
      this.$emit('tableValue', { 'id': this.identify, 'value': this.dataToParent})
    },
    titleValue (val){
      this.dataToParent.targetTitle = val
      this.$emit('tableValue', { 'id': this.identify, 'value': this.dataToParent})
    },
    selectTimeActivate(val){
      this.dataToParent.selectTimeActivate = val
      this.$emit('tableValue', { 'id': this.identify, 'value': this.dataToParent})
    },
    timeValue(val){
      this.dataToParent.targetTimeRange = val
      this.$emit('tableValue', { 'id': this.identify, 'value': this.dataToParent})
    },
  },
  methods:{
    selfRemove(){
      this.$emit('selfRemove', this.id)
    },
    switchTime(){
      this.selectTimeActivate = !this.selectTimeActivate
    }
  },
  computed:{
    timeButtonStr (){
      if (this.selectTimeActivate){
        return '关闭时间筛选'
      }else{
        return '开启时间筛选'
      }
    },

  }
}
</script>

<style></style>
