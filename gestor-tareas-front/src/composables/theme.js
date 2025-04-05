// src/composables/theme.js
import { ref, watch } from 'vue'

export const darkMode = ref(false)

export const toggleTheme = () => {
  darkMode.value = !darkMode.value
}

// (Opcional) Persistencia en localStorage
if (localStorage.getItem('theme') === 'dark') {
  darkMode.value = true
}

watch(darkMode, (val) => {
  localStorage.setItem('theme', val ? 'dark' : 'light')
})
