<template>
  <main>
    <article class="container flex flex-row align-center">
      <section class=" flex flex-column justify-center align-center bg-violet w-50 h-full">
        <div>
          <object class="logo" type="image/svg+xml" :data="logo"></object>
        </div>
        <h1>Kronos</h1>
        <h4><i>Master Your Time, Embrace the Golden Age.</i></h4>
      </section>
      <section class="bg-black w-50 flex flex-column justify-center align-center h-full">
        <h1 class="mb-4">Sign In</h1>
        <form class="form-container mx-auto max-w-365">
          <Input v-model="username" type="text" placeholder="Username" />
          <Input v-model="password" type="password" placeholder="Password" />
          <div class="flex flex-row justify-start gap-3 mt-4">
            <Button type="button" colour="bg-violet" text-color="white" @click="submitForm">
              Log In
            </Button>
            <Button type="a" colour="bg-black" text-color="white" route-name="signUp">
              Sign Up
            </Button>
          </div>
          <p class="mt-4"><a href="">Forgot your password?</a></p>
        </form>
      </section>
    </article>
  </main>
</template>

<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import Button from "@/components/Button.vue";
  import Input from "@/components/Input.vue";
  import logo from "@/assets/kronos.svg";
  import { useLoaderStore } from "@/stores/loader.js";
  import { useMessageStore } from "@/stores/message.js";
  import { useUserStore } from "@/stores/user.js";

  const username = ref("");
  const password = ref("");
  const loaderStore = useLoaderStore();
  const messageStore = useMessageStore();
  const userStore = useUserStore();
  const router = useRouter();

  const submitForm = async (e) => {
    e.preventDefault();

    loaderStore.setLoader(true);

    await axios.post("/api/login", {
      username: username.value,
      password: password.value
    }).then((res) => {
      if(res.status === 200) {
        if(res.data.user) {
          loaderStore.setLoader(false);
          messageStore.setMessage(res.data.message);
          userStore.setUser(res.data.user);
          router.push({ name: 'calendar' });
        }
      }
    }).catch((err) => {
      loaderStore.setLoader(false);
      console.log(err);
    });
  }
</script>

<style scoped>
  .logo {
    width: clamp(15rem, 5vw, 20rem);
    height: clamp(15rem, 5vw, 20rem);
  }
</style>
