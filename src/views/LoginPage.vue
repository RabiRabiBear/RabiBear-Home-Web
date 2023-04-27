<!--
 * @Author: Alchemist
 * @Date: 2023-04-22
 * @LastEditTime: 2023-04-27
 * @FilePath: /RabiBear-Home-Web/src/views/LoginPage.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->


<template>
  <div v-if="isLoggedIn">
    <img :src="useravatar" alt="User Avatar" style="width: 5em" />
    <div>{{ username }}</div>
    <div>{{ slogan }}</div>
    <el-button type="primary" plain @click="logout">Logout</el-button>
  </div>
  <div v-else>
    <el-form :model="form" label-position="top" label-width="120px" class="login-form">
      <el-form-item label="Name" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" plain @click="submitForm">Login</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
  
<script>
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import Cookies from 'js-cookie'

export default {
  name: 'LoginForm',
  setup() {
    const form = reactive({
      name: '',
      password: ''
    })
    const isLoggedIn = ref(false)
    const username = ref('')
    const slogan = ref('')
    const useravatar = ref('')

    const submitForm = async () => {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })

      if (response.ok) {
        const userData = await response.json()
        console.log(userData)
        Cookies.set('username', userData.userName, { expires: 14 })
        Cookies.set('slogan', userData.slogan, { expires: 14 })
        Cookies.set('useravatar', userData.useravatar, { expires: 14 })
        isLoggedIn.value = true
        username.value = userData.userName
        slogan.value = userData.slogan
        useravatar.value = userData.avatar
      } else {
        ElMessage.error('Login failed. Please try again.')
      }
    }

    const logout = () => {
      Cookies.remove('username')
      Cookies.remove('slogan')
      Cookies.remove('useravatar')
      isLoggedIn.value = false
      username.value = ''
      slogan.value = ''
      useravatar.value = ''
    }

    // check if user is logged in on page load
    const usernameCookie = Cookies.get('username')
    const sloganCookie = Cookies.get('slogan')
    if (usernameCookie && sloganCookie) {
      isLoggedIn.value = true
      username.value = usernameCookie
      slogan.value = sloganCookie
    }

    return { form, submitForm, isLoggedIn, username, slogan, useravatar, logout }
  }
}
</script>
  
<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
  