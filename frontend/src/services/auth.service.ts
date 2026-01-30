import axios from 'axios';

const API_URL = 'http://localhost:5003'; 

export const authService = {
  login: async (username: string, password: string) => {
    const { data } = await axios.post(`${API_URL}/login`, { 
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