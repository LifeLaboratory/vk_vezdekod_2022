<template>
<a-row type="flex" justify="center">
  <a-col :span="35">
    <div class="box">
      <h2 style="font-size: 20pt;">Авторизация</h2>
        <a-form
          id="components-form"
          :form="form"
          class="form"
          @submit="handleSubmit"
        >
          <a-form-item>
            <a-input
              v-decorator="[
                'login',
                { rules: [{ required: true, message: 'Введите имя!' }] },
              ]"
              placeholder="Username"
              style="font-size: 20pt; height: 60px"
            >
              <a-icon slot="prefix" type="user" style="color: rgba(0,0,0,.25);" />
            </a-input>
          </a-form-item>
          <a-form-item>
            <a-input
              v-decorator="[
                'password',
                { rules: [{ required: true, message: 'Введите пароль!' }] },
              ]"
              type="password"
              placeholder="Password"
              style="font-size: 20pt; height: 60px"
            >
              <a-icon slot="prefix" type="lock" style="color: rgba(0,0,0,.25)" />
            </a-input>
          </a-form-item>
          <a-form-item style="font-size: 20pt;">
            <a-button type="primary" html-type="submit" class="form-button" style="margin-bottom: 15px;">
              Вход
            </a-button>
            или
            <router-link to="/reg" style="color: #5a0000;">
              Зарегистрироваться
            </router-link>
          </a-form-item>
        </a-form>
      </div>
    </a-col>
</a-row>
</template>

<script>
import {authUser, getProfile} from "../api/auth";

export default {
  beforeCreate() {
    this.form = this.$form.createForm(this, { name: 'normal_login' });
  },
  methods: {
    handleSubmit(e) {
      e.preventDefault();
      this.form.validateFields( async (err, values) => {
        if (!err) {
          console.log('Received values of form: ', values);
          let res = await authUser(values)
          if (res.error) {
            this.$message.error(res.error);
            return
          }
          if (res !== false) {
            localStorage.setItem('session', res.session)
            this.$router.push('/start')
          } else {
            this.$message.error("Пользователь с таким именем и паролем не существует");
          }
        }
      });
    },
  },
  mounted() {
    if (localStorage.getItem('session') !== null) {
      let profile = getProfile()
      if (profile !== false) {
        this.profileUser = profile;
        profile.then(val => {
          this.profileUser = val
          console.log("Профиль: ", this.profileUser);
          if (this.profileUser !== false) {
            this.$router.push('/start')
          }
        });
      }
    }
  },
};
</script>
<style>
#components-form .form {
  max-width: 300px;
}
#components-form .form-button {
  width: 100%;
  font-size: 28pt;
  height: 75px;
}
.ant-input-affix-wrapper .ant-input:not(:first-child) {
  padding-left: 50px;
}
</style>
