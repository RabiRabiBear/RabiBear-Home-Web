<!--
 * @Author: Alchemist
 * @Date: 2023-04-15
 * @LastEditTime: 2023-04-15
 * @FilePath: /RabiBear-Home-Web/src/views/SavingPot.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<template>
    <div class="saving-pot">
      <img :src="potImage" alt="Pot image" />
      <el-progress :percentage="percentage" />

      <p>
        Saved Amount ¥{{ showAmount }} / Target Amount ¥{{ targetAmount }}
      </p>

      <div class="stars">
      <img v-for="star in stars" style="float: left; width: 15%;" :key="star" src='../assets/imgs/tracker/star.png' alt="Star image" />
    </div>

      <div class="buttons">
        <el-button @click="deposit(30)">Deposit ¥30</el-button>
        <el-button @click="deposit(20)">Deposit ¥20</el-button>
        <el-button @click="withdraw(10)">withdraw ¥10</el-button>
      </div>

    </div>
  </template>
  


<script>

import pot1Image from '@/assets/imgs/tracker/pot1.jpeg';
import pot2Image from '@/assets/imgs/tracker/pot2.jpeg';

export default {
  data() {
    return {
      savedAmount: 0,
      showAmount: 0,
      targetAmount: 100,
      potImages: {
        0: pot1Image,
        25: pot2Image,
        50: 'image3.jpg',
        75: 'image4.jpg'
      }
    };
  },
  computed: {
    percentage() {
      return Math.min(100, Math.floor((this.showAmount / this.targetAmount) * 100));
    },
    potImage() {
      const percentages = Object.keys(this.potImages);
      const maxPercentage = Math.max(...percentages.filter(p => p <= this.percentage));
      return this.potImages[maxPercentage];
    },
    stars() {
    //   const stars = Math.floor((this.savedAmount - this.targetAmount) / 50);
      const stars = Math.floor(this.savedAmount / this.targetAmount);
      return new Array(stars).fill(0);
    }
  },
  methods: {
    deposit(amount) {
      this.savedAmount += amount;
    //   if (this.savedAmount >= this.targetAmount) {
    //     // const stars = Math.floor(this.savedAmount / this.targetAmount);
    //     this.savedAmount = this.savedAmount % this.targetAmount;
    //     console.log(this.savedAmount)
    //     // this.targetAmount += stars * 50;
    //   }
      this.showAmount = this.savedAmount % this.targetAmount;
    },
    withdraw(amount) {
      this.savedAmount = Math.max(0, this.savedAmount - amount);
      this.showAmount = this.savedAmount % this.targetAmount;
    }
  }
};
</script>
