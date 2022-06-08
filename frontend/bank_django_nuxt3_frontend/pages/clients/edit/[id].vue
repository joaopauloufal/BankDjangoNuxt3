<template>
  <div>
    <BaseBreadcumb>
      <li><NuxtLink to="/clients">Clients</NuxtLink></li>
      <li class="is-active"><a href="#">Edit Client #{{$route.params.id}}</a></li>
    </BaseBreadcumb>
    <div class="columns">
      <div class="column is-6">
        <o-loading :active.sync="loading">
          <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
        </o-loading>
        <FormClient v-if="client" title="Edit Client" :initial-data="client"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">


definePageMeta({
  layout: 'custom'
})

const { getClient, client, loading } = useClient()

const route = useRoute()

onMounted(async () =>  await getClient(route.params.id as unknown as number))

</script>