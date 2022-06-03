<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/banks">Agencies</NuxtLink></li>
      <li class="is-active"><a href="#" aria-current="page">New Agency</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <FormAgency title="New Agency" :initial-data="initialData"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Agency from '~~/types/agency';



definePageMeta({
  layout: 'custom'
})

const initialData:Agency = {
  id: -1,
  agency_code: '',
  bank: '',
  name: ''
}
 
</script>