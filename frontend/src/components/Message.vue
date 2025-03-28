<script setup>
  import { defineProps, defineEmits, watch } from 'vue';

  const props = defineProps({
    message: String
  });
  const emit = defineEmits(['close-message']);

  watch(() => props.message, (newMessage) => {
    if (newMessage && newMessage.trim() !== '') {
      setTimeout(() => {
        emit('close-message');
      }, 5000);
    }
  });
</script>

<template>
  <div class="message-container flex justify-start align-center" v-if="message">
    <p class="message"> {{ message }} </p>
    <span class="close-message" @click="emit('close-message')">
      <font-awesome-icon icon="xmark" />
    </span>
  </div>
</template>

<style scoped>
  .message-container {
    position: absolute;
    max-width: 600px;
    width: 100%;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    margin: 0 auto;
    background: var(--color-light-violet);
    border-radius: 100px;
    padding: 0.75rem 1rem;
  }
  .message {
    color: var(--color-black);
  }
  .close-message {
    color: var(--color-black);
    margin-left: 0;
  }
</style>
