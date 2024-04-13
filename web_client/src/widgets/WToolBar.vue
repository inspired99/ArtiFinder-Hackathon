<template>
    <div class="tw-w-full tw-flex tw-flex-row tw-items-end tw-h-full tw-container tw-m-auto">
        <div class="tw-basis-5/7 tw-flex tw-items-center">
            <q-input class="tw-w-80 tw-mr-8" :loading="loadingState" v-model="text" label="Поиск по title" />
            <!-- <div class="tw-flex tw-flex-row tw-items-center tw-mt-2"> -->

            <q-avatar v-for="n in 1" :key="n" class="overlapping">
                <img :src="`https://staticg.sportskeeda.com/editor/2023/09/d0917-16959581724408-1920.jpg`">
            </q-avatar>
            <q-chip v-for="tag in ['Bull shit']" :key="tag" removable>
                {{ tag }}
            </q-chip>
            <!-- </div> -->
        </div>
        <div class="tw-basis-2/7 tw-flex tw-justify-end">
            <q-btn color="white" text-color="black" unelevated outline icon="add" label="Добавить фото"
                @click="op = true"></q-btn>
            <q-btn class="tw-ml-1" text-color="text-primary" unelevated outline icon="camera_enhance"
                label="Найти по фото" @click="op = true"></q-btn>
        </div>
        <WPopUpSearch v-model="op" headerTitle="Search with photo" :categoryOptions="['a', 'b', 'c']"
            v-model:category="category" v-model:description="desc" />
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import WPopUpSearch from 'src/widgets/WPopUpSearch.vue';

const op = ref(false);
const category = ref('');
const desc = ref('');

const text = ref('');
const loadingState = ref(false);
</script>