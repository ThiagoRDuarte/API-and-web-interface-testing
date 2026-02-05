<template>
  <div>
    <h2>{{ operadora?.razao_social }}</h2>

    <ul>
      <li v-for="d in despesas" :key="d.id">
        R$ {{ d.valor_despesas }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/api'
import { useRoute } from 'vue-router'

const route = useRoute()
const operadora = ref(null)
const despesas = ref([])

onMounted(async () => {
  const cnpj = route.params.cnpj
  operadora.value = (await api.get(`/operadoras/${cnpj}`)).data
  despesas.value = (await api.get(`/operadoras/${cnpj}/despesas`)).data
})
</script>
