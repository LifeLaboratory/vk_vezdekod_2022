import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import 'ant-design-vue/dist/antd.css';
import 'ant-design-vue/es/message/style/css'
import { Card, Row, Col, Button, Input, Form } from 'ant-design-vue';
import VueCountdown from '@chenfengyuan/vue-countdown';
import Countdown from 'vue3-flip-countdown'
import connect from '@vkontakte/vkui-connect';
connect.send('VKWebAppInit', {});

const app = createApp(App);

app.use(store).use(router)
app.use(Card)
app.use(Button)
app.use(Row)
app.use(VueCountdown.name, VueCountdown)
app.use(Countdown)
app.use(Form)
app.use(Input)
app.use(Col)
app.mount('#app')
        
