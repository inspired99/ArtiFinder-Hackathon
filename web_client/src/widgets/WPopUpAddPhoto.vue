<script setup lang="ts">
import CPopUp from 'src/components/CPopUp.vue';
import CUploadImage from 'src/components/CUploadImage.vue';
import { useAddArtObjectStore } from 'src/stores/AddArtObjectStore';
import { useQuasar } from 'quasar';
import { computed } from 'vue';

const $q = useQuasar();
const isVisible = defineModel<boolean>({ default: false });

const imageModel = defineModel<File>('imageModel');
const description = defineModel<string>('description', { default: '' });
const selectedCategory = defineModel<string>('category', { default: '' });

const { uploadImage, createItem, addItem } = useAddArtObjectStore();

const upload = async (value: unknown) => {
    try {
        if (!value) return;
        await uploadImage();
        $q.notify({
            message: 'Изображение загружено',
            color: 'positive',
            position: 'top',
        });
    } catch (error) {
        $q.notify({
            message: 'Ошибка загрузки изображения',
            color: 'negative',
            position: 'top',
        });
    }
};

const CreateItem = async () => {
    try {
        await createItem();
        $q.notify({
            message: 'Объект добавлен',
            color: 'positive',
            position: 'top',
        });
        reset();
        isVisible.value = false;
    } catch (error) {
        $q.notify({
            message: 'Ошибка добавления объекта',
            color: 'negative',
            position: 'top',
        });
    }
};

const reset = () => {
    imageModel.value = undefined;
    description.value = '';
    selectedCategory.value = '';
    addItem.title = '';
};

const isSendDisabled = computed(() => !imageModel.value || !description.value || !selectedCategory.value || !addItem.title);

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
                <div class="column tw-pb-4">
                    <CUploadImage v-model:imageModel="imageModel" v-on:update:imageModel="upload" />
                </div>
                <q-input class="column tw-pb-4" outlined v-model="addItem.title" label="Название" type="text" />

                <div class="column tw-pb-4">
                    <q-select outlined v-model="selectedCategory" :options="categoryOptions" label="Категория" />
                </div>
                <div class="column tw-pb-4">
                    <q-input outlined v-model="description" label="Описание" type="textarea" />
                </div>
                <q-btn class="tw-mt-8" label="Сгенерировать" color="primary" @click="$emit('submit')" />
            </div>
        </template>
        <template v-slot:footer>
            <div class="row justify-start tw-p-8">
                <q-btn label="Отправить" color="primary" @click="CreateItem" outline :disable="isSendDisabled" />
                <q-btn class="tw-mx-2" label="Сбросить" color="negative" @click="reset" />
            </div>
        </template>
    </CPopUp>
</template>