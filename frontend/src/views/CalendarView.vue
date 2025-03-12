<script setup>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import Button from "@/components/Button.vue";
  import CalendarScheduler from "@/components/CalendarScheduler.vue";
  import EventForm from "@/components/EventForm.vue";

  const router = useRouter();
  const events = ref([]);
  const isEventFormVisible = ref(false);

  onMounted(async () => {
    try {
      const response = await axios.get('/api/events');

      if(response && response.status === 200) {
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

  const toggleForm = () => {
    isEventFormVisible.value = !isEventFormVisible.value;
  };
</script>

<template>
  <article class="container bg-black calender-container">
    <section class="calendar-operations-wrapper">
      <Button colour="bg-black" text-color="white" @click="toggleForm">
        Add new Event
      </Button>
    </section>
    <section class="calender-wrapper">
      <CalendarScheduler />
      <EventForm :is-visible="isEventFormVisible" />
    </section>
    <router-view />
  </article>
</template>

<style scoped>
  .calendar-operations-wrapper {
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    gap: 1rem;
  }
  .calender-wrapper {
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
  }
</style>
