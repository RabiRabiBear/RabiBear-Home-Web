<!--
 * @Author: Alchemist
 * @Date: 2023-03-04
 * @LastEditTime: 2023-03-17
 * @FilePath: /RabiBear-Home-Web/src/views/Tracker.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->

<!-- <template>
  <ActivityCalendar
    :data="data"
    :width="40"
    :height="7"
    :header="header"
    :showWeekDayFlag="false"
    :cellLength="20"
    :cellInterval="10"
    :cellBorderRadius="4" 
    :fontSize="12"
    :showLevelFlag="true"
    :levelFlagText="levels"
    :levelMapper="levelMapper"
  />

 <div>
    Daily TODO
    <el-checkbox-group v-model="checkList">
      <el-checkbox label="Option A" />
      <el-checkbox label="Option B" />
      <el-checkbox label="Option C" />
      <el-button round @click="addNewItem">+</el-button>
      <el-input v-model="input" v-if="show_input" placeholder="Add new item" />
  </el-checkbox-group>
  </div> 
  

</template> -->



<!-- <script lang="ts" setup>
// import TodoApp from './TodoApp.vue'

const header = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
const levels = ["less", "more"]
const data = ref([{ date: "2022-09-22", count: 5 }, { date: "2022-09-21", count: 50 }])

function levelMapper(count) {
  if (count == 0) {
    return 0;
  } else if (count <= 1) {
    return 1;
  } else if (count <= 3) {
    return 2;
  } else if (count <= 6) {
    return 3;
  } else if (count <= 9) {
    return 4;
  } else {
    return 5;
  }
}

const checkList = ref([])
var show_input = false
const input = ref('')

function addNewItem() {
  show_input = !show_input
}


</script> -->


<!--
 * @Author: Alchemist
 * @Date: 2023-03-17
 * @LastEditTime: 2023-03-17
 * @FilePath: /RabiBear-Home-Web/src/views/TodoApp.vue
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

export default {
  name: 'TodoList',
  data() {
    return {
      todos: [
        { id: 1, text: 'Learn Vue 3', done: false },
        { id: 2, text: 'Build an app with Vue 3', done: false },
        { id: 3, text: 'Explore Element Plus', done: false }
      ],
      newTodo: ''
    }
  },
  methods: {
    addTodo() {
      
      // const newId = this.todos.length > 0 ? this.todos[this.todos.length - 1].id + 1 : 1
      const maxId = Math.max(...this.todos.map(todo => todo.id));
      this.todos.push({ id: maxId+1, text: this.newTodo, done: false })
      this.newTodo = ''
      this.sortTodos()
      console.log(this.todos[this.todos.length - 1].id, maxId+1)
    },
    removeTodo(todo) {
      this.todos = this.todos.filter(t => t.id !== todo.id)
      this.sortTodos()
      console.log(todo.id)
    },
    // markAsDone(todo) {
    //   todo.done = true
    //   this.todos.push(this.todos.splice(this.todos.indexOf(todo), 1)[0])
    // },
    // markAsRedo(todo) {
    //   todo.done = false
    //   this.todos.unshift(this.todos.splice(this.todos.indexOf(todo), 1)[0])
    // },
    toggleDone(todo) {
    todo.done = !todo.done
    this.sortTodos()
    console.log(todo.id)
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
  },
  setup() {
    const title = 'Daily Todo List'
    return { title }
  }
}
</script>
