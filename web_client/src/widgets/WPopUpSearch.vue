<script setup lang="ts">
import CPopUp from 'src/components/CPopUp.vue';
import CUploadImage from 'src/components/CUploadImage.vue';
import { useQuasar } from 'quasar';
import { useSerchArtObjectStore } from 'src/stores/SearchArtObjectStore';
// import { computed } from 'vue';

const $q = useQuasar();
const isVisible = defineModel<boolean>({ default: false });
const imageModel = defineModel<File>('imageModel');
const selectedCategory = defineModel<string>('category', { default: '' });
const { uploadImage } = useSerchArtObjectStore();

const upload = async (value: unknown) => {
    try {
        if (!value) return;
        await uploadImage();
        $q.notify({
            message: 'Изображение загружено',
            color: 'positive',
            position: 'bottom',
        });
    } catch (error) {
        $q.notify({
            message: 'Ошибка загрузки изображения',
            color: 'negative',
            position: 'bottom',
        });
    }
}

const reset = () => {
    imageModel.value = undefined;
    selectedCategory.value = '';
};

// const isSendDisabled = computed(() => !imageModel.value || !selectedCategory.value);

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
                <div class="column tw-pb-4">
                    <CUploadImage v-model:image-model="imageModel" v-on:update:imageModel="upload" />
                </div>
                <div class="column tw-pb-4">
                    <q-select outlined v-model="selectedCategory" :options="categoryOptions" label="Категория" />
                </div>
            </div>
        </template>
        <template v-slot:footer>
            <div class="row justify-start tw-p-8">
                <q-btn label="Найти" color="primary" @click="isVisible = false" outline />
                <q-btn class="tw-mx-2" label="Сбросить" color="negative" @click="reset" />
            </div>
        </template>
    </CPopUp>
</template>