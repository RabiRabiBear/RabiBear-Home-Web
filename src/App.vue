<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <el-container>
    <el-header>
      <!-- <nav> -->
      <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
    
      <!-- <img></img> -->
      <RouterLink to="/"><img alt="logo" class="logo" src="@/assets/imgs/avatar_rabbit.png" width="50" height="50" /></RouterLink>
      <el-menu-item index="1"><RouterLink to="/">Home</RouterLink></el-menu-item>
      <el-menu-item index="2"><RouterLink to="/about">Gallery</RouterLink></el-menu-item>
      <el-menu-item index="3"><RouterLink to="/about">Timelines</RouterLink></el-menu-item>
      <el-menu-item index="4"><RouterLink to="/about">100 Things & Wish List</RouterLink></el-menu-item>
      <el-menu-item index="11"><RouterLink to="/tracker">Tracker</RouterLink></el-menu-item>
      <el-menu-item index="5"><RouterLink to="/about">Whisper</RouterLink></el-menu-item>
      <el-menu-item index="6"><RouterLink to="/what_to_eat">What To Eat</RouterLink></el-menu-item>
      <el-menu-item index="6"><RouterLink to="/about">Records</RouterLink></el-menu-item>
      
      <el-sub-menu index="7">
        <template #title>Tools</template>
        <el-menu-item index="7-1"><RouterLink to="/what_to_eat">What To Eat</RouterLink></el-menu-item>
        <el-menu-item index="7-2"><RouterLink to="/tracker">Tracker</RouterLink></el-menu-item>
        <el-menu-item index="7-3"><RouterLink to="/web_labeler">Web Labeler</RouterLink></el-menu-item>
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


    <el-main><RouterView /></el-main>
    

    <el-footer>
      <el-divider>
        ˗ˋˏ꒰ঌ ♡ ໒꒱ྀིˎˊ˗   
      </el-divider>
      ❤ Copyright © 2023 RabiBear. All rights reserved. ❤
    </el-footer>
  </el-container>
  
</template>

<style scoped>


.el-container {
  background-color: aliceblue;
}

.el-footer{
  margin: 2rem auto;
}

.el-menu a.router-link-exact-active {
  color: var(--color-text);
}

.el-menu a.router-link-exact-active:hover {
  background-color: transparent;
}

.el-menu a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

.el-menu  a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    /* padding-right: calc(var(--section-gap) / 2); */
  }

  .logo {
    display: block;
    margin: 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    width: 100%;
  }

  .el-menu  {
    text-align: left;
    /* margin-left: -1rem; */
    font-size: 1rem;
    margin-top: 1rem;
    /* max-width: 500px; */
    width: 100%;
  }

}
</style>