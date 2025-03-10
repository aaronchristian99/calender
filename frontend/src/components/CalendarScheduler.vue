<template>
  <div class="calendar-container">
    <div class="calendar">
      <div v-for="day in days" :key="day" class="day-header">{{ day }}</div>
      <div
        v-for="(date, index) in calendar"
        :key="index"
        class="calendar-cell"
        :class="{
          'no-border-right': (index + 1) % 7 === 0,
          'no-border-bottom': index >= calendar.length - 7,
          'today': date && isToday(date)
        }"
        @click="selectDate(date)">
        <p class="date-number" v-if="date">{{ date.getDate() }}</p>
        <p class="event-text" v-if="events[date]">
          {{ events[date] }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      calendar: [],
      selectedDate: null,
      eventText: "",
      events: {}
    };
  },
  created() {
    this.generateCalendar();
  },
  methods: {
    generateCalendar() {
      const today = new Date();
      const firstDayOfMonth = new Date(today.getFullYear(), today.getMonth(), 1);
      const lastDayOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0);
      const firstDayOfWeek = firstDayOfMonth.getDay();
      const totalDays = lastDayOfMonth.getDate();
      const totalCells = Math.ceil((firstDayOfWeek + totalDays) / 7) * 7;

      this.calendar = [];

      // Fill empty spaces before first day of the month
      for (let i = 0; i < firstDayOfWeek; i++) {
        this.calendar.push(null);
      }

      // Fill actual days of the month
      let tempDate = new Date(firstDayOfMonth);
      while (tempDate <= lastDayOfMonth) {
        this.calendar.push(new Date(tempDate));
        tempDate.setDate(tempDate.getDate() + 1);
      }

      // Fill empty spaces after last day of the month
      while (this.calendar.length < totalCells) {
        this.calendar.push(null);
      }
    },
    selectDate(date) {
      if (!date) return;
      this.selectedDate = date;
      this.eventText = this.events[date] || "";
    },
    isToday(date) {
      const today = new Date();
      return date.getDate() === today.getDate() &&
        date.getMonth() === today.getMonth() &&
        date.getFullYear() === today.getFullYear();
    }
  }
};
</script>

<style scoped>
  .calendar-container {
    max-width: 100%;
    height: 100%;
    margin: auto;
    padding: 20px;
  }
  .calendar {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    border: 1px solid var(--color-text-input);
    border-radius: 10px;
  }
  .day-header {
    font-size: 1.2rem;
    text-align: center;
    font-weight: 700;
    color: var(--color-text);
    border-right: 1px solid var(--color-text-input);
    border-bottom: 1px solid var(--color-text-input);
    padding: 0.8rem;
  }
  .day-header:last-child {
    border-right: none;
  }
  .calendar-cell {
    border-right: 1px solid var(--color-text-input);
    border-bottom: 1px solid var(--color-text-input);
    padding: 10px;
    min-height: 120px;
    position: relative;
    cursor: pointer;
  }
  .no-border-right {
    border-right: none;
  }
  .no-border-bottom {
    border-bottom: none;
  }
  .event-text {
    position: absolute;
    bottom: 5px;
    left: 5px;
  }
  .today {
    background-color: var(--color-background-button);
    color: var(--color-text-button);
  }
</style>
