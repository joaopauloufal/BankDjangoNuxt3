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
        label="Type"
      >
        <o-select placeholder="Select..." v-model="typeClient">
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
        label="CPF/CNPJ"
        :variant="clientErrors.cpf_cnpj ? 'danger': ''"
        :message="clientErrors.cpf_cnpj ? clientErrors.cpf_cnpj: ''"
      >
        <o-input 
          v-model="formData.cpf_cnpj" 
          name="cpf_cnpj"
          v-maska="mask"
        >
        </o-input>
      </o-field>
      <o-field
        label="Name"
        :variant="clientErrors.name ? 'danger': ''"
        :message="clientErrors.name ? clientErrors.name: ''"
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
import Client from '~~/types/client'
  
const props = defineProps<{
  title: string,
  initialData: Client
}>()

const typeClient = ref('PHYSICAL')

const mask = ref('')

const formData = ref({
  id: -1,
  cpf_cnpj: '',
  name: ''
})

const options = [
  { key: 'PHYSICAL', description: 'Physical person' },
  { key: 'LEGAL', description: 'Legal person' },
]

const { addClient, clientErrors, clearErrors, clearClient, editClient, loading } = useClient()


onMounted(() => {
  formData.value = props.initialData
})

onUnmounted(() => {
  clearClient()
})

const router = useRouter()

function cancel ():void  {
  clearErrors()
  router.push('/clients')
}

watch(() => typeClient.value, (currentValue) => {
  if (currentValue == 'PHYSICAL') {
    mask.value = '###.###.###-##'
  } else if (currentValue == 'LEGAL') {
    mask.value = '##.###.###/####-##'
  }
}, { immediate: true })

async function submit():Promise<void>  {
  if (formData.value.id != -1) {
    await editClient(formData.value).then(() => {
      NotificationProgrammatic.open({
        message: 'Client updated successfully!',
        variant: 'success',
        rootClass: 'toast-notification',
        position: 'top',
        duration: 3000,
      })
      router.push('/clients')
    })
  } else {
    await addClient(formData.value).then(() => {
      NotificationProgrammatic.open({
        message: 'Client created successfully!',
        variant: 'success',
        rootClass: 'toast-notification',
        position: 'top',
        duration: 3000,
      })
      router.push('/clients')
    })
  }

}

</script>