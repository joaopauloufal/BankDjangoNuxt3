<template>
  <section class="section">
    <div class="columns">
      <div class="column is-size-4 is-9">Agencies</div>
      <div class="column">
        <o-button
          variant="primary"
          tag="router-link"
          class="is-pulled-right"
          icon-left="plus"
          icon-pack="fas"
          to="/agencies/create"
        >
          New Agency
        </o-button>
      </div>
    </div>
      <o-loading :active.sync="loading">
        <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
      </o-loading>
      <div class="columns">
        <div class="column">
          <o-table
            v-if="agencies"
            :data="agencies"
            per-page="10"
            paginated
            default-sort="name"
          >
            <o-table-column label="Agency Code" field="agency_code" v-slot="props" sortable searchable>
              {{ props.row.agency_code }}
            </o-table-column>
            <o-table-column label="Name" field="name" v-slot="props" sortable searchable>
              {{ props.row.name }}
            </o-table-column>
            <o-table-column label="Bank" field="agency" v-slot="props">
              {{ props.row.bank.bank_code }} - {{ props.row.bank.name }}
            </o-table-column>
            <o-table-column label="Actions" v-slot="props">
              <div class="buttons">
                <o-button
                  tag="router-link"
                  variant="primary"
                  icon-right="pencil"
                  icon-pack="fas"
                  :to="`/agencies/edit/${props.row.id}`"
                />
                <o-button variant="danger" icon-pack="fas" icon-right="trash" @click="openConfirmModal(props.row)"/>
              </div>
            </o-table-column>
            <template #empty>
              <div class="has-text-centered">There are no registered agencies.</div>
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

const { getAgencies, deleteAgency, clearAgencies, agencies, loading } = useAgency()

onMounted(() => getAgencies())

onUnmounted(() => clearAgencies())

const openConfirmModal = async (data:any):Promise<void> => {
  const instance = ModalProgrammatic.open({
      component: BaseConfirmDialog, 
      props: { 
        title: `Delete agency #${data.id}`,
        message: `Are you sure you want to delete agency #${data.id}?`,
      }
  })

  const result = await instance.promise

  if (result.action === 'ok') {
    await deleteAgency(data.id)
  }
}
 
</script>
