<script setup>
  import { ref, useAttrs, computed } from 'vue'
  import Input from './Input.vue'

  const attrs = useAttrs();
  const emit = defineEmits(["update:modelValue"]);
  const searchQuery = ref('');
  const options = ref([]);

  const initAutoComplete = async () => {
    if(searchQuery.value.length >= 2) {
      const response = await fetch(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(searchQuery.value)}&key=dff04552b6b4486b956bde7409e0bb06&limit=5`);
      const data = await response.json();
      options.value = data.results.map(result => result.formatted);
    }
  }

  const selectOption = (option) => {
    emit("update:modelValue", option);
    searchQuery.value = option;
    options.value = [];
  }
</script>

<template>
  <Input v-model="searchQuery" @input="initAutoComplete" v-bind="attrs" />
  <ul class="options-wrapper" v-if="options.length">
    <li class="option-text" v-for="(option, index) in options" :key="index" @click="selectOption(option)">
      {{ option }}
    </li>
  </ul>
</template>

<style scoped>
  .options-wrapper {
    background-color: var(--color-background-input);
    border-radius: 12px;
    padding-left: 0;
    margin-bottom: 1rem;
  }
  .options-wrapper .option-text {
    color: var(--color-text-input);
    padding: 0.8rem;
    list-style: none;
    border-bottom: 1px solid var(--color-text-input);
  }
  .options-wrapper .option-text:hover {
    cursor: pointer;
  }
  .options-wrapper .option-text:last-child {
    border-bottom: none;
  }
</style>
