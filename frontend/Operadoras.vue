<template>
  <div>
    <h2>Operadoras</h2>

    <input v-model="search" placeholder="Buscar por razão social ou CNPJ" />

    <table>
      <tr v-for="op in operadoras" :key="op.cnpj">
        <td>
          <router-link :to="`/operadora/${op.cnpj}`">
            {{ op.razao_social }}
          </router-link>
        </td>
        <td>{{ op.cnpj }}</td>
        <td>{{ op.uf }}</td>
      </tr>
    </table>

    <button @click="prev" :disabled="page === 1">Anterior</button>
    <button @click="next">Próximo</button>

    <GraficoUF />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import api from '../api/api'
import GraficoUF from '../components/GraficoUF.vue'

const operadoras = ref([])
const page = ref(1)
const limit = 5
const search = ref('')

const load = async () => {
  const res = await api.get('/operadoras', {
    params: { page: page.value, limit }
  })
  operadoras.value = res.data.data
}

watch(page, load)
onMounted(load)

const next = () => page.value++
const prev = () => page.value--
</script>
