<!--
 * @Author: Alchemist
 * @Date: 2023-03-04
 * @LastEditTime: 2023-07-06
 * @FilePath: /RabiBear-Home-Web/src/views/Tracker.vue
 * @Description: 
 * 
 * Copyright (c) 2023, All Rights Reserved. 
-->


<template>
  <div class="tracker">



    <div class="todo_list">
      <el-row justify="space-between" style="margin: 2rem;">
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
          <!-- <img style="float: left; width: 15%;" src="../assets/imgs/sakura.png" /> -->
          <todo-list :todos="daily" :title="'Daily Todo'" :editable="false" />
        </el-col>
        <el-col :span="1"></el-col>
      </el-row>
    </div>

    <el-row justify="space-between" style="margin: 2rem;">
      <SavingPot />
    </el-row>

    <div class="container">
    <div class="container-select-modes">
      <Calendar backgroundText class-name="multi-mode" selectMode="multi" :monFirst="true" language="en"
                :tileContent="tileContent" :select-date="exerciseDate" :begin="begin" 
                @onSelect="onSelect"/>
    </div>
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
import { ref } from 'vue'
import Cookies from 'js-cookie';
import { onMounted } from 'vue';

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
      daily: [],
      exerciseDate: '',
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


      // create new arrays for today and daily
      const todayTodos = JSON.parse(JSON.stringify(today));
      const dailyTodos = JSON.parse(JSON.stringify(daily));



      Object.keys(todayTodos).forEach(key => {
        combinedData[key] = todayTodos[key];
      });

      Object.keys(dailyTodos).forEach(key => {
        if (combinedData[key]) {
          combinedData[key].push(...dailyTodos[key]);
        } else {
          combinedData[key] = dailyTodos[key];
        }
      });

      delete combinedData['daily'];
      // console.log('combined data', combinedData)

      // count the number of done todos for each date
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
      // console.log('calendaer data', this.Calenderdata);
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

    // console.log(formattedDate);
    // console.log(this.userName);

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


    const json_todos = []
    // Fetch data for list 1 from server and assign it to list1
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'today_todo' },
    })
      .then((response) => {
        json_todos.push(response.data)
        this.today = response.data[formattedDate];
      })
      .catch((error) => {
        console.error(error);
      });


    // Fetch data for list 2 from server and assign it to list2
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: this.userName, opt_type: 'daily_todo' },
    })
      .then((response) => {
        json_todos.push(response.data)
        this.daily = response.data[formattedDate];
      })
      .then(() => {
        // json_todos array may still be empty if the axios request to the server hasn't finished executing yet. The axios.get() method is asynchronous, meaning that it doesn't block the execution of the rest of the code while waiting for a response from the server.
        this.countDoneTodos(json_todos[0], json_todos[1]);
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

    const currentDate = new Date();
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth() + 1;
    const currentDay = currentDate.getDate();
    const userName = Cookies.get('username');
    // console.log(Cookies.get('username'));

    // const tileContent = ref({ '2023-7-13': { className: 'tip class', content: 'some tip' } })
    const tileContent = ref({
        [`${currentYear}-${currentMonth}-${currentDay}`]: {
          className: 'content-item-classname',
          content: 'some things'
        }
      })
    const begin = ref('2023-7-01')
    // const multiModeDate = ref(['2023-7-1', '2023-7-11', '2023-7-21'])
    // let exerciseDate = ref(['2023-7-4', '2023-7-5'])
    const exerciseDate = ref([]);
    axios.get(`${API_BASE_URL}/get_data`, {
      headers: { 'Content-Type': 'application/json' },
      params: { user_name: userName, opt_type: 'exercise_calendar' },
    })
      .then((response) => {
        exerciseDate.value = response.data;
        // console.log(response.data, 'response.data')
        // exerciseDate.push(response.data)
        // let exerciseDate = ref(response.data);
      })
      .catch((error) => {
        console.error(error);
      });

      // let exerciseDate = ref(response.data);

      console.log(exerciseDate, 'exerciseDate')

    function onSelect(selectDate) {
        console.log(selectDate, 'selectDate')
      }
    
      function selectYear(y, m) {
        console.log(y, m, 'selectYear')
      }

      function onMonthChange(y, m) {
        console.log(y, m, 'onMonthChange')
      }

      function selectMonth(y, m) {
        console.log(y, m, 'selectMonth')
      }

      function next(y, m, d) {
        console.log(y, m, d, 'nextnext')
      }

      function prev(y, m, d) {
        console.log(y, m, d, 'prevprev')
      }

    return {
      begin,
      tileContent,
      exerciseDate,
      onSelect,
      onMonthChange,
        next,
        prev,
        selectMonth,
        selectYear,
    }
  }
  // mounted() {
  //   const now = new Date();
  //   const refreshTime = new Date(
  //     now.getFullYear(),
  //     now.getMonth(),
  //     now.getDate(),
  //     10, // set refresh time to 8:00 am
  //     0,
  //     0,
  //     0
  //   );

  //   const timeUntilRefresh = refreshTime - now;
  //   if (timeUntilRefresh > 0) {
  //     setTimeout(() => {
  //       location.reload();
  //       console.log('refreshed')
  //     }, timeUntilRefresh);
  //   }
  // }

};
</script>


<style scoped>
.tracker {
  font-family: 'Bad Script', cursive;
  text-align: center;
}

/* .checkin_calendar * {
  all: revert;
} */
.container{
    width: 1000px;
    margin: 0 auto;
    .select-mode{
      .vc-calendar-year{
        margin-right: 10px;
      }
    }
    .container-select-modes{
      display: flex;
      flex-wrap: wrap;
      .select-mode, .multi-mode, .range-mode, .multiRange-mode{
        &.mpvue-calendar{
          width: 400px;
          margin: 0 auto;
          flex: none;
        }
      }
    }
    .container-view-modes{
      display: flex;
      flex-wrap: wrap;
      position: relative;
      .week-mode, .multi-mode, .range-mode, .multiRange-mode, .monthRange-mode{
        &.mpvue-calendar{
          width: 400px;
          margin: 0 auto;
          flex: none;
        }
      }
    }
  }

  .multi-mode{
    &:before{
      content: 'multi select mode';
      text-align: center;
      display: block;
      color: #38778a;
      font-weight: bold;
      margin-bottom: 5px;
    }
    .content-item-classname{
      color: #fff;
      background: #0b6cbc;
      display: inline-block;
      white-space: nowrap;
      padding: 0 3px;
      border-radius: 3px;
      transform: scale(.8);
    }
  }
</style>