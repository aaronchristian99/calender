<template>
  <div class="year-view">
    <div v-for="month in months" :key="month.name" class="month">
      <h3 class="month-title">{{ month.name }}</h3>
      <div class="month-grid">
        <div
          v-for="day in month.days"
          :key="day"
          class="day-box"
          :class="{'current-day': isCurrentDay(month.name, day)}">
          {{ day }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Year',
  data() {
    return {
      months: Array.from({ length: 12 }, (_, i) => ({
        name: new Date(2025, i).toLocaleString('default', { month: 'long' }),
        days: Array.from({ length: new Date(2025, i + 1, 0).getDate() }, (_, d) => d + 1),
      })),
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
  },
};
</script>

<style scoped>

.year-view {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  font-family: Arial, sans-serif;
  padding: 10px;
}

/* 4x3 month grid */
.month {
  width: 22%;
  height: calc(33.3% - 20px);
  border: 1px solid #a855f7;
  border-radius: 8px;
  background: #f9f9f9;
  padding: 10px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 10px;
}

.month-title {
  text-align: center;
  font-size: 16px;
  color: #333;
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
  color: #333;
  background-color: #f9f9f9;
  cursor: pointer;
}

/* Violet highlight for the current day */
.current-day {
  border: 2px solid #a855f7 !important; /* Hardcoded violet border */
  color: #a855f7 !important; /* Hardcoded violet text */
  font-weight: bold;
  background-color: #ffffff;
}
</style>
