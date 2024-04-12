<template>
  <q-layout view="lHh Lpr lFf">
    <q-header bordered reveal class="text-primary bg-white">
      <q-toolbar>
        <q-btn flat label="CatHackers" />
        <q-space />

        <q-tabs v-model="tab" shrink>
          <q-tab name="tab1" label="Main" @click="$router.push('/')" />
          <q-tab name="tab2" label="About" @click="$router.push('/about')" />
        </q-tabs>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const tab = ref('tab1');
</script>
