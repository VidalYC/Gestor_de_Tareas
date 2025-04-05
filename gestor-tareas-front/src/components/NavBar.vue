<template>
  <nav :class="['navbar', { dark: darkMode }]">
    <ul class="navbar__menu">
      <li class="navbar__item" v-for="(link, index) in links" :key="index">
        <router-link 
          :to="link.path" 
          class="navbar__link"
          active-class="active"
        >
          <i :class="link.icon"></i>
          <span>{{ link.text }}</span>
        </router-link>
      </li>
      <li class="navbar__item">
        <a href="#" @click.prevent="logout" class="navbar__link">
          <i class="fas fa-sign-out-alt"></i>
          <span>Salir</span>
        </a>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

defineProps({
  darkMode: Boolean
});

const links = [
  { path: '/', text: 'Inicio', icon: 'fas fa-home' },
  { path: '/tasks', text: 'Tareas', icon: 'fas fa-tasks' },
  { path: '/profile', text: 'Perfil', icon: 'fas fa-user' }
];

const logout = () => {
  auth.logout();
  router.push('/login');
};
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@600&display=swap');

.navbar {
  position: fixed;
  top: 1rem;
  left: 1rem;
  background: #fff;
  border-radius: 10px;
  padding: 1rem 0;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1), 
  0 4px 20px rgba(0, 0, 0, 0.05);
  height: calc(100vh - 4rem);
  z-index: 1000;
  transition: box-shadow 0.3s ease, background 0.3s ease;
}

.navbar.dark {
  background: #2b3241;
  box-shadow: 0 2px 15px rgba(0, 0, 0, 0.3),
              0 4px 20px rgba(0, 0, 0, 0.2);
}

.navbar__menu {
  list-style: none;
  padding: 0;
  margin: 0;
  position: relative;
}

.navbar__item {
  position: relative;
  margin: 0.5rem 0;
}

.navbar__link {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 3.5rem;
  width: 5.5rem;
  color: #6a778e;
  transition: all 250ms ease;
  text-decoration: none;
}

.navbar__link i {
  font-size: 1.5rem;
}

.navbar__link span {
  position: absolute;
  left: 100%;
  transform: translateX(-3rem);
  margin-left: 1rem;
  opacity: 0;
  pointer-events: none;
  background: #406ff3;
  color: white;
  padding: 0.75rem;
  border-radius: 17.5px;
  white-space: nowrap;
  transition: all 250ms ease;
}

.navbar__link:hover span {
  opacity: 1;
  transform: translateX(0);
}

.navbar__link:hover,
.navbar__link.active {
  color: #406ff3;
}

.navbar__item::before {
  content: '';
  position: absolute;
  top: 0;
  left: 1rem;
  width: 3.5rem;
  height: 3.5rem;
  background: #406ff3;
  border-radius: 17.5px;
  opacity: 0;
  transition: all 250ms cubic-bezier(1, 0.2, 0.1, 1.2);
  z-index: -1;
}

@keyframes gooeyEffect {
  0% { transform: scale(1, 1); }
  50% { transform: scale(0.5, 1.5); }
  100% { transform: scale(1, 1); }
}

.navbar__item:hover::before {
  opacity: 0.1;
  animation: gooeyEffect 250ms 1;
}

/* Modo oscuro */
.navbar.dark .navbar__link {
  color: #a0aec0;
}

.navbar.dark .navbar__link:hover,
.navbar.dark .navbar__link.active {
  color: #667eea;
}

.navbar.dark .navbar__link span {
  background: #667eea;
  color: #fff;
}

.navbar.dark .navbar__item:last-child::before {
  background: #667eea;
}

/* Animaciones */
@keyframes gooeyEffect {
  0% { transform: scale(1, 1); }
  50% { transform: scale(0.5, 1.5); }
  100% { transform: scale(1, 1); }
}

.navbar__item:hover::before {
  animation: gooeyEffect 250ms 1;
}
</style>