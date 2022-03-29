import Vue from 'vue'
import Router from 'vue-router'
import home from "../components/home";
import select_title from '../components/pages/select-title'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      children:[
        {
          path:'select',
          name:'select-title',
          component : select_title
        }
      ]
    },

  ]
})
