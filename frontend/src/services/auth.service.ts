import api from '@/lib/axios';

export const authService = {
  login: async (username: string, password: string) => {
    const { data } = await api.post('/security/login', { 
      username, 
      password 
    });
    return data;
  },

  logout: () => {
    if (typeof window !== 'undefined') {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
    }
  }
};