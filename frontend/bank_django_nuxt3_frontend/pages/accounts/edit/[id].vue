<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/accounts">Accounts</NuxtLink></li>
      <li class="is-active"><a href="#">Edit Account #{{$route.params.id}}</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <o-loading :active.sync="loading">
          <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
        </o-loading>
        <FormAccount v-if="account" title="Edit Account" :initial-data="account"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


definePageMeta({
  layout: 'custom'
})

const { getAccount, account, loading } = useAccount()

const route = useRoute()

onMounted(async () =>  await getAccount(route.params.id as unknown as number))

</script>