<template>
    <div class="box">
        <div class="white_text">
            Добро пожаловать в игру! <br/>
            Ознакомтесь с локациями в игре:
        </div>
        <a-row :gutter="[16,16]" type="flex" justify="center" align="top">
            <a-col v-for="(el, key) in 10" :key=key>
                <a-card hoverable style="width: 340px">
                    <template #cover>
                        <img alt="card1" :src="require('@/assets/cards/'+el+'.png')" />
                    </template>
                </a-card>
            </a-col>
        </a-row>
    </div>
</template>

<style scoped>
    .white_text {
        font-family: 'Courier New', Courier, monospace;
        font-weight: 600;
        color: white;
        padding-bottom: 20px;
        font-size: 35px;
    }
</style>

<style>
    .box {
        padding: 50px 0px;
        background: rgba(0, 0, 0, 0.745);
        border-radius: 12px;
        width: 40%;
        height: 100vh;
        overflow-y: auto;
        overflow-x: hidden;
        margin: auto;
    }

    @media (max-width: 900px) {
        .box {
            width: 100%;
        }
    }
</style>