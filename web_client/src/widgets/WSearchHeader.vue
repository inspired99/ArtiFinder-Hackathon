<template>
    <div>
        <div class="row justify-between tw-bg-white tw-sticky tw-top-4 tw-z-10 tw-opacity-100">
            <q-input v-model="text">
                <template v-slot:prepend>
                    <q-icon name="event" />
                </template>
            </q-input>
            <div class="row justify-between">
                <q-btn text-color="text-primary" unelevated icon="camera_enhance" label="Search with photo"
                    @click="op = true" />
                <!-- reset filter button -->
                <q-btn unelevated icon="clear" />
            </div>
            <WPopUpSearch v-model="op" headerTitle="Search with photo" :categoryOptions="['a', 'b', 'c']"
                v-model:category="category" v-model:description="desc" />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import WPopUpSearch from 'src/widgets/WPopUpSearch.vue';

const text = ref('');
const op = ref(false);
const category = ref('');
const desc = ref('');
</script>