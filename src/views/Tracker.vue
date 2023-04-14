<!--
 * @Author: Alchemist
 * @Date: 2023-03-04
 * @LastEditTime: 2023-04-14
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


<!-- ---------------------------------------- -->


<!-- <template>
  <el-row :gutter="2" justify="space-between" style="margin: 2em;">
    <el-col :span="11">
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
    </el-col>
    <el-col :span="11">
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
    </el-col>
  </el-row>
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
      this.todos.push({ id: maxId + 1, text: this.newTodo, done: false })
      this.newTodo = ''
      this.sortTodos()
      console.log(this.todos[this.todos.length - 1].id, maxId + 1)
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
</script> -->


<template>
  <div class="todo_list">
    <el-row :gutter="2" justify="space-between" style="margin: 2em;">
      <el-col :span="11">
        <todo-list :todos="today" :title="'Today\'s Todo'" />
      </el-col>
      <el-col :span="11">
        <todo-list :todos="daily" :title="'Daily Todo'" />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import TodoList from "./TodoList.vue";
import axios from "axios";

export default {
  components: {
    TodoList,
  },
  data() {
    return {
      today: [],
      daily: [],
      // list1: [{ text: "Todo 1", done: false },
      // { text: "Todo 2", done: false },
      // { text: "Todo 3", done: false },],
      // list2: [{ text: "Task 1", done: false },
      // { text: "Task 2", done: false },
      // { text: "Task 3", done: false },],
    };
  },
  methods: {
    initialNewDay(currentDate, formattedDate, data, keys) {
      // const yesterday = new Date(currentDate);
      // yesterday.setDate(yesterday.getDate() - 1);
      // const formattedYesterday = `${yesterday.getFullYear()}-${yesterday.getMonth() + 1}-${yesterday.getDate()}`;
      // this.today = [];
      // data.filter(item => !item.done)
      const lastKey = keys[keys.length - 1];
      const undone = data[lastKey].filter(item => !item.done);

      // change the id of the undone todos to 1, 2, 3, ...
      const sortedUndone = undone.map((todo, index) => {
        return { ...todo, id: index + 1 }
      });

      // const today_data = {
      //   date: formattedDate,
      //   title : 'Today\'s Todo',
      //   todo: undone,
      // }
      // // axios.post('http://localhost:8000/init_new_day', today_data)

      // const daily_data = {
      //   date: formattedDate,
      //   title : 'Daily Todo',
      //   todo: [],
      // }
      axios.post('http://localhost:8000/init_new_day', { date: formattedDate, today_todo: sortedUndone })

    },
    // initialTodayTODO(formattedDate, jsonfile) {}
  },
  created() {
    // Get the current date
    const currentDate = new Date();
    // Format the date as YYYY-MM-DD
    const formattedDate = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`;

    console.log(formattedDate);
    const today_filename = "../../server/resources/today_todo.json";
    const daily_filename = "../../server/resources/daily_todo.json";

    // First get the data from the server, and check if there is data for today
    axios
      .get(today_filename)
      .then((response) => {
        const keys = Object.keys(response.data); // get the keys of the object
        if (!keys.includes(formattedDate)) {
          this.initialNewDay(currentDate, formattedDate, response.data, keys);
          // this.today = response.data[formattedDate];
          // this.initialNewDay(formattedDate, response.data);
          // this.initialTodayTODO(formattedDate, today_filename);
          // this.initialDailyTODO(formattedDate, daily_filename);
        }
        // this.daily = response.data["daily"];
      });

    // Fetch data for list 1 from server and assign it to list1
    axios
      .get(today_filename)
      .then((response) => {
        // console.log(response.data);
        // const keys = Object.keys(response.data); // get the keys of the object
        // if (not keys.includes(formattedDate)) {
        //   // this.today = response.data[formattedDate];
        //   this.initialTodayTODO(formattedDate, "../../server/resources/today_todo.json");
        // }
        // else {

        // }
        this.today = response.data[formattedDate];
      })
      .catch((error) => {
        console.error(error);
      });


    // // Fetch data for list 2 from server and assign it to list2
    axios
      .get(daily_filename)
      .then((response) => {
        // console.log(JSON.parse(response.data))
        // const data = JSON.parse(response.data);
        // console.log(data)
        this.daily = response.data[formattedDate];
      })
      .catch((error) => {
        console.error(error);
      });

    // axios.get("../../server/resources/daily_todo.json")
    // .then(({ data }) => {
    //   // const dailyTodo = JSON.parse(data);
    //   // console.log(dailyTodo);
    //   this.daily = data[formattedDate];
    // })
    // .catch((error) => {
    //   console.error(error);
    // });


  },
};
</script>



