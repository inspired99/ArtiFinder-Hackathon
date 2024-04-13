<template>
    <div class="tw-w-full tw-flex tw-flex-row tw-items-end tw-h-full tw-container tw-m-auto">
        <div class="tw-basis-5/7 tw-flex tw-items-center">
            <q-input class="tw-w-2/3 tw-mr-8" :loading="loadingState" v-model="text" label="Поиск по названию...">
                <template v-slot:append>
                    <q-icon v-if="text === ''" name="search" />
                    <q-icon v-else name="clear" class="cursor-pointer" @click="text = ''" />
                </template>
            </q-input>
            <!-- <div class="tw-flex tw-flex-row tw-items-center tw-mt-2"> -->

            <q-avatar class="overlapping">
                <img
                    :src="`https://goskatalog.ru/muzfo-imaginator/rest/images/original/63103841?originalName=3659866.jpg`">
            </q-avatar>
            <q-chip v-for="tag in ['Живопись']" :key="tag" removable>
                {{ tag }}
            </q-chip>
            <!-- </div> -->
        </div>
        <div class="tw-basis-2/7 tw-flex tw-justify-end">
            <q-btn-dropdown v-if="isMobile" stretch flat outline icon="search">
                <q-list>
                    <q-item-label header>Поиск</q-item-label>
                    <q-item>
                        <q-btn color="white" text-color="black" unelevated outline icon="add" label="Добавить фото"
                            @click="op = true"></q-btn>
                    </q-item>
                    <q-item>
                        <q-btn class="tw-ml-1" text-color="text-primary" unelevated outline icon="camera_enhance"
                            label="Найти по фото" @click="op = true"></q-btn>
                    </q-item>
                </q-list>
            </q-btn-dropdown>
            <div v-else>
                <q-btn color=" white" text-color="black" unelevated outline icon="add" label="Добавить"
                    @click="op = true"></q-btn>

                <q-btn class="tw-ml-1" text-color="text-primary" unelevated outline icon="camera_enhance" label="Найти"
                    @click="op = true"></q-btn>

            </div>
            <WPopUpSearch v-model="op" headerTitle="Search with photo" :categoryOptions="['a', 'b', 'c']"
                v-model:category="category" v-model:description="desc" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { computed, ref } from 'vue';
import WPopUpSearch from 'src/widgets/WPopUpSearch.vue';

const op = ref(false);
const category = ref('');
const desc = ref('');
const $q = useQuasar();

const isMobile = computed(() => $q.screen.lt.md);

const text = ref('');
const loadingState = ref(false);
</script>