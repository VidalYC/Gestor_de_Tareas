import { defineStore } from 'pinia';
import api from '@/services/api';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    returnUrl: null
  }),
  actions: {
    async login(username, password) {
      try {
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);
    
        const response = await api.post('/usuarios/login', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
        });
    
        localStorage.setItem('access_token', response.data.access_token);
        this.user = await this.me();
        return this.user;
      } catch (error) {
        throw error.response?.data?.detail || 'Error de autenticación';
      }
    },

    async me() {
      try {
        const response = await api.get('/usuarios/me');
        this.user = response.data;
        return this.user;
      } catch (error) {
        this.logout();
        return null;
      }
    },

    logout() {
      localStorage.removeItem('access_token');
      this.user = null;
    }
  }
});
