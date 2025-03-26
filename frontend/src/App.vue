<script setup>
  import { RouterView, useRoute, useRouter } from 'vue-router'
  import Button from "@/components/Button.vue";
  import axios from "axios";

  const route = useRoute();
  const router = useRouter();

  const logout = async () => {
    const response = await axios.get('/api/logout')

    if (response && response.status === 200){
      if(response.data.success){
        localStorage.removeItem("user");
        await router.push({name: 'home'});
      }
    }
  }
</script>

<template>
  <header class="bg-black p-3" v-if="!['home', 'signUp'].includes(route.name)">
    <nav class="flex flex-row justify-end align-center">
      <Button class="p-4 icon-button" type="button" @click="logout" colour="bg-violet" text-color="white">
        <font-awesome-icon icon="right-from-bracket" />
      </Button>
    </nav>
  </header>
  <RouterView />
</template>

<style scoped>
.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
