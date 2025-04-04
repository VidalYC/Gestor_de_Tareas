<template>
    <nav>
      <router-link to="/">Inicio</router-link> |
      <router-link to="/tasks">Tareas</router-link> |
      <router-link to="/profile">Perfil</router-link> |
      <a href="#" @click.prevent="logout">Salir</a>
    </nav>
  </template>
  
  <script setup>
  import { useAuthStore } from '@/stores/auth';
  import { useRouter } from 'vue-router';
  
  const auth = useAuthStore();
  const router = useRouter();
  
  const logout = () => {
    auth.logout();
    router.push('/login');
  };
  </script>
  