<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/banks">Banks</NuxtLink></li>
      <li class="is-active"><a href="#" aria-current="page">Edit Bank #{{$route.params.id}}</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <o-loading :active.sync="loading">
          <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
        </o-loading>
        <FormBank v-if="bank" title="Edit Bank" :initial-data="bank"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


definePageMeta({
  layout: 'custom'
})

const { getBank, bank, loading } = useBank()

const route = useRoute()

onMounted(async () =>  await getBank(route.params.id as unknown as number))

</script>