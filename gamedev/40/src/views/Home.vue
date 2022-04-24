<template>
  <div class="home">
    <a-modal v-model:visible="visible" title="Вы сгорели в лаве(" @cancel="handleOk" @ok="handleOk">
      <p>Печалька</p>
      <p>Попробуем еще раз?</p>
    </a-modal>
    <div class="rows">
      <div class="left">
        <img @click="makeScore(-10)" style="z-index: 99999" :src="require('@/assets/arrow.png')" />
      </div>
      <div class="right">
        <img @click="makeScore(10)"  style="z-index: 99999" :src="require('@/assets/arrow.png')" />
      </div>
    </div>
    <div class="body">
      <div ref="board" class="board">
        <div class="pepopleimg"  >
          <img :src="require('@/assets/people.svg')" ref="down" style="height: 300px; margin-top: -70px"/>
        </div>
        <img :src="require('@/assets/balance.png')"  style="height: 300px"  class="balanceimg" />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, reactive } from 'vue'
import router from '@/router'

function getRandomInt(max) {
  var pos = max,
    neg = max,
    result;

    result = Math.floor(Math.random() * (pos + neg)) - neg;
    result = result < 0 ? result : result + 1;
    return result
}

export default defineComponent({
  setup() {
    let value = ref('');
    let actual = ref(0);
    let defaultValue = ref(0);
    let level = ref(0.1);
    let rand = ref(10);
    const visible = ref(false);

    const radioStyle = reactive({
      display: 'flex',
      height: '30px',
      lineHeight: '30px',
    });

    const showModal = () => {
      visible.value = true;
    };

    const handleOk = () => {
      router.push('/')
      visible.value = false;
    };

    const makeScore = (value) => {
      defaultValue.value = defaultValue.value + value
    }

    setInterval(() => {
      defaultValue.value = defaultValue.value + level.value * Math.sign(actual.value)
    }, 100)

    setInterval(() => {
      level.value = level.value + 0.1
    }, 1000)

    actual.value = getRandomInt(rand.value)
    defaultValue.value = actual.value

    return {
      rand,
      handleOk,
      radioStyle,
      level,
      defaultValue,
      value,
      visible,
      actual,
      showModal,
      makeScore
    }
  },
  mounted() {
    setInterval(() => {
      console.log(this.defaultValue)
      if (this.defaultValue > 90) {
        this.$refs.down.style.transform = 'translate(2000px,0)'
        this.showModal()
      } else if (this.defaultValue < -90) {
        this.$refs.down.style.transform = 'translate(-2000px,0)'
        this.showModal()
      } else {
        this.$refs.board.style.transform = 'rotate3d(0, 0, 1, ' + this.defaultValue +'deg)'
      }
      // let i = 0
      // if (Math.sign(this.defaultValue) < 0 ) {
      //   i = this.defaultValue * 2
      // }

      // this.$refs.pople.style.transform = 'rotate3d(0, 0, 1, ' + this.defaultValue +'deg) translate(0px, -'+ i +');'
    },1000)
  }
})
</script>


<style scoped>
* {
  transition: 3s;
}
  .left img{
    left: 25px;
    position: absolute;
    width: 60px;
    transform: scale(-1, 1);
    top: calc(50% - 30px)
  }

  .right img{
    right: 25px;
    position: absolute;
    width: 60px;
    top: calc(50% - 30px)
  }

  img:hover {
    cursor: pointer;
  }
  .body {

  }
  .board {
    transform: rotate3d(0, 0, 1, 0deg);
    position: relative;
    transition: 3s;
    margin-top: 200px;
  }
  .pople {
    margin-top: -80px;
    height: 40px;
    left: calc(50% - 20px);
    position: absolute;
    height: 300px;
    transform-origin: 100px 100px;
    transition: 3s;
  }
  
  .pepopleimg {
    height: 20px;
  }
</style>


