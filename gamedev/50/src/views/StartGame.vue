<template>
<a-row type="flex" justify="center" v-if="isLoaded">
  <a-col :span="24">
      <div class="box profile">
        <a-row class="title-profile">
          <a-col :span="8">
            <a-avatar :size="96" :src="this.profileUser.pic" />
          </a-col>
          <a-col :span="16" class="mini-rating">
            <div style="font-size: 20pt">Имя: {{profileUser.names}}</div>
            <div style="font-size: 20pt">Игр сыграно: {{profileUser.count_game}}</div>
            <div style="font-size: 20pt">Максимально дней: {{profileUser.max_point}}</div>
          </a-col>
        </a-row>
        <div class="button-group">
          <a-button @click="toChoicePers" block>Начать игру</a-button>
          <a-button v-if="profileUser.continue" @click="toGame" block>Продолжить игру</a-button>
          <a-button @click="toRating" block>Рейтинг</a-button>
          <a-button @click="toMain" block>Выход</a-button>
        </div>

        <div class="person-list" v-if="profileUser.game_history && profileUser.game_history.length !== 0">
          <h1 block>История игр</h1>
          <div v-for="item in profileUser.game_history" style="border: 1px solid black;">
            <a-row>
              <a-col :span="4">
                <img :src="item.pic" height="60" width="60" style="margin-top: 5px;"/>
                <h3>{{item.name}}</h3>
              </a-col>
              <a-col :span="20">
                <table width="100%" border="1">
                  <tr>
                    <th>Информационное здоровье</th>
                    <th>Деньги</th>
                    <th>Очки</th>
                    <th>Прожито дней</th>
                  </tr>
                  <tr>
                    <td>{{item.health}}</td>
                    <td>{{item.money}}₽</td>
                    <td>{{item.point}}</td>
                    <td>{{item.round}}</td>
                  </tr>
                </table>
              </a-col>
            </a-row>
          </div>

        </div>
      </div>
  </a-col>
</a-row>
</template>

<script>
  import {getPerson, getProfile} from "../api/auth";
  import { getGame } from "@/api/game"
  import LineChart from '../store/LineChart.js'
export default {
    components: {
      LineChart,
    },
  data() {
    return {
      newGame: Boolean,
      isLoaded: false,
      persons: [],
      profileUser: undefined,
      progress: null,
    }
  },
  methods: {
    toGame () {
      this.$router.push({ path: '/game', query: { type: 'resume' } })
    },
    toChoicePers: function() {
      this.$router.push('/choice')
    },
    toRating: function() {
      this.$router.push('/rating');
    },
    toMain: function() {
      localStorage.removeItem('session');
      this.$router.push('/');
    },
    getMyProfile: function () {
      // получение информации о пользователе
      let profile = getProfile()
      console.log(profile);
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser)
          var tmpArr = [];
          if (val.game_history && val.game_history > 0) {
            val.game_history.forEach(param => {
              tmpArr.push({
                data: [param.round, param.round],
                backgroundColor: '#1b68b3'
              });
            });
          }
          Chart.defaults.global.legend.display = false;
          this.progress = {
            datasets: tmpArr
          };
        });
      } else {
        this.$message.error('Ошибка получения профиля');
      }
    },
    getAllPerson: function () {
      // получение всех персонажей
      let res = getPerson()
      if (res !== false) {
        res.then(val => {
          this.persons = val;
          console.log("Персонажи: ", this.persons);
        });
      } else {
        this.$message.error('Ошибка получения персонажей');
      }
    }
  },
  mounted() {
    this.getMyProfile();
    this.getAllPerson();
    this.isLoaded = true;
  },
};
</script>
<style>
.profile .button-group {
  margin-top: 20px;
}
.profile .button-group button{
  margin-top: 5px;
  font-size: 20pt;
  height: 55px;
}
.mini-rating {
  margin-top: 10px;
}
.mini-rating div {
  text-decoration: underline;
  font-size: 16px;
  text-align: left;
}
.title-profile {

}
.ant-avatar {
  background: #ad768f;
  border: 1px #440522 solid;
}
#components-form .form {
  max-width: 300px;
}
#components-form .form-button {
  width: 100%;
}
.person-list {
  margin-top: 20px;
}
</style>
