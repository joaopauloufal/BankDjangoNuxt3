<template>
  <o-loading :active.sync="loading">
    <o-icon pack="fas" icon="sync-alt" size="large" spin></o-icon>
  </o-loading>
  <div class="card">
    <div class="card-header">
      <p class="card-header-title">
        {{title}}
      </p>
    </div>
    <div class="card-content">
      <o-field
        label="Number"
        :variant="accountErrors.number ? 'danger': ''"
        :message="accountErrors.number ? accountErrors.number: ''"
      >
        <o-input v-model="formData.number" name="number"></o-input>
      </o-field>
      <o-field
        label="Type"
        :variant="accountErrors.type ? 'danger': ''"
        :message="accountErrors.type ? accountErrors.type: ''"
      >
        <o-select placeholder="Select..." v-model="formData.type">
          <option 
            v-for="option in options"
            :value="option.key"
            :key="option.key"
          >
            {{option.description}}
          </option>
        </o-select>
      </o-field>
      <o-field
        label="Client"
        :variant="accountErrors.client ? 'danger': ''"
        :message="accountErrors.client ? accountErrors.client: ''"
      >
        <BaseSelectField 
          placeholder="Select a client..."
          key-name="name"
          key-value="id"
          entrypoint="clients/"
          :initial-value="formData.client"
          :return-object="false"
          v-model="formData.client"
        />
      </o-field>
      <o-field
        label="Agency"
        :variant="accountErrors.agency ? 'danger': ''"
        :message="accountErrors.agency ? accountErrors.agency: ''"
      >
        <BaseSelectField 
          placeholder="Select a agency..."
          key-name="name"
          key-value="id"
          entrypoint="agencies/"
          :initial-value="formData.agency"
          :return-object="false"
          v-model="formData.agency"
        />
      </o-field>
      <o-field
        label="Initial Balance"
        :variant="accountErrors.balance ? 'danger': ''"
        :message="accountErrors.balance ? accountErrors.balance: ''"
      >
        <o-input v-model="formData.balance" v-maska="'#*.##'" name="balance"></o-input>
      </o-field>
    </div>
    <footer class="card-footer is-justify-content-center pt-3 pb-3">
      <div class="buttons">
        <o-button variant="primary" @click="submit">Save</o-button>
        <o-button variant="danger" @click="cancel">Cancel</o-button>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { NotificationProgrammatic } from '@oruga-ui/oruga-next'
import Account from '~~/types/account';

  const props = defineProps<{
    title: string,
    initialData: Account
  }>()

  let formData = ref({
    id: -1,
    type: 'PHYSICAL',
    client: '' as any,
    balance: 0,
    agency: '' as any,
    number: ''
  })

  const options = [
    { key: 'PHYSICAL', description: 'Physical person' },
    { key: 'LEGAL', description: 'Legal person' },
  ]

  const { addAccount, accountErrors, clearErrors, clearAccount, editAccount, loading } = useAccount()


  onMounted(() => {
    formData.value = {
      id: props.initialData.id,
      type: props.initialData.type,
      client: props.initialData.client.id ?? '',
      balance: props.initialData.balance,
      agency: props.initialData.agency.id ?? '',
      number: props.initialData.number
    }
  })

  onUnmounted(() => {
    clearAccount()
  })

  const router = useRouter()

  function cancel ():void  {
    clearErrors()
    router.push('/accounts')
  }

  async function submit():Promise<void>  {
    if (formData.value.id != -1) {
      await editAccount(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Account updated successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/accounts')
      })
    } else {
      await addAccount(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Account created successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/accounts')
      })
    }

  }

</script>