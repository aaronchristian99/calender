<template>
  <div class="calendar-container">
    <div class="calendar-header flex flex-row justify-between align-center">
      <div class="flex flex-row justify-start align-center gap-4">
        <Button type="button" colour="bg-violet" text-color="white" @click="goToToday">
          Today
        </Button>
        <div class="flex flex-row justify-start align-center gap-2">
          <Button type="button" colour="bg-violet" text-color="white" @click="previousWeek">
            <font-awesome-icon icon="chevron-left" />
          </Button>
          <Button type="button" colour="bg-violet" text-color="white" @click="nextWeek">
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
          'today': isToday(date)
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
      view: 'week',
      currentDate: new Date(),
      today: new Date(),
      startOfWeek: new Date(),
      endOfWeek: new Date(),
    };
  },
  created() {
    this.generateWeek();
  },
  methods: {
    generateWeek(date = this.today) {
      const startOfWeek = date.getDate() - date.getDay();
      const targetYear = date.getFullYear();
      const targetMonth = date.getMonth();

      this.calendar = [];
      
      for (let i = 0; i < 7; i++) {
        const day = new Date(targetYear, targetMonth, startOfWeek + i);
        this.calendar.push(day);
      }

      this.currentDate = new Date(targetYear, targetMonth, date.getDate());

      this.startOfWeek = this.calendar[0];
      this.endOfWeek = this.calendar[6]; 
    },
    isToday(date) {
      return date.getDate() === this.today.getDate() &&
        date.getMonth() === this.today.getMonth() &&
        date.getFullYear() === this.today.getFullYear();
    },
    changeView() {
      console.log(this.view);
    },
    previousWeek() {
      const newDate = new Date(this.currentDate);
      newDate.setDate(newDate.getDate() - 7);
      this.generateWeek(newDate);
    },
    nextWeek() {
      const newDate = new Date(this.currentDate);
      newDate.setDate(newDate.getDate() + 7);
      this.generateWeek(newDate);
    },
    goToToday() {
      this.generateWeek();
    },
    getEventsForDate(date) {
      if (!date) {
        return;
      }

      return this.events.filter(event => {
        const eventDate = new Date(event.start_at);
        return eventDate.getDate() === date.getDate() &&
          eventDate.getMonth() === date.getMonth() &&
          eventDate.getFullYear() === date.getFullYear();
      });
    }
  },
  computed: {
    currentDate() {
      const startMonth = this.startOfWeek.getMonth();
      const endMonth = this.endOfWeek.getMonth();
      const startYear = this.startOfWeek.getFullYear();
      const endYear = this.endOfWeek.getFullYear();

      if (startMonth !== endMonth) {
        const startMonthName = this.startOfWeek.toLocaleString('default', { month: 'long' });
        const endMonthName = this.endOfWeek.toLocaleString('default', { month: 'long' });

      if (startYear !== endYear) {
        return `${startMonthName} ${startYear} - ${endMonthName} ${endYear}`;
      }
      
        return `${startMonthName} - ${endMonthName} ${startYear}`;
      }
        
      return this.currentDate.toLocaleDateString(undefined, {month: 'long', year: 'numeric'});
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
    appearance: none;
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
    pointer-events: none;
    color: var(--color-light-grey);
    font-size: 1.2rem;
  }
  .calendar {
    display: grid;
    border: 1px solid var(--color-light-grey);
    border-radius: 10px;
  }
  .calendar.week {
    grid-template-columns: repeat(7, 1fr);
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