<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/banks">Banks</NuxtLink></li>
      <li class="is-active"><a href="#">New Bank</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <FormBank title="New Bank" :initial-data="initialData"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Bank from '~~/types/bank';



definePageMeta({
  layout: 'custom'
})

const initialData:Bank = {
  id: -1,
  bank_code: '',
  name: ''
}
 
</script>