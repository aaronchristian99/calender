<template>
  <div class="spinner-container">
    <span class="spinner">
      <font-awesome-icon icon="circle-notch" spin />
    </span>
  </div>
</template>

<style scoped>
  .spinner-container {
    position: absolute;
    top: 0;
    left: 0;
    background: rgba(28, 19, 36, 0.85);
    width: 100%;
    height: 100%;
  }
  .spinner {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 2rem;
  }
</style>
