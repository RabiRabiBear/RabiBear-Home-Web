<!--
 * @Author: Alchemist
 * @Date: 2023-03-04
 * @LastEditTime: 2023-04-15
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
          <todo-list :todos="today" :title="'Today\'s Todo'" :editable="true"/>
        </el-col>
        <el-col :span="10">
          <!-- <img style="float: left; width: 15%;" src="../assets/imgs/sakura.png" /> -->
          <todo-list :todos="daily" :title="'Daily Todo'" :editable="false"/>
        </el-col>
        <el-col :span="1"></el-col>
      </el-row>
    </div>

    
  </div>
</template>

<script>
import TodoList from "./TodoList.vue";
// import DailyTodo from "./DailyTodo.vue";
import axios from "axios";


export default {
  components: {
    TodoList,
  },
  data() {
    return {
      today: [],
      daily: [],
      header: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      levels: ["less", "more"],
      Calenderdata: [],
      colors: ["#F5F5F5", "#ECF5FF", "#C4E1FF", "#97CBFF", "#66B3FF", "#46A3FF",],
      // WeekDayFlagText: ["abc", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
      // data: [{ date: "2022-09-22", count: 5 }, { date: "2022-09-21", count: 50 }],
      // list1: [{ text: "Todo 1", done: false },
      // { text: "Todo 2", done: false },
      // { text: "Todo 3", done: false },],
    };
  },
  methods: {
    initialNewDay(currentDate, formattedDate, data, keys) {
      const lastKey = keys[keys.length - 1];
      const undone = data[lastKey].filter(item => !item.done);

      // change the id of the undone todos to 1, 2, 3, ...
      const sortedUndone = undone.map((todo, index) => {
        return { ...todo, id: index + 1 }
      });

      axios.post('http://localhost:8000/init_new_day', { date: formattedDate, today_todo: sortedUndone })

    },
    countDoneTodos(today, daily) {

      // console.log(json_todos);
      // const today = json_todos.today;
      // const daily = json_todos.daily;
      // combine today and daily todos
      const combinedData = {};


      // create new arrays for today and daily
      // const todayTodos = Array.from(today);
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
      console.log('combined data', combinedData)

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
      console.log('calendaer data', this.Calenderdata);
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
    }
  },
  // TODO: when change the page from header ruter, the data will not be updated for calender!!
  created() {
    // // Get the current date
    // const currentDate = new Date();
    // // Format the date as YYYY-MM-DD
    // const formattedDate = `${currentDate.getFullYear()}-${currentDate.getMonth() + 1}-${currentDate.getDate()}`;

    // use the padStart() method to add a leading zero to the month/day if it's a single digit.
    const currentDate = new Date();
    const year = currentDate.getFullYear();
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    const day = currentDate.getDate().toString().padStart(2, '0');
    const formattedDate = `${year}-${month}-${day}`;

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
        }
      });


    const json_todos = []
    // Fetch data for list 1 from server and assign it to list1
    axios
      .get(today_filename)
      .then((response) => {
        json_todos.push(response.data)
        this.today = response.data[formattedDate];
      })
      .catch((error) => {
        console.error(error);
      });


    // Fetch data for list 2 from server and assign it to list2
    axios
      .get(daily_filename)
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

    // this.countDoneTodos(json_todos);

  },
};
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bad+Script&family=Open+Sans:ital,wght@0,300;0,400;1,300&display=swap');

.tracker {
  font-family: 'Bad Script', cursive;
  /* font-family: 'Dancing Script', cursive; */
  text-align: center;
  /* font-size: 2.5rem; */
}

</style>