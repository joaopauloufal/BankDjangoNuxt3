<template>
  <aside class="column is-2 section">
    <p class="menu-label is-hidden-touch">Main Menu</p>
    <ul class="menu-list">
      <li v-for="(item, key) of items" :key="key">
        <NuxtLink :to="item.to" active-class="is-active">
          <o-icon pack="fas" :icon="item.icon" /> {{ item.title }}
        </NuxtLink>
      </li>
    </ul>
  </aside>
</template>

<script setup lang="ts">

 const items = [
    {
      title: 'Home',
      icon: 'home',
      to: { name: 'index' },
    },
    {
      title: 'Banks',
      icon: 'bank',
      to: { name: 'banks' },
    },
    {
      title: 'Agencies',
      icon: 'house-user',
      to: { name: 'agencies' },
    },
 ]

</script>