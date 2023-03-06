<!--
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2023-03-06
 * @FilePath: /RabiBear-Home-Web/src/views/HomeView.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->

<template>
  <main class="card_view">
    <!-- gutter specify the spacing between columns -->
    <!-- span: means that each column will take up 8/24 or one-third of the total width -->
    <el-row :gutter="0">
      <el-col :span="6">
        <el-card shadow="hover"> Hover </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card.png" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover"> Hover </el-card>
    </el-col>
    <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card.png" />
        </el-card>
      </el-col>
  </el-row>
  <el-row>
    <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card.png" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover"> Hover </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card.png" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover"> Hover </el-card>
    </el-col>
  </el-row>
  <!-- <el-row>
      <el-col
        v-for="(o, index) in 2"
        :key="o"
        :span="8"
        :offset="index > 0 ? 2 : 0"
      >
        <el-card :body-style="{ padding: '0px' }">
          <img
            src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
            class="image"
          />
          <div style="padding: 14px">
            <span>Yummy hamburger</span>
            <div class="bottom">
              <time class="time">{{ currentDate }}</time>
              <el-button text class="button">Operating</el-button>
              </div>
            </div>
          </el-card>
        
        </el-col>
      
      </el-row>
      <el-card class="box-card">
            <div v-for="o in 4" :key="o" class="text item">{{ 'List item ' + o }}</div>
          </el-card> -->
  </main>
</template>


<script lang="ts" setup>
import { ref } from 'vue'

const currentDate = ref(new Date())
</script>

<style scoped>
/* .time {
  font-size: 12px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
} */
.card_view {
  width: 90%;
  margin: 0 auto;
  /* background-color: aquamarine; */
}

.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.el-card {
  height: 200px;
}

.card_img {
  max-width: 100%;
  max-height: 100%;
  display: block;
}

</style>




