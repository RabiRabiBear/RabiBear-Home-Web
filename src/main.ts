/*
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2023-04-27
 * @FilePath: /RabiBear-Home-Web/src/main.ts
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
 */
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store.js'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import ActivityCalendar from "vue-activity-calendar";
import "vue-activity-calendar/style.css"; 
 

import './assets/main.css'


const app = createApp(App)

app.use(router)
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.use(ActivityCalendar)
app.use(store)

app.mount('#app')
