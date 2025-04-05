<!-- src/components/FloatingAlert.vue -->
<template>
    <transition name="alert">
      <div v-if="visible" :class="['alert', type]">
        <span class="icon">{{ icon }}</span>
        <div class="content">
          <p class="message">{{ message }}</p>
        </div>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  
  const props = defineProps({
    message: String,
    type: {
      type: String,
      default: 'success',
      validator: (value) => ['success', 'error', 'warning', 'info'].includes(value)
    },
    duration: {
      type: Number,
      default: 3000
    }
  })
  
  const visible = ref(true)
  
  onMounted(() => {
    setTimeout(() => {
      visible.value = false
    }, props.duration)
  })
  
  const icon = {
    success: '✔',
    error: '✖',
    warning: '⚠',
    info: 'ℹ'
  }[props.type]
  </script>
  
  <style scoped>
  .alert {
    position: fixed;
    top: 1.5rem;
    right: 1.5rem;
    padding: 1rem 1.5rem;
    border-radius: 0.8rem;
    display: flex;
    align-items: center;
    gap: 1.2rem;
    max-width: 320px;
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    cursor: pointer;
    transform-origin: top right;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.27, 1.55);
  }
  
 /* Animación de entrada mejorada */
.alert-enter-active {
  animation: bounceIn 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

/* Animación de salida */
.alert-leave-active {
  animation: fadeOut 0.4s ease-out;
}

@keyframes bounceIn {
  0% {
    opacity: 0;
    transform: translateX(100%) scale(0.3);
  }
  60% {
    opacity: 1;
    transform: translateX(-20px) scale(1.1);
  }
  100% {
    transform: translateX(0) scale(1);
  }
}

@keyframes fadeOut {
  from { opacity: 1; }
  to { opacity: 0; }
}
  
  /* Efecto hover */
  .alert:hover {
    transform: translateY(-2px) scale(1.02);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
  }
  
  /* Estilos de color */
  .alert.success {
    background: #d1fae5;
    border: 2px solid #10b981;
    color: #065f46;
  }
  
  .alert.error {
    background: #fee2e2;
    border: 2px solid #ef4444;
    color: #991b1b;
  }
  
  .alert.warning {
    background: #fef3c7;
    border: 2px solid #f59e0b;
    color: #92400e;
  }
  
  .alert.info {
    background: #dbeafe;
    border: 2px solid #3b82f6;
    color: #1e40af;
  }
  
  /* Modo oscuro */
  .dark .alert.success {
    background: #059669;
    border-color: #10b981;
    color: #d1fae5;
  }
  
  .dark .alert.error {
    background: #dc2626;
    border-color: #ef4444;
    color: #fee2e2;
  }
  
  .dark .alert.warning {
    background: #d97706;
    border-color: #f59e0b;
    color: #fef3c7;
  }
  
  .dark .alert.info {
    background: #2563eb;
    border-color: #3b82f6;
    color: #dbeafe;
  }
  
  .icon {
    font-size: 1.4rem;
    line-height: 1;
  }
  
  .message {
    margin: 0;
    font-size: 0.95rem;
    line-height: 1.4;
  }
  </style>