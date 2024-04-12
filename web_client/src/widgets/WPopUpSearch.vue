<script setup lang="ts">
import CPopUp from 'src/components/CPopUp.vue';
import CUploadImage from 'src/components/CUploadImage.vue';

const isVisible = defineModel<boolean>({ default: false });
const selectedCategory = defineModel<string>('category', { default: '' });
const description = defineModel<string>('description', { default: '' });

defineProps({
    headerTitle: { type: String, required: true },
    categoryOptions: { type: Array, required: true },
});

</script>

<template>
    <CPopUp v-model="isVisible" :width="700">
        <template v-slot:header>
            <div class="row justify-between tw-p-8 tw-border-b tw-border-neutral-200">
                <h3 class="tw-text-neutral-700">
                    {{ headerTitle }}
                </h3>
                <q-icon size="sm" name="close" class="tw-cursor-pointer" @click="isVisible = false" />
            </div>
        </template>
        <template v-slot:default>
            <div class="column tw-p-8">
                <div class="column tw-pb-8">
                    <CUploadImage />
                </div>
                <div class="column tw-pb-8">
                    <q-select outlined v-model="selectedCategory" :options="categoryOptions" label="Category" />
                </div>
                <div class="column">
                    <q-input outlined v-model="description" label="Description" type="textarea" />
                </div>
            </div>
        </template>
        <template v-slot:footer>
            <div class="row justify-start tw-p-8">
                <q-btn label="Save" color="primary" @click="isVisible = false" outline />
                <q-btn class="tw-mx-2" label="Cancel" color="negative" @click="isVisible = false" />
            </div>
        </template>
    </CPopUp>
</template>