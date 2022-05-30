<template>
  <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
          <p class="modal-card-title">{{ title }}</p>
          <o-icon
              clickable
              native-type="button"
              icon="times"
              @click.native="$emit('close')"/>
      </header>
      <section class="modal-card-body">
          <p>{{ message }}</p>
      </section>
      <footer class="modal-card-foot">
          <o-button variant="danger" @click="$emit('close', { action: 'cancel', method: 'x' })">Cancel</o-button>
          <o-button variant="primary" @click="$emit('close', { action: 'ok'})">OK</o-button>
      </footer>
  </div>
</template>

<script setup lang="ts">

const props = defineProps<{
  title: string,
  message: string
}>()

</script>