// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import router from './router'

import axios from 'axios'
import VueAxios from 'vue-axios'

// fade/zoom 等
import 'element-ui/lib/theme-chalk/base.css';

axios.defaults.baseURL = 'http://127.0.0.1:5000'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
Vue.use(VueAxios, axios)

// Vue.component(CollapseTransition.name, CollapseTransition)

Vue.use(ElementUI)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
