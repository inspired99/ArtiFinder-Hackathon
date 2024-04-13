<script setup lang="ts">
import CPopUp from 'src/components/CPopUp.vue';
import CUploadImage from 'src/components/CUploadImage.vue';

const isVisible = defineModel<boolean>({ default: false });

const imageModel = defineModel<File>('imageModel');
const description = defineModel<string>('description', { default: '' });
const selectedCategory = defineModel<string>('category', { default: '' });

defineEmits<{
    (e: 'submit'): void;
}>();

defineProps({
    headerTitle: { type: String, required: true },
    categoryOptions: { type: Array, required: true },
});

</script>

<template>
    <CPopUp position="standard" v-model="isVisible" :width="700">
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
                    <CUploadImage v-model="imageModel" />
                </div>
                <div class="column tw-pb-8">
                    <q-select outlined v-model="selectedCategory" :options="categoryOptions" label="Категория" />
                </div>
                <div class="column">
                    <q-input outlined v-model="description" label="Описание" type="textarea" />
                </div>
                <q-btn class="tw-mt-8" label="Сгенерировать" color="primary" @click="$emit('submit')" />
            </div>
        </template>
        <template v-slot:footer>
            <div class="row justify-start tw-p-8">
                <q-btn label="Отправить" color="primary" @click="$emit('submit')" outline />
                <q-btn class="tw-mx-2" label="Отменить" color="negative" @click="isVisible = false" />
            </div>
        </template>
    </CPopUp>
</template>