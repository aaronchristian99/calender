<template>
  <button v-if="type === 'button'" @click="$emit('click')"
          :class="['button', colour, textColor]">
    {{ label }}
  </button>
  <a v-else :class="['button', colour, textColor]" :href="url"> {{ label }}</a>
</template>

<script>
  export default {
    name: 'Button',
    props: {
      label: {
        type: String,
        required: true
      },
      colour: {
        type: String,
        required: false,
        default: 'bg-black'
      },
      textColor: {
        type: String,
        required: false,
        default: 'green'
      },
      type: {
        type: String,
        default: 'a'
      },
      url: {
        type: String
      }
    }
  }
</script>

<style scoped>
  .button {
    display: inline-block;
    vertical-align: middle;
    padding: 0.5rem;
    outline: none;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    font-size: 1rem;
    font-weight: 700;
  }
</style>
