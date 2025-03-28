<script setup>
  import { RouterView, useRoute, useRouter } from 'vue-router'
  import Button from "@/components/Button.vue";
  import axios from "axios";
  import Spinner from "@/components/Spinner.vue";
  import {useLoaderStore} from "@/stores/loader.js";
  import {useMessageStore} from "@/stores/message.js";
  import Message from "@/components/Message.vue";
  import logo from "@/assets/kronos.svg";

  const route = useRoute();
  const router = useRouter();
  const loaderStore = useLoaderStore();
  const messageStore = useMessageStore();

  const logout = async () => {
    const response = await axios.get('/api/logout')

    if(response && response.status === 200) {
      if(response.data.success) {
        messageStore.setMessage(null);
        await router.push({name: 'home'});
      }
    }
  }

  const closeMessage = () => {
    messageStore.setMessage(null);
  }
</script>

<template>
  <header class="bg-black p-3" v-if="!['home', 'signUp'].includes(route.name)">
    <nav class="flex flex-row justify-between align-center px-3">
      <div class="logo-wrapper">
        <object class="header-logo" type="image/svg+xml" :data="logo"></object>
      </div>
      <Button class="p-4 icon-button" type="button" @click="logout" colour="bg-violet" text-color="white">
        <font-awesome-icon icon="right-from-bracket" />
      </Button>
    </nav>
  </header>
  <Spinner v-if="loaderStore.load" />
  <Message :message="messageStore.message" @close-message="closeMessage" v-if="messageStore.message" />
  <RouterView />
</template>

<style scoped>
.header-logo {
  width: clamp(5rem, 5vw, 10rem);
  height: clamp(5rem, 5vw, 10rem);
}
</style>
