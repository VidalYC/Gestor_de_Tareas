<template>
  <div class="register">
    <h2>Registro</h2>
    <form @submit.prevent="handleRegister">
      <input v-model="username" placeholder="Nombre de usuario" required />
      <input v-model="email" type="email" placeholder="Correo electrónico" required />
      <input v-model="password" type="password" placeholder="Contraseña" required />
      <button type="submit">Registrarse</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '@/services/api';
import { useRouter } from 'vue-router';

const username = ref('');
const email = ref('');
const password = ref('');
const error = ref('');

const router = useRouter();

const handleRegister = async () => {
  try {
    error.value = '';
    await api.post('/usuarios/register', {
      username: username.value,
      email: email.value,
      password: password.value,
    });
    router.push('/login');
  } catch (err) {
    error.value = err.response?.data?.detail || 'Error al registrar usuario';
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
