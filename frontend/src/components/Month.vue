<script>
export default {
  name: "Month",
  props: {
    events: Array
  },
  data() {
    return {
      currentDate: new Date(),
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      calendar: [],
    }
  },
  created() {
    this.generateCalendar();
  },
  methods: {
    generateCalendar(year = null, month = null) {
      const targetYear = year !== null ? year : this.currentDate.getFullYear();
      const targetMonth = month !== null ? month : this.currentDate.getMonth();
      const firstDayOfMonth = new Date(targetYear, targetMonth, 1);
      const lastDayOfMonth = new Date(targetYear, targetMonth + 1, 0);
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

      this.currentDate = new Date(targetYear, targetMonth, this.currentDate.getDate());
    },
    isToday(date) {
      return date.getDate() === this.currentDate.getDate() &&
        date.getMonth() === this.currentDate.getMonth() &&
        date.getFullYear() === this.currentDate.getFullYear();
    },
    getEventsForDate(date) {
      if(!date) {
        return;
      }

      return this.events.filter(event => {
        const eventDate = event.startDate;
        return (eventDate.getDate() === date.getDate() && eventDate.getMonth() === date.getMonth() && eventDate.getFullYear() === date.getFullYear())
      });
    }
  },
}
</script>

<template>
  <div v-for="day in days" :key="day" class="day-header">{{ day }}</div>
  <div v-for="(date, index) in calendar"
       :key="index"
       class="calendar-cell"
       :class="{
             'no-border-right': (index + 1) % 7 === 0,
             'no-border-bottom': index >= calendar.length - 7,
             'today': date && isToday(date)
           }">
    <p class="date-number" v-if="date">{{ date.getDate() }}</p>
    <div v-for="event in getEventsForDate(date)"
         :key="event.id"
         class="event-badge"
         @click="$emit('toggle-view', event.id)">
      <p>
        {{ event.title }}
      </p>
    </div>
  </div>
</template>

<style scoped>
  .day-header {
    font-size: 1.2rem;
    text-align: center;
    font-weight: 700;
    color: var(--color-white);
    border-right: 1px solid var(--color-light-grey);
    border-bottom: 1px solid var(--color-light-grey);
    padding: 0.8rem;
  }
  .day-header:last-child {
    border-right: none;
  }
  .calendar-cell {
    border-right: 1px solid var(--color-light-grey);
    border-bottom: 1px solid var(--color-light-grey);
    padding: 10px;
    min-height: 120px;
    position: relative;
  }
  .no-border-right {
    border-right: none;
  }
  .no-border-bottom {
    border-bottom: none;
  }
  .event-badge {
    background-color: var(--color-light-violet);
    padding: 4px 8px;
    border-radius: 5px;
    margin-top: 5px;
    font-size: 0.8rem;
  }
  .event-badge p {
    color: var(--color-black);
  }
  .event-badge:hover {
    cursor: pointer;
  }
  .today {
    background-color: var(--color-violet);
    color: var(--color-white);
  }
</style>
