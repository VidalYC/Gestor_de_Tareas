import { ref } from 'vue'
import api from '@/services/api'
import { useRouter } from 'vue-router'

export function useRegister() {
  const username = ref('')
  const email = ref('')
  const password = ref('')
  const error = ref('')

  const router = useRouter()

  const handleRegister = async () => {
    try {
      error.value = ''
      await api.post('/usuarios/register', {
        username: username.value,
        email: email.value,
        password: password.value,
      })
      router.push('/login')
    } catch (err) {
      error.value = err.response?.data?.detail || 'Error al registrar usuario'
    }
  }

  return {
    username,
    email,
    password,
    error,
    handleRegister,
  }
}
