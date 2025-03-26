import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useLoaderStore = defineStore('loader', () => {
  const load = ref(false);
  const getLoader = computed(() => load.value);
  const setLoader = (value) => {
    load.value = value;
  };
  return { load, getLoader, setLoader }
});
