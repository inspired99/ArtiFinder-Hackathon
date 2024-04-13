<template>
  <q-layout view="lHh Lpr lFf">
    <q-header bordered class="text-primary bg-white">
      <q-toolbar class="tw-h-24">
        <q-btn flat label="ArtiFinder" class="tw-absolute tw-top-0 tw-left-1" />
        <WToolBar :categoryOptions="categoryOptions" v-model:imageAddModel="imageAddModel"
          v-model:categoryAddModel="categoryAddModel" v-model:descriptionAddModel="descriptionAddModel"
          v-model:imageSearchModel="imageSearchModel" v-model:categorySearchModel="categorySearchModel"
          v-model:titleSearchModel="titleSearchModel" />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import WToolBar from 'src/widgets/WToolBar.vue';


const categoryOptions = ref<string[]>(['Книги', 'Живопись', 'Фотографии', 'Скульптура', 'Музыка', 'Кино', 'Театр', 'Архитектура', 'Дизайн', 'Искусство', 'Культура', 'История', 'Наука', 'Техника', 'Спорт', 'Природа', 'Путешествия', 'Люди', 'События', 'Другое']);

const imageAddModel = ref<File>();
const categoryAddModel = ref<string>();
const descriptionAddModel = ref<string>();

const imageSearchModel = ref<File>();
const categorySearchModel = ref<string>();
const titleSearchModel = ref<string>();

</script>
