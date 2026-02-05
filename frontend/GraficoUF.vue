<template>
  <canvas ref="canvas"></canvas>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import Chart from 'chart.js/auto'
import api from '../api/api'

const canvas = ref(null)

onMounted(async () => {
  const res = await api.get('/estatisticas')

  new Chart(canvas.value, {
    type: 'bar',
    data: {
      labels: res.data.map(i => i.uf),
      datasets: [{
        data: res.data.map(i => i.total)
      }]
    }
  })
})
</script>
