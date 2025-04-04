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
import { ref, onMounted } from 'vue';
import api from '@/services/api';
import TaskForm from '@/components/TaskForm.vue';
import NavBar from '@/components/NavBar.vue';

const tasks = ref([]);
const tareaParaEditar = ref(null); // almacena la tarea seleccionada para edición

const loadTasks = async () => {
  try {
    const res = await api.get('/tareas');
    tasks.value = res.data;
  } catch (error) {
    console.error('Error al cargar tareas:', error);
  }
};

const completarTarea = async (task) => {
  try {
    await api.put(`/tareas/${task.id}`, {
      titulo: task.titulo,
      descripcion: task.descripcion,
      prioridad: task.prioridad,
      fecha_limite: task.fecha_limite,
      estado: 'Completada',
    });
    loadTasks();
  } catch (error) {
    console.error('Error al completar tarea:', error);
  }
};

const editarTarea = (task) => {
  tareaParaEditar.value = { ...task }; // pasamos la tarea al formulario
};

const limpiarEdicion = () => {
  tareaParaEditar.value = null; // resetea el formulario al crear nueva
};

const eliminarTarea = async (id) => {
  try {
    await api.delete(`/tareas/${id}`);
    loadTasks();
  } catch (error) {
    console.error('Error al eliminar tarea:', error);
  }
};

const formatDate = (dateStr) => {
  if (!dateStr) return 'No asignada';
  const date = new Date(dateStr);
  return date.toLocaleDateString('es-ES', { year: 'numeric', month: 'short', day: 'numeric' });
};

onMounted(() => {
  loadTasks();
});
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
