<template>
  <div :class="['home-container', { dark: darkMode }]">
    <!-- Componente del botón de modo oscuro -->
    <ThemeToggle />

    <h1 class="home-title">Bienvenido al Gestor de Tareas</h1>

    <div class="home-content">
      <div class="home-text">
        <h3>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut dolores neque recusandae nisi soluta nostrum omnis molestiae libero iure expedita repudiandae quaerat blanditiis sequi repellat, quam corrupti ducimus. Magni, aut?
        </h3>
        <router-link to="/login" class="start-button">Get Started</router-link>
      </div>
      <div class="home-image">
        <img :src="tareaImage" alt="Ilustración de tareas" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { darkMode } from '@/composables/theme'
import ThemeToggle from '@/components/ThemeToggle.vue'
import tareaImage from '@/assets/task.png'
</script>

<style scoped>

.home-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  min-height: 100vh;
  padding: 3rem 2rem 2rem;
  background: linear-gradient(to bottom right, #d9e4ff, #ffd9fa);
  text-align: center;
  font-family: 'Poppins', sans-serif;
  transition: background 0.3s ease, color 0.3s ease;
  color: #333;
  gap: 1rem;
}

.home-container.dark {
  background: linear-gradient(to bottom right, #1a1f2b, #2b3241);
  color: #e0e0e0;
}

.home-title {
  font-size: 3rem;
  margin: 4rem 0 20px;
  transform: perspective(500px) rotateX(5deg) rotateY(-3deg);
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
  background: linear-gradient(90deg, #0051ff, #00a2ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  transition: background 0.3s ease;
}

.home-container.dark .home-title {
  background: linear-gradient(90deg, #0a84ff, #5856d6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.home-content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 5px;
  max-width: 1000px;
  flex-wrap: wrap;
  margin-top: 2rem;
}

.home-text {
  flex: 1;
  min-width: 300px;
  max-width: 1000px;
  text-align: left;
}

.home-text h3 {
  font-size: 1.3rem;
  margin-bottom: 1.5rem;
  line-height: 1.5;
  padding-right: 0;
}

.start-button {
  font-size: 1rem;
  padding: 0.8em 2em;
  background-color: #ffffff;
  border: 3px solid #00a2ff;
  border-radius: 1em;
  color: #000000;
  font-weight: bolder;
  transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55), box-shadow 0.4s ease;
  box-shadow: -5px 5px 0px 0px #00a2ff;
  text-decoration: none;
  display: inline-block;
}

.start-button:hover {
  transform: translate(5px, -5px);
}

.home-container.dark .start-button {
  background-color: #1d1f36;
  color: #ffffff;
  border-color: #5856d6;
  box-shadow: -5px 5px 0px 0px #5856d6;
}

.home-container.dark .start-button:hover {
  transform: translate(5px, -5px);
}

.home-image img {
  flex: 1;
  max-width: 100%;
  height: auto;
  border: none;
  box-shadow: none;
  transform: translateX(200px);
  margin-left: 0;
}
</style>
