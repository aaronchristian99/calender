<script setup>
  import { ref, onMounted } from "vue";
  import axios from "axios";
  import { CalendarView as Calendar } from "vue-simple-calendar";
  import CalendarViewHeader from "@/components/CalendarViewHeader.vue";
  import "../../node_modules/vue-simple-calendar/dist/style.css";
  import Button from "@/components/Button.vue";

  const showDate = ref(new Date());
  const period = ref('month');
  const events = ref([]);

  onMounted(async () => {
    try {
      const response = await axios.get('/api/events');
      console.log(response);
      events.value = response.data;
    } catch (error) {
      console.log(error);
    }
  });

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
  <section class="calendar-operations-wrapper">
    <Button label="Add new Event" href="" type="a" />
    <Button label="Download" @click="downloadEvents" />
    <Button label="Upload" @click="uploadEvent" />
  </section>
  <Calendar :show-date="showDate"
            :displayPeriodUom="period"
            :items="events"
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

  .calendar-operations-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-items: center;
    gap: 1rem;
  }
</style>
