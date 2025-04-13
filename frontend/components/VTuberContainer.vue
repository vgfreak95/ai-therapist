<template>
  <div class="vtuber-container">
    <canvas ref="live2dCanvas" class="live2d-canvas"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';

const live2dCanvas = ref(null);

onMounted(() => {
  console.log("Loaded");
  // Check if canvas and WebGL are available
  const canvas = live2dCanvas.value;
  const gl = canvas.getContext('webgl');

  if (!gl) {
    alert('Your browser does not support WebGL.');
    return;
  }

  // Initialize Live2D model
  const model = new Live2DModel();
  model.load('/assets/your_model/model.moc3', function () {
    // Set the position and scale of the model on the canvas
    model.setPosition(canvas.width / 2, canvas.height / 2);
    model.setScale(1.0);

    // Render loop to keep the model animating
    function render() {
      gl.clear(gl.COLOR_BUFFER_BIT);
      model.update();
      model.draw();
      requestAnimationFrame(render);
    }
    render();
  });
});
</script>

<style scoped>
.vtuber-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.live2d-canvas {
  width: 100%;
  height: 100%;
  max-width: 600px;
  max-height: 800px;
}
</style>
