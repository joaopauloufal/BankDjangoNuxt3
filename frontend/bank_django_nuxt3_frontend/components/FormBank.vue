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
        label="Bank Code"
        :variant="bankErrors.bank_code ? 'danger': ''"
        :message="bankErrors.bank_code ? bankErrors.bank_code: ''"
      >
        <o-input v-model="formData.bank_code" name="bank_code"></o-input>
      </o-field>
      <o-field
        label="Name"
        :variant="bankErrors.name ? 'danger': ''"
        :message="bankErrors.name ? bankErrors.name: ''"
      >
        <o-input v-model="formData.name" name="name"></o-input>
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
import Bank from '~~/types/bank';

  const props = defineProps<{
    title: string,
    initialData: Bank
  }>()

  let formData = ref({
    id: -1,
    bank_code: '',
    name: ''
  })

  const { addBank, bankErrors, clearErrors, clearBank, editBank, loading } = useBank()


  onMounted(() => {
    formData.value = props.initialData
  })

  onUnmounted(() => {
    clearBank()
  })

  const router = useRouter()

  function cancel ():void  {
    clearErrors()
    router.push('/banks')
  }

  async function submit():Promise<void>  {
    window.console.log()
    if (formData.value.id != -1) {
      await editBank(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Bank updated successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/banks')
      })
    } else {
      await addBank(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Bank created successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/banks')
      })
    }

  }

</script>