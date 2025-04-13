<script setup>
import TherapistImage from '../components/TherapistImage.vue'
import HistoryBox from '../components/HistoryBox.vue'

import { ref } from 'vue';

const backgroundUrl = ref('hospital.jpg')

</script>

<template>
  <!-- Render the background image -->
  <div class="background-overlay" id="app" :style="{ backgroundImage: `url(${backgroundUrl})` }"></div>

  <TherapistImage />
  <HistoryBox />

</template>

<style scoped>
#app {
  background-size: cover;
  /* Cover the entire screen */
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  /* Full height of viewport */
  width: 100vw;
  /* Full width */
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
