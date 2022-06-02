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
        label="Agency Code"
        :variant="agencyErrors.agency_code ? 'danger': ''"
        :message="agencyErrors.agency_code ? agencyErrors.agency_code: ''"
      >
        <o-input v-model="formData.agency_code" name="agency_code"></o-input>
      </o-field>
      <o-field
        label="Name"
        :variant="agencyErrors.name ? 'danger': ''"
        :message="agencyErrors.name ? agencyErrors.name: ''"
      >
        <o-input v-model="formData.name" name="name"></o-input>
      </o-field>
      <o-field
        label="Bank"
        :variant="agencyErrors.bank ? 'danger': ''"
        :message="agencyErrors.bank ? agencyErrors.bank: ''"
      >
        <BaseSelectField 
          placeholder="Select a bank..."
          key-name="name"
          key-value="id"
          entrypoint="banks/"
          initial-value=""
          :return-object="false"
          v-model="formData.bank"
        />
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
import Agency from '~~/types/agency';

  const props = defineProps<{
    title: string,
    initialData: Agency
  }>()

  let formData = ref({
    id: -1,
    agency_code: '',
    bank: '',
    name: ''
  })

  const { addAgency, agencyErrors, clearErrors, clearAgency, editAgency, loading } = useAgency()


  onMounted(() => {
    formData.value = props.initialData
  })

  onUnmounted(() => {
    clearAgency()
  })

  const router = useRouter()

  function cancel ():void  {
    clearErrors()
    router.push('/agencies')
  }

  async function submit():Promise<void>  {
    if (formData.value.id != -1) {
      await editAgency(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Agency updated successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/agencies')
      })
    } else {
      await addAgency(formData.value).then(() => {
        NotificationProgrammatic.open({
          message: 'Agency created successfully!',
          variant: 'success',
          rootClass: 'toast-notification',
          position: 'top',
          duration: 3000,
        })
        router.push('/agencies')
      })
    }

  }

</script>