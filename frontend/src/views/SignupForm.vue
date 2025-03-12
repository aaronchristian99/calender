<script setup>
  import { ref } from "vue";
  import { useRouter } from "vue-router";
  import axios from "axios";
  import Input from "../components/Input.vue";
  import Button from "../components/Button.vue";

  const firstName = ref('');
  const lastName = ref('');
  const email = ref('');
  const password = ref('');
  const passwordConfirm = ref('');
  const username = ref('');
  const router = useRouter();

  const submitForm = async(e) => {
    e.preventDefault();

    await axios.post('/api/user/create', {
      firstName: firstName.value,
      lastName: lastName.value,
      email: email.value,
      username: username.value,
      password: password.value
    }).then(res => {
      if(res.status === 200){
        console.log(res);
        router.push({ name: 'calender' });
      }
    }).catch(err => console.log(err));
  }
</script>

<template>
  <main>
    <article class="container">
      <section class="bg-black w-full h-full p-4">
        <form class="form-container mx-auto max-w-365">
          <Input v-model="firstName" type="text" placeholder-text="First name" />
          <Input v-model="lastName" type="text" placeholder-text="Last name" />
          <Input v-model="email" type="email" placeholder-text="Email" />
          <Input v-model="username" type="text" placeholder-text="Username" />
          <Input v-model="password" type="password" placeholder-text="Password" />
          <Input v-model="passwordConfirm" type="password" placeholder-text="Confirm Password" />
          <div class="flex flex-row justify-center gap-3 mt-4">
            <Button type="button" colour="bg-violet" text-color="white" @click="submitForm">
              Submit
            </Button>
          </div>
        </form>
      </section>
    </article>
  </main>
</template>

<style scoped>

</style>
