  <script setup>
    import { ref, onMounted } from "vue";
    import axios from "axios";
    import Button from "@/components/Button.vue";
    import CalendarScheduler from "@/components/CalendarScheduler.vue";
    import EventForm from "@/components/EventForm.vue";
    import EventView from "@/components/EventView.vue";
    import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
    import Message from "@/components/Message.vue";

    const events = ref([]);
    let isEventFormVisible = ref(false);
    let isEventVisible = ref(false);
    const selectedEvent = ref(null);
    const message = ref("");

    onMounted(async () => {
      try {
        // const response = await axios.get('/api/events');
        //
        // if(response && response.status === 200){
        //   events.value = response.data.events.map(event => {
        //     return {
        //       id: event.id,
        //       title: event.title,
        //       location: event.location,
        //       startDate: new Date(event.start_at),
        //       endDate: new Date(event.end_at),
        //       tooltip: event.title,
        //       type: event.type
        //     }
        //   });
        // }
        const tempEvents = [
          {
            "created_at": "2025-03-25T23:20:20",
            "created_by": 1,
            "deleted_at": null,
            "description": "<p>This is event &nbsp;2. Making the event public</p>",
            "end_at": "2025-03-30T13:00:00",
            "id": 2,
            "location": "Brampton, Ontario, Canada",
            "start_at": "2025-03-28T16:00:00",
            "title": "Event 2",
            "type": "public",
            "updated_at": "2025-03-26T00:34:11"
          },
          {
            "created_at": "2025-03-25T23:29:05",
            "created_by": 2,
            "deleted_at": null,
            "description": "<p>This is event 3 at OTU</p>",
            "end_at": "2025-03-27T18:00:00",
            "id": 3,
            "location": "Oshawa, Ontario, Canada",
            "start_at": "2025-03-27T14:00:00",
            "title": "Event 3",
            "type": "private",
            "updated_at": "2025-03-25T23:29:05"
          },
          {
            "created_at": "2025-03-26T00:35:33",
            "created_by": 1,
            "deleted_at": null,
            "description": "<p>Adding last event in list updating this event</p>",
            "end_at": "2025-03-29T04:35:00",
            "id": 5,
            "location": "49800 Toro, Spain",
            "start_at": "2025-03-26T04:35:00",
            "title": "Event 5",
            "type": "private",
            "updated_at": "2025-03-26T17:49:05"
          },
          {
            "created_at": "2025-03-26T17:52:30",
            "created_by": 1,
            "deleted_at": null,
            "description": "<p>This is a test event...</p><p>&nbsp;</p>",
            "end_at": "2025-03-29T14:00:00",
            "id": 6,
            "location": "Ontario Tech University, 2000 Simcoe Street North, Oshawa, ON L1H 7K0, Canada",
            "start_at": "2025-03-27T11:00:00",
            "title": "Test Event",
            "type": "private",
            "updated_at": "2025-03-26T17:52:30"
          }
        ];

        events.value = tempEvents.map(event => {
          return {
            id: event.id,
            title: event.title,
            location: event.location,
            startDate: new Date(event.start_at),
            endDate: new Date(event.end_at),
            tooltip: event.title,
            type: event.type,
            colour: getColour()
          }
        })
      } catch (error) {
        console.log(error);
      }
    });

    const getColour = () => {
      const colors = [
        '--color-blue',
        '--color-pink',
        '--color-lilac',
        '--color-gray',
        '--color-magenta',
        '--color-cyan'
      ];

      return colors[Math.floor(Math.random() * colors.length)];
    };

    const toggleForm = (event = null) => {
      selectedEvent.value = event;
      isEventVisible.value = false;
      isEventFormVisible.value = !isEventFormVisible.value;
    };

    const toggleEvent = async (eventId) => {
      selectedEvent.value = null;

      if(eventId) {
        const response = await axios.get(`/api/event/${eventId}`);

        if(response && response.status === 200){
          selectedEvent.value = {
            id: response.data.event.id,
            title: response.data.event.title,
            description: response.data.event.description,
            location: response.data.event.location,
            type: response.data.event.type,
            startDate: new Date(response.data.event.start_at),
            endDate: new Date(response.data.event.end_at),
            tags: response.data.tags,
            tagCount: response.data.tagCount,
            createdBy: response.data.event.created_by,
            collaborators: response.data.users.map(user => user.user_id)
          };
        }
      }

      isEventVisible.value = !isEventVisible.value;
    };

    const deleteEvent = async (eventId) => {
      const response = await axios.delete(`/api/event/delete/${eventId}`);

      if(response && response.status === 200){
        const index = events.value.findIndex(e => e.id === eventId);
        events.value.splice(index, 1);
      }
    }

    const updateEvents = (event) => {
      const key = events.value.findIndex(e => e.id === event.id);

      if(key === -1) {
        events.value.push({
          id: event.id,
          title: event.title,
          location: event.location,
          startDate: new Date(event.start_at),
          endDate: new Date(event.end_at),
          tooltip: event.title,
          type: event.type
        });
      } else {
        events.value[key] = event;
      }
    }
  </script>

  <template>
    <article class="container bg-black">
      <section class="calendar-operations-wrapper">
        <Button id="add-event"
                :class="['icon-button', isEventFormVisible ? 'hidden' : '']"
                type="button"
                colour="bg-violet"
                text-color="white"
                @click="toggleForm(null)">
          <font-awesome-icon icon="plus" />
        </Button>
      </section>
      <section class="calender-wrapper">
        <CalendarScheduler :events="events" @toggle-view="toggleEvent" />
        <EventForm :is-visible="isEventFormVisible"
                   :event="selectedEvent"
                   @toggle-form="toggleForm(null)"
                   @update-events="updateEvents" />
        <EventView :event="selectedEvent"
                   :is-visible="isEventVisible"
                   @toggle-view="toggleEvent"
                   @toggle-edit="toggleForm"
                   @toggle-delete="deleteEvent"/>
      </section>
      <router-view />
    </article>
    <Message :message="message" />
  </template>

  <style scoped>
    .calendar-operations-wrapper {
      position: absolute;
      bottom: 1rem;
      right: 1rem;
      display: flex;
      flex-flow: row nowrap;
      justify-content: start;
      gap: 1rem;
      z-index: 1;
    }
    .calender-wrapper {
      display: flex;
      flex-flow: row nowrap;
      justify-content: center;
      align-items: center;
    }
  </style>
