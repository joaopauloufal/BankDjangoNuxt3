<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/clients">Clients</NuxtLink></li>
      <li class="is-active"><a href="#" aria-current="page">New Client</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <FormClient title="New Client" :initial-data="initialData"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Client from '~~/types/client';



definePageMeta({
  layout: 'custom'
})

const initialData:Client = {
  id: -1,
  cpf_cnpj: '',
  name: ''
}
 
</script>