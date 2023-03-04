/*
 * @Author: Alchemistyui
 * @Date: 2023-01-29
 * @LastEditTime: 2023-03-04
 * @FilePath: /RabiBear-Home-Web/src/router/index.ts
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
 */
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/what_to_eat',
      name: 'what_to_eat',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/WhatToEat.vue')
    },
    {
      path: '/tracker',
      name: 'tracker',
      component: () => import('../views/Tracker.vue')
    },
    // {
    //   path: '/web_labeler',
    //   name: 'web_labeler',
    //   component: () => import('../views/ .vue')
    // }
  ]
})

export default router
