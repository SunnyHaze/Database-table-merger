// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// ElementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// SideBar
Vue.config.productionTip = false
import axios from 'axios'
import qs from 'qs'
const baseURL = 'http://localhost:5000' //数据请求服务器统一地址
Vue.use(ElementUI);
axios.defaults.baseURL = baseURL

Vue.prototype.$http = axios
// Vue.prototype.$qs = qs
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
