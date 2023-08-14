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
        <el-avatar :src="bearAvatar" size="large"></el-avatar>
        <el-avatar :src="rabbitAvatar" size="large"></el-avatar>
        <h1>In your whisper, I find the secrets of the universe.</h1>
    </div>

    <el-timeline class="timeline" hollow="true">
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
        <div class="user-info">
            <el-avatar :src="userAvatar" size="large"></el-avatar>
            <div class="user-name">{{ userName }}</div>
        </div>
        <div class="input-section">
            <el-input v-model="inputText" type="textarea" placeholder="Whispering hearts, tangled souls." clearable></el-input>
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
            userAvatar: localStorage.getItem('useravatar')
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
            headers: { 'Content-Type': 'application/json' },
            params: {},
        })
            .then((response) => {
                this.msgs = response.data;
            })
            .catch((error) => {
                console.error(error);
            });
    }
}
</script>

<style scoped>
@import '@/assets/fonts/fonts.css';

/* .timeline_area {
    font-family: 'FangzhengYoumaozai', sans-serif;
} */
.timeline {
    padding: 5em;

    font-size: large;
}

.rabbit-msg {
    left: 50%;
    width: 40%;
    font-family: 'OZJiaotangxiawucha', sans-serif;
}

.bear-msg {
    left: 50%;
    width: 40%;
    font-family: 'FZShaeryingbi', sans-serif;
}

.bear-msg :deep(.el-timeline-item__wrapper) {
    right: 100%;
    padding: 0 19px 0 0;
    text-align: right;
}
</style>