<template>
  <div style="height: 100%">
<el-container :style = "{height:'100%'}">
<el-container>
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-row class="tac">
          <el-col :span="24">
            <h1 style="text-align: center;">查找并合并数据表</h1>
            <el-menu
              default-active="4"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="#545c64"
              text-color="#fff"
              :router = true
              active-text-color="#ffd04b">
              <el-menu-item index="4" route="select">
                <i class="el-icon-setting"></i>
                <span slot="title">筛选数据表及条件</span>
              </el-menu-item>
            </el-menu>
          </el-col>
        </el-row>


      </el-aside>

<el-container>
  <el-header style="text-align: right; font-size: 12px">
<!--    <el-dropdown>-->
<!--      <i class="el-icon-setting" style="margin-right: 15px"></i>-->
<!--      <el-dropdown-menu slot="dropdown">-->
<!--        <el-dropdown-item>查看</el-dropdown-item>-->
<!--        <el-dropdown-item>新增</el-dropdown-item>-->
<!--        <el-dropdown-item>删除</el-dropdown-item>-->
<!--      </el-dropdown-menu>-->
<!--    </el-dropdown>-->
<!--    <span>王小虎</span>-->
  </el-header>

  <el-main :style="{height:[windowHeight]}">
    <router-view></router-view>
  </el-main>
</el-container>

</el-container >
  <el-footer height="5px"><covariant-footer></covariant-footer></el-footer>
</el-container>



</div>
</template>
<style>
.el-container,body,html,#app{
  height: 100%;
}
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>

<script>
import selectTitle from './pages/select-title'
import covariantFooter from './basic/Covfooter'
export default {
  name : "home",

  components : {
    selectTitle,
    covariantFooter
  },
  data() {
    const item = {
      date: '2016-05-02',
      name: '王小虎',
      address: '上海市普陀区金沙江路 1518 弄'
    };
    return {
      windowHeight : document.documentElement.clientHeight,
      tableData: Array(20).fill(item)
    }
  },
  created () {
    console.log(this.windowHeight)
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>
