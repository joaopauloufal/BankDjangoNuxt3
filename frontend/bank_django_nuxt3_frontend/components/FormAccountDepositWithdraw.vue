<template>
  <o-button v-if="operationType === 'deposit'" variant="info" size="small" icon-pack="fas" icon-right="download" @click="open"/>
  <o-button v-if="operationType === 'withdraw'" variant="success" size="small" icon-pack="fas" icon-right="upload" @click="open"/>
  <o-modal :active.sync="isActive">
    <div class="modal-card" style="width: auto">
      <o-loading :active.sync="loading">
        <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
      </o-loading>
      <header class="modal-card-head">
        <p class="modal-card-title">{{ operationType === 'deposit' ? 'Make Deposit' : 'Make Withdraw'}} (Account: {{account.number}})</p>
        <o-icon
          clickable
          native-type="button"
          icon="times"
          @click.native="close"
        />
      </header>
      <section class="modal-card-body">
        <o-field
          label="Value"
          :variant="accountDepositWithdrawErrors.value ? 'danger': ''"
          :message="accountDepositWithdrawErrors.value ? accountDepositWithdrawErrors.value: ''"
        >
          <o-input v-model="formData.value" v-maska="'#*.##'" name="value"></o-input>
        </o-field>
      </section>
      <footer class="modal-card-foot is-justify-content-flex-end">
        <o-button variant="primary" @click="submit">OK</o-button>
        <o-button variant="danger" @click="close">Cancel</o-button>
      </footer>
    </div>
  </o-modal>
</template>

<script setup lang="ts">

import { NotificationProgrammatic } from '@oruga-ui/oruga-next'
import Account from '~~/types/account';


const props = defineProps<{
  account: Account,
  operationType: string
}>()

const formData = ref({
  value: 0,
  id: props.account.id
})

const isActive = ref(false)

const { accountDepositWithdrawErrors, loading, clearErrors, deposit, getAccounts, withdraw } = useAccount()

const close = () => {
  isActive.value = false
  formData.value.value = 0
  clearErrors()
}

const open = () => {
  isActive.value = true
}

const submit = async () => {
  if (props.operationType === 'deposit') {
    await deposit(formData.value).then((response) => {
      NotificationProgrammatic.open({
        message: response.message,
        variant: 'success',
        rootClass: 'toast-notification',
        position: 'top',
        duration: 3000,
      })
      close()
      getAccounts()
    })
  } else if (props.operationType === 'withdraw') {
    await withdraw(formData.value).then((response) => {
      NotificationProgrammatic.open({
        message: response.message,
        variant: 'success',
        rootClass: 'toast-notification',
        position: 'top',
        duration: 3000,
      })
      close()
      getAccounts()
    })
  }

}


</script>