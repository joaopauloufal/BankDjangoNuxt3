<template>
  <section class="section">
    <div class="columns">
      <div class="column is-size-4 is-9">Clients</div>
      <div class="column">
        <o-button
          variant="primary"
          tag="router-link"
          class="is-pulled-right"
          icon-left="plus"
          icon-pack="fas"
          to="/clients/create"
        >
          New Client
        </o-button>
      </div>
    </div>
      <o-loading :active.sync="loading">
        <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
      </o-loading>
      <div class="columns">
        <div class="column">
          <o-table
            v-if="clients"
            :data="clients"
            per-page="10"
            paginated
            default-sort="name"
            striped
          >
            <o-table-column label="CPF/CNPJ" field="cpf_cnpj" v-slot="props" searchable>
              {{ props.row.cpf_cnpj }}
            </o-table-column>
            <o-table-column label="Name" field="name" v-slot="props" sortable searchable>
              {{ props.row.name }}
            </o-table-column>
            <o-table-column label="Actions" v-slot="props">
              <div class="buttons">
                <o-button
                 size="small"
                  tag="router-link"
                  variant="primary"
                  icon-right="pencil"
                  icon-pack="fas"
                  :to="`/clients/edit/${props.row.id}`"
                />
                <o-button size="small" variant="danger" icon-pack="fas" icon-right="trash" @click="openConfirmModal(props.row)"/>
              </div>
            </o-table-column>
            <template #empty>
              <div class="has-text-centered">There are no registered clients.</div>
            </template>
          </o-table>
        </div>
      </div>
  </section>
</template>
<script setup lang="ts">

import { ModalProgrammatic } from '@oruga-ui/oruga-next'
import BaseConfirmDialog from '../../components/BaseConfirmDialog.vue'

definePageMeta({
  layout: 'custom'
})

const { getClients, deleteClient, clearClients, clients, loading } = useClient()

onMounted(() => getClients())

onUnmounted(() => clearClients())

const openConfirmModal = async (data:any):Promise<void> => {
  const instance = ModalProgrammatic.open({
    component: BaseConfirmDialog, 
    props: { 
      title: `Delete client #${data.id}`,
      message: `Are you sure you want to delete client #${data.id}?`,
    }
  })

  const result = await instance.promise

  if (result.action === 'ok') {
    await deleteClient(data.id)
  }
}
 
</script>
