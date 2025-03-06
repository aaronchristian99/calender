<script setup>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import { CalendarView as Calendar } from "vue-simple-calendar";
  import CalendarViewHeader from "@/components/CalendarViewHeader.vue";
  import "../../node_modules/vue-simple-calendar/dist/style.css";
  import Button from "@/components/Button.vue";

  const router = useRouter();
  const showDate = ref(new Date());
  const period = ref('month');
  const events = ref([]);
  const createEventHref = ref(router.resolve({ name: "createEvent" } ).href);

  onMounted(async () => {
    try {
      const response = await axios.get('/api/events');

      if(response.status === 200) {
        events.value = response.data.events.map(event => {
          return {
            id: event.id,
            title: event.title,
            location: event.location,
            startDate: new Date(event.time),
            endDate: new Date(event.time),
            tooltip: event.title,
            url: router.resolve({ name: "event", params: { id: event.id } })
          }
        });
        console.log(events.value);
      }
    } catch (error) {
      console.log(error);
    }
  });

  const setShowDate = (date) => {
    showDate.value = date;
  };

  const changeView = (newPeriod) => {
    period.value = newPeriod;
  }

  const isToday = (date) => {
    const today = new Date();
    return (
      date.getDate() === today.getDate() &&
      date.getMonth() === today.getMonth() &&
      date.getFullYear() === today.getFullYear()
    );
  };
</script>

<template>
  <article class="container bg-black calender-container">
    <section class="calendar-operations-wrapper">
      <Button label="Add new Event" colour="bg-black" text-color="white" route-name="" type="a" />
      <Button label="Upload" colour="bg-violet" text-color="white" type="button" @click="uploadEvent" />
    </section>
    <section class="calender-wrapper">
      <Calendar :show-date="showDate"
                :displayPeriodUom="period"
                :items="events"
                class="calendar theme-default holiday-us-official">
        <template #header="{ headerProps }">
          <CalendarViewHeader :header-props="headerProps" @input="setShowDate" @changeView="changeView" />
        </template>
        <template #day-content="{ day }">
          <div class="day-cell" :day :class="{ 'highlight-today': isToday(day) }">
            {{ day.getDate() }}
          </div>
        </template>
      </Calendar>
    </section>
    <router-view />
  </article>
</template>

<style scoped>
  .calender-container {
    width: 100%;
    height: 100%;
    padding: 0 1.5rem;
  }

  .calender-wrapper .calendar {
    background: var(--color-background);
    border-radius: 10px;
    width: 100%;
    height: 100%;
  }

  .calendar-operations-wrapper {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-items: center;
    gap: 1rem;
    padding: 2rem 0;
  }
</style>
