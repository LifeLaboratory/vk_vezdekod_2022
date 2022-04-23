import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import 'ant-design-vue/dist/antd.css';
import { Card, Row, Col } from 'ant-design-vue';

const app = createApp(App);

app.use(store).use(router)
app.use(Card)
app.use(Row)
app.use(Col)
app.mount('#app')
