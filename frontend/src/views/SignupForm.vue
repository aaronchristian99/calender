<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import Input from "../components/Input.vue";
  import Button from "../components/Button.vue";
  import kronos from "@/assets/kronos_signup.webp";
  import {useLoaderStore} from "@/stores/loader.js";
  import {useMessageStore} from "@/stores/message.js";

  const firstName = ref('');
  const lastName = ref('');
  const email = ref('');
  const password = ref('');
  const passwordConfirm = ref('');
  const username = ref('');
  const loaderStore = useLoaderStore();
  const messageStore = useMessageStore();
  const router = useRouter();

  const submitForm = async(e) => {
    e.preventDefault();

    loaderStore.setLoader(true);

    await axios.post('/api/user/create', {
      firstName: firstName.value,
      lastName: lastName.value,
      email: email.value,
      username: username.value,
      password: password.value
    }).then(res => {
      if(res.status === 200){
        loaderStore.setLoader(false)
        messageStore.setMessage(res.data.message);
        router.push({ name: 'home' });
      }
    }).catch(err => {
      loaderStore.setLoader(false);
      console.log(err)
    });
  }

  const getRoute = (routeName) => {
    return router.resolve({ name: routeName }).fullPath;
  }
</script>

<template>
  <main>
    <article class="container flex flex-row align-center">
      <section class="bg-black w-50 h-full p-4 flex flex-column justify-center align-center">
        <h1>Sign up now</h1>
        <h3 class="text-light-violet">Kronos: Master Your Time, Embrace the Golden Age.</h3>
        <p class="mb-4"><i>Inspired by the god of time and the mythical golden era he ruled</i></p>
        <form class="form-container mx-auto max-w-365">
          <Input v-model="firstName" type="text" placeholder="First name" />
          <Input v-model="lastName" type="text" placeholder="Last name" />
          <Input v-model="email" type="email" placeholder="Email" />
          <Input v-model="username" type="text" placeholder="Username" />
          <Input v-model="password" type="password" placeholder="Password" />
          <Input v-model="passwordConfirm" type="password" placeholder="Confirm Password" />
          <div class="flex flex-column justify-center align-center gap-3 mt-4">
            <Button type="button" colour="bg-violet" text-color="white" @click="submitForm">
              Submit
            </Button>
            <p>Already a user? <a :href="getRoute('home')">Log In</a></p>
          </div>
        </form>
      </section>
      <section class="flex justify-center align-center bg-violet w-50 h-full">
        <img :src="kronos" class="image" alt="kronos" />
      </section>
    </article>
  </main>
</template>

<style scoped>
  h3 {
    text-align: center;
  }
  .image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
