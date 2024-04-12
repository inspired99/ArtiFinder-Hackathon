<script setup lang="ts">
import { computed, ref } from 'vue';
import { QFile } from 'quasar';

const quasarFilePickerRef = ref<InstanceType<typeof QFile> | null>(null);

const imageModel = defineModel<File>();
const imageURL = computed(() =>
    imageModel.value ? URL.createObjectURL(imageModel.value) : '',
);
</script>

<template>
    <div class="upload-image-container column">
        <div class="column justify-center items-center w-full">
            <q-icon v-if="imageModel === undefined" name="image" size="100px" />
            <div v-else class="uploaded-image-area row justify-between">
                <div class="row">
                    <q-avatar square size="100px">
                        <img :src="imageURL" alt="uploaded image" style="width: 100%; height: 100%" />
                    </q-avatar>
                    <div class="column tw-ml-4">
                        <p class="tw-text-neutral-600 sub-2-medium">
                            {{
                imageModel.name.length > 50
                    ? imageModel.name.slice(0, 30) +
                    '...' +
                    imageModel.type.split('/')[1]
                    : imageModel.name
            }}
                        </p>
                        <p class="tw-text-neutral-600 sub-3-medium">
                            {{ (imageModel.size * 0.000001).toFixed(2) }} MB
                        </p>
                    </div>
                </div>
                <q-icon name="close" class="tw-cursor-pointer" @click="imageModel = undefined" />
            </div>
            <p class="tw-mt-5 sub-4-medium tw-text-neutral-600">
                Drag and drop your image here or
            </p>
            <q-file style="display: none" ref="quasarFilePickerRef" v-model="imageModel" accept=".jpg, .png, .jpeg" />
            <q-btn v-if="imageModel === undefined" label="Upload file" @click="quasarFilePickerRef!.pickFiles()"
                icon="cloud_upload" />
            <div v-else class="row justify-center items-center">
                <q-btn @click="quasarFilePickerRef!.pickFiles()" unelevated label="Change" />
                <q-btn @click="imageModel = undefined" color="warning" shape="outline" label="Remove" />
            </div>
        </div>
        <p style="letter-spacing: 0.2px; text-align: center">
            Maximum file size: 5MB
        </p>
    </div>
</template>

<style scoped lang="scss">
.upload-image-container {
    padding: 48px 32px;
    justify-content: center;
    align-items: center;
    align-self: stretch;
    border-radius: 8px;
    border: 1px dashed #CACDD7;
    background: #FEFFFF;
    cursor: pointer;
}

.uploaded-image-area {
    border-radius: 8px;
    border: 1px solid #E5E6EB;
    padding: 16px;
}

.upload-image-container:hover {
    border: 1px dashed #007BFF;
}
</style>
