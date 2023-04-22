<!--
 * @Author: Alchemist
 * @Date: 2023-04-22
 * @LastEditTime: 2023-04-22
 * @FilePath: /RabiBear-Home-Web/src/views/Maintenance.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->

<template>
    <div class="maintenance">
        <img src="../assets/imgs/maintenance.png" alt="Maintenance image" />
        <h2>Sorry, this page is under maintenance.</h2>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Bad+Script&family=Open+Sans:ital,wght@0,300;0,400;1,300&display=swap');
.maintenance {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 50vh;
}

.maintenance img {
  max-width: 10%;
  height: auto;
  margin-bottom: 2rem;
}

/* .maintenance h1 {
  font-size: 2rem;
  text-align: center;
  margin: 0;
} */

h2 {
  /* font-family: 'Open Sans', sans-serif; */
  margin: 1rem;
  font-family: 'Bad Script', cursive;
  text-align: center;
  font-size: 1.5rem;
}

</style>