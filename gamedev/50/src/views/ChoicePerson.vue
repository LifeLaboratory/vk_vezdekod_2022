<template>
<a-row type="flex" justify="center">
  <a-col :span="24">
      <div class="box">
         <h1>Выберите персонажа</h1>
        <a-row>
         <a-col :span="24"  :gutter="10" v-for="(el, key) in profile">
          <a-card hoverable @click="selectPerson(el.id_person)" style="height:320px; width: 90%; margin-left: 5%; margin-top: 25px;">

            <img
              alt="example"
              :src="el.pic"
              style="height: 100px"
            /><br />
            <a-card-meta :title="el.name" style="height: 80px;">
              <template slot="description">{{el.description}}</template>
            </a-card-meta>
            <div style="text-align: left; margin-top: 5px;">
                <div>Информационное здоровье: {{el.health}}</div>
                <div>Деньги: {{el.money}}₽</div>
            </div>
          </a-card>
         </a-col>
        </a-row>
      </div>

  </a-col>
</a-row>
</template>

<script>
import { getPerson } from "@/api/auth"

export default {
  data() {
    return {
        profile: Array
    }
  },
  methods: {
    selectPerson(key) {
        this.$router.push({ path: 'game', query: { id: key } })
    }
  },

  created: async function () {
    let res = await getPerson()
    console.log(res);
    this.profile = res 
  }
};
</script>
<style>

.ant-card:hover {
    border: solid 1px #ccc;
    background: #e2e0e0;
}

</style>
