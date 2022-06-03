<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/agencies">Agencies</NuxtLink></li>
      <li class="is-active"><a href="#" aria-current="page">Edit Agency #{{$route.params.id}}</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <o-loading :active.sync="loading">
          <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
        </o-loading>
        <FormAgency v-if="agency" title="Edit Agency" :initial-data="agency"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


definePageMeta({
  layout: 'custom'
})

const { getAgency, agency, loading } = useAgency()

const route = useRoute()

onMounted(async () =>  await getAgency(route.params.id as unknown as number))

</script>