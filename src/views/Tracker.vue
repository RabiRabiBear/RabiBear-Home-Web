
<template>
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
</template>


<script lang="ts" setup>
import {ref} from 'vue'
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

</script>