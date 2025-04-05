<template>
  <div :class="['task-container', { dark: darkMode }]">
    <transition-group 
      name="alerts"
      tag="div"
      class="alerts-container"
    >
      <FloatingAlert 
        v-for="alert in alerts"
        :key="alert.id"
        :message="alert.message"
        :type="alert.type"
        :duration="alert.duration"
      />
    </transition-group>
    
    <NavBar :darkMode="darkMode" />
    <ThemeToggle class="theme-toggle" />

    <div class="task-view">
      <div class="task-form-container">
        <h2 class="section-title">Crear / Editar Tarea ✍️</h2>
        <TaskForm 
          :tareaEditable="tareaParaEditar" 
          @refresh="loadTasks"
          @limpiar="limpiarEdicion"
          @created="handleCreated"
          @updated="handleUpdated"
          @error="handleError"
        />
      </div>
      
      <div class="task-list-container">
        <h2 class="section-title">Lista de Tareas 📝</h2>
        <ul class="task-list">
          <li v-for="task in tasks" :key="task.id" class="task-item">
            <div class="task-header">
              <strong>{{ task.titulo }}</strong>
              <div class="task-actions">
                <button 
                  v-if="task.estado !== 'Completada'"
                  @click="completarTarea(task)"
                  class="complete-btn"
                >
                  Completar
                </button>
                <button @click="editarTarea(task)" class="edit-btn">
                  Editar
                </button>
                <button @click="eliminarTarea(task.id)" class="delete-btn">
                  Eliminar
                </button>
              </div>
            </div>

            <p>{{ task.descripcion }}</p>

            <div class="task-meta">
              <p><strong>Prioridad:</strong> {{ task.prioridad || 'No definida' }}</p>
              <p><strong>Fecha límite:</strong> {{ formatDate(task.fecha_limite) }}</p>
              <p>
                <strong>Estado:</strong> 
                <span :class="{ completada: task.estado === 'Completada' }">
                  {{ task.estado || 'Pendiente' }}
                </span>
              </p>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import TaskForm from '@/components/TaskForm.vue'
import NavBar from '@/components/NavBar.vue'
import ThemeToggle from '@/components/ThemeToggle.vue'
import FloatingAlert from '@/components/FloatingAlert.vue'
import { useTareas } from '@/composables/useTareas.js'
import { darkMode } from '@/composables/theme'
import { useAlerts } from '@/composables/useAlerts'

const { alerts, showAlert } = useAlerts()

const {
  tasks,
  tareaParaEditar,
  loadTasks,
  completarTarea,
  editarTarea,
  limpiarEdicion,
  eliminarTarea,
  formatDate
} = useTareas(showAlert)

// Manejadores de alertas para el formulario
const handleCreated = () => {
  showAlert('¡Tarea creada exitosamente! 🎉', 'success')
}

const handleUpdated = () => {
  showAlert('¡Tarea actualizada correctamente! ✏️', 'success')
}

const handleError = (message) => {
  showAlert(message || '❌ Error en la operación', 'error')
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');


.alerts-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.alerts-enter-active {
  animation: alertSlideIn 0.4s ease-out;
}

.alerts-leave-active {
  animation: alertSlideOut 0.3s ease-in;
}

@keyframes alertSlideIn {
  from {
    opacity: 0;
    transform: translateX(100%);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes alertSlideOut {
  from {
    opacity: 1;
    transform: translateX(0);
  }
  to {
    opacity: 0;
    transform: translateX(100%);
  }
}


.alerts-enter-from,
.alerts-leave-to {
  opacity: 0;
  transform: translateX(100px);
}

.alerts-move {
  transition: transform 0.5s ease;
}

.task-container {
  min-height: 100vh;
  padding: 1rem 7rem 1rem 7.5rem;
  background: linear-gradient(to bottom right, #f4f4f5, #e0e7ff);
  color: #333;
  transition: background 0.3s ease, color 0.3s ease;
  position: relative;
  font-family: 'Poppins', sans-serif;
}

.task-container.dark {
  background: linear-gradient(to bottom right, #1a1f2b, #2b3241);
  color: #e0e0e0;
}

.theme-toggle {
  position: absolute;
  top: 1rem;
  right: 1rem;
}

.task-view {
  display: flex;
  gap: 20px;
  margin-top: 0;
  height: calc(100vh - 5rem);
}

.task-form-container,
.task-list-container {
  flex: 1;
  padding: 1.5rem;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', sans-serif;
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.task-container.dark .task-form-container,
.task-container.dark .task-list-container {
  background-color: #2b3241;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
}

.section-title {
  font-size: 2.2rem;
  margin-bottom: 1rem;
  font-family: 'Poppins', sans-serif;
}

.task-form-container input {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  background-color: #fff;
  width: 100%;
  margin-bottom: 1rem;
  font-family: 'Poppins', sans-serif;
}

.task-container.dark .task-form-container input {
  background-color: #2b3241;
  border-color: #444;
  color: white;
}

.task-form-container input:focus {
  outline: none;
  border-color: #00a2ff;
  box-shadow: 0 0 0 3px #00a2ff;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.task-container.dark .task-form-container input:focus {
  border-color: #5856d6;
  box-shadow: 0 0 0 3px #5856d6;
}

.task-list {
  list-style: none;
  padding: 0;
  margin: 0;
  overflow-y: auto;
  flex-grow: 1;
  padding-right: 8px;
}

.task-list::-webkit-scrollbar {
  width: 8px;
}

.task-list::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.task-list::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.task-container.dark .task-list::-webkit-scrollbar-track {
  background: #2b3241;
}

.task-container.dark .task-list::-webkit-scrollbar-thumb {
  background: #555;
}

.task-item {
  margin-bottom: 15px;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  min-height: 120px;
}

.task-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.task-actions {
  display: flex;
  gap: 8px;
}

.complete-btn {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.edit-btn {
  background-color: #2196f3;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}

.completada {
  color: rgb(4, 223, 4);
  font-weight: bold;
  font-family: 'Poppins', sans-serif;
}
</style>
