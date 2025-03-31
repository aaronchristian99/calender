<template>
  <button v-if="type === 'button'"
          :class="['button', colour, textColor, icon ? 'icon-button' : '' ]">
    <slot></slot>
  </button>
  <a v-else
     :class="['button', colour, textColor, 'border-white']"
     :href="resolvedUrl">
    <slot></slot>
  </a>
</template>

<script>
  export default {
    name: 'Button',
    props: {
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
      routeName: {
        type: String
      },
      icon: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      resolvedUrl() {
        if(!this.routeName) return '#';
        return this.$router.resolve({ name: this.routeName }).href;
      }
    }
  }
</script>

<style scoped>
  .button {
    display: block;
    font-size: 1rem;
    font-weight: 500;
    padding: 0.8rem;
    border-radius: 100px;
    border: none;
    text-decoration: none;
  }

  .button:hover {
    cursor: pointer;
  }

  .button.bg-violet:hover {
    background-color: var(--color-light-violet);
    color: #000;
  }

  .button:has(.p-4) {
    border-radius: 10px;
  }

  .border-white {
    border: 1px solid var(--color-white);
  }
</style>
