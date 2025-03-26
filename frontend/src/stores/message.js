import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMessageStore = defineStore('loader', () => {
  const message = ref(false);
  const getMessage = computed(() => message.value);
  const setMessage = (value) => {
    message.value = value;
  };
  return { load, getMessage, setMessage }
});
