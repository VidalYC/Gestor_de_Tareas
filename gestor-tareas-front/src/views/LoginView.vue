<template>
  <div class="login">
    <h2>Iniciar Sesión</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="username" placeholder="Usuario" required />
      <input v-model="password" type="password" placeholder="Contraseña" required />
      <button type="submit">Ingresar</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

const username = ref('');
const password = ref('');
const error = ref('');
const router = useRouter();
const auth = useAuthStore();

const handleLogin = async () => {
  try {
    error.value = '';
    await auth.login(username.value, password.value);
    router.push(auth.returnUrl || '/tasks');
  } catch (err) {
    error.value = err;
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
