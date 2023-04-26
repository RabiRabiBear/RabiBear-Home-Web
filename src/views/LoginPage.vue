<!--
 * @Author: Alchemist
 * @Date: 2023-04-22
 * @LastEditTime: 2023-04-26
 * @FilePath: /RabiBear-Home-Web/src/views/LoginPage.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<!-- <template>
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" label-width="120px">
      <el-form-item label="Username" prop="username">
        <el-input v-model="loginForm.username"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input v-model="loginForm.password" type="password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login">Login</el-button>
      </el-form-item>
    </el-form>
  </template>
   -->
  <!-- <script>
    export default {
      data() {
        return {
          loginForm: {
            username: '',
            password: ''
          },
          loginRules: {
            username: [{ required: true, message: 'Please enter your username', trigger: 'blur' }],
            password: [{ required: true, message: 'Please enter your password', trigger: 'blur' }]
          }
        }
      },
      methods: {
        login() {
          this.$refs.loginForm.validate((valid) => {
            if (valid) {
              // Perform login action
            } else {
              return false;
            }
          });
        }
      }
    }
  </script>
   -->

   <!-- <script>
import { reactive } from 'vue'
import { ElMessage } from 'element-plus'

export default {
  name: 'LoginForm',
  setup() {
    const form = reactive({
      email: '',
      password: ''
    })

    const submitForm = async () => {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(form)
      })

      if (response.ok) {
        const userData = await response.json()
        // Load the appropriate JSON file for the user and store the data in the Vuex store
      } else {
        ElMessage.error('Login failed')
      }
    }

    return { form, submitForm }
  }
}
</script> -->




<template>
    <el-form :model="form" label-position="top" label-width="120px" class="login-form">
      <el-form-item label="Name" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">Login</el-button>
      </el-form-item>
    </el-form>
  </template>
  
  <script>
  import { reactive } from 'vue'
  import { ElMessage } from 'element-plus'
  import { useStore } from 'vuex'
  
  export default {
    name: 'LoginForm',
    setup() {
      const form = reactive({
        name: '',
        password: ''
      })

      const store = useStore()
  
      const submitForm = async () => {
        const response = await fetch('http://localhost:8000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(form)
        })
  
        if (response.ok) {
          const userData = await response.json()
          store.commit('setUsername', userData.username)
          // Load the appropriate JSON file for the user and store the data in the Vuex store
          console.log(userData)
        } else {
          ElMessage.error('Login failed. Please try again.')
        }
      }
  
      return { form, submitForm }
    }
  }
  </script>
  
  <style scoped>
  .login-form {
    max-width: 400px;
    margin: 0 auto;
  }
  </style>
  