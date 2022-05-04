<template>
  <div>
    {{banks}}
    <NuxtPage />
  </div>
</template>

<script lang="ts">

import { defineComponent } from 'vue'
import BanksApiRepository from '../../repositories/banks_api_repository'

export default defineComponent({

  data: () => ({
    banks: []
  }),

  created () {
    this.getData()
  },

  methods: {
    async getData():Promise<void> {
      this.banks = await useAsyncData('banks', () => BanksApiRepository.all())
    }
  }
})



</script>