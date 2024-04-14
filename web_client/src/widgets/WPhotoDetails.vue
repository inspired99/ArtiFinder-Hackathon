<script setup lang="ts">
import { PropType } from 'vue';
import CPopUp from 'src/components/CPopUp.vue';
import { ArtItemT } from 'src/entities/ArtItem';
// import { colors } from 'src/utils/Colors';

const isVisible = defineModel<boolean>({ default: false });
// const colorsLength = colors.length;

defineProps({
    artItem: { type: Object as PropType<ArtItemT>, required: true },
});

</script>

<template>
    <CPopUp position="standard" v-model="isVisible" :width="500">
        <template v-slot:default>
            <div class="column">
                <q-card flat bordered>
                    <q-img :src="artItem.imageUrl" />

                    <q-card-section>
                        <div class="text-h5 q-mt-sm q-mb-xs">{{ artItem.title }}</div>
                        <div class="text-caption text-black">
                            {{ artItem.description }}
                            <q-badge rounded class="tw-mx-0.5" color="primary" :label="artItem.tag" />
                        </div>
                    </q-card-section>

                    <!-- <q-card-actions>
                        <q-btn flat color="primary" label="Share" />
                        <q-btn flat color="secondary" label="Book" />
                    </q-card-actions> -->
                </q-card>
            </div>
        </template>
    </CPopUp>
</template>