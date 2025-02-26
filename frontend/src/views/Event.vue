<script setup>
  import { onMounted } from "vue";
  import axios from "axios";

  onMounted(async () => {
    await axios.get(`/api/event/${id}`).then((response) => {
      console.log(response);
    }).catch((error) => {
      console.log(error);
    });
  });

  const deleteEvent = async(e) => {
    e.preventDefault();

    await axios.post(`/api/event/${id}`).then((response) => {
      console.log(response);
    }).catch((error) => {
      console.log(error);
    });
  }
</script>

<template>

</template>

<style scoped>

</style>
