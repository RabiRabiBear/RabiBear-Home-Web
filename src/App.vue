<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <el-container>
    <el-header style="font-family: 'Parisienne', cursive;">
      <!-- <nav> -->
      <el-menu mode="horizontal" 
          active-text-color="#ee827c">

        <el-menu-item index="0" class="logo_router">
          <RouterLink class="router_link" to="/"><img alt="logo" class="logo" src="@/assets/imgs/avatar_rabbit.png" width="50" height="50" style="display: flex; align-items: center;"/>
        </RouterLink>
        </el-menu-item>
        
        <el-menu-item index="1">
          <RouterLink class="router_link" to="/home">Home</RouterLink>
        </el-menu-item>
        <el-menu-item index="2">
          <RouterLink class="router_link" to="/maintenance">Gallery</RouterLink>
        </el-menu-item>
        <el-menu-item index="3">
          <RouterLink class="router_link" to="/timelines">Timelines</RouterLink>
        </el-menu-item>
        <el-menu-item index="4">
          <RouterLink class="router_link" to="/100Things">100 Things & Wish List</RouterLink>
        </el-menu-item>
        <el-menu-item index="5">
          <RouterLink class="router_link" to="/tracker">Tracker</RouterLink>
        </el-menu-item>

        <el-menu-item index="6">
          <!-- <template #title><img alt="logo" src="@/assets/imgs/home_card/icon_lock.png" width="30" height="30" /></template> -->
          <RouterLink class="router_link" to="/login"><img alt="logo" class="router_link" src="@/assets/imgs/home_card/icon_lock.png" width="25" height="25" style="margin-top: 0.8em; margin-bottom: 0.8em; display: flex; align-items: center;"/></RouterLink>
        </el-menu-item>


        <el-menu-item index="7">
          <RouterLink class="router_link" to="/maintenance">Whisper</RouterLink>
        </el-menu-item>
        <el-menu-item index="8">
        
          <RouterLink class="router_link" to="/what_to_eat">What To Eat</RouterLink>
        </el-menu-item>
        <el-menu-item index="9">
          <RouterLink class="router_link" to="/maintenance">Records</RouterLink>
        </el-menu-item>

        <!-- <el-sub-menu index="10">
          <template #title>Tools</template>
          <el-menu-item index="10-1">
            <RouterLink class="router_link" to="/what_to_eat">What To Eat</RouterLink>
          </el-menu-item>
          <el-menu-item index="10-2">
            <RouterLink class="router_link" to="/tracker">Tracker</RouterLink>
          </el-menu-item>
      </el-sub-menu> -->

      <!-- <el-sub-menu index="7">
        <template #title>Records</template>
        <el-menu-item index="7-1">On Movies</el-menu-item>
          <el-menu-item index="7-2">On Games</el-menu-item>
          <el-menu-item index="7-3">On The Way</el-menu-item>
          <el-menu-item index="7-4">Recipes</el-menu-item>
          <el-menu-item index="7-5">Tracking</el-menu-item>
        </el-sub-menu> -->



        <el-sub-menu index="11">
          <!-- <template #title><img alt="logo" src="@/assets/imgs/home_card/icon_lock.png" width="30" height="30" /></template> -->
          <!-- <img class="card_img" style="width: 40%;" src="../assets/imgs/home_card/icon_lock.png" /> -->
          <!-- <el-menu-item index="8-1">Accounting</el-menu-item> -->
          <el-menu-item index="11-1">Photos</el-menu-item>
          <el-menu-item index="11-2">Expiry Alert</el-menu-item>
          <!-- <el-menu-item index="3-3">Diary</el-menu-item> -->
        </el-sub-menu>
      </el-menu>
      <!-- </nav> -->
    </el-header>


    <el-main>
      <RouterView />
    </el-main>


    <el-footer>
      <!-- <el-footer> -->
      <el-divider>
        ˗ˋˏ꒰ঌ ♡ ໒꒱ྀིˎˊ˗
      </el-divider>
      <!-- <el-divider>
       <p style="background-color: #FFFFFB;">asss</p>
      </el-divider> -->
      <p style="font-family: 'Parisienne', cursive;"> 
        ❤ Copyright © 2023 RabiBear. All rights reserved. ❤
      </p>
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
