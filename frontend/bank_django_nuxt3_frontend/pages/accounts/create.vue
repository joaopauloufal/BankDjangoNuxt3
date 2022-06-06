<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/banks">Accounts</NuxtLink></li>
      <li class="is-active"><a href="#">New Account</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <FormAccount title="New Account" :initial-data="initialData"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Account from '~~/types/account';



definePageMeta({
  layout: 'custom'
})

const initialData:Account = {
  id: -1,
  number: '',
  agency: '' as any,
  client: '' as any,
  type: 'PHYSICAL' as any,
  balance: 0.0
}
 
</script>