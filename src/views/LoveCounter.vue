<!--
 * @Author: Alchemist
 * @Date: 2023-08-11
 * @LastEditTime: 2023-08-12
 * @FilePath: /RabiBear-Home-Web/src/views/LoveCounter.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<template>
    <div class="love-counter">
      <h1 class="title">Our Love Journey</h1>
      <!-- <div class="date-input">
        <el-date-picker v-model="startDate" type="date" placeholder="Select a date" />
      </div> -->
      <div class="duration-output">
        <p>
          <span class="duration-value" style="color: #cdb1e4;">{{ total_days }}</span>
          <span class="duration-label">days</span>
        </p>
        <p><span class="duration-value">=</span></p>
        <p>
          <span class="duration-value" style="color: #ed556a;">{{ years }}</span>
          <span class="duration-label">years</span>
        </p>
        <p>
          <span class="duration-value" style="color: #29b7cb;">{{ months }}</span>
          <span class="duration-label">months</span>
        </p>
        <p>
          <span class="duration-value" style="color: #f8d86a;">{{ days }}</span>
          <span class="duration-label">days</span>
        </p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        startDate: new Date("2021-01-06"),
        years: 0,
        months: 0,
        days: 0,
        total_days: 0,
      };
    },
    created() {
      this.calculateDuration();
    },
    methods: {
      calculateDuration() {
        const today = new Date();
        const start = this.startDate;
        const yearsDiff = today.getFullYear() - start.getFullYear();
        const monthsDiff = today.getMonth() - start.getMonth();
        const daysDiff = today.getDate() - start.getDate();
  
        this.years = yearsDiff;
        this.months = monthsDiff < 0 ? 12 - Math.abs(monthsDiff) : monthsDiff;
        this.days = daysDiff < 0 ? 30 - Math.abs(daysDiff) : daysDiff;
        this.total_days = yearsDiff * 365 + monthsDiff * 30 + daysDiff;
      },
    },
  };
  </script>
  
  
  <style scoped>
  .love-counter {
    text-align: center;
    padding: 5rem 10rem;
    font-family: 'Pangolin', cursive;
  }
  
  .title {
    font-size: 40px;
    margin-bottom: 20px;
  }
  
  .date-input {
    margin-bottom: 20px;
  }
  
  .duration-output {
    display: flex;
    justify-content: space-evenly;
    margin-bottom: 20px;
  }
  
  .duration-value {
    font-size: 40px;
    padding: 0 1rem;
    font-weight: bold;
  }
  
  .duration-label {
    font-size: 20px;
    font-weight: bold;
  }
  </style>
  