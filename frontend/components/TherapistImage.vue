<script setup>

import { ref } from 'vue'
const characterImage = ref('anne/default2.png');

</script>

<template>
  <div class="character-container">
    <img :src="characterImage" alt="Character" class="character-image" />
  </div>
</template>

<style>
img {
  height: 1100px;
  width: 1100px;
  position: fixed;
  left: 20%;
  transform: translateX(-50%);
  bottom: 0px;
  z-index: 0;
}
</style>
