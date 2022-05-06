<template>
  <section class="section">
    <div class="columns">
      <div class="column is-size-4 is-9">Banks</div>
      <div class="column">
        <o-button
          variant="primary"
          tag="nuxt-link"
          class="is-pulled-right"
          icon-left="plus"
          icon-pack="fas"
          to="banks/create"
        >
          New Bank
        </o-button>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <o-table
          v-if="banks"
          :data="banks"
          per-page="10"
          paginated
          default-sort="name"
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
                variant="primary"
                icon-right="pencil"
                icon-pack="fas"
                tag="nuxt-link"
              />
              <o-button variant="danger" icon-pack="fas" icon-right="trash" v-slot="props"/>
            </div>
          </o-table-column>
          <template #empty>
            <div class="has-text-centered">Não há bancos cadastrados.</div>
          </template>
        </o-table>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
import { Ref } from 'vue'
import Bank from '~~/types/bank'

definePageMeta({
  layout: 'custom'
})

const banks:Ref<Bank[]> = getBanks()
 
</script>
