<!--
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2023-01-30
 * @FilePath: /RabiBear-Home-Web/src/views/WhatToEat.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<!-- <template>
    <el-transfer v-model="value" :data="data" />
    <el-button type="primary" round>Primary</el-button>
  </template> -->


<template>
    <div class="eat-box">
      <el-transfer v-model="selected" :data="data" />
      <div>
        <el-button type="primary" round @click="select">Select</el-button>
      </div>
      <div>
        <div v-show="buttonStatus">{{ msg }}</div>
      </div>
      <!-- <div @click="start" v-show="!buttonStatus">
        <button>开始</button>
      </div>
      <div @click="end" v-show="buttonStatus">
        <button>结束</button>
      </div> -->
    </div>
  </template>


  <script lang="ts" setup>
  import { reactive, toRefs, ref, getCurrentInstance, onMounted } from 'vue'

  interface Option {
    key: number
    label: string
    disabled: boolean
  }
  
  const generateData = () => {
    const data: Option[] = []
    const eat_list = ['マクドナルド','まぜそば','油そば','松屋','ナン','王将','サイゼリヤ']
    for (let i = 0; i < eat_list.length; i++) {
      data.push({
        key: i,
        label: eat_list[i],
        disabled: false,
      })
    }
    return data
  }
  
  const data = ref<Option[]>(generateData())
  const selected = ref([])

  var msg = ref('')
  var buttonStatus = ref(false)

  const select = () => {
    let index = Math.floor(Math.random() * selected.value.length)
    console.log(index)
    msg.value = data.value[selected.value[index]].label
    buttonStatus.value = true
  }

  // export default {
  //   setup() {
  //     const state = reactive({
  //       eatList: ['火锅','烤鸡','麦当劳','肯德基','披萨','意面','轻食沙拉','烤肉','热干面','桂林米粉'],
  //       msg: '',
  //       // timer: null,
  //       buttonStatus: false
  //     })
  //     const select = () => {
  //       let index = Math.floor(Math.random() * state.eatList.length)
  //       console.log(index)
  //       state.msg = state.eatList[index]
  //       state.buttonStatus = true
  //     }
  //     // const start = () => {
  //     //   state.buttonStatus = !state.buttonStatus
  //     //   if(state.timer){
  //     //     clearInterval(state.timer)
  //     //   }
  //     //   state.timer = setInterval(()=>{
  //     //     let index = Math.floor(Math.random() * state.eatList.length)
  //     //     console.log(index)
  //     //     state.msg = state.eatList[index]
  //     //   },50)
  //     // }
  //     // const end = () => {
  //     //   state.buttonStatus = !state.buttonStatus
  //     //   clearInterval(state.timer)
  //     // }
  //     return {
  //       ...toRefs(state),
  //       select
  //       // start,
  //       // end
  
  //     }
  //   },
  // }
  </script>

<!--   
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  interface Option {
    key: number
    label: string
    disabled: boolean
  }
  
  const generateData = () => {
    const data: Option[] = []
    for (let i = 1; i <= 15; i++) {
      data.push({
        key: i,
        label: `Option ${i}`,
        disabled: i % 4 === 0,
      })
    }
    return data
  }
  
  const data = ref<Option[]>(generateData())
  const value = ref([])
  </script> -->
  


