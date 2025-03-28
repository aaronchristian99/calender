<template>
  <div class="year-view">
    <div v-for="month in months" :key="month.name" class="month">
      <h3 class="month-title">{{ month.name }}</h3>
      <div class="month-grid">
        <p class="day-box" v-for="(day, index) in days" :key="index">{{ day }}</p>
        <p
          v-for="day in month.days"
          :key="day.date"
          class="day-box"
          :class="{'current-day': day.isToday }">
          {{ day.date }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Year',
  props: {
    events: Array,
    date: Date,
    days: Array
  },
  data() {
    return {
      months: this.generateYearlyCalendar(new Date(this.date).getFullYear())
    };
  },
  computed: {
    currentDay() {
      return new Date().getDate();
    },
    currentMonth() {
      return new Date().toLocaleString('default', { month: 'long' });
    },
  },
  methods: {
    isCurrentDay(monthName, day) {
      return monthName === this.currentMonth && day === this.currentDay;
    },
    generateYearlyCalendar(year) {
      return Array.from({ length: 12 }, (_, i) => {
        const firstDayOfMonth = new Date(year, i, 1).getDay(); // 0 = Sunday, 6 = Saturday
        const daysInMonth = new Date(year, i + 1, 0).getDate();

        // Get previous month's days if the current month starts mid-week
        const prevMonthDays = [];
        if (firstDayOfMonth > 0) {
          const lastDayOfPrevMonth = new Date(year, i, 0).getDate();
          for (let j = firstDayOfMonth - 1; j >= 0; j--) {
            prevMonthDays.push({
              date: lastDayOfPrevMonth - j,
              isToday: false,
            });
          }
        }

        // Get current month's days
        const currentMonthDays = Array.from({ length: daysInMonth }, (_, d) => {
          const today = new Date();
          const date = new Date(year, i, d + 1);
          return {
            date: d + 1,
            isToday: date.getFullYear() === today.getFullYear() && date.getMonth() === today.getMonth() && date.getDate() === today.getDate()
          }
        });

        return {
          name: new Date(year, i).toLocaleString("default", { month: "long" }),
          days: [...prevMonthDays, ...currentMonthDays]
        };
      });
    }
  },
  watch: {
    date(newDate) {
      const year = new Date(newDate).getFullYear();
      this.months = this.generateYearlyCalendar(year);
    }
  }
};
</script>

<style scoped>
  .year-view {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    overflow: hidden;
    font-family: Arial, sans-serif;
  }

  /* 4x3 month grid */
  .month {
    width: 24%;
    min-height: calc(33.3% - 20px);
    border: 1px solid var(--color-light-grey);
    border-radius: 8px;
    padding: 10px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 1.5rem;
  }

  .month-title {
    text-align: center;
    font-size: 16px;
    color: var(--color-light-grey);
    margin-bottom: 5px;
  }

  /* days grid */
  .month-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    width: 100%;
    gap: 2px;
    grid-auto-rows: 30px;
  }

  /* the days are circles not squares */
  .day-box {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    color: var(--color-light-grey);
    cursor: pointer;
  }

  /* Violet highlight for the current day */
  .current-day {
    color: var(--color-white);
    background-color: var(--color-violet);
  }
</style>
