<!--
 * @Author: Alchemist
 * @Date: 2023-04-15
 * @LastEditTime: 2023-08-14
 * @FilePath: /RabiBear-Home-Web/src/views/SavingPot.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<template>
    <div class="saving-pot">
      <img :src="potImage" alt="Pot image" style="width: 5em;"/>
      <div class="stars">
      <img v-for="star in stars" style="float: left; width: 15%;" :key="star" src='../assets/imgs/tracker/star.png' alt="Star image" />
    </div>
      <el-progress :percentage="percentage" />

      <p>
        Saved Amount ¥{{ shownAmount }} / Target Amount ¥{{ targetAmount }}
      </p>

      

      <div class="buttons">
        <el-button @click="deposit(30)">Deposit ¥30</el-button>
        <el-button @click="deposit(20)">Deposit ¥20</el-button>
        <el-button @click="withdraw(10)">withdraw ¥10</el-button>
      </div>

    </div>
  </template>
  


<script>
import axios from "axios";

import pot1Image from '@/assets/imgs/tracker/pot1.png';
import pot2Image from '@/assets/imgs/tracker/pot2.png';
import pot3Image from '@/assets/imgs/tracker/pot3.png';
import pot4Image from '@/assets/imgs/tracker/pot4.png';
import { API_BASE_URL } from '@/config.js';

import { ref } from 'vue'
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      savedAmount: 0,
      shownAmount: 0,
      targetAmount: 100,
      potImages: {
        0: pot1Image,
        25: pot2Image,
        50: pot3Image,
        75: pot4Image
      },
      userName: ref(Cookies.get('username')),
    };
  },
  computed: {
    percentage() {
      return Math.min(100, Math.floor((this.shownAmount / this.targetAmount) * 100));
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
      this.shownAmount = this.savedAmount % this.targetAmount;
      // axios.post('http://localhost:8000/modify_saving_pot', { user_name: this.userName, key: 'savedAmount', val: this.savedAmount })
      axios.post(`${API_BASE_URL}/modify_saving_pot`, { user_name: this.userName, key: 'savedAmount', val: this.savedAmount })
      
    },
    withdraw(amount) {
      this.savedAmount = Math.max(0, this.savedAmount - amount);
      this.shownAmount = this.savedAmount % this.targetAmount;
      axios.post(`${API_BASE_URL}/modify_saving_pot`, { user_name: this.userName, key: 'savedAmount', val: this.savedAmount })
    }
  },
  created() {
    // axios
    //   .get("../../server/resources/"+this.userName+"/saving_pot.json")
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'saving_pot' },
    })
      .then((response) => {
        this.savedAmount = response.data.savedAmount;
        this.shownAmount = response.data.shownAmount;
        this.targetAmount = response.data.targetAmount;
        // console.log(this.savedAmount, this.shownAmount, this.targetAmount);
      });
  }
};
</script>
