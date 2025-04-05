import { ref, onMounted } from 'vue'
import api from '@/services/api'

export function useProfile() {
  const user = ref(null)
  const error = ref('')

  const loadProfile = async () => {
    try {
      const response = await api.get('/usuarios/me')
      user.value = response.data
    } catch (err) {
      error.value = 'Error al cargar el perfil'
      console.error(err)
    }
  }

  onMounted(loadProfile)

  return {
    user,
    error,
  }
}
