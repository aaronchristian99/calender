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
      <Day v-if="view === 'day'" :events="events" />
      <Month v-if="view === 'month'" :events="events" />
      <Year v-if="view === 'year'" :events="events" />
    </div>
  </div>
</template>

<script>
  import Button from "@/components/Button.vue";
  import Day from "@/components/Day.vue";
  import Month from "@/components/Month.vue";
  import Year from "@/components/Year.vue";

  export default {
    components: {Button, Day, Month,Year },
    props: {
      events: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        selectedDate: null,
        view: 'month',
        currentDate: new Date()
      };
    },
    methods: {
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

  .month {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    border: 1px solid var(--color-light-grey);
    border-radius: 10px;
  }
</style>
