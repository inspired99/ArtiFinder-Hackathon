<template>
    <q-infinite-scroll class="tw-container tw-grid tw-grid-cols-1 sm:tw-grid-cols-2 lg:tw-grid-cols-3 tw-gap-4"
        @load="(index, done) => $emit('loadMore', index, done)">
        <template v-slot:loading>
            <div class="tw-absolute tw-bottom-0 tw-w-full tw-items-center tw-justify-center tw-flex">
                <q-spinner-ios size="80px" />
            </div>
        </template>
        <template v-slot:default>
            <q-card v-for="item in items" :key="item.id" @click="$emit('cardClick', item)" class="tw-cursor-pointer">
                <q-img :src="item.imageUrl" alt="Image" class="tw-h-64" loading="lazy" spinner-color="white" fit="contain">
                    <div class="absolute-bottom tw-bg-neutral-800 tw-text-white tw-p-2">
                        {{ item.title }}
                        <q-badge rounded class="tw-mx-0.5" v-for="(tag, index) in item.tags" :key="tag"
                            :color="colors[index % colorsLength]" :label="tag" />
                    </div>
                </q-img>
            </q-card>
        </template>
    </q-infinite-scroll>
</template>

<script setup lang="ts">
import { PropType } from 'vue';
import { ArtItemT } from 'src/entities/ArtItem';
import { colors } from 'src/utils/Colors';

const colorsLength = colors.length;

defineEmits<{
    (e: 'loadMore', value: number, done: () => void): void;
    (e: 'cardClick', value: ArtItemT): void;
}>();

defineProps(
    {
        items: {
            type: Array as PropType<ArtItemT[]>,
            required: true,
        },
    },
);
</script>