<template>
    <q-infinite-scroll class="tw-container tw-grid tw-grid-cols-1 sm:tw-grid-cols-2 lg:tw-grid-cols-3 tw-gap-4"
        @load="(index, done) => $emit('loadMore', index, done)">
        <template v-slot:loading>
            <div class="tw-absolute tw-bottom-0 tw-w-full tw-items-center tw-justify-center tw-flex">
                <q-spinner-ios size="80px" />
            </div>
        </template>
        <template v-slot:default>
            <q-card v-for="item in items" :key="item.id" @click="$emit('cardClick', item.id)">
                <q-img :src="item.src" alt="Image" class="tw-h-64">
                    <div class="absolute-bottom tw-bg-neutral-800 tw-text-white tw-p-2">
                        {{ item.description }}
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

type Item = {
    id: number;
    src: string;
    description: string;
    tags: string[];
};

const colors = ['primary', 'secondary', 'accent', 'dark'];
const colorsLength = colors.length;

defineEmits<{
    (e: 'loadMore', value: number, done: () => void): void;
    (e: 'cardClick', value: number): void;
}>();

defineProps(
    {
        items: {
            type: Array as PropType<Item[]>,
            required: true,
        },
    },
);
</script>