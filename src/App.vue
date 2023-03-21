<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <el-container>
    <el-header>
      <!-- <nav> -->
      <el-menu mode="horizontal" 
          active-text-color="#ee827c">

        <!-- <img></img> -->
        <el-menu-item index="0" class="logo_router">
          <RouterLink class="router_link" to="/"><img alt="logo" class="logo" src="@/assets/imgs/avatar_rabbit.png" width="50" height="50" />
        </RouterLink>
        </el-menu-item>
        
        <el-menu-item index="1">
          <RouterLink class="router_link" to="/home">Home</RouterLink>
        </el-menu-item>
        <el-menu-item index="2">
          <RouterLink class="router_link" to="/about">Gallery</RouterLink>
        </el-menu-item>
        <el-menu-item index="3">
          <RouterLink class="router_link" to="/about">Timelines</RouterLink>
        </el-menu-item>
        <el-menu-item index="4">
          <RouterLink class="router_link" to="/about">100 Things & Wish List</RouterLink>
        </el-menu-item>
        <el-menu-item index="11">
          <RouterLink class="router_link" to="/tracker">Tracker</RouterLink>
        </el-menu-item>
        <el-menu-item index="5">
          <RouterLink class="router_link" to="/about">Whisper</RouterLink>
        </el-menu-item>
        <el-menu-item index="6">
          <RouterLink class="router_link" to="/what_to_eat">What To Eat</RouterLink>
        </el-menu-item>
        <el-menu-item index="6">
          <RouterLink class="router_link" to="/about">Records</RouterLink>
        </el-menu-item>

        <el-sub-menu index="7">
          <template #title>Tools</template>
          <el-menu-item index="7-1">
            <RouterLink class="router_link" to="/what_to_eat">What To Eat</RouterLink>
          </el-menu-item>
          <el-menu-item index="7-2">
            <RouterLink class="router_link" to="/tracker">Tracker</RouterLink>
          </el-menu-item>
          <!-- <el-menu-item index="7-3">
          <RouterLink class="router_link" to="/web_labeler">Web Labeler</RouterLink>
        </el-menu-item> -->
      </el-sub-menu>

      <!-- <el-sub-menu index="7">
        <template #title>Records</template>
        <el-menu-item index="7-1">On Movies</el-menu-item>
          <el-menu-item index="7-2">On Games</el-menu-item>
          <el-menu-item index="7-3">On The Way</el-menu-item>
          <el-menu-item index="7-4">Recipes</el-menu-item>
          <el-menu-item index="7-5">Tracking</el-menu-item>
        </el-sub-menu> -->



        <el-sub-menu index="8">
          <template #title><img alt="logo" src="@/assets/imgs/heart_key.png" width="40" height="40" /></template>
          <el-menu-item index="8-1">Accounting</el-menu-item>
          <el-menu-item index="8-2">Photos</el-menu-item>
          <el-menu-item index="8-2">Expiry Alert</el-menu-item>
          <!-- <el-menu-item index="3-3">Diary</el-menu-item> -->
        </el-sub-menu>
      </el-menu>
      <!-- </nav> -->
    </el-header>


    <el-main>
      <RouterView />
    </el-main>


    <!-- <el-footer style="font-family: 'Bad Script', cursive;"> -->
      <el-footer>
      <el-divider>
        ˗ˋˏ꒰ঌ ♡ ໒꒱ྀིˎˊ˗
      </el-divider>
      <!-- <el-divider>
       <p style="background-color: #FFFFFB;">asss</p>
      </el-divider> -->
      ❤ Copyright © 2023 RabiBear. All rights reserved. ❤
    </el-footer>
  </el-container>
</template>

<style scoped>

@media (min-width: 1024px) {

  .el-menu {
    background-color: #FFFFFB;
    /* text-align: left; */
    /* font-family: 'Bad Script', cursive; */
    font-size: 1rem;
    margin-top: 1rem;
    width: 100%;
  }

  .el-main {
    /* text-align: left; */
    font-size: 1rem;
    margin-top: 1rem;
    /* max-width: 500px; */
    width: 100%;
  }

  .el-container {
    background-color: #FFFFFB;
    /* background-color: #fffffc; */
  }

  .el-footer {
    margin: 2rem auto;
  }

  .el-menu a.router-link-exact-active {
    font-weight: bold;
  }

  .el-menu a.router-link-exact-active:hover {
    background-color: transparent; 
    /* background-color: red; */
  }

  .el-menu a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
    /* border-left-color: red; */
    /* #fefefe; */
  }

  .el-menu a:first-of-type {
    border: 0;
  }

  .router_link:hover {
    background-color: transparent; 
    /* background-color: red;  */
    /* padding: 5px 20px; */
  }

.el-menu-item:hover{  
  /* outline: 0 !important;   */
  color: #f0908d !important; 
  background-color: transparent !important; 
   
} 

.el-menu--horizontal>.logo_router.is-active {
  border-bottom: 1px solid #FFFFFB;
}
}</style>