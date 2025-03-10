<script setup>
  import { ref, onMounted } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import Button from "@/components/Button.vue";
  import CalendarScheduler from "@/components/CalendarScheduler.vue";
  import EventForm from "@/components/EventForm.vue";

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
</script>

<template>
  <article class="container bg-black calender-container">
    <section class="calendar-operations-wrapper">
      <Button label="Add new Event" colour="bg-black" text-color="white" route-name="" type="a" />
      <Button label="Upload" colour="bg-violet" text-color="white" type="button" @click="uploadEvent" />
    </section>
    <section class="calender-wrapper">
      <CalendarScheduler />
      <EventForm />
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
