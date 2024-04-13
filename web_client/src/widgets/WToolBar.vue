<template>
    <div class="tw-w-full tw-flex tw-flex-row tw-items-end tw-h-full tw-container tw-m-auto">
        <div class="tw-basis-5/7 tw-flex tw-items-center">
            <q-input class="tw-w-2/3 tw-mr-8" v-model="titleSearchModel" label="Поиск по названию...">
                <template v-slot:append>
                    <q-icon v-if="titleSearchModel === ''" name="search" />
                    <q-icon v-else name="clear" class="cursor-pointer" @click="titleSearchModel = ''" />
                </template>
            </q-input>
            <q-avatar class="overlapping" v-if="imageSearchUrl">
                <img :src="imageSearchUrl">
            </q-avatar>
            <q-chip v-if="categorySearchModel" removable v-on:remove="() => categorySearchModel = ''">
                {{ categorySearchModel }}
            </q-chip>
            <!-- </div> -->
        </div>
        <div class="tw-basis-2/7 tw-flex tw-justify-end">
            <q-btn-dropdown v-if="isMobile" stretch flat outline icon="search">
                <q-list>
                    <q-item-label header>Поиск</q-item-label>
                    <q-item>
                        <q-btn color="white" text-color="black" unelevated outline icon="add" label="Добавить фото"
                            @click="isAddOpen = true"></q-btn>
                    </q-item>
                    <q-item>
                        <q-btn class="tw-ml-1" text-color="text-primary" unelevated outline icon="camera_enhance"
                            label="Найти по фото" @click="isSearchOpen = true"></q-btn>
                    </q-item>
                </q-list>
            </q-btn-dropdown>
            <div v-else>
                <q-btn color=" white" text-color="black" unelevated outline icon="add" label="Добавить"
                    @click="isAddOpen = true"></q-btn>

                <q-btn class="tw-ml-1" text-color="text-primary" unelevated outline icon="camera_enhance" label="Найти"
                    @click="isSearchOpen = true"></q-btn>

            </div>
            <WPopUpSearch v-model="isSearchOpen" headerTitle="Найти по фото" :categoryOptions="categoryOptions"
                v-model:imageModel="imageSearchModel" v-model:category="categorySearchModel" />

            <WPopUpAddPhoto v-model="isAddOpen" headerTitle="Добавить фото" :categoryOptions="categoryOptions"
                v-model:imageModel="imageAddModel" v-model:category="categoryAddModel"
                v-model:description="descriptionAddModel" @submit="console.log('Add Photo')" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar';
import { PropType, computed, ref } from 'vue';
import WPopUpSearch from 'src/widgets/WPopUpSearch.vue';
import WPopUpAddPhoto from 'src/widgets/WPopUpAddPhoto.vue';

const $q = useQuasar();
const isMobile = computed(() => $q.screen.lt.md);

const imageSearchUrl = computed(() =>
    imageSearchModel.value ? URL.createObjectURL(imageSearchModel.value) : '',
);


defineProps({
    categoryOptions: { type: Array as PropType<string[]>, required: true },
});

const imageAddModel = defineModel<File>('imageAddModel');
const categoryAddModel = defineModel<string>('categoryAddModel');
const descriptionAddModel = defineModel<string>('descriptionAddModel');

const imageSearchModel = defineModel<File>('imageSearchModel');
const categorySearchModel = defineModel<string>('categorySearchModel');
const titleSearchModel = defineModel<string>('titleSearchModel');

const isSearchOpen = ref(false);
const isAddOpen = ref(false);
</script>