<template>
  <q-layout view="lHh Lpr lFf">
    <q-header bordered class="text-primary bg-white">
      <q-toolbar class="tw-h-24">
        <q-btn flat label="ArtiFinder" class="tw-absolute tw-top-0 tw-left-1" />
        <WToolBar />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import WToolBar from 'src/widgets/WToolBar.vue';

</script>
