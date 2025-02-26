<script setup>
  defineProps(["headerProps"]);
  const emit = defineEmits(["input"]);
</script>

<template>
  <div class="calendar-header">
    <!-- Periods -->
    <div class="period">
      <ul>
        <li @click="emit('changeView', 'day')">Day</li>
        <li @click="emit('changeView', 'week')">Week</li>
        <li @click="emit('changeView', 'month')">Month</li>
        <li @click="emit('changeView', 'year')">Year</li>
      </ul>
    </div>
    <!-- Navigation -->
    <div class="navigation">
      <button @click="emit('input', headerProps.previousPeriod)">⬅️</button>
      <button @click="emit('input', new Date())">Today</button>
      <button @click="emit('input', headerProps.nextPeriod)">➡️</button>
    </div>

    <!-- Display Current Period -->
    <div class="current-period">
      {{ headerProps.periodLabel }}
    </div>
  </div>
</template>

<style scoped>
.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background: #333;
  color: white;
}

.navigation button {
  margin: 0 5px;
  padding: 5px 10px;
  border: none;
  background: #555;
  color: white;
  cursor: pointer;
  border-radius: 5px;
}

.period ul {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 0;
  border-radius: 8px;
  background-color: #555;
}

.period ul li {
  padding: 10px;
  color: #fff;
  cursor: pointer;
  list-style: none;
  border-right: 1px solid #fff;
}

.period ul li:last-child {
  border-right: none;
}
</style>
