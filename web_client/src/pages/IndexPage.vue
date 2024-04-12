<template>
  <q-page class="column" style="width: 100%">
    <!-- <header
      class="tw-container tw-mx-auto tw-w-full tw-bg-white tw-shadow-md tw-p-4 tw-rounded-md tw-mb-4 tw-z-10 tw-sticky tw-top-3"> -->
    <WSearchHeader />
    <!-- </header> -->
    <CInfiniteScroll :items="items" @card-click="console.log" @load-more="loadMore" class="tw-m-auto tw-pt-4" />
  </q-page>
</template>

<script setup lang="ts">
import CInfiniteScroll from 'src/components/CInfiniteScroll.vue';
import WSearchHeader from 'src/widgets/WSearchHeader.vue';
import { ref } from 'vue';

const items = ref([
  { id: 1, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit'] },
  { id: 2, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit'] },
  { id: 3, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit'] },
]);

const loadMore = (index: number, done: () => void) => {
  setTimeout(() => {
    items.value.push(
      { id: items.value.length + 1, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit', 'sdfsdfsdf', 'sdfdsfsd', 'sdfdsf', 'sdfdsf'] },
      { id: items.value.length + 2, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit'] },
      { id: items.value.length + 3, src: 'https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg', description: 'Two Girls in White and Black Dress Standing on Brown Wooden Dock during Daytime', tags: ['Bull shit', 'Yet another shit'] },
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
