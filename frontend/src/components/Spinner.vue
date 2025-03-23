<script setup>
  import { defineProps } from 'vue';

  const props = defineProps({
    show: Boolean
  });
</script>

<template>
  <div class="spinner-container">
    <span class="spinner">
      <font-awesome-icon icon="circle-notch" spin />
    </span>
  </div>
</template>

<style scoped>
  .spinner-container {
    position: relative;
    background-color: var(--color-black);
    opacity: 0.5;
    width: 100%;
    height: 100%;
  }
  .spinner {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 1.2rem;
  }
</style>
