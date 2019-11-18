import Vue from 'vue'
import App from '@/App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
Vue.use(VueResource)
import store from '@/store'
import router from '@/router'

Vue.config.productionTip = false
Vue.config.devtools = true
// Vue.use(VueRouter)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
