<template>
    <div class="todo-list">
      <h1>{{ title }}</h1>
      <!-- <el-input v-model="newTodo" placeholder="Enter a new todo"></el-input>
      <el-button type="primary" @click="addTodo">Add</el-button> -->
  
      <div style="display: flex; margin: 1rem auto;">
        <el-input v-model="newTodo" placeholder="Enter a new todo" @keyup.enter="addTodo" size="small"
          maxlength="20">
        </el-input>
      </div>
  
        <el-table :data="todos" stripe>
          <el-table-column prop="text" label="Todo"></el-table-column>
          <el-table-column label="Actions">
            <template #default="{ row }">
              <el-button type="danger" @click="removeTodo(row)">Delete</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    name: 'TodoList',
    data() {
      return {
        todos: [
          { id: 1, text: 'Learn Vue 3' },
          { id: 2, text: 'Build an app with Vue 3' },
          { id: 3, text: 'Explore Element Plus' }
        ],
        newTodo: ''
      }
    },
    methods: {
      addTodo() {
        const newId = this.todos.length > 0 ? this.todos[this.todos.length - 1].id + 1 : 1
        this.todos.push({ id: newId, text: this.newTodo })
        this.newTodo = ''
      },
      removeTodo(todo) {
        this.todos = this.todos.filter(t => t.id !== todo.id)
      }
    },
    setup() {
      const title = 'Daily Todo List'
      return { title }
    }
  }
  </script>
  
  