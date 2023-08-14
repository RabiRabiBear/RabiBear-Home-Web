<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2023-08-14
 * @FilePath: /RabiBear-Home-Web/src/views/Whisper.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<template>

    <div class="title">
        <el-avatar :src="bearAvatar" :size="70"></el-avatar>
        <img class="pixel_heart" src="../assets/imgs/pixel_heart.png" />
        <el-avatar :src="rabbitAvatar" :size="70"></el-avatar>
        <h1>In your whisper, I find the secrets of the universe.</h1>
    </div>

    <el-timeline class="timeline">
        <!-- 循环判断索引的奇偶区分开左右 -->
        <el-timeline-item v-for="(msg, index) in this.msgs" :key="index"
            :class="msg.author === 'rabbit' ? 'rabbit-msg' : 'bear-msg'" :timestamp="msg.timestamp" placement="top">
            <!-- <el-card> -->
            <!-- <h4>{{ activity.timestamp }}</h4> -->
            <p>{{ msg.content }}</p>
            <!-- </el-card> -->
        </el-timeline-item>
    </el-timeline>

    <div class="input-zone">
        <div class="user-info" style="margin-right: 1em; margin-top: -0.5em;">
            <el-avatar :src="userAvatar" :size="50"></el-avatar>
            <div class="user-name" style="margin-top: -0.5em;">{{ userName }}</div>
        </div>
        <div class="input-section">
            <el-input v-model="inputText" type="textarea" :rows="3" placeholder="Whispering hearts, tangled souls." clearable class="custom-input"></el-input>
            <el-button type="primary" @click="submitMessage">Submit</el-button>
        </div>
    </div>
</template>


<script>
import Cookies from 'js-cookie';
import { ref } from 'vue';
import axios from "axios";
import { API_BASE_URL } from '@/config.js';

export default {
    data() {
        return {
            msgs: [],
            userName: ref(Cookies.get('username')),
            inputText: '',
            userAvatar: localStorage.getItem('useravatar'),
            bearAvatar: '',
            rabbitAvatar: '',
            // bearAvatar: axios.get(`${API_BASE_URL}/get_avatar/bear`).then(res => res.data),
            // rabbitAvatar: axios.get(`${API_BASE_URL}/get_avatar/rabbit`).then(res => res.data),
        }
    },
    methods: {
        async submitMessage() {
            if (this.inputText.trim() !== '') {
                const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone.split('/')[1];
                // const now = new Date();
                // const formatter = new Intl.DateTimeFormat('en', {
                //     year: '2-digit',
                //     month: '2-digit',
                //     day: '2-digit',
                //     hour: '2-digit',
                //     minute: '2-digit',
                // });

                // const currentTime = formatter.format(now);

                const now = new Date();
                const year = now.getFullYear().toString().slice(-2); // 获取年份的后两位
                const month = String(now.getMonth() + 1).padStart(2, '0'); // 月份从0开始计数，需要加1
                const day = String(now.getDate()).padStart(2, '0');
                const hours = String(now.getHours()).padStart(2, '0');
                const minutes = String(now.getMinutes()).padStart(2, '0');

                const formattedTime = `${year}-${month}-${day} ${hours}:${minutes} ${userTimeZone}`;
                console.log(formattedTime);

                const data = {
                    author: this.userName,
                    content: this.inputText,
                    timestamp: formattedTime,
                }

                try {
                    const response = await axios.post(`${API_BASE_URL}/update_whisper`, data);
                    this.msgs.unshift({
                        author: this.userName,
                        content: this.inputText,
                        timestamp: formattedTime,
                    });
                    this.inputText = '';
                } catch (error) {
                    console.error('Error submitting message:', error);
                }
            }
        },
    },
    created() {
        axios.get(`${API_BASE_URL}/get_whisper`, {
            params: {},
        })
            .then((response) => {
                this.msgs = response.data;
            })
            .catch((error) => {
                console.error(error);
            });


        axios.get(`${API_BASE_URL}/get_avatar`, {
            params: {user_name: ['bear', 'rabbit']},
        })
            .then((response) => {
                this.bearAvatar = `data:image/png;base64,${response.data['bear']}`;
                this.rabbitAvatar = `data:image/png;base64,${response.data['rabbit']}`;
                
            })
            .catch((error) => {
                console.error(error);
            });
    }
}
</script>

<style scoped>
@import '@/assets/fonts/fonts.css';

.timeline {
    font-size: large;
}

.rabbit-msg {
    left: 48%;
    width: 40%;
    font-family: 'OZJiaotangxiawucha', sans-serif;
}

.bear-msg {
    left: 48%;
    width: 40%;
    font-family: 'FZShaeryingbi', sans-serif;
}

.bear-msg :deep(.el-timeline-item__wrapper) {
    right: 100%;
    padding: 0 19px 0 0;
    text-align: right;
}

.pixel_heart {
    width: 3em;
    
    margin: 0 3em;
    padding-bottom: 0.7em;
    
}

.title {
    text-align: center;
    font-family: 'OZJiaotangxiawucha', sans-serif;
    margin: 3em 0;
}

.input-zone {
    display: flex;
    justify-content: center;
    /* align-items: center; */
    margin: 3em 0;
    text-align: center;
    font-family: 'FZShaeryingbi', sans-serif;
}

</style>
