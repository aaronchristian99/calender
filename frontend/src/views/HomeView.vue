<template>
  <main>
    <article class="container flex flex-row align-center">
      <section class="bg-violet w-50 h-full">
        <!-- LOGO goes here -->
      </section>
      <section class="bg-black w-50 flex flex-row align-center h-full">
        <h1 class="mb-4">Sign In</h1>
        <form class="form-container mx-auto max-w-365">
          <div class="input-wrapper">
            <input v-model="username" type="text" placeholder="Username" />
          </div>
          <div class="input-wrapper">
            <input v-model="password" type="password" placeholder="Password" />
          </div>
          <div class="flex flex-row justify-start gap-3 mt-4">
            <Button label="Log In" type="button" colour="bg-violet" text-color="white" @click="submitForm" />
            <Button label="Sign Up" type="a" colour="bg-black" text-color="white" url="" />
          </div>
          <p class="mt-4"><a href="">Forgot your password?</a></p>
        </form>
      </section>
    </article>
  </main>
</template>

<script setup>
  import { ref } from "vue";
  import axios from "axios";
  import Button from "@/components/Button.vue";

  const username = ref("");
  const password = ref("");

  const submitForm = async (e) => {
    e.preventDefault();

    await axios.post("/api/login", {
      username: username.value,
      password: password.value
    }).then((res) => {
      if(res.status === 200) {
        this.$router.push({ name: 'calender' });
      }
    })
  }
</script>

<style scoped>

</style>
