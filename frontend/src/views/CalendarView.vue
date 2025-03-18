  <script setup>
    import { ref, onMounted } from "vue";
    import { useRouter } from "vue-router";
    import axios from "axios";
    import Button from "@/components/Button.vue";
    import CalendarScheduler from "@/components/CalendarScheduler.vue";
    import EventForm from "@/components/EventForm.vue";
    import EventView from "@/components/EventView.vue";

    const router = useRouter();
    const events = ref([
      { id: 1, title: 'Meeting', start_at: '2025-03-12T10:00:00', location: 'Office', description: 'Project discussion' },
      { id: 2, title: 'Conference', start_at: '2025-03-15T14:00:00', location: 'Downtown', description: 'Tech event' }
    ]);
    let isEventFormVisible = ref(false);
    let isEventVisible = ref(false);
    const selectedEvent = ref(null);

    // onMounted(async () => {
    //   try {
    //     const response = await axios.get('/api/events');
    //
    //     if(response && response.status === 200) {
    //       events.value = response.data.events.map(event => {
    //         return {
    //           id: event.id,
    //           title: event.title,
    //           location: event.location,
    //           startDate: new Date(event.time),
    //           endDate: new Date(event.time),
    //           tooltip: event.title,
    //           url: router.resolve({ name: "event", params: { id: event.id } })
    //         }
    //       });
    //       console.log(events.value);
    //     }
    //   } catch (error) {
    //     console.log(error);
    //   }
    // });

    const toggleForm = () => {
      isEventFormVisible.value = !isEventFormVisible.value;
    };
    const toggleEvent = (event) => {
      selectedEvent.value = event;
      isEventVisible.value = !isEventVisible.value;
    };
  </script>

  <template>
    <article class="container bg-black">
      <section class="calendar-operations-wrapper">
        <Button type="button" colour="bg-violet" text-color="white" @click="toggleForm">
          Add new Event
        </Button>
      </section>
      <section class="calender-wrapper">
        <CalendarScheduler :events="events" @toggle-view="toggleEvent" />
        <EventForm :is-visible="isEventFormVisible" @toggle-form="toggleForm" />
        <EventView :event="selectedEvent" :is-visible="isEventVisible" @toggle-view="toggleEvent" />
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
