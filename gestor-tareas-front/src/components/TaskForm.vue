<template>
  <form @submit.prevent="handleSubmit" class="task-form">
    <input v-model="titulo" placeholder="Título" required />
    <textarea v-model="descripcion" placeholder="Descripción" rows="3"></textarea>

    <label>
      Prioridad:
      <select v-model="prioridad">
        <option disabled value="">Selecciona una prioridad</option>
        <option value="Alta">Alta</option>
        <option value="Media">Media</option>
        <option value="Baja">Baja</option>
      </select>
    </label>

    <label>
      Fecha Límite:
      <input type="date" v-model="fecha_limite" />
    </label>

    <button type="submit">
      {{ tareaEditable ? 'Actualizar tarea' : 'Crear tarea' }}
    </button>

    <button v-if="tareaEditable" type="button" @click="cancelarEdicion" class="cancelar-btn">
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

const emit = defineEmits(['refresh', 'limpiar']);

const titulo = ref('');
const descripcion = ref('');
const prioridad = ref('');
const fecha_limite = ref('');

// Cuando se pasa una tarea para editar, llenamos los campos
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
      // Actualizar tarea existente
      await api.put(`/tareas/${props.tareaEditable.id}`, {
        titulo: titulo.value,
        descripcion: descripcion.value,
        prioridad: prioridad.value,
        fecha_limite: fecha_limite.value || null,
        estado: props.tareaEditable.estado || 'Pendiente'
      });
    } else {
      // Crear nueva tarea
      await api.post('/tareas', {
        titulo: titulo.value,
        descripcion: descripcion.value,
        prioridad: prioridad.value,
        fecha_limite: fecha_limite.value || null
      });
    }

    limpiarFormulario();
    emit('refresh');
    emit('limpiar');
  } catch (error) {
    console.error('Error al enviar el formulario:', error);
  }
};

const cancelarEdicion = () => {
  limpiarFormulario();
  emit('limpiar'); // le dice al padre que limpie la edición
};
</script>

<style scoped>
.task-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
}

.cancelar-btn {
  background-color: #ccc;
  color: black;
  border: none;
  padding: 6px 10px;
  border-radius: 4px;
  cursor: pointer;
}
</style>
