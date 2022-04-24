<template>
<a-row type="flex" justify="center" v-if="isLoaded">
  <a-col :span="24">
      <div class="box">
        <h2 style="font-size: 28pt;">Рейтинг</h2>
        <div class="button-group">
          <a-button block v-on:click="toProfile()" style="font-size: 16pt; height: 60px">Вернуться в профиль</a-button>
        </div>
        <div class="rating-list">
          <table width="100%" border="1"  style="margin-top: 15px;">
            <tr>
              <th>№</th>
              <th><a-icon slot="prefix" type="qq" title="Персонаж" /></th>
              <th><a-icon slot="prefix" type="user" title="Логин" /></th>
              <th><a-icon slot="prefix" type="dashboard" title="Информационное здоровь" /></th>
              <th><a-icon slot="prefix" type="dollar" title="Деньги" /></th>
              <th><a-icon slot="prefix" type="retweet" title="Количество раундов" /></th>
              <th><a-icon slot="prefix" type="star" title="Очков" /></th>
            </tr>
            <tr v-for="(item, index) in this.rating">
              <template v-if="index < 20">
                <td>
                  <img src="../assets/cup1.png" v-if="index === 0" style="width: 24px; margin: 3px;" />
                  <img src="../assets/cup2.png" v-else-if="index === 1" style="width: 24px; margin: 3px;" />
                  <img src="../assets/cup3.png" v-else-if="index === 2" style="width: 24px; margin: 3px;" />
                  <template v-else>{{item.id}}</template>
                </td>
                <td><a-avatar :size="64" :src="item.person_pic" /></td>
                <td @click.prevent="showPersonInfo(item)"><b style="cursor: pointer; text-decoration: underline;">{{item.user_name}}</b></td>
                <td>{{item.health}}</td>
                <td>{{item.money}}</td>
                <td>{{item.round}}</td>
                <td>{{item.point}}</td>
              </template>
              <template v-else-if="rating.length === 25 && index === 20">
                <td>...</td>
                <td></td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
                <td>...</td>
              </template>
              <template v-else-if="item.user_name === profileUser.names">
                <td style="background: #1b68b380;">{{item.id}}</td>
                <td style="background: #1b68b380;"><a-avatar :size="64" :src="item.person_pic" /></td>
                <td style="background: #1b68b380;" @click.prevent="showPersonInfo(item)"><b style="cursor: pointer; text-decoration: underline;">{{item.user_name}}</b></td>
                <td style="background: #1b68b380;">{{item.health}}</td>
                <td style="background: #1b68b380;">{{item.money}}</td>
                <td style="background: #1b68b380;">{{item.round}}</td>
                <td style="background: #1b68b380;">{{item.point}}</td>
              </template>
              <template v-else>
                <td>{{item.id}}</td>
                <td><a-avatar :size="64" :src="item.person_pic" /></td>
                <td @click.prevent="showPersonInfo(item)"><b style="cursor: pointer; text-decoration: underline;">{{item.user_name}}</b></td>
                <td>{{item.health}}</td>
                <td>{{item.money}}</td>
                <td>{{item.round}}</td>
                <td>{{item.point}}</td>
              </template>
            </tr>
          </table>
        </div>
      </div>
    <div class="selectProfileModal" v-if="showModalOne">
      <div class="selectProfileModalTitle">{{selectPerson.name}}</div>
      <div class="selectProfileModalBody">
        <a-row class="title-profile">
          <a-col :span="8">
            <a-avatar :size="128" :src="this.selectPerson.pic" />
          </a-col>
          <a-col :span="16" class="mini-rating">
            <div>Имя: {{selectPerson.names}}</div>
            <div>Игры сыграно: {{selectPerson.count_game}}</div>
            <div>Максимально прожито дней: {{selectPerson.max_point}}</div>
          </a-col>
        </a-row>

        <div class="person-list">
          <h1 block>История игр</h1>
          <div v-for="item in this.selectPerson.game_history" style="border: 1px solid black;">
            <table width="100%" border="1">
              <tr>
                <th>Здоровье</th>
                <th>Очки</th>
              </tr>
              <tr>
                <td>{{item.health}}</td>
                <td>{{item.point}}</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
      <div class="selectProfileModalFooter">
        <button class="btn btn-primary" @click.prevent="showModalOne = !showModalOne">Закрыть</button>
      </div>
    </div>
  </a-col>
</a-row>
</template>

<script>
import {getProfile, getProfileInfo, getRating} from "../api/auth";

export default {
  data() {
    return {
      isLoaded: false,
      rating: [],
      showModalOne: false,
      selectPerson: undefined
    }
  },
  async beforeCreate() {
    // получение рейтинга пользователей
    let res = await getRating()
    if (res !== false) {
      console.log(res);
      this.rating = res.top;
      this.isLoaded = true;
    } else {
      this.$message.error('Ошибка получения персонажей');
    }
  },
  methods: {
    showPersonInfo: function(person) {
      let profile = getProfileInfo(person.id_user)
      if (profile !== false) {
        profile.then(val => {
          this.selectPerson = val;
          if (!this.showModalOne)
            this.showModalOne = !this.showModalOne
          console.log("Выбранный профиль: ", val)
        });
      }
    },
    toProfile: function () {
      this.$router.push('/start');
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
        });
      } else {
        this.$message.error('Ошибка получения профиля');
      }
    },
  },
  mounted() {
    this.getMyProfile();
    this.isLoaded = true;
  },
};
</script>
<style>
.rating-list {
  margin-top: 5px;
}
.selectProfileModal {
  box-shadow: 0px 1px 12px rgba(0, 0, 0, 0.4);
  margin:0 auto;
  position: absolute;
  z-index: 999;
  width: 600px;
  top: 20vh;
  border-radius: 5px;
  overflow: hidden;
}
.selectProfileModal .selectProfileModalTitle {
  background-color: #eee;
  text-align: left;
  padding: 8px 12px;
  font-size: 1.5em;
}
.selectProfileModal .selectProfileModalTitle .close {
  line-height: 32px;
  color: #5c4084;
}
.selectProfileModal .selectProfileModalBody {
  background-color: #fff;
  padding: 8px 12px;
  text-align: left;
  padding: 12px;
}
.selectProfileModal .selectProfileModalFooter {
  background-color: #eee;
  padding: 4px 12px;
  text-align: left;
}
</style>
