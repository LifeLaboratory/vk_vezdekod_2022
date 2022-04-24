<template>
    <a-modal v-model:visible="visible" title="Сбалансируешь или сгоришь ?!!?" @cancel="handleOk" @ok="handleOk">
      <p>Привет!</p>
      <p>Ты на канале Влада А4 и сегодня мы будем играть в баланс или лава</p>
      <p>Правила узнаешь по ходу игры, Поехали!!!!</p>
    </a-modal>
</template>

<script>
import { defineComponent, ref} from 'vue'
import router from '@/router'

export default defineComponent({
    setup() {
        let visible = ref(true)

        const handleOk = () => {
            router.push('/game')
        }
        return {
            visible,
            handleOk
        }
    },
})
</script>
