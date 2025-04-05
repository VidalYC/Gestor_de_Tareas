// src/composables/useTareas.js
import { ref, onMounted } from 'vue'
import api from '@/services/api'

export function useTareas() {
  const tasks = ref([])
  const tareaParaEditar = ref(null)

  const loadTasks = async () => {
    try {
      const res = await api.get('/tareas')
      tasks.value = res.data
    } catch (error) {
      console.error('Error al cargar tareas:', error)
    }
  }

  const completarTarea = async (task) => {
    try {
      await api.put(`/tareas/${task.id}`, {
        titulo: task.titulo,
        descripcion: task.descripcion,
        prioridad: task.prioridad,
        fecha_limite: task.fecha_limite,
        estado: 'Completada'
      })
      loadTasks()
    } catch (error) {
      console.error('Error al completar tarea:', error)
    }
  }

  const editarTarea = (task) => {
    tareaParaEditar.value = { ...task }
  }

  const limpiarEdicion = () => {
    tareaParaEditar.value = null
  }

  const eliminarTarea = async (id) => {
    try {
      await api.delete(`/tareas/${id}`)
      loadTasks()
    } catch (error) {
      console.error('Error al eliminar tarea:', error)
    }
  }

  const formatDate = (dateStr) => {
    if (!dateStr) return 'No asignada'
    const date = new Date(dateStr)
    return date.toLocaleDateString('es-ES', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  }

  onMounted(() => {
    loadTasks()
  })

  return {
    tasks,
    tareaParaEditar,
    loadTasks,
    completarTarea,
    editarTarea,
    limpiarEdicion,
    eliminarTarea,
    formatDate
  }
}
