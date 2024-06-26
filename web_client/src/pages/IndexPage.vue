<template>
  <q-page class="column" style="width: 100%">
    <CInfiniteScroll v-model:disable="disable" :items="items"
      @card-click="(item) => { isVisible = true; currentArtItem = item }" @load-more="loadMore"
      class="tw-m-auto tw-pt-4" />
  </q-page>
  <WPhotoDetails :artItem="currentArtItem" v-model="isVisible" />
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { ref } from 'vue';
import { useSerchArtObjectStore } from 'src/stores/SearchArtObjectStore';
import CInfiniteScroll from 'src/components/CInfiniteScroll.vue';
import { ArtItemT } from 'src/entities/ArtItem';
import WPhotoDetails from 'src/widgets/WPhotoDetails.vue';

// console.log the version of Frontend
console.log('Frontend version: 0.0.1');

type ItemBackend = {
  id: number;
  title: string;
  description: string;
  path: string;
  category: string;
};

const mapBackendItem = (item: ItemBackend): ArtItemT => ({
  id: item.id,
  title: item.title,
  description: item.description,
  imageUrl: item.path.replace('/home/ubuntu', 'https://cathackers.xyz'), // TODO: fix this
  tag: item.category,
});

const searchArtStore = useSerchArtObjectStore();
const searchItem = searchArtStore.searchItem;

const notFound = () => $q.notify({
  message: 'Нет больше объектов с такими параметрами',
  color: 'negative',
  position: 'top',
});

const cb = debounce(() => resetScroll(), 800);

searchArtStore.$subscribe(() => {
  cb();
  if (!searchItem.image) {
    searchItem.path = undefined;
  }
});

function debounce(func: (...args: unknown[]) => void, delay: number) {
  let timeoutId: ReturnType<typeof setTimeout>;
  return function (...args: unknown[]) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  };
}

const resetScroll = () => {
  disable.value = false;
  offset = 0;
  items.value = [];
  loadContent().then((data) => {
    if (!data.length) {
      notFound();
      return;
    }
    items.value = data.map(mapBackendItem);
  }).catch(console.error);
};

const $q = useQuasar();
const currentArtItem = ref();
const disable = ref(false);

let limit = 12;
let offset = 0;

const isVisible = ref(false);

const items = ref<ArtItemT[]>([]);

const loadContent = async () => {
  try {
    const response = await fetch(`/api/get_arts_info?limit=${limit}&offset=${offset}`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: searchItem?.title,
          path: searchItem?.path,
          category: searchItem?.category,
        }),
      });

    if (!response.ok) {
      $q.notify({
        message: 'Ошибка загрузки объектов',
        color: 'negative',
        position: 'top',
      });
    }

    const data = await response.json();
    // items.value = items.value.concat(data.map(mapBackendItem));
    offset += limit;
    return data;
  } catch (error) {
    console.error(error);
  }
};

const loadMore = (page: number, done: () => void) => {
  // disable.value = true;
  loadContent().then((data) => {
    console.log(data.length);
    if (!data.length) {
      disable.value = true;
      notFound();
      done();
      return;
    }
    // disable.value = false;

    items.value = items.value.concat(data.map(mapBackendItem));
    done();
  }).catch(console.error);
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
