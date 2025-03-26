<script setup>
  import { ref, defineProps, defineEmits } from "vue";
  import Button from "@/components/Button.vue";

  const props = defineProps({
    event: Object,
    isVisible: Boolean
  });
  const emit = defineEmits(['toggle-view', 'toggle-edit']);
  const user = ref(JSON.parse(localStorage.getItem("user")));

  const close = () => {
    emit('toggle-view', null); // Emit toggle-view event to close the view
  };

  const edit = () => {
    emit('toggle-view', null);
    emit('toggle-edit', props.event);
  }

  const deleteEvent = () => {
    emit('toggle-view', null);
    emit('toggle-delete', props.event.id);
  }

  const download = () => {
    const icsContent = `BEGIN:VCALENDAR
                        VERSION:2.0
                        PRODID:-//My Calendar App//EN
                        BEGIN:VEVENT
                        UID:${new Date().getTime()}@myapp.com
                        DTSTAMP:${formatDate(new Date())}
                        DTSTART:${formatDate(props.event.startDate)}
                        DTEND:${formatDate(props.event.endDate)}
                        SUMMARY:${props.event.title}
                        DESCRIPTION:${props.event.description}
                        LOCATION:${props.event.location}
                        END:VEVENT
                        END:VCALENDAR`;

    const blob = new Blob([icsContent], { type: "text/calendar" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "event.ics";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  const formatDate = (date) => {
    return date.toISOString().replace(/[-:]/g, "").split(".")[0] + "Z";
  };

  const getDateString = (date) => {
    const options = {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    };
    return new Date(date).toLocaleDateString('en', options);
  }
</script>

<template>
  <Transition name="slide">
    <section v-if="isVisible" class="form-container">
      <div class="flex flex-row justify-end align-center gap-3 align-self-end">
        <Button class="p-4"
                type="button"
                v-if="user.id === event.createdBy"
                @click="edit"
                colour="bg-violet"
                text-color="white">
          <font-awesome-icon icon="pencil" />
        </Button>
        <Button class="p-4"
                type="button"
                v-if="user.id === event.createdBy"
                @click="deleteEvent"
                colour="bg-violet"
                text-color="white">
          <font-awesome-icon icon="trash" />
        </Button>
        <Button class="p-4" type="button" @click="download" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="download" />
        </Button>
        <Button class="p-4" type="button" @click="close" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="xmark" />
        </Button>
      </div>
      <div class="event-details">
        <div>
          <p>Tag Count: <span>{{ event.tagCount }}</span></p>
        </div>
        <div class="flex flex-row wrap justify-start gap-2 mt-3">
          <span class="event-tag" v-for="tag in event.tags" :key="tag">
            {{ tag }}
          </span>
        </div>
        <div class="flex flex-row justify-start align-center gap-3 mt-3">
          <span :class="`event-type ${props.event.type}`"></span>
          <h1>{{ props.event.title }}</h1>
        </div>
        <div class="flex flex-row justify-start align-center gap-3">
          <span>
            <font-awesome-icon class="icon" icon="clock" />
          </span>
          <p>{{ getDateString(props.event.startDate) }}</p>
        </div>
        <div class="flex flex-row justify-start align-center gap-3 mt-3">
          <span>
            <font-awesome-icon class="icon" icon="location-dot" />
          </span>
          <p>{{ props.event.location }}</p>
        </div>
        <div class="flex flex-row justify-start align-center gap-3 mt-3">
          <span>
            <font-awesome-icon class="icon" icon="note-sticky" />
          </span>
          <div v-html="props.event.description"></div>
        </div>
      </div>
    </section>
  </Transition>
</template>

<style scoped>
  .form-container {
    position: relative;
    max-width: 650px;
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
    right: 0;
    padding: 0 2rem;
  }
  .icon {
    font-size: 2rem;
    color: var(--color-light-grey);
  }
  .event-details {
    width: 100%;
  }
  .event-tag {
    background-color: var(--color-dark-grey);
    color: var(--color-light-grey);
    padding: 0.5rem;
    border-radius: 100px;
  }
  .event-type {
    width: clamp(2rem, 2vw, 4rem);
    height: clamp(2rem, 2vw, 4rem);
    border-radius: 100%;
  }
  .event-type.private {
    background-color: var(--color-violet);
  }
  .event-type.public {
    background-color: var(--color-light-violet);
  }
  .slide-enter-active,
  .slide-leave-active {
    transition: right 0.3s ease-out;
  }
  .slide-enter-from,
  .slide-leave-to {
    right: -100%;
  }
</style>
