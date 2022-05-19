<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/banks">Banks</NuxtLink></li>
      <li class="is-active"><a href="#" aria-current="page">New Bank</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <FormBank title="New Bank" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


definePageMeta({
  layout: 'custom'
})
 
</script>