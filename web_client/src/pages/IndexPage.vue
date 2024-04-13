<template>
  <q-page class="column" style="width: 100%">
    <CInfiniteScroll :items="items" @card-click="(item) => { isVisible = true; currentArtItem = item }"
      @load-more="loadMore" class="tw-m-auto tw-pt-4" />
  </q-page>
  <WPhotoDetails :art-item="currentArtItem" v-model="isVisible" />
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import CInfiniteScroll from 'src/components/CInfiniteScroll.vue';
import { ArtItemT } from 'src/entities/ArtItem';
import WPhotoDetails from 'src/widgets/WPhotoDetails.vue';
import { provide, ref } from 'vue';

const $q = useQuasar();
const currentArtItem = ref();

provide('loading', {
  show: () => $q.loading.show({
    message: 'Подождите, идет загрузка...'
  }),
  hide: () => $q.loading.hide()
});

const isVisible = ref(false);

const items = ref<ArtItemT[]>(
  [
    {
      id: 1,
      title: 'Книга. «К.Э. Циолковский известный и неизвестный»/ сост. А.Л. Голованов, Е.А. Тимошенкова. - М.: «ГЕЛИОС», 2023.',
      description: 'Книга в мягкой обложке. Рассказывает о жизненном пути великого человека, основоположника теоретической космонавтики Константина Эдуардовича Циолковского.',
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63103841?originalName=3659866.jpg',
      tags: ['Книги']
    },
    {
      id: 2,
      title: 'Брошюра. Как собирать горные породы и минералы. 45 стр.',
      description: 'Местонахождение: Муниципальное бюджетное учреждение культуры "Краснотурьинский краеведческий музей',
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63099146?originalName=3826657.jpg',
      tags: ['Книги']
    },
    {
      id: 3,
      title: `Шмагин Вячеслав Николаевич "Скорбящий ангел"`,
      description: `Местонахождение
Федеральное государственное бюджетное учреждение культуры "Государственный центральный музей современной истории России"`,
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63096049?originalName=46116_3.jpg',
      tags: ['Живопись']
    },
    {
      id: 4,
      title: 'Книга. «К.Э. Циолковский известный и неизвестный»/ сост. А.Л. Голованов, Е.А. Тимошенкова. - М.: «ГЕЛИОС», 2023.',
      description: 'Книга в мягкой обложке. Рассказывает о жизненном пути великого человека, основоположника теоретической космонавтики Константина Эдуардовича Циолковского.',
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63103841?originalName=3659866.jpg',
      tags: ['Книги']
    },
    {
      id: 5,
      title: 'Брошюра. Как собирать горные породы и минералы. 45 стр.',
      description: 'Местонахождение: Муниципальное бюджетное учреждение культуры "Краснотурьинский краеведческий музей',
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63099146?originalName=3826657.jpg',
      tags: ['Книги']
    },
    {
      id: 6,
      title: `Шмагин Вячеслав Николаевич "Скорбящий ангел"`,
      description: `Местонахождение
Федеральное государственное бюджетное учреждение культуры "Государственный центральный музей современной истории России"`,
      imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63096049?originalName=46116_3.jpg',
      tags: ['Живопись']
    },
  ]
);

const loadMore = (index: number, done: () => void) => {
  setTimeout(() => {
    items.value.push(
      {
        id: items.value.length + 1,
        title: 'Книга. «К.Э. Циолковский известный и неизвестный»/ сост. А.Л. Голованов, Е.А. Тимошенкова. - М.: «ГЕЛИОС», 2023.',
        description: 'Книга в мягкой обложке. Рассказывает о жизненном пути великого человека, основоположника теоретической космонавтики Константина Эдуардовича Циолковского.',
        imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63103841?originalName=3659866.jpg',
        tags: ['Книги']
      },
      {
        id: items.value.length + 2,
        title: 'Брошюра. Как собирать горные породы и минералы. 45 стр.',
        description: 'Местонахождение: Муниципальное бюджетное учреждение культуры "Краснотурьинский краеведческий музей',
        imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63099146?originalName=3826657.jpg',
        tags: ['Книги']
      },
      {
        id: items.value.length + 3,
        title: `Шмагин Вячеслав Николаевич "Скорбящий ангел"`,
        description: `Местонахождение
Федеральное государственное бюджетное учреждение культуры "Государственный центральный музей современной истории России"`,
        imageUrl: 'https://goskatalog.ru/muzfo-imaginator/rest/images/original/63096049?originalName=46116_3.jpg',
        tags: ['Живопись']
      },
    );
    done();
  }, 2000);
}
</script>

<style scoped lang="scss">
.search-header {
  position: sticky;
  z-index: 10;
  margin-top: 50px;
  top: 20px;
  width: 90%;
  left: 5%;
  border-bottom: 1px solid #ccc;
}
</style>
