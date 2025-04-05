<template>
  <div :class="['login-container', { dark: darkMode }]">
    <transition-group 
      name="alerts"
      tag="div"
      class="alerts-container"
    >
      <FloatingAlert 
        v-for="alert in alerts"
        :key="alert.id"
        :message="alert.message"
        :type="alert.type"
        :duration="alert.duration"
      />
    </transition-group>

    <ThemeToggle class="theme-toggle" />

    <h2 class="login-title">Iniciar Sesión</h2>

    <form class="login-form" @submit.prevent="handleLogin">
      <input v-model="username" class="login-input" placeholder="Usuario" required />
      <input v-model="password" class="login-input" type="password" placeholder="Contraseña" required />
      <button type="submit" class="login-button">Ingresar</button>
    </form>

    <p class="register-text custom-font">¿No tienes cuenta?
      <router-link to="/register" class="start-link">Registro</router-link>
    </p>
  </div>
</template>

<script setup>
import { useLogin } from '@/composables/useLogin'
import { darkMode } from '@/composables/theme'
import ThemeToggle from '@/components/ThemeToggle.vue'
import FloatingAlert from '@/components/FloatingAlert.vue'
import { useAlerts } from '@/composables/useAlerts'

const { alerts, showAlert } = useAlerts()
const { username, password, handleLogin } = useLogin(showAlert)
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');


.alerts-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.login-input:focus {
  outline: none;
  border-color: #00a2ff;
  box-shadow: 0 0 0 3px #00a2ff;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.login-container.dark .login-input:focus {
  border-color: #5856d6;
  box-shadow: 0 0 0 3px #5856d6;
}

.custom-font {
  font-family: 'Poppins', sans-serif; /* o la que estés usando */
  font-weight: 500;
  font-size: 1rem;
}

.start-link {
  color: #4f46e5;
  font-weight: bold;
  text-decoration: underline;
  margin-left: 0.4rem;
  transition: color 0.3s;
}

.login-container.dark .start-link {
  color: #00a2ff;
}

.start-link:hover {
  color: #6366f1;
}


.login-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: linear-gradient(to bottom right, #f4f4f5, #e0e7ff);
  color: #333;
  transition: background 0.3s ease, color 0.3s ease;
  position: relative;
}

.login-container.dark {
  background: linear-gradient(to bottom right, #1a1f2b, #2b3241);
  color: #e0e0e0;
}

.login-title {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  font-family: 'Poppins', sans-serif;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  max-width: 400px;
}

.login-input {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  background-color: #fff;
}

.login-container.dark .login-input {
  background-color: #2b3241;
  border-color: #444;
  color: white;
}

.login-button {
  font-size: 1rem;
  padding: 0.8em 2em;
  background-color: #ffffff;
  border: 3px solid #00a2ff;
  border-radius: 1em;
  color: #000000;
  font-weight: bolder;
  transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  box-shadow: -5px 5px 0px 0px #00a2ff;
  cursor: pointer;
}

.login-button:hover {
  transform: translate(5px, -5px);
}

.login-container.dark .login-button {
  background-color: #1d1f36;
  color: #ffffff;
  border-color: #5856d6;
  box-shadow: -5px 5px 0px 0px #5856d6;
}

.register-text {
  margin-top: 1rem;
}

.error {
  margin-top: 1rem;
  color: red;
}

/* Posicionamiento del ThemeToggle */
.theme-toggle {
  position: absolute;
  top: 1rem;
  right: 1rem;
}
</style>
