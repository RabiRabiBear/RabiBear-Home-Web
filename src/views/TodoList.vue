<!--
 * @Author: Alchemistyui
 * @Date: 2023-04-12
 * @LastEditTime: 2023-04-12
 * @FilePath: /RabiBear-Home-Web/src/views/TodoList.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->
<template>
  <div class="todo-list">
    <h1>{{ title }}</h1>

    <div style="display: flex; margin: 1rem auto;">
      <el-input v-model="newTodo" placeholder="Enter a new todo" @keyup.enter="addTodo" size="small" maxlength="20">
      </el-input>
      <el-button type="primary" @click="addTodo" style="margin-left: 0.5rem;">Add</el-button>
    </div>

    <el-table :data="todos" stripe>
      <el-table-column prop="text" label="Todo">
        <template #default="{ row }">
          <div :style="row.done ? 'text-decoration: line-through;' : ''">{{ row.text }}</div>
        </template>
      </el-table-column>
      <el-table-column label="Actions">
        <template #default="{ row }">
          <el-button v-if="!row.done" type="success" @click="toggleDone(row)">Done</el-button>
          <el-button v-else type="warning" @click="toggleDone(row)">Redo</el-button>
          <el-button type="danger" @click="removeTodo(row)">Delete</el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>
</template>

<script>
import { ref } from 'vue'
import axios from "axios";

export default {
  name: 'TodoList',
  props: {
    todos: {
      type: Array,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      //   todos: [
      //     { id: 1, text: 'Learn Vue 3', done: false },
      //     { id: 2, text: 'Build an app with Vue 3', done: false },
      //     { id: 3, text: 'Explore Element Plus', done: false }
      //   ],
      newTodo: ''
    }
  },
  methods: {
    updateServerData(todo, opt) {

      const currentDate = new Date();
      const formattedDate = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`;


      const form_data_desktop = {
        date: formattedDate,
        title : this.title,
        todo: todo,
        opt: opt
      }
      // console.log(JSON.stringify(form_data));
      axios.post('http://localhost:8000/submit', form_data_desktop)
    },
    addTodo() {
      const maxId = Math.max(...this.todos.map(todo => todo.id));
      const todo = { id: maxId + 1, text: this.newTodo, done: false }
      this.todos.push(todo)
      this.newTodo = ''
      this.sortTodos()
      console.log(this.todos[this.todos.length - 1].id, maxId + 1)
      this.updateServerData(todo, 'add')
    },
    removeTodo(todo) {
      // console.log(this.todos)
      // this.todos = this.todos.filter(t => t.id !== todo.id)
      const index = this.todos.indexOf(todo);
      if (index > -1) {
        this.todos.splice(index, 1);
      }
      this.sortTodos()
      // console.log(this.todos)
      console.log(todo.id)
      this.updateServerData(todo, 'remove')
    },
    toggleDone(todo) {
      todo.done = !todo.done
      this.sortTodos()
      console.log(todo.id)
      this.updateServerData(todo, 'toggle')
    },
    sortTodos() {
      this.todos.sort((a, b) => {
        if (a.done && !b.done) {
          return 1
        } else if (!a.done && b.done) {
          return -1
        } else {
          return a.id - b.id
        }
      })
    }
  }
}
</script>
