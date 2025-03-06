<script setup>
  import { defineProps, defineEmits, computed} from "vue";

  const props = defineProps({
    modelValue: {
      type: String,
      default: ""
    },
    type: {
      type: String,
      default: "text"
    },
    placeholderText: {
      type: String,
      default: "Placeholder"
    },
    isRequired: {
      type: Boolean,
      default: false
    }
  });

  const emit = defineEmits(["update:modelValue"]);
  const value = computed({
    get: () => props.modelValue ?? "",
    set: (newValue) => emit("update:modelValue", newValue)
  });

  const updateValue = (e) => {
    value.value = e.target.value;
  }
</script>

<template>
  <div class="input-wrapper">
    <input :value="value" @input="updateValue" :type="type" :placeholder="placeholderText" :required="isRequired" />
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
</style>
