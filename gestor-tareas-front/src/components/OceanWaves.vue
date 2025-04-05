<template>
  <div class="wave-box">
    <div class="wave -one"></div>
    <div class="wave -two"></div>
  </div>
</template>

<style scoped>
.wave-box {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  z-index: -1; /* asegúrate de que quede detrás del contenido */
  transform: rotate(80deg);
  pointer-events: none;
}

.wave {
  position: absolute;
  width: 1500px;
  height: 1300px;
  margin-left: -150px;
  margin-top: -250px;
  border-radius: 43%;
  background: white;
  opacity: 0.05;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.wave.-one {
  animation: rotate 10s infinite linear;
}

.wave.-two {
  animation: rotate 6s infinite linear;
  opacity: 0.1;
}
</style>
