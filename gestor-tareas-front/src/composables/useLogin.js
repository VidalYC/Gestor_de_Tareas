import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

export function useLogin() {
  const username = ref('')
  const password = ref('')
  const error = ref('')

  const router = useRouter()
  const auth = useAuthStore()

  const handleLogin = async () => {
    try {
      error.value = ''
      await auth.login(username.value, password.value)
      router.push(auth.returnUrl || '/tasks')
    } catch (err) {
      error.value = err
    }
  }

  return {
    username,
    password,
    error,
    handleLogin
  }
}
