import { createRouter, createWebHistory } from 'vue-router'
import Operadoras from '../views/Operadoras.vue'
import OperadoraDetalhe from '../views/OperadoraDetalhe.vue'

const routes = [
  { path: '/', component: Operadoras },
  { path: '/operadora/:cnpj', component: OperadoraDetalhe, props: true }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
