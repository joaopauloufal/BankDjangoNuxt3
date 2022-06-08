<template>
  <section class="section">
    <div class="columns">
      <div class="column is-size-4 is-9">Banks</div>
      <div class="column">
        <o-button
          variant="primary"
          tag="router-link"
          class="is-pulled-right"
          icon-left="plus"
          icon-pack="fas"
          to="/banks/create"
        >
          New Bank
        </o-button>
      </div>
    </div>
      <o-loading :active.sync="loading">
        <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
      </o-loading>
      <div class="columns">
        <div class="column">
          <o-table
            v-if="banks"
            :data="banks"
            per-page="10"
            paginated
            default-sort="name"
            striped
          >
            <o-table-column label="Bank Code" field="bank_code" v-slot="props" sortable searchable>
              {{ props.row.bank_code }}
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
                  :to="`/banks/edit/${props.row.id}`"
                />
                <o-button size="small" variant="danger" icon-pack="fas" icon-right="trash" @click="openConfirmModal(props.row)"/>
              </div>
            </o-table-column>
            <template #empty>
              <div class="has-text-centered">There are no registered banks.</div>
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

const { getBanks, deleteBank, clearBanks, banks, loading } = useBank()

onMounted(() => getBanks())

onUnmounted(() => clearBanks())

const openConfirmModal = async (data:any):Promise<void> => {
  const instance = ModalProgrammatic.open({
    component: BaseConfirmDialog, 
    props: { 
      title: `Delete bank #${data.id}`,
      message: `Are you sure you want to delete bank #${data.id}?`,
    }
  })

  const result = await instance.promise

  if (result.action === 'ok') {
    await deleteBank(data.id)
  }
}
 
</script>
