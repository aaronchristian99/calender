<script setup>
  import { ref, computed } from "vue";
  import { CalendarView as Calendar } from "vue-simple-calendar";
  import CalendarViewHeader from "@/components/CalendarViewHeader.vue";
  import "../../node_modules/vue-simple-calendar/dist/style.css";

  const showDate = ref(new Date());
  const period = ref('month');

  const setShowDate = (date) => {
    showDate.value = date;
  };

  const changeView = (newPeriod) => {
    period.value = newPeriod;
  }

  const isToday = (date) => {
    const today = new Date();
    return (
      date.getDate() === today.getDate() &&
      date.getMonth() === today.getMonth() &&
      date.getFullYear() === today.getFullYear()
    );
  };
</script>

<template>
  <Calendar :show-date="showDate"
            :displayPeriodUom="period"
            class="calendar theme-default holiday-us-official">
    <template #header="{ headerProps }">
      <CalendarViewHeader :header-props="headerProps" @input="setShowDate" @changeView="changeView" />
    </template>
    <template #day-content="{ day }">
      <div class="day-cell" :day :class="{ 'highlight-today': isToday(day) }">
        {{ day.getDate() }}
      </div>
    </template>
  </Calendar>
</template>

<style scoped>
  .calendar {
    background: #333;
    border-radius: 8px;
  }
</style>
