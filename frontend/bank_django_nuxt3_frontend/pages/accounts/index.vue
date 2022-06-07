<template>
  <section class="section">
    <div class="columns">
      <div class="column is-size-4 is-9">Accounts</div>
      <div class="column">
        <o-button
          variant="primary"
          tag="router-link"
          class="is-pulled-right"
          icon-left="plus"
          icon-pack="fas"
          to="/accounts/create"
        >
          New Account
        </o-button>
      </div>
    </div>
      <o-loading :active.sync="loading">
        <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
      </o-loading>
      <div class="columns">
        <div class="column">
          <o-table
            v-if="accounts"
            :data="accounts"
            per-page="10"
            paginated
            default-sort="number"
          >
            <o-table-column label="Number" field="number" v-slot="props" sortable searchable>
              {{ props.row.number }}
            </o-table-column>
            <o-table-column label="Type" field="type" v-slot="props" searchable>
              {{ props.row.type }}
            </o-table-column>
            <o-table-column label="Client" field="client" v-slot="props" searchable>
              {{ props.row.client.cpf_cnpj }} - {{ props.row.client.name }}
            </o-table-column>
            <o-table-column label="Agency" field="agency" v-slot="props" searchable>
              {{ props.row.agency.agency_code }} - {{ props.row.agency.name }}
            </o-table-column>
            <o-table-column label="Balance" field="balance" v-slot="props" sortable>
              {{ props.row.balance }}
            </o-table-column>
            <o-table-column label="Actions" v-slot="props">
              <div class="buttons">
                <o-button
                  tag="router-link"
                  variant="primary"
                  icon-right="pencil"
                  icon-pack="fas"
                  :to="`/accounts/edit/${props.row.id}`"
                />
                <o-button variant="danger" icon-pack="fas" icon-right="trash" @click="openConfirmModal(props.row)"/>
                <FormAccountDepositWithdraw :account="props.row" operation-type="deposit" />
                <FormAccountDepositWithdraw :account="props.row" operation-type="withdraw" />
              </div>
            </o-table-column>
            <template #empty>
              <div class="has-text-centered">There are no registered accounts.</div>
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

const { getAccounts, deleteAccount, clearAccounts, accounts, loading } = useAccount()

onMounted(() => getAccounts())

onUnmounted(() => clearAccounts())

const openConfirmModal = async (data:any):Promise<void> => {
  const instance = ModalProgrammatic.open({
    component: BaseConfirmDialog, 
    props: { 
      title: `Delete account #${data.id}`,
      message: `Are you sure you want to delete account #${data.id}?`,
    }
  })

  const result = await instance.promise

  if (result.action === 'ok') {
    await deleteAccount(data.id)
  }
}
 
</script>
