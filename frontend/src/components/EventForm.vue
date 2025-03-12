<script setup>
  import { ref } from "vue";
  import VueDatePicker from "@vuepic/vue-datepicker";
  import "@vuepic/vue-datepicker/dist/main.css"
  import axios from "axios";
  import Button from "@/components/Button.vue";
  import Input from "@/components/Input.vue";

  const props = defineProps({
    isVisible: Boolean,
  });
  const emit = defineEmits(['toggle-form']);

  const title = ref('');
  const description = ref('');
  const location = ref('');
  const date = ref();
  const message = ref('');

  const toggleForm = () => {
    emit('toggle-form'); // Emit toggle-form event to close the form
  };

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
  <section :class="!isVisible ? 'hidden' : 'form-container'">
    <div class="bg-green p-4" v-if="message !== ''">
      <p class="white">{{ message }}</p>
    </div>
    <div class="flex justify-end items-center">
      <Button type="button" @click="toggleForm" colour="bg-violet" text-color="white">
        <font-awesome-icon icon="xmark" />
      </Button>
    </div>
    <form>
      <Input v-model="title" type="text" placeholder-text="Title" :is-required="true" />
      <Input v-model="description" type="textarea" placeholder-text="Description" :is-required="true" />
      <Input v-model="location" type="text" placeholder-text="Location" :is-required="true" />
      <VueDatePicker v-model="date" range dark :clearable="true" placeholder="Select the dates" />
      <Button class="mt-4"
              type="button"
              colour="bg-violet"
              text-color="white"
              @click="submitForm">
        Submit
      </Button>
    </form>
  </section>
</template>

<style scoped>
  .form-container {
    position: relative;
    display: flex;
    flex-flow: row nowrap;
    justify-content: center;
    align-items: center;
    padding: 0 2rem;
    animation: moveFromRight 0.3s ease-in-out forwards;
  }
  form {
    width: 100%;
    margin-top: 2rem;
  }
  input, textarea {
    width: 100%;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 0.5rem;
    font-size: 1rem;
    resize: none;
  }
  @keyframes moveFromRight {
    0% {
      right: -500px;
    }
    100% {
      right: 0;
    }
  }
</style>
