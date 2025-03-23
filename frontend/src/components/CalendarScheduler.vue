<template>
  <div class="calendar-container">
    <div class="calendar-header flex flex-row justify-between align-center">
      <div class="flex flex-row justify-start align-center gap-4">
        <Button type="button" colour="bg-violet" text-color="white" @click="goToToday">
          Today
        </Button>
        <div class="flex flex-row justify-start align-center gap-2">
          <Button type="button" colour="bg-violet" text-color="white" @click="previousPeriod">
            <font-awesome-icon icon="chevron-left" />
          </Button>
          <Button type="button" colour="bg-violet" text-color="white" @click="nextPeriod">
            <font-awesome-icon icon="chevron-right" />
          </Button>
        </div>
        <div class="current-date">
          <h3>{{ currentDate }}</h3>
        </div>
      </div>
      <div class="flex flex-row justify-start align-center gap-2">
        <div class="select-wrapper">
          <select v-model="view" @change="changeView">
            <option value="day">Day</option>
            <option value="week">Week</option>
            <option value="month">Month</option>
            <option value="year">Year</option>
          </select>
          <font-awesome-icon icon="angle-down" class="select-icon" />
        </div>
      </div>
    </div>
    <div :class="`calendar ${view}`">
      <div v-for="day in days" :key="day" class="day-header">{{ day }}</div>
      <div
        v-for="(date, index) in calendar"
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
             @click="$emit('toggle-view', event)">
          <p>
            {{ event.title }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "@/components/Button.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

export default {
  components: {FontAwesomeIcon, Button},
  props: {
    events: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      calendar: [],
      selectedDate: null,
      view: 'month',
      currentDate: new Date()
    };
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
    changeView() {
      console.log(this.view);
    },
    previousPeriod() {
      let newMonth = this.currentDate.getMonth() - 1;
      let newYear = this.currentDate.getFullYear();

      if (newMonth < 0) {
        newMonth = 11;
        newYear -= 1;
      }

      this.generateCalendar(newYear, newMonth);
    },
    nextPeriod() {
      let newMonth = this.currentDate.getMonth() + 1;
      let newYear = this.currentDate.getFullYear();

      if (newMonth > 11) {
        newMonth = 0;
        newYear += 1;
      }

      this.generateCalendar(newYear, newMonth);
    },
    goToToday() {
      const today = new Date();
      this.generateCalendar(today.getFullYear(), today.getMonth());
    },
    getEventsForDate(date) {
      if(!date) {
        return;
      }

      return this.events.filter(event => {
        const eventDate = new Date(event.start_at);

        return (eventDate.getDate() === date.getDate() && eventDate.getMonth() === date.getMonth() && eventDate.getFullYear() === date.getFullYear())
      });
    }
  },
  computed: {
    currentDate() {
      const options = {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      };
      return this.currentDate.toLocaleDateString(undefined, options);
    }
  }
};
</script>

<style scoped>
  .calendar-container {
    max-width: 75vw;
    width: 100%;
    height: 100%;
    margin: auto;
    padding: 20px;
  }
  .calendar-header {
    margin: 1rem 0;
  }
  .select-wrapper {
    position: relative;
    display: inline-block;
    width: 100%;
  }
  .select-wrapper select {
    width: 100%;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    background-color: var(--color-dark-grey);
    border: none;
    color: var(--color-light-grey);
    font-size: 1rem;
    line-height: 1.5rem;
    min-height: 58px;
    appearance: none; /* Removes default browser styling */
    -webkit-appearance: none;
    -moz-appearance: none;
    padding-right: 3rem;
    cursor: pointer;
  }
  .select-wrapper .select-icon {
    position: absolute;
    right: 1rem;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none; /* Prevent click interference */
    color: var(--color-light-grey); /* Match the theme */
    font-size: 1.2rem;
  }
  .calendar {
    display: grid;
    border: 1px solid var(--color-light-grey);
    border-radius: 10px;
  }
  .calendar.month {
    grid-template-columns: repeat(7, 1fr);
  }
  .calendar.day {
    grid-template-rows: repeat(24, 1fr);
  }
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
    background-color: var(--color-violet);
    color: var(--color-whitebutton);
    padding: 4px 8px;
    border-radius: 5px;
    margin-top: 5px;
    font-size: 0.8rem;
    text-align: center;
  }
  .event-badge:hover {
    cursor: pointer;
  }
  .today {
    background-color: var(--color-violet);
    color: var(--color-white);
  }
</style>
