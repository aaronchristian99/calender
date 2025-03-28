<script>
export default {
  name: "Month",
  props: {
    events: Array,
    date: Date,
    days: Array
  },
  data() {
    return {
      currentDate: new Date(),
      calendar: [],
    }
  },
  created() {
    this.generateCalendar();
  },
  methods: {
    generateCalendar(year = null, month = null) {
      const targetYear = year ?? this.currentDate.getFullYear();
      const targetMonth = month ?? this.currentDate.getMonth();

      const firstDayOfMonth = new Date(targetYear, targetMonth, 1);
      const lastDayOfMonth = new Date(targetYear, targetMonth + 1, 0);

      const firstDayOfWeek = firstDayOfMonth.getDay(); // Day index (0 - Sunday, 6 - Saturday)
      const totalDays = lastDayOfMonth.getDate();

      this.calendar = [];

      // Helper function to format the date
      const formatDate = (date) => {
        const options = { month: "short", day: "numeric" };
        return date.toLocaleDateString("en-US", options);
      };

      // Fill previous month's days only if needed
      if (firstDayOfWeek > 0) {
        const prevMonthLastDate = new Date(targetYear, targetMonth, 0).getDate();
        for (let i = firstDayOfWeek - 1; i >= 0; i--) {
          const prevDate = new Date(targetYear, targetMonth - 1, prevMonthLastDate - i);
          this.calendar.push({ date: prevDate, label: prevDate.getDate(), isOtherMonth: true });
        }
      }

      // Fill current month days
      for (let i = 1; i <= totalDays; i++) {
        const currDate = new Date(targetYear, targetMonth, i);
        const label = i === 1 ? formatDate(currDate) : i;
        this.calendar.push({ date: currDate, label, isOtherMonth: false });
      }

      // Determine if we need extra rows to complete the last week
      const totalCells = this.calendar.length;
      const remainingCells = totalCells % 7 !== 0 ? 7 - (totalCells % 7) : 0;

      // Fill next month's days only if required to complete the last week
      for (let i = 1; i <= remainingCells; i++) {
        const nextDate = new Date(targetYear, targetMonth + 1, i);
        const label = i === 1 ? formatDate(nextDate) : i;
        this.calendar.push({ date: nextDate, label, isOtherMonth: true });
      }
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
  watch: {
    date(newDate) {
      const changedDate = new Date(newDate);
      this.generateCalendar(changedDate.getFullYear(), changedDate.getMonth());
    }
  }
}
</script>

<template>
  <div v-for="(day, index) in days"
       :key="day"
       class="day-header"
       :class="{ 'no-border-right': (index + 1) % 7 === 0 }">
    {{ day }}
  </div>
  <div v-for="(date, index) in calendar"
       :key="index"
       class="calendar-cell flex justify-center"
       :class="{
             'no-border-right': (index + 1) % 7 === 0,
             'no-border-bottom': index >= calendar.length - 7,
           }">
    <p class="date-number flex justify-center align-center" :class="{ 'today': date && isToday(date.date)}" v-if="date">
      {{ date.label }}
    </p>
    <div v-for="event in getEventsForDate(date.date)"
         :key="event.id"
         class="event-badge flex justify-start gap-2"
         @click="$emit('toggle-view', event.id)">
      <div class="dot"></div>
      <p>{{ event.title }}</p>
    </div>
  </div>
</template>

<style scoped>
  .day-header {
    font-size: 1rem;
    text-align: center;
    font-weight: 400;
    color: var(--color-light-grey);
    border-right: 1px solid var(--color-light-grey);
  }
  .day-header:last-child {
    border-right: none;
  }
  .calendar-cell {
    border-right: 1px solid var(--color-light-grey);
    border-bottom: 1px solid var(--color-light-grey);
    padding: 5px 10px;
    min-height: 150px;
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
  .date-number {
    min-width: 2rem;
    width: max-content;
    height: 2rem;
    border-radius: 50%;
    margin-top: 3px;
    margin-bottom: 3px;
  }
  .dot {
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 50%;
    background-color: var(--color-light-violet);
  }
</style>
