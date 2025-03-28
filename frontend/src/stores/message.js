import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMessageStore = defineStore('message', () => {
  const message = ref(null);
  const getMessage = computed(() => message.value);
  const setMessage = (value) => {
    message.value = value;
  };
  return { message, getMessage, setMessage }
});
