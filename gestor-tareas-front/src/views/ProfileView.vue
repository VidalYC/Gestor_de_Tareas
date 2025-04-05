<template>
  <div class="profile">
    <NavBar />
    <h2>Perfil de Usuario</h2>

    <div v-if="user">
      <p><strong>Nombre de usuario:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue'
import { useProfile } from '@/composables/useProfile'

const { user, error } = useProfile()
</script>

<style scoped>
.profile {
  padding: 1rem;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>
