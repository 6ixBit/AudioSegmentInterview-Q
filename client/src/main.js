import Vue from 'vue'
import App from './App.vue'
import VueApexCharts from 'vue-apexcharts'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.component('apexchart', VueApexCharts)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
