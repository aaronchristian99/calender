  <script setup>
    import { ref, onMounted } from "vue";
    import { useRouter } from "vue-router";
    import axios from "axios";
    import Button from "@/components/Button.vue";
    import CalendarScheduler from "@/components/CalendarScheduler.vue";
    import EventForm from "@/components/EventForm.vue";
    import EventView from "@/components/EventView.vue";
    import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
    import Message from "@/components/Message.vue";

    const router = useRouter();
    const events = ref([]);
    let isEventFormVisible = ref(false);
    let isEventVisible = ref(false);
    const selectedEvent = ref(null);
    const message = ref("");

    onMounted(async () => {
      try {
        const response = await axios.get('/api/events');

        if(response && response.status === 200) {
          events.value = response.data.events.map(event => {
            return {
              id: event.id,
              title: event.title,
              location: event.location,
              startDate: new Date(event.start_at),
              endDate: new Date(event.end_at),
              tooltip: event.title,
              type: event.type
            }
          });
        }
      } catch (error) {
        console.log(error);
      }
    });

    const toggleForm = (event = null) => {
      selectedEvent.value = event;
      isEventVisible.value = false;
      isEventFormVisible.value = !isEventFormVisible.value;
    };

    const toggleEvent = (event) => {
      selectedEvent.value = event;
      isEventVisible.value = !isEventVisible.value;
    };

    const updateEvents = (event) => {
      const key = events.value.findIndex(e => e.id === event.id);

      if(key === -1) {
        events.value.push(event);
      } else {
        events.value[key] = event;
      }
    }
  </script>

  <template>
    <article class="container bg-black">
      <section class="calendar-operations-wrapper">
        <Button id="add-event" :class="['icon-button', isEventFormVisible ? 'hidden' : '']" type="button" colour="bg-violet" text-color="white" @click="toggleForm">
          <font-awesome-icon icon="plus" />
        </Button>
      </section>
      <section class="calender-wrapper">
        <CalendarScheduler :events="events" @toggle-view="toggleEvent(null)" />
        <EventForm :is-visible="isEventFormVisible" @toggle-form="toggleForm(null)" :event="selectedEvent" @update-events="updateEvents" />
        <EventView :event="selectedEvent" :is-visible="isEventVisible" @toggle-view="toggleEvent" @toggle-edit="toggleForm" />
      </section>
      <router-view />
    </article>
    <Message :message="message" />
  </template>

  <style scoped>
    .calendar-operations-wrapper {
      display: flex;
      flex-flow: row nowrap;
      justify-content: start;
      gap: 1rem;
    }
    .calender-wrapper {
      display: flex;
      flex-flow: row nowrap;
      justify-content: center;
      align-items: center;
    }
    #add-event {
      position: absolute;
      bottom: 1rem;
      right: 1rem;
    }
  </style>
