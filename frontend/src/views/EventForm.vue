<script setup>
  import axios from "axios";

  const submitForm = async (e) => {
    e.preventDefault();

    await axios.post("/api/event/create", {
      data: {}
    }).then((res) => {
      console.log(res);
    }). catch(error => {
      console.log(error);
    });
  }
</script>

<template>

</template>

<style scoped>

</style>
