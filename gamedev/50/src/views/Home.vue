<template>
  <a-row type="flex" justify="center">
    <a-col :span="35">
      <div class="box">
        <img alt="Vue logo" src="../assets/logo_life.png" width="90%" style="margin-top: 50px;">
        <h1 style="margin-top: 50px; margin-bottom: 50px; font-size: 32pt;">Добро пожаловать в "Интернет"!</h1>
        <a-button type="primary" class="start-button" v-on:click="toAuth" style="margin-bottom: 50px; height: 75px; font-size: 20pt;">
          Подключиться
        </a-button>
      </div>
    </a-col>
  </a-row>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
// import aituBridge from '@btsd/aitu-bridge';
// import {authUser, registerUser} from "../api/auth";

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  methods: {
    toAuth(e) {
      this.$router.push('/auth')
    }
    // async toAuth(e) {
    //   try {
    //     const profile = await aituBridge.getMe();
    //     if (profile.name !== undefined) {
    //       let login = profile.name + " " + profile.lastname;
    //       let password = profile.id;
    //       let res = await registerUser({"login": login, "password": password})
    //       if (res.error === undefined) {
    //         console.log(res);
    //         localStorage.setItem('session', res.session);
    //         await this.$router.push('/start')
    //       } else {
    //         // this.$message.error('Пользователь с таким именем уже существует');
    //
    //         let res = await authUser({"login": login, "password": password})
    //         if (res.error) {
    //           return
    //         }
    //         if (res !== false) {
    //           localStorage.setItem('session', res.session)
    //           await this.$router.push('/start')
    //         }
    //       }
    //     } else {
    //       await this.$router.push('/auth')
    //     }
    //   } catch (e) {
    //     console.log(e);
    //     await this.$router.push('/start')
    //   }
    // },
  },
}
</script>
