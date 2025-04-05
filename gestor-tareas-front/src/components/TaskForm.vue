<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <input v-model="titulo" class="form-input" placeholder="Título" required />

    <textarea
      v-model="descripcion"
      class="form-input"
      placeholder="Descripción"
      rows="3"
    ></textarea>

    <label class="form-label">
      Prioridad:
      <select v-model="prioridad" class="form-input">
        <option disabled value="">Selecciona una prioridad</option>
        <option value="Alta">Alta</option>
        <option value="Media">Media</option>
        <option value="Baja">Baja</option>
      </select>
    </label>

    <label class="form-label">
      Fecha Límite:
      <input type="date" v-model="fecha_limite" class="form-input" />
    </label>

    <button type="submit" class="submit-btn">
      {{ tareaEditable ? 'Actualizar tarea' : 'Crear tarea' }}
    </button>

    <button
      v-if="tareaEditable"
      type="button"
      @click="cancelarEdicion"
      class="cancelar-btn"
    >
      Cancelar
    </button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue';
import api from '@/services/api';

const props = defineProps({
  tareaEditable: Object
});

const emit = defineEmits(['refresh', 'limpiar', 'created', 'updated', 'error']);

const titulo = ref('');
const descripcion = ref('');
const prioridad = ref('');
const fecha_limite = ref('');

watch(() => props.tareaEditable, (nuevaTarea) => {
  if (nuevaTarea) {
    titulo.value = nuevaTarea.titulo;
    descripcion.value = nuevaTarea.descripcion;
    prioridad.value = nuevaTarea.prioridad || '';
    fecha_limite.value = nuevaTarea.fecha_limite?.split('T')[0] || '';
  } else {
    limpiarFormulario();
  }
});

const limpiarFormulario = () => {
  titulo.value = '';
  descripcion.value = '';
  prioridad.value = '';
  fecha_limite.value = '';
};

const handleSubmit = async () => {
  try {
    if (props.tareaEditable) {
      await api.put(`/tareas/${props.tareaEditable.id}`, {
        titulo: titulo.value,
        descripcion: descripcion.value,
        prioridad: prioridad.value,
        fecha_limite: fecha_limite.value || null,
        estado: props.tareaEditable.estado || 'Pendiente'
      });
      emit('updated'); // Nuevo evento para actualización
    } else {
      await api.post('/tareas', {
        titulo: titulo.value,
        descripcion: descripcion.value,
        prioridad: prioridad.value,
        fecha_limite: fecha_limite.value || null
      });
      emit('created'); // Nuevo evento para creación
    }

    limpiarFormulario();
    emit('refresh');
    emit('limpiar');
  } catch (error) {
    console.error('Error al enviar el formulario:', error);
    emit('error', error.response?.data?.message || 'Error en el formulario'); // Nuevo evento de error
  }
};

const cancelarEdicion = () => {
  limpiarFormulario();
  emit('limpiar');
};
</script>


<style scoped>

.task-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
  box-sizing: border-box;
  width: 100%;
}

.form-input {
  padding: 0.8rem;
  width: 100%;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  background-color: #fff;
  color: #333;
  margin-bottom: 0.5rem;
  transition: all 0.3s ease;
  font-family: 'Poppins', sans-serif;
  box-sizing: border-box;
  width: calc(100% - 2px);
}

textarea.form-input {
  resize: vertical;
  min-height: 80px;
}

.form-input:focus {
  outline: none;
  border-color: #00a2ff;
  box-shadow: 0 0 0 3px rgba(0, 162, 255, 0.3);
}

.task-container.dark .form-input {
  background-color: #1e2533;
  border: 1px solid #444;
  color: #eee;
}

.task-container.dark .form-input:focus {
  border-color: #5856d6;
  box-shadow: 0 0 0 3px rgba(88, 86, 214, 0.4);
}

.form-label {
  font-weight: 500;
  font-size: 0.95rem;
  margin-bottom: 4px;
  display: flex;
  flex-direction: column;
  color: inherit;
  font-family: 'Poppins', sans-serif;
}

.submit-btn {
  background-color: #4caf50;
  color: white;
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.submit-btn:hover {
  background-color: #43a047;
}

.cancelar-btn {
  background-color: #ccc;
  color: black;
  border: none;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.2s ease;
}

.cancelar-btn:hover {
  background-color: #b0b0b0;
}
</style>
