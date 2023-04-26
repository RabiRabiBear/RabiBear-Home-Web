<!--
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2023-04-26
 * @FilePath: /RabiBear-Home-Web/src/views/HomeView.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->

<template>
  <!-- <div class="title">
        <img> 
    
      </div> -->
  <div class="article">
    <div class="border" style="display: flex; justify-content: space-between;">
      <img style="max-width: 10%;" src="../assets/imgs/home_card/border1.png" />
      <img style="max-width: 30%; object-fit: contain;" src="../assets/imgs/home_card/rose_divider1.png" />
      <img style="max-width: 10%; transform: scaleX(-1);" src="../assets/imgs/home_card/border1.png" />
    </div>

    <h1>Rabbit & Bear</h1>
    <h2> Welcome to our story</h2>
    <p> Love alters not with his brief hours and weeks. <br>

      But bears it out even to the edge of doom. <br>

      If this be error and upon me proved. <br>

      I never writ, nor no man ever loved. <br>

    </p>

    <div class="border" style="display: flex; justify-content: space-between;">
      <img style="max-width: 10%; transform: scaleY(-1);" src="../assets/imgs/home_card/border1.png" />
      <img style="max-width: 30%; object-fit: contain;" src="../assets/imgs/home_card/rose_divider2.png" />
      <img style="max-width: 10%; transform: scale(-1, -1);" src="../assets/imgs/home_card/border1.png" />
    </div>
  </div>
  <main class="card_view">
    <!-- gutter specify the spacing between columns -->
    <!-- span: means that each column will take up 8/24 or one-third of the total width -->
    <el-row :gutter="0">
      <el-col :span="6">

        <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_calender.png" />
          <span style="margin-top: 10em;">Gallery</span>
        </el-card>

      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card1.JPG" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_letter.png" />
          <span style="margin-top: 10em;">Whisper</span>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card2.JPG" />
        </el-card>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="6">
        <el-card shadow="hover" :body-style="{ padding: '0px' }">
          <img class="card_img" src="../assets/imgs/home_card/card3.JPG" />
        </el-card>
      </el-col>
      <!-- <el-col :span="6">
        <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%;" src="../assets/imgs/home_card/icon_lock.png" />
          <span style="margin-top: 10em;">Secret World</span>
        </el-card>
      </el-col> -->

      <el-col :span="6">
  <el-card shadow="hover" class="card_link" >
    <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_lock.png" />
    <span style="text-align: center;">Secret World</span>
  </el-card>
</el-col>


    <el-col :span="6">
      <el-card shadow="hover" :body-style="{ padding: '0px' }">
        <img class="card_img" src="../assets/imgs/home_card/card4.JPG" />
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card shadow="hover" class="card_link">
          <img class="card_img" style="width: 40%; margin: 0 auto;" src="../assets/imgs/home_card/icon_diamond.png" />
          <span style="margin-top: 10em;">Wish List</span>
        </el-card>
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
/* @import url('https://fonts.googleapis.com/css?family=Inconsolata|Oswald'); */
@import url('https://fonts.googleapis.com/css2?family=Parisienne&family=Dancing+Script&display=swap');
/* @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@1,300&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Bad+Script&family=Open+Sans:ital,wght@0,300;0,400;1,300&display=swap');

.article h1 {
  font-family: 'Parisienne', cursive;
  /* font-family: 'Dancing Script', cursive; */
  text-align: center;
  font-size: 2.5rem;
}

.article h2 {
  margin-top: 2rem;
  font-family: 'Bad Script', cursive;
  text-align: center;
  font-size: 2rem;
}

.article p {
  /* font-family: 'Open Sans', sans-serif; */
  margin: 1rem;
  font-family: 'Bad Script', cursive;
  text-align: center;
  font-size: 1.3rem;
}

/* .article {
  background-image: '../assets/imgs/home_card/card.png';
  
  background-size: cover;
  background-position: center;
  padding: 20px;
} */

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
  width: 100%;
  margin: 0 auto;
  margin-top: 5rem;
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
  display: flex; 
  align-items: center;
}

.card_link {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: 'Bad Script', cursive;
  font-size: 17px;
  text-align: center;
}
</style>




