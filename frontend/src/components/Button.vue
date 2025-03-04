<template>
  <button v-if="type === 'button'" @click="$emit('click')"
          :class="['button', colour, textColor]">
    {{ label }}
  </button>
  <a v-else :class="['button', colour, textColor, 'border-white']" :href="url"> {{ label }}</a>
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
    display: block;
    font-size: 1rem;
    font-weight: 500;
    padding: 0.25rem 1.5rem;
    border-radius: 100px;
    border: none;
    text-decoration: none;
  }

  .button:hover {
    cursor: pointer;
  }

  .border-white {
    border: 1px solid var(--color-text);
  }
</style>
