<script setup lang="ts">
import { computed, PropType } from 'vue';
export type Position =
    | 'standard'
    | 'top'
    | 'right'
    | 'bottom'
    | 'left';

const props = defineProps({
    value: { type: Boolean, default: false },
    seamless: { type: Boolean, default: false },
    position: { type: String as PropType<Position>, default: 'right' },
    width: { type: Number },
    persistent: { type: Boolean, default: false },
});
const model = defineModel<boolean>();
const innerStyle = computed(() => {
    return { width: `${props.width}px` };
});
</script>

<template>
    <q-dialog :seamless="seamless" :position="position" :persistent="persistent" :value="value" v-model="model">
        <div class="popup" style="max-width: 2000px" :style="innerStyle">
            <slot name="header"></slot>
            <slot name="default"></slot>
            <slot name="footer"></slot>
        </div>
    </q-dialog>
</template>

<style scoped lang="scss">
.popup {
    border-radius: 12px;
    box-shadow: 0px 2px 6px 0px rgba(82, 86, 130, 0.14);
    opacity: 1;
    background-color: rgb(254 255 255);
}
</style>
