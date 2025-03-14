<script setup>
  import { defineProps, defineEmits, computed, useAttrs } from "vue";

  const props = defineProps({
    modelValue: {
      type: String,
      default: ""
    }
  });

  const attrs = useAttrs();
  const emit = defineEmits(["update:modelValue"]);
  const value = computed({
    get: () => props.modelValue ?? "",
    set: (newValue) => emit("update:modelValue", newValue)
  });
</script>

<template>
  <div class="input-wrapper">
    <input v-model="value" v-bind="attrs" />
  </div>
</template>

<style scoped>
  .input-wrapper {
    margin-bottom: 1rem;
  }

  .input-wrapper input {
    width: 100%;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    background-color: var(--color-background-input);
    border: none;
    color: var(--color-text-input);
    font-size: 1rem;
    line-height: 1.5rem;
    min-height: 58px;
  }

  .input-wrapper input[type='radio'] {
    display: grid;
    place-content: center;
    min-height: unset;
    -webkit-appearance: none;
    appearance: none;
    background-color: var(--color-background-input);
    margin: 0;
    font: inherit;
    color: var(--color-text-input);
    width: 1.15rem;
    height: 1.15rem;
    border: 1px solid var(--color-text-input);
    border-radius: 50%;
    padding: 0;
  }

  input[type="radio"]::before {
    content: "";
    width: 0.65em;
    height: 0.65em;
    border-radius: 50%;
    transform: scale(0);
    transition: 120ms transform ease-in-out;
    box-shadow: inset 1em 1em var(--color-background-button);
  }

  input[type="radio"]:checked::before {
    transform: scale(1);
  }
</style>
