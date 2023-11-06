<!--
 * @Author: Alchemist
 * @Date: 2023-03-04
 * @LastEditTime: 2023-11-06
 * @FilePath: /RabiBear-Home-Web/src/views/Tracker.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->


<template>
  <div class="tracker">



    <div class="todo_list">
      <el-row justify="center" style="margin: 2rem;">
        <ActivityCalendar :data="Calenderdata" :width="35" :height="7" :header="header" :showWeekDayFlag="true"
          :cellLength="17" :cellInterval="10" :cellBorderRadius="4" :fontSize="8" :showLevelFlag="true"
          :levelFlagText="levels" :levelMapper="levelMapper" :backgroundColor="'#FFFFFB'" :colors="colors" />
      </el-row>
      <el-row :gutter="2" justify="space-between" style="margin: 1rem;">
        <el-col :span="1"></el-col>
        <el-col :span="10">
          <todo-list :todos="today" :title="'Today\'s Todo'" :editable="true" />
        </el-col>
        <el-col :span="10">
          <!-- <todo-list :todos="daily" :title="'Daily Todo'" :editable="false" /> -->
          <todo-list :todos="hobbies" :title="'Hobbies'" :editable="true" />
        </el-col>
        <el-col :span="1"></el-col>
      </el-row>
    </div>

    <!-- <el-row justify="space-between" style="margin: 2rem;">
      <SavingPot />
    </el-row> -->

    <div class="daily_calendar"> 
    <el-row :gutter="1" justify="space-between" style="margin: 4rem;">
      <!-- <el-col :span="1"></el-col> -->
        <el-col :span="7">
        <Calendar ref="calendar" backgroundText class-name="exercise_calendar" selectMode="multi" :monFirst="true" language="en"
          :select-date="exerciseDate" :begin="begin" @onSelect="exercise_onSelect" />
        </el-col>
        <!-- <el-col :span="1"></el-col> -->
        <el-col :span="7"><SavingPot /></el-col>
        <el-col :span="7">
          <Calendar ref="skincareCalendar" backgroundText class-name="skincare_calendar" selectMode="multi" :monFirst="true" language="en"
          :select-date="skincareDate" :begin="begin" @onSelect="skincare_onSelect" />
        </el-col>
    </el-row>
  </div>


  </div>
</template>

<script>
import TodoList from "./TodoList.vue";
// import DailyTodo from "./DailyTodo.vue";
import SavingPot from './SavingPot.vue';
import axios from "axios";
import { API_BASE_URL } from '@/config.js';


// import { computed } from 'vue'
// import { useStore } from 'vuex'
import { ref,onMounted, computed } from 'vue'
import Cookies from 'js-cookie';
// import { onMounted } from 'vue';

import Calendar from 'mpvue-calendar'


export default {
  components: {
    TodoList,
    SavingPot,
    Calendar,
  },
  data() {
    return {
      today: [],
      // daily: [],
      // json_todos: [],
      hobbies: [],
      exerciseDate: [],
      skincareDate: [],
      header: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      levels: ["less", "more"],
      Calenderdata: [],
      colors: ["#F5F5F5", "#ECF5FF", "#C4E1FF", "#97CBFF", "#66B3FF", "#46A3FF",],
      userName: ref(Cookies.get('username')),
    };
  },
  methods: {
    initialNewDay(currentDate, formattedDate, data, keys) {
      const lastKey = keys[keys.length - 1];
      console.log('initial new day', data)
      const undone = data[lastKey].filter(item => !item.done);

      // change the id of the undone todos to 1, 2, 3, ...
      const sortedUndone = undone.map((todo, index) => {
        return { ...todo, id: index + 1 }
      });

      axios.post(`${API_BASE_URL}/init_new_day`, { user_name: this.userName, date: formattedDate, today_todo: sortedUndone })

    },
    countDoneTodos(today, daily) {

      // combine today and daily todos
      const combinedData = {};

      const test_list = [1,2,3,4,5];
      const test_list_hashMap = [{1:1,2:2,3:3}];
      console.log("test_list", test_list);
      console.log("test_list_hashMap", test_list_hashMap);
      console.log("test_list_hashMap[0]", test_list_hashMap[0]);
      console.log('today', today[0])
      // create new arrays for today and daily
      const todayTodos = JSON.parse(JSON.stringify(today));
      console.log('todayTodos', todayTodos)



      Object.keys(todayTodos).forEach(key => {
        combinedData[key] = todayTodos[key];
      });
      console.log('combined data', combinedData)

      if(daily){
        const dailyTodos = JSON.parse(JSON.stringify(daily));
        Object.keys(dailyTodos).forEach(key => {
          if (combinedData[key]) {
            combinedData[key].push(...dailyTodos[key]);
          } else {
            combinedData[key] = dailyTodos[key];
          }
        });

        delete combinedData['daily'];
      }
        
     
      const result = [];

      for (const date in combinedData) {
        const todos = combinedData[date];
        let doneCount = 0;
        for (const todo of todos) {
          if (todo.done) {
            doneCount++;
          }
        }
        result.push({ date, count: doneCount });
      }

      this.Calenderdata = result;
    },
    levelMapper(count) {
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
    },
  },
  // TODO: when change the page from header ruter, the data will not be updated for calender!!
  created() {
    // // Get the current date
    // use the padStart() method to add a leading zero to the month/day if it's a single digit.
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    const day = currentDate.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'today_todo' },
    })
      .then((response) => {
        const keys = Object.keys(response.data); // get the keys of the object
        if (!keys.includes(formattedDate)) {
          this.initialNewDay(currentDate, formattedDate, response.data, keys);
        }
      });


    // let json_todos = []
    // Fetch data for list 1 from server and assign it to list1
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'today_todo' },
    })
      .then((response) => {
        // console.log('response', response.data)
        // json_todos.push(response.data)
        // this.json_todos = response.data;
        this.countDoneTodos(response.data, null);
        // console.log('aaaa json_todos', json_todos)
        this.today = response.data[formattedDate];
      })
      .catch((error) => {
        console.error(error);
      });

    // console.log('bbb json_todos', json_todos)
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'hobbies' },
    })
      .then((response) => {
        // json_todos.push(response.data)
        this.hobbies = response.data;
        // console.log('daily', this.daily)
      })
      .then(() => {
        // console.log('json_todos', json_todos)
        // this.countDoneTodos(json_todos[0], null);
      })
      .catch((error) => {
        console.error(error);
      });

    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'exercise_calendar' },
    })
      .then((response) => {
        this.exerciseDate = response.data;
        // console.log('exerciseDate', this.exerciseDate)
        this.$refs.calendar.render(year, (currentDate.getMonth() + 1).toString());
      })
      .catch((error) => {
        console.error(error);
      });

    // this.$refs.calendar.render(year, month);
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'skincare_calendar' },
    })
      .then((response) => {
        this.skincareDate = response.data;
        this.$refs.skincareCalendar.render(year, (currentDate.getMonth() + 1).toString());
      })
      .catch((error) => {
        console.error(error);
      });
    
  },
  mounted() {
    const lastRefresh = localStorage.getItem("lastRefresh");
    const now = new Date();

    if (!lastRefresh) {
      // First visit, store current time and do not refresh
      localStorage.setItem("lastRefresh", now.toISOString());
    } else {
      const lastRefreshDate = new Date(lastRefresh);
      const timeSinceLastRefresh = now - lastRefreshDate;

      if (timeSinceLastRefresh > 24 * 60 * 60 * 1000) {
        // More than 24 hours since last refresh, store current time and refresh
        localStorage.setItem("lastRefresh", now.toISOString());
        location.reload();
      }
    }

    // Refresh on the first click of the day after 8:00 am
    document.addEventListener("click", () => {
      const clickTime = new Date();
      const clickHour = clickTime.getHours();
      if (clickHour >= 8 && !lastRefresh) {
        // After 8:00 am and no refresh has occurred yet, store current time and refresh
        localStorage.setItem("lastRefresh", clickTime.toISOString());
        location.reload();
      }
    });
  },


  setup() {
    const userName = Cookies.get('username');

    const begin = ref('2023-7-01')
      
    function exercise_onSelect(selectDate) {
      axios.post(`${API_BASE_URL}/update_date_calendar`, { type: 'exercise_calendar', user_name: userName, values: Object.values(selectDate) })
      console.log(selectDate, 'selectDate')
    }

    function skincare_onSelect(selectDate) {
      axios.post(`${API_BASE_URL}/update_date_calendar`, { type: 'skincare_calendar', user_name: userName, values: Object.values(selectDate) })
      console.log(selectDate, 'selectDate')
    }


    return {
      begin,
      exercise_onSelect,
      skincare_onSelect,
    }
  }
};
</script>


<style scoped>
.tracker {
  font-family: 'Bad Script', cursive;
  text-align: center;
}



.exercise_calendar{
    &:before{
      content: 'Exercise Calendar';
      text-align: center;
      display: block;
      color: #38778a;
      font-weight: bold;
      margin-bottom: 5px;
    }
    .selected {
  background: red;
  color:  yellow;
}
.skincare_calendar {
  &:before{
    content: 'Skincare Calendar';
    text-align: center;
    display: block;
    color: #38778a;
    font-weight: bold;
    margin-bottom: 5px;
  }
}
  }
</style>