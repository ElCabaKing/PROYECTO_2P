import axios from 'axios';
import { Reserva } from '@/types/reserva.types';

// PUERTO 5002: Microservicio de Reservas
const API_URL = 'http://localhost:5002'; 

export const reservasService = {
  checkAvailability: async (sucursalId: string, date: string, people: number) => {
    // Endpoint hipotético: GET /availability?date=2023-10-20&people=4
    const { data } = await axios.get(`${API_URL}/availability`, {
      params: { sucursal_id: sucursalId, date, people }
    });
    return data.data; 
  },

  createReserva: async (reserva: Reserva) => {
    const { data } = await axios.post(`${API_URL}/reservas`, reserva);
    return data.data;
  },

  getMyReservas: async (email: string) => {
    const { data } = await axios.get(`${API_URL}/reservas?email=${email}`);
    return data.data;
  },

  getAllReservas: async (sucursalId?: string, date?: string) => {
    let url = `${API_URL}/reservas`;
    const params = new URLSearchParams();
    if (sucursalId) params.append('sucursal_id', sucursalId);
    if (date) params.append('date', date);
    
    if (params.toString()) url += `?${params.toString()}`;

    const { data } = await axios.get(url); 
    return data.data;
  },

  updateStatus: async (id: string, status: 'CONFIRMED' | 'CANCELLED' | 'NO_SHOW') => {
    const { data } = await axios.patch(`${API_URL}/reservas/${id}/status`, { status });
    return data.data;
  }
};