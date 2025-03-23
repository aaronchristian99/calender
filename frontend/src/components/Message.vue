<script setup>
  import { ref, defineProps } from 'vue';
  import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

  const props = defineProps({
    message: String
  });
</script>

<template>
  <div class="message-container flex justify-start align-center">
    <p class="message"> {{ message }} </p>
    <span class="close-message">
      <font-awesome-icon icon="xmark" />
    </span>
  </div>
</template>

<style scoped>
  .message-container {
    max-width: 600px;
    position: relative;
    bottom: 1.5rem;
    margin: 0 auto;
    background: var(--color-light-violet);
    border-radius: 50%;
    padding: 0.75rem 1rem;
  }
  .message {
    color: var(--color-black);
  }
  .close-message {
    color: var(--color-black);
  }
</style>
