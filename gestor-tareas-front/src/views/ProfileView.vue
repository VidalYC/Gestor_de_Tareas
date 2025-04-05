<template>
  <div :class="['profile-container', { dark: darkMode }]">
    <NavBar :darkMode="darkMode" />
    <ThemeToggle class="theme-toggle" />
    
    <div class="profile-content">
      <div class="profile-card">
        <h2 class="section-title">Perfil de Usuario</h2>
        
        <div v-if="user" class="profile-info">
          <div class="info-item">
            <label>Nombre de usuario:</label>
            <p>{{ user.username }}</p>
          </div>
          
          <div class="info-item">
            <label>Email:</label>
            <p>{{ user.email }}</p>
          </div>
        </div>

        <p v-if="error" class="error-message">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import NavBar from '@/components/NavBar.vue'
import ThemeToggle from '@/components/ThemeToggle.vue'
import { useProfile } from '@/composables/useProfile'
import { darkMode } from '@/composables/theme'

const { user, error } = useProfile()
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.profile-container {
  min-height: 100vh;
  padding: 1rem 7rem 1rem 7.5rem;
  background: linear-gradient(to bottom right, #f4f4f5, #e0e7ff);
  color: #333;
  transition: background 0.3s ease, color 0.3s ease;
  position: relative;
  font-family: 'Poppins', sans-serif;
}

.profile-container.dark {
  background: linear-gradient(to bottom right, #1a1f2b, #2b3241);
  color: #e0e0e0;
}

.profile-content {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
}

.profile-card {
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 2rem;
  width: 100%;
  max-width: 600px;
}

.profile-container.dark .profile-card {
  background-color: #2b3241;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.section-title {
  font-size: 2.2rem;
  margin-bottom: 1.5rem;
  color: #406ff3;
}

.profile-container.dark .section-title {
  color: #667eea;
}

.profile-info {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.info-item label {
  font-weight: 600;
  color: #6a778e;
}

.profile-container.dark .info-item label {
  color: #a0aec0;
}

.info-item p {
  background-color: #f8fafc;
  padding: 0.8rem;
  border-radius: 0.5rem;
  border: 1px solid #e2e8f0;
  font-family: 'Poppins', sans-serif;
}

.profile-container.dark .info-item p {
  background-color: #1a1f2b;
  border-color: #2d3748;
  color: #e0e0e0;
}

.error-message {
  color: #f44336;
  margin-top: 1.5rem;
  padding: 1rem;
  background-color: #fee2e2;
  border-radius: 0.5rem;
  border: 1px solid #fecaca;
}

.profile-container.dark .error-message {
  background-color: #2d1a1a;
  border-color: #5c2a2a;
  color: #ff7d7d;
}

.theme-toggle {
  position: absolute;
  top: 1rem;
  right: 1rem;
}
</style>