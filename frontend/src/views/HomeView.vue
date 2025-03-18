<template>
  <main>
    <article class="container flex flex-row align-center">
      <section class="bg-violet w-50 h-full">
        <!-- LOGO goes here -->
      </section>
      <section class="bg-black w-50 flex flex-row align-center h-full">
        <h1 class="mb-4">Sign In</h1>
        <form class="form-container mx-auto max-w-365">
          <Input v-model="username" type="text" placeholder-text="Username" />
          <Input v-model="password" type="password" placeholder-text="Password" />
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

  const username = ref("");
  const password = ref("");
  const router = useRouter();

  const submitForm = async (e) => {
    e.preventDefault();

    await axios.post("/api/login", {
      username: username.value,
      password: password.value
    }).then((res) => {
      if(res.status === 200) {
        router.push({ name: 'calendar' });
      }
    }).catch((err) => {
      console.log(err);
    });
  }
</script>

<style scoped>

</style>
