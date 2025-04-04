<template>
  <nav v-if="$route.name !== 'home'">
    <router-link to="/">Home</router-link> |
    <router-link to="/tareas" v-if="authStore.user">Tareas</router-link>
    <template v-else>
      <router-link to="/login">Login</router-link> |
      <router-link to="/register">Register</router-link>
    </template>
  </nav>
  <router-view/>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
const authStore = useAuthStore()
</script>

<style>
nav {
  padding: 1rem;
  background: #f0f0f0;
  margin-bottom: 2rem;
}
nav a {
  margin: 0 0.5rem;
}
</style>