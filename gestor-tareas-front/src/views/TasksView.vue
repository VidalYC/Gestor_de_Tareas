<template>
  <div>
    <NavBar />
    <h1>Mis Tareas</h1>

    <TaskForm :tareaEditable="tareaParaEditar" @refresh="loadTasks" @limpiar="limpiarEdicion" />

    <ul>
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
            <button @click="editarTarea(task)" class="edit-btn">Editar</button>
            <button @click="eliminarTarea(task.id)" class="delete-btn">Eliminar</button>
          </div>
        </div>

        <p>{{ task.descripcion }}</p>

        <div class="task-meta">
          <span><strong>Prioridad:</strong> {{ task.prioridad || 'No definida' }}</span>
          <span><strong>Fecha límite:</strong> {{ formatDate(task.fecha_limite) }}</span>
          <span><strong>Estado:</strong> 
            <span :class="{ completada: task.estado === 'Completada' }">
              {{ task.estado || 'Pendiente' }}
            </span>
          </span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup>
import TaskForm from '@/components/TaskForm.vue'
import NavBar from '@/components/NavBar.vue'
import { useTareas } from '@/composables/useTareas.js'

const {
  tasks,
  tareaParaEditar,
  loadTasks,
  completarTarea,
  editarTarea,
  limpiarEdicion,
  eliminarTarea,
  formatDate
} = useTareas()
</script>

<style scoped>
.task-item {
  margin-bottom: 15px;
  padding: 10px;
  border-bottom: 1px solid #ccc;
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
  color: green;
  font-weight: bold;
}
</style>
