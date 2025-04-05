<template>
  <div :class="['register-container', { dark: darkMode }]">
    <ThemeToggle />

    <h2 class="register-title">Crear cuenta</h2>

    <form @submit.prevent="handleRegister" class="register-form">
      <input
        v-model="username"
        placeholder="Nombre de usuario"
        required
        class="input"
      />
      <input
        v-model="email"
        type="email"
        placeholder="Correo electrónico"
        required
        class="input"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Contraseña"
        required
        class="input"
      />
      <button type="submit" class="register-button">Registrarse</button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>

    <p class="login-redirect">
      ¿Ya tienes cuenta?
      <router-link to="/login" class="link">Inicia sesión</router-link>
    </p>
  </div>
</template>

<script setup>
import { useRegister } from '@/composables/useRegister'
import { darkMode } from '@/composables/theme'
import ThemeToggle from '@/components/ThemeToggle.vue'

const { username, email, password, error, handleRegister } = useRegister()
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.register-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  min-height: 100vh;
  font-family: 'Poppins', sans-serif;
  background: linear-gradient(to bottom right, #f0f4ff, #ffe6f0);
  color: #222;
  transition: background 0.3s ease, color 0.3s ease;
}

.register-container.dark {
  background: linear-gradient(to bottom right, #1a1f2b, #2b3241);
  color: #e0e0e0;
}

.register-title {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  background: linear-gradient(90deg, #0051ff, #00a2ff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.register-container.dark .register-title {
  background: linear-gradient(90deg, #0a84ff, #5856d6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.register-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 100%;
  max-width: 400px;
}

.input {
  padding: 0.8rem;
  font-size: 1rem;
  border: 2px solid #ccc;
  border-radius: 8px;
  outline: none;
  transition: border 0.3s, box-shadow 0.3s;
  background-color: white;
  color: #333;
}

.input:focus {
  border-color: #00a2ff;
  box-shadow: 0 0 0 3px rgba(0, 162, 255, 0.2);
}

.register-container.dark .input {
  background-color: #2b3241;
  color: #fff;
  border-color: #555;
}

.register-container.dark .input:focus {
  border-color: #5856d6;
  box-shadow: 0 0 0 3px rgba(88, 86, 214, 0.3);
}

.register-button {
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
  cursor: pointer;
}

.register-button:hover {
  transform: translate(5px, -5px);
}

.register-container.dark .register-button {
  background-color: #1d1f36;
  color: #ffffff;
  border-color: #5856d6;
  box-shadow: -5px 5px 0px 0px #5856d6;
}

.register-container.dark .register-button:hover {
  transform: translate(5px, -5px);
}

.error {
  color: red;
  margin-top: 1rem;
}

.login-redirect {
  margin-top: 1.5rem;
  font-size: 0.95rem;
}

.link {
  color: #007bff;
  text-decoration: underline;
  font-weight: 600;
}

.link:hover {
  color: #0056b3;
}

.register-container.dark .link {
  color: #7aa8ff;
}

.register-container.dark .link:hover {
  color: #a3c9ff;
}
</style>
