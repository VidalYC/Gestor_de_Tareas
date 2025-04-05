import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

export function useLogin(showAlert) {
  const username = ref('')
  const password = ref('')
  const router = useRouter()
  const auth = useAuthStore()

  const handleLogin = async () => {
    try {
      await auth.login(username.value, password.value)
      
      if (showAlert) {
        showAlert('¡Bienvenido! Redirigiendo... 🚀', 'success', 2000)
      }
      
      // Limpiar campos
      username.value = ''
      password.value = ''

      setTimeout(() => {
        router.push(auth.returnUrl || '/tasks')
      }, 2000)

    } catch (err) {
      const errorMessage = err.response?.data?.detail || 'Error en el inicio de sesión'
      if (showAlert) {
        showAlert(`${errorMessage}`, 'error', 5000)
      }
    }
  }

  return {
    username,
    password,
    handleLogin
  }
}