<template>
  <q-layout view="lHh Lpr lFf">
    <q-header bordered class="text-primary bg-white">
      <q-toolbar class="tw-h-24">
        <q-btn flat label="ArtiFinder" class="tw-absolute tw-top-0 tw-left-1" />
        <WToolBar :categoryOptions="categoryOptions" v-model:imageAddModel="addItem.image"
          v-model:categoryAddModel="addItem.category" v-model:descriptionAddModel="addItem.description"
          v-model:imageSearchModel="searchItem.image" v-model:categorySearchModel="searchItem.category"
          v-model:titleSearchModel="searchItem.title" />
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useAddArtObjectStore } from 'src/stores/AddArtObjectStore';
import { useSerchArtObjectStore } from 'src/stores/SearchArtObjectStore';
import WToolBar from 'src/widgets/WToolBar.vue';


const categoryOptions = ref<string[]>([
  'Минералогия', 'Археология', 'Нумизматика', 'Печатная продукция', 'Графика',
    'Фото, негативы', 'ДПИ', 'Естественнонауч.коллекция', 'Скульптура', 'Прочие',
    'Редкие книги', 'Техника', 'Оружие', 'Документы', 'Живопись'
]);


const { searchItem } = useSerchArtObjectStore();
const { addItem } = useAddArtObjectStore();

</script>
