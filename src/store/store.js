/*
 * @Author: Alchemist
 * @Date: 2023-04-26
 * @LastEditTime: 2023-04-26
 * @FilePath: /RabiBear-Home-Web/store/store.js
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
 */
import { createStore } from 'vuex'

const store = createStore({
  state: {
    username: null
  },
  mutations: {
    setUsername(state, username) {
      state.username = username
    }
  }
})

export default store
