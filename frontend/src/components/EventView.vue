<script setup>
  import { ref, onMounted, defineProps, defineEmits } from "vue";
  import Button from "@/components/Button.vue";

  const props = defineProps({
    event: Object,
    isVisible: Boolean
  });
  const emit = defineEmits(['toggle-view', 'toggle-edit']);

  const close = () => {
    emit('toggle-view', null); // Emit toggle-view event to close the view
  };

  const edit = () => {
    emit('toggle-view', null);
    emit('toggle-edit', props.event);
  }

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
        <Button class="p-4" type="button" @click="edit" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="pencil" />
        </Button>
        <Button class="p-4" type="button" @click="close" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="download" />
        </Button>
        <Button class="p-4" type="button" @click="close" colour="bg-violet" text-color="white">
          <font-awesome-icon icon="xmark" />
        </Button>
      </div>
      <div class="event-details">
        <div class="flex flex-row justify-start gap-3">
          <span :class="`event-type ${props.event.type}`"></span>
          <h1>{{ props.event.title }}</h1>
        </div>
        <div class="flex flex-row justify-start gap-3">
          <span>
            <font-awesome-icon class="icon" icon="clock" />
          </span>
          <p>{{ getDateString(props.event.start_at) }}</p>
        </div>
        <div class="flex flex-row justify-start gap-3 mt-3">
          <span>
            <font-awesome-icon class="icon" icon="location-dot" />
          </span>
          <p>{{ props.event.location }}</p>
        </div>
        <div class="flex flex-row justify-start gap-3 mt-3">
          <span>
            <font-awesome-icon class="icon" icon="note-sticky" />
          </span>
          <p>{{ props.event.description }}</p>
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
  .slide-enter-active,
  .slide-leave-active {
    transition: right 0.3s ease-out;
  }
  .slide-enter-from,
  .slide-leave-to {
    right: -100%;
  }
</style>
