<template>
  <div class="day-view">
    <div class="schedule-column">
      <div class="date-wrapper">
        <p class="text-center" :class="{ 'today-text': isToday }">{{ days[currentTime.getDay()] }}</p>
        <h3 class="flex justify-center align-center"
            :class="{ 'today-background': isToday }">
          {{ currentTime.getDate() }}
        </h3>
      </div>
      <div v-for="hour in hours" :key="hour" class="schedule-slot">
        <p class="hour-label">{{ formatHour(hour) }}</p>
        <div class="grid-line"></div>
      </div>
      <div class="current-time-line" :style="currentTimeStyle" v-if="isToday">
        <div class="dot"></div>
        <div class="short-line"></div>
      </div>
      <div v-for="event in getEventsForDate(currentTime)"
           :key="event.id"
           class="event"
           :style="eventStyle(event)"
           @click="$emit('toggle-view', event.id)">
        <p>{{ event.title }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Day',
  props: {
    events: Array,
    date: Date,
    days: Array
  },
  data() {
    return {
      hours: Array.from({ length: 24 }, (_, i) => i),
      currentTime: new Date()
    };
  },
  computed: {
    currentTimeStyle() {
      const now = new Date();
      const totalMinutes = now.getHours() * 60 + now.getMinutes();
      const percentage = (totalMinutes / (24 * 60)) * 100;
      return { top: `${percentage}%` };
    },
    eventStyle() {
      return (event) => {
        const start = new Date(event.startDate);
        const end = new Date(event.endDate);
        console.log(start.getHours());
        const startMinutes = start.getHours() * 60 + start.getMinutes();
        console.log('start minutes: ', startMinutes);
        const endMinutes = end.getHours() * 60 + end.getMinutes();
        console.log('end minutes: ', endMinutes);
        const top = (startMinutes / (24 * 60)) * 100;
        const height = ((endMinutes - startMinutes) / (24 * 60)) * 100;
        console.log('top: ', top);
        console.log('height: ', height);
        return {
          top: `calc(${top}% + 70px)`,
          height: `${height}%`,
          backgroundColor: `var(${event.colour})`
        };
      };
    },
    isToday() {
      const today = new Date();
      return today.getFullYear() === this.currentTime.getFullYear() &&
            today.getMonth() === this.currentTime.getMonth() &&
            today.getDate() === this.currentTime.getDate();
    }
  },
  mounted() {
    this.updateTime();
  },
  methods: {
    updateTime() {
      this.currentTime = new Date();
    },
    formatHour(hour) {
      const period = hour < 12 ? "AM" : "PM";
      const formattedHour = hour % 12 === 0 ? 12 : hour % 12;
      return `${formattedHour} ${period}`;
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
      this.currentTime = new Date(newDate);
    }
  }
};
</script>

<style scoped>
  .day-view {
    display: flex;
    overflow-y: auto;
  }

  .schedule-column {
    width: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
  }

  .schedule-slot {
    display: flex;
    align-items: center;
    position: relative;
    min-height: 80px;
  }

  .hour-label {
    width: 50px;
    text-align: right;
    padding-right: 10px;
    font-size: 12px;
    color: var(--color-light-grey);
  }

  .grid-line {
    flex-grow: 1;
    height: 1px;
    background: var(--color-light-grey);
  }

  .current-time-line {
    position: absolute;
    left: 50px;
    width: calc(100% - 50px);
    height: 2px;
    background: var(--color-light-violet);
    display: flex;
    align-items: center;
    z-index: 10;
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

  .event {
    position: absolute;
    left: 60px;
    width: calc(100% - 60px);
    background: rgba(0, 123, 255, 0.7);
    color: white;
    padding: 5px;
    border-radius: 4px;
    font-size: 14px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  }

  .event p {
    font-size: 0.8rem;
  }

  .event:hover {
    cursor: pointer;
  }

  .date-wrapper {
    width: max-content;
    min-width: 3.5rem;
    height: 3.5rem;
    margin-bottom: 2rem;
  }

  .text-center {
    text-align: center;
  }

  .today-text {
    color: var(--color-violet);
  }

  .today-background {
    width: 100%;
    height: 100%;
    background-color: var(--color-violet);
    color: var(--color-white);
    border-radius: 50%;
  }
</style>
