<template>
    <div class="box">
        <div class="white_text">
            Добро пожаловать в игру! <br/>
            Ознакомтесь с локациями в игре:
        </div>
        <a-button @click="submit" style="margin-bottom: 30px">Начать игру</a-button>
        <a-row :gutter="[16,16]" type="flex" justify="center" align="top">
            <a-col v-for="(el, key) in 10" :key=key>
                <a-card hoverable class="card">
                    <template #cover>
                        <img alt="card1" :src="require('@/assets/cards/'+el+'.png')" />
                    </template>
                </a-card>
            </a-col>
        </a-row>
    </div>
</template>

<script>
import connect from '@vkontakte/vkui-connect';

export default ({
    setup() {
        
    },
    methods: {
        submit() {
            this.$router.push('startGame')
        }
    },
    async mounted() {
        await connect.send("VKWebAppFlashSetLevel", {"level": 1})
    }
})
</script>


<style>
    .white_text {
        font-family: 'Courier New', Courier, monospace;
        font-weight: 600;
        color: white;
        padding-bottom: 20px;
        font-size: 35px;
    }
    .box {
        padding: 50px 0px;
        background: rgba(0, 0, 0, 0.842);
        border-radius: 12px;
        width: 40%;
        height: 100vh;
        overflow-y: auto;
        overflow-x: hidden;
        margin: auto;
    }
    
    .card {
        width: 340px
    }

    @media (max-width: 900px) {
        .box {
            width: 100%;
        }
        .card {
            width: 240px
        }
    }
</style>