import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  const user = ref(null);
  const getUser = computed(() => user.value);
  const setUser = (value) => {
    user.value = value;
  };
  return { user, getUser, setUser }
});
