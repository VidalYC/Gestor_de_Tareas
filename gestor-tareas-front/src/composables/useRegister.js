import { ref } from 'vue'
import api from '@/services/api'
import { useRouter } from 'vue-router'

export function useRegister(showAlert) {
  const username = ref('')
  const email = ref('')
  const password = ref('')
  const router = useRouter()

  const handleRegister = async () => {
    try {
      await api.post('/usuarios/register', {
        username: username.value,
        email: email.value,
        password: password.value,
      })

      // Eliminar nextTick() ya que no es necesario
      if (showAlert) {
        showAlert('¡Registro exitoso! Redirigiendo... 🎉', 'success', 2500)
      }

      username.value = ''
      email.value = ''
      password.value = ''

      setTimeout(() => {
        router.push('/login')
      }, 2500)

    } catch (err) {
      const errorMessage = err.response?.data?.detail || 'Error en el registro'
      if (showAlert) {
        showAlert(`❌ ${errorMessage}`, 'error', 5000)
      }
    }
  }

  return {
    username,
    email,
    password,
    handleRegister
  }
}