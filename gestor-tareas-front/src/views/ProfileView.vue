<template>
    <div>
      <NavBar />
      <h2>Perfil de Usuario</h2>
      <p><strong>Nombre:</strong> {{ user?.username }}</p>
      <p><strong>Email:</strong> {{ user?.email }}</p>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import NavBar from '@/components/NavBar.vue';
  
  const auth = useAuthStore();
  const user = ref(null);
  
  onMounted(async () => {
    user.value = await auth.me();
  });
  </script>
  