<script setup>
  import { ref, useAttrs, watch, defineProps } from 'vue'
  import Input from './Input.vue'
  import axios from "axios";

  const attrs = useAttrs();
  const emit = defineEmits(["update:modelValue"]);
  const props = defineProps({
    modelValue: String
  });
  const searchQuery = ref('');
  const options = ref([]);
  const isOpen = ref(false);

  watch(searchQuery, async (newValue) => {
    if(isOpen.value){
      isOpen.value = false;
      return;
    }

    if(newValue.length >= 2) {
      options.value = await getLocations(newValue);
    } else {
      options.value = [];
    }
  });

  const getLocations = async (query) => {
    const response = await axios.get('https://api.opencagedata.com/geocode/v1/json', {
      params: {
        q: encodeURIComponent(query),
        key: 'dff04552b6b4486b956bde7409e0bb06',
        limit: 5
      }
    });

    if(response && response.status === 200) {
      return response.data.results.map(result => result.formatted);
    }
  }

  const selectOption = (option) => {
    emit("update:modelValue", option);
    searchQuery.value = option;
    options.value = [];
    isOpen.value = true;
  }
</script>

<template>
  <Input v-model="searchQuery" @input="fetchOptions" v-bind="attrs" />
  <ul class="options-wrapper" v-if="options.length && !isOpen">
    <li class="option-text" v-for="(option, index) in options" :key="index" @click="selectOption(option)">
      {{ option }}
    </li>
  </ul>
</template>

<style scoped>
  .options-wrapper {
    background-color: var(--color-dark-grey);
    border-radius: 12px;
    padding-left: 0;
    margin-bottom: 1rem;
  }
  .options-wrapper .option-text {
    color: var(--color-light-grey);
    padding: 0.8rem;
    list-style: none;
    border-bottom: 1px solid var(--color-light-grey);
  }
  .options-wrapper .option-text:hover {
    cursor: pointer;
  }
  .options-wrapper .option-text:last-child {
    border-bottom: none;
  }
</style>
