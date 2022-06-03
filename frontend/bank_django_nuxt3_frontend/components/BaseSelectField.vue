<template>
  <o-select :placeholder="placeholder" v-model="selected">
    <option 
      v-for="option in records"
      :value="returnObject ? option: option[keyValue]"
      :key="option[keyValue]"
    >
      {{option[keyName]}}
    </option>
  </o-select>
</template>

<script setup lang="ts">

import ApiRepository from '~~/repositories/api_repository'

const props = defineProps<{
  placeholder: string,
  keyName: string,
  keyValue: string,
  entrypoint: string,
  initialValue: any,
  returnObject: boolean
}>()

const emit = defineEmits<{
  (event: 'input', value:any):void
}>()

const records = ref([])
const selected = ref('')

onMounted(() => {
  getDataFromApi()
})

watch(() => props.entrypoint, (currentValue, oldValue) => {
  if (currentValue !== '') {
    getDataFromApi()
  }
})

watch(() => selected, (currentValue, oldValue) => {
  emit('input', currentValue)
})

function initValue():void {
  if (props.initialValue && props.initialValue !== '') {
    records.value.forEach((item) => {
      if (item[props.keyValue] == props.initialValue) {
        selected.value = item[props.keyValue]
        return
      }
    })
    
  }
}


async function getDataFromApi():Promise<void> {
  await ApiRepository.get(props.entrypoint).then((response:any)=>{
    records.value = response
    initValue()
  })
  
}

</script>