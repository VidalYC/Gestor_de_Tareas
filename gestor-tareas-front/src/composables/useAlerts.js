// src/composables/useAlerts.js
import { ref } from 'vue'

export function useAlerts() {
  const alerts = ref([])

  const showAlert = (message, type = 'success', duration = 3000) => {
    const id = Date.now()
    alerts.value.push({ id, message, type, duration })
    
    setTimeout(() => {
      alerts.value = alerts.value.filter(alert => alert.id !== id)
    }, duration)
  }

  return { alerts, showAlert }
}