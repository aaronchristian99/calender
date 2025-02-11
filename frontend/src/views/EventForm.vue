<script setup>
  import { ref } from "vue";
  import axios from "axios";
  import Button from "@/components/Button.vue";

  const title = ref('');
  const description = ref('');
  const location = ref('');
  const date = ref('');
  const message = ref('');

  const submitForm = async (e) => {
    e.preventDefault();

    await axios.post("/api/event/create", {
      title: title.value,
      description: description.value,
      location: location.value,
      date: date.value,
    }).then((res) => {
      if(res.status === 200) {
        title.value = '';
        description.value = '';
        location.value = '';
        date.value = '';
        message.value = 'Event is successfully created!';
        this.$router.push({ name: 'calendar' });
      } else {
        message.value = 'There was an error creating your event!';
      }
    }). catch(error => {
      console.log(error);
    });
  }
</script>

<template>
  <section class="form-container">
    <div class="bg-green p-4" v-if="message !== ''">
      <p class="white">{{ message }}</p>
    </div>
    <form>
      <div class="input-wrapper">
        <label class="text-bold">Title</label>
        <input class="input" type="text" v-model="title" placeholder="Title" required />
      </div>
      <div class="input-wrapper">
        <label class="text-bold">Description</label>
        <textarea class="input" type="text" v-model="description" placeholder="Description" required />
      </div>
      <div class="input-wrapper">
        <label class="text-bold">Location</label>
        <input class="input" type="text" v-model="location" placeholder="Location" required />
      </div>
      <div class="input-wrapper">
        <label class="text-bold">Date</label>
        <input class="input" type="datetime-local" v-model="date" placeholder="Date" required />
      </div>
      <div class="input-wrapper">
        <Button label="Submit" type="button" colour="bg-green" text-color="white" @click="submitForm" />
      </div>
    </form>
  </section>
</template>

<style scoped>
  .form-container {
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    padding: 0 2rem;
  }

  form {
    width: 100%;
    margin-top: 2rem;
  }

  .input-wrapper {
    width: 100%;
    display: flex;
    flex-flow: column nowrap;
    align-items: flex-start;
    gap: 0.5rem;
    margin-bottom: 1rem;
  }

  .input-wrapper:last-child {
    margin-bottom: 0;
  }

  input, textarea {
    width: 100%;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 0.5rem;
    font-size: 1rem;
    resize: none;
  }

  .p-4 {
    margin-bottom: 1.5rem;
  }
</style>
