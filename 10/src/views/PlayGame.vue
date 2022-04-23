<template>
    <div class="box">
        <template v-if="statusGame === 0">
            <div class="white_text">
                Вы зарегистрировали {{getUsers.length}} человек<br>
                Из них {{getUsers.length >= 6 ? 2 : 1}} шпион(ов)<br>
            </div>
            <div class="white_text">
                Передавайте телефон по кругу и ознакомтесь со своей ролью
            </div>
            <a-button @click="changeStatus(1)">Начать игру</a-button>
        </template>
        <template v-else-if="statusGame === 1">
            <div class="white_text">
                Передайте телефон игроку - {{actualUser.value}}<br>
                <a-button v-if="!makeShowRole" @click="showRole()">Показать роль</a-button>
                <a-button v-else @click="closeRole()">Скрыть роль</a-button>
                <div :class="makeShowRole ? 'container-open' : 'container' ">
                <div class="flipper">
                    <div class="front">
                        <img :src="require('@/assets/who.png')" style="height: 100%"/>
                    </div>
                    <div class="back">
                        <img :src="actualUser.role === 1 ? require('@/assets/shpion.png') : require('@/assets/cards/'+ actualRound + '.png')" style="height: 100%"/>
                    </div>
                </div>
                </div>
            </div>
        </template>
        <template v-else-if="statusGame === 3">
            <div class="white_text">
                <div v-if="new Date() < actualTimer">
                    Рыба - карась, игра началась !!!
                    <br>
                    Времечко тикает:
                </div>
                <div v-else>
                    Время вышло, вскрываемся
                </div>
                 <br>
                  <br>
                <vue3-flip-countdown v-if="new Date() < actualTimer" :showDays="false" :showHours="false" :labels="{minutes: 'Минуты',seconds: 'Секунды',}" :deadlineDate="actualTimer" />
                <a-button v-else @click="goTo('startGame')">Играть еще раз</a-button>
                
            </div>
        </template>
    </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import store from '@/store'
import bridge from '@vkontakte/vk-bridge';
import router from '@/router'

function randomInteger(min, max) {
  // случайное число от min до (max+1)
  let rand = min + Math.random() * (max + 1 - min);
  return Math.floor(rand);
}

export default defineComponent({
    setup() {
        let statusGame = ref(0)
        let lengthUser = ref(0)
        let activeUsers = ref([])
        let actualUser = ref({})
        let makeShowRole = ref(false)
        let actualRound = ref(randomInteger(1, 20))
        let actualTimer = ref(new Date())
        const nextPlayer = () => {
            if (activeUsers.value.length > 0) {
                const randomInt = randomInteger(0, activeUsers.value.length - 1)
                actualUser.value = activeUsers.value[randomInt]
                activeUsers.value.splice(randomInt, 1)
            } else {
                let d = new Date()
                console.log('1', d)
                d.setMinutes(d.getMinutes() + lengthUser.value)
                console.log(lengthUser.value)
                console.log('2', d)
                actualTimer.value = d
                console.log('33', d)
                console.log('3--',actualTimer.value)
                changeStatus(3)
                setInterval(() => {
                    if(!new Date() < actualTimer.value) {
                        bridge.send("VKWebAppFlashSetLevel", {"level": 1})
                        setTimeout(() => {
                            bridge.send("VKWebAppFlashSetLevel", {"level": 0})
                        }, 3000)
                        setTimeout(() => {
                            bridge.send("VKWebAppFlashSetLevel", {"level": 1})
                        }, 3000)
                        setTimeout(() => {
                            bridge.send("VKWebAppFlashSetLevel", {"level": 0})
                        }, 3000)
                    }
                }, 1000)
            }
        }

        const closeRole = () => {
            makeShowRole.value = false
            setTimeout(() => nextPlayer(), 500)
        }
        
        const goTo = (value) => {
            router.push(value)
        }

        const changeStatus = (value) => {
            statusGame.value = value
            if (value === 1) {
                nextPlayer()
            }
        }

        const showRole = () => {
            makeShowRole.value = true
        }

        return {
            makeShowRole,
            actualUser,
            activeUsers,
            statusGame,
            actualRound,
            actualTimer,
            lengthUser,
            changeStatus,
            showRole,
            nextPlayer,
            goTo,
            closeRole
        }
    },
    computed: {
        getUsers: function() {
            return store.state.users
        }
    },
    mounted() {
        this.activeUsers = this.getUsers
        this.lengthUser = this.getUsers.length
    },
    methods: {

    },
})
</script>

<style scoped>
    .container, container-open {
    text-align: center;
    width: 320px;
    margin: 20px auto;
    -webkit-perspective: 1200;
    perspective: 1200;
    -moz-transform: perspective(1200px);
    -webkit-transform-style: preserve-3d;
    -moz-transform-style: preserve-3d; 
    transform-style: preserve-3d;
    }
    .flipper {
        position: relative;
        width: 320px;
        height: 220px;
        -webkit-transform-style: preserve-3d;
        -moz-transform-style: preserve-3d;
        transform-style: preserve-3d;
        -webkit-transition: .3s linear;
        -moz-transition: .3s linear;
        -o-transition: .3s linear;
        transition: .3s linear;  
    }

    @media (max-width: 900px) {
        .flipper {
            width: 240px;
            height: 155px;
        }
    }
    .front, .back {
    box-sizing: border-box;
    font-family: 'Cabin', sans-serif;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    }
    .front {
    z-index: 2;
    -webkit-transform: rotateY(0deg);
    -moz-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    transform: rotateY(0deg);
    background: white;
    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.1);
    border-bottom: 1px solid #f5f5f5;
    }
    i {
    color: #DCB8B2;
    display: inline-block;
    margin-bottom: 15px;
    }
    h3 {
    font-size: 16px;
    line-height: 20px;
    text-transform: uppercase;
    margin: 0 0 15px;
    }
    p {
    font-size: 14px;
    line-height: 25px;
    }
    .header h3 {
    color: #18191a;
    }
    .front p {
    color: #818285;
    }
    .back {
    -webkit-transform: rotateY(-180deg);
    -moz-transform: rotateY(-180deg);
    -ms-transform: rotateY(-180deg);
    transform: rotateY(-180deg);
    background: #DCB8B2;
    color: white;
    }
    .back h3 {
    position: relative;
    }
    .back h3:after {
    content: "";
    width: 50px;
    height: 1px;
    position: absolute;
    bottom: -10px;
    left: 50%;
    background: white;
    margin-left: -25px;
    }
    .back p {
    padding-top: 15px;
    }
    .container-open .flipper{
        margin: auto;
    -webkit-transform: rotateY(180deg);
    -moz-transform: rotateY(180deg);
    -ms-transform: rotateY(180deg);
    transform: rotateY(180deg);
    }
</style>

<style>
    .flip-clock__slot {
        color: white !important;
        font-size: 24px !important;
    }
</style>