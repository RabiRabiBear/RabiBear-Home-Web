<!--
 * @Author: Alchemist
 * @Date: 2023-04-22
 * @LastEditTime: 2023-08-14
 * @FilePath: /RabiBear-Home-Web/src/views/LoginPage.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->


<template>
  <div v-if="isLoggedIn" class="loggedin">
    <img :src="useravatar" alt="User Avatar" style="width: 5em" />
    <div>{{ username }}</div>
    <div>{{ slogan }}</div>
    <el-button type="primary" plain @click="logout">Logout</el-button>
  </div>
  <div v-else class="login">
    <!-- <el-form :model="form" label-position="top" label-width="120px" class="login-form">
      <el-form-item label="Name" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" plain @click="submitForm">Login</el-button>
      </el-form-item>
    </el-form> -->
    <el-form :model="form" label-position="top" label-width="120px" class="login-form">
      <el-row>
        <el-col :span="12">
          <el-form-item label="Name" prop="name">
            <el-input v-model="form.name"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="Password" prop="password">
            <el-input type="password" v-model="form.password" @keyup.enter="submitForm"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24" style="text-align: center;">
          <el-form-item>
            <el-button type="primary" plain @click="submitForm">Login</el-button>
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

  </div>
</template>
  
<script>
import { reactive, ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import Cookies from 'js-cookie'
import defaultAvatar from '@/assets/imgs/default_avatar.png';
import { API_BASE_URL } from '@/config.js';

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
      // const response = await fetch('http://localhost:8000/login', {
        const expire_date = 31
        const response = await fetch(`${API_BASE_URL}/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })
      

      if (response.ok) {
        const userData = await response.json()
        // console.log(userData)
        Cookies.set('username', userData.userName, { expires: expire_date })
        isLoggedIn.value = true
        username.value = userData.userName


        
        if (userData['slogan']) {
          slogan.value = userData.slogan
        } else {
          slogan.value = '啊呜啊呜吐泡泡'
        }
        Cookies.set('slogan', slogan.value, { expires: expire_date })


        // console.log(userData['avatar'])
        if (userData['avatar']) {
          useravatar.value = `data:image/png;base64,${userData['avatar']}`;
          

          // Cookies.set('useravatar', `data:image/png;base64,${userData['avatar']}`, { expires: expire_date })
          // console.log('>??:', Cookies.get('useravatar'));
        } else {
          useravatar.value = defaultAvatar
        }
        localStorage.setItem('useravatar', `data:image/png;base64,${userData['avatar']}`);
        
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
      useravatar.value = localStorage.getItem('useravatar')
    }

    return { form, submitForm, isLoggedIn, username, slogan, useravatar, logout }
  }
}
</script>
  
<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
  align-items: center;
}

.loggedin {
  text-align: center;
  margin: 4em auto;
  max-width: 400px;

  /* font-family: 'Parisienne', cursive; */
  font-family: 'Dancing Script', cursive;
  text-align: center;
  font-size: 1.2rem;
}

.loggedin img {
  border-radius: 50%;
  margin-bottom: 1em;
  width: 100px;
}

button {
  font-family: 'Parisienne', cursive;
  /* font-family: 'Dancing Script', cursive; */
  text-align: center;
}

/* 
el-row {
  margin-bottom: 1rem;
  align-items: center;
} */

/* .login {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
} */
</style>
  