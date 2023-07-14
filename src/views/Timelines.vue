<!--
 * @Author: Alchemistyui
 * @Date: 2023-07-12
 * @LastEditTime: 2023-07-14
 * @FilePath: /RabiBear-Home-Web/src/views/Timelines.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<script lang="ts" setup>
const activities = [
    {
        content: ['05.12 小兔子哭着要回家→回国&见父母'],
        timestamp: '2023',
    },
    {
        content: ['嗷呜嗷呜'],
        timestamp: '2022',
    },
    {
        content: ['01.16 在一起啦啦啦', '07.28 一起住啦'],
        timestamp: '2021',
    },
    {
        content: ['12.05 第一次见面'],
        timestamp: '2020',
    },
]
</script>

<template>
    <el-timeline class="timeline" hollow="true">
        <!-- 循环判断索引的奇偶区分开左右 -->
        <el-timeline-item v-for="(activity, index) in activities" :key="index"
            :class="index % 2 === 0 ? 'timeline-left' : 'timeline-right'" :timestamp="activity.timestamp" placement="top">
            <el-card>
                <!-- <h4>{{ activity.timestamp }}</h4> -->
                <p v-for="item in activity.content">{{ item }}</p>
            </el-card>
        </el-timeline-item>
    </el-timeline>
</template>

<style scoped>
@import '@/assets/fonts/fonts.css';
/* .timeline_area {
    font-family: 'FangzhengYoumaozai', sans-serif;
} */
.timeline {
    padding: 50px;
    font-family: 'FZShaeryingbi', sans-serif;
    font-size: large;
}
.timeline-right {
    left: 50%;
    width: 40%;
}
.timeline-left {
    left: 50%;
    width: 40%;
}
.timeline-left :deep(.el-timeline-item__wrapper) {
    right: 100%;
    padding: 0 19px 0 0;
    text-align: right;
}
</style>