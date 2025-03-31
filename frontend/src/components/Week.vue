<template>
  <div class="week-view">
    <div class="schedule-column">
      <div v-for="hour in hours" :key="hour" class="schedule-slot">
        <p class="hour-label">{{ formatHour(hour) }}</p>
        <div class="grid-line"></div>
      </div>
    </div>
    <div class="week-wrapper">
      <div v-for="(day, index) in days"
           :key="day"
           class="day-header"
           :class="{ 'no-border-right': (index + 1) % 7 === 0 }">
        {{ day }}
      </div>
      <div
        v-for="(date, index) in calendar"
        :key="index"
        class="calendar-cell flex justify-center"
        :class="{
          'no-border-right': (index + 1) % 7 === 0,
          'no-border-bottom': index >= calendar.length - 7
        }">
        <p class="date-number flex justify-center align-center"
           :class="{ 'today': date && isToday(date) }"
           v-if="date">
          {{ date.getDate() }}
        </p>
        <div class="current-time-line" :style="currentTimeStyle" v-if="isToday(date)">
          <div class="dot"></div>
          <div class="short-line"></div>
        </div>
        <div v-for="event in getEventsForDate(date)"
             :key="event.id"
             class="event"
             :style="eventStyle(event)"
             @click="$emit('toggle-view', event.id)">
          <p>{{ event.title }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  props: {
    events: {
      type: Array,
      required: true
    },
    days: Array,
    date: Date,
  },
  data() {
    return {
      calendar: [],
      currentDate: new Date(),
      hours: Array.from({ length: 24 }, (_, i) => i),
      startOfWeek: new Date(),
      endOfWeek: new Date()
    };
  },
  created() {
    this.generateWeek();
  },
  methods: {
    generateWeek(date = this.currentDate) {
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
      const today = new Date();
      return date.getDate() === today.getDate() &&
        date.getMonth() === today.getMonth() &&
        date.getFullYear() === today.getFullYear();
    },
    getEventsForDate(date) {
      if(!date) {
        return;
      }

      return this.events.filter(event => {
        const eventDate = event.startDate;
        return (eventDate.getDate() === date.getDate() && eventDate.getMonth() === date.getMonth() && eventDate.getFullYear() === date.getFullYear())
      });
    },
    formatHour(hour) {
      const period = hour < 12 ? "AM" : "PM";
      const formattedHour = hour % 12 === 0 ? 12 : hour % 12;
      return `${formattedHour} ${period}`;
    },
  },
  computed: {
    currentDate() {
      const startMonth = this.startOfWeek.getMonth();
      const endMonth = this.endOfWeek.getMonth();
      const startYear = this.startOfWeek.getFullYear();
      const endYear = this.endOfWeek.getFullYear();

      if (startMonth !== endMonth) {
        const startMonthName = this.startOfWeek.toLocaleString('default', {month: 'long'});
        const endMonthName = this.endOfWeek.toLocaleString('default', {month: 'long'});

        if (startYear !== endYear) {
          return `${startMonthName} ${startYear} - ${endMonthName} ${endYear}`;
        }

        return this.currentDate.toLocaleDateString(undefined, {month: 'long', year: 'numeric'});
      }
    },
    currentTimeStyle() {
      const now = new Date();
      const totalMinutes = now.getHours() * 60 + now.getMinutes();
      const percentage = (totalMinutes / (24 * 60)) * 100;
      return { top: `calc(${percentage}% + 50px)` };
    },
    eventStyle() {
      return (event) => {
        console.log(event);
        const start = new Date(event.startDate);
        const end = new Date(event.endDate);
        const startMinutes = start.getHours() * 60 + start.getMinutes();
        const endMinutes = end.getHours() * 60 + end.getMinutes();
        const top = (startMinutes / (24 * 60)) * 100;
        const height = ((endMinutes - startMinutes) / (24 * 60)) * 100;
        return {
          top: `calc(${top}% + 52px)`,
          height: `${height}%`,
          backgroundColor: `var(${event.colour})`
        };
      };
    }
  },
  watch: {
    date(newDate) {
      this.generateWeek(new Date(newDate));
    }
  }
}
</script>

<style scoped>
  .week-view {
    display: flex;
    flex-flow: row nowrap;
    overflow-y: auto;
  }
  .schedule-column {
    width: 50px;
    display: flex;
    flex-direction: column;
    position: relative;
    margin-top: 50px;
  }

  .schedule-slot {
    display: flex;
    align-items: center;
    position: relative;
    min-height: 80px;
  }

  .hour-label {
    text-align: right;
    padding-right: 10px;
    font-size: 12px;
    color: var(--color-light-grey);
  }

  .current-time-line {
    position: absolute;
    left: 0;
    width: 100%;
    height: 2px;
    background: var(--color-light-violet);
    display: flex;
    align-items: center;
    z-index: 10;
  }

  .grid-line {
    position: absolute;
    width: calc(100vw - 90px);
    z-index: 100;
    right: 0;
    left: 100%;
    flex-grow: 1;
    height: 1px;
    background: var(--color-light-grey);
  }

  .short-line {
    flex-grow: 1;
    height: 2px;
    background: var(--color-light-violet);
  }

  .dot {
    width: 8px;
    height: 8px;
    background: var(--color-light-violet);
    border-radius: 50%;
    position: absolute;
    left: -4px;
  }
  .week-wrapper {
    width: 100%;
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-template-rows: max-content 1fr;
    border: 1px solid var(--color-light-grey);
    border-radius: 10px;
  }
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
    position: relative;
  }
  .no-border-right {
    border-right: none;
  }
  .no-border-bottom {
    border-bottom: none;
  }
  .event {
    position: absolute;
    left: 0;
    width: 100%;
    min-height: 30px;
    padding: 5px;
    border-radius: 4px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  }
  .event p {
    font-size: 0.8rem;
  }
  .event:hover {
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
</style>
