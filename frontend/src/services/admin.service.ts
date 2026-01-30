import axios from 'axios';
import { Restaurante, CrearRestauranteDTO } from '@/types/restaurante.types';
import { Sucursal, CrearSucursalDTO } from '@/types/sucursal.types';
import { Mesa, CrearMesaDTO } from '@/types/mesa.types';
import { Horario, CrearHorarioDTO } from '@/types/horario.types';
import { Promocion, CrearPromocionDTO } from '@/types/promocion.types';

const API_URL = 'http://localhost:5001/api/admin'; 

// Configuración para enviar el Token en cada petición
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return { headers: { Authorization: `Bearer ${token}` } };
};

export const adminService = {
  
  getRestaurantes: async () => {
    const { data } = await axios.get(`${API_URL}/restaurantes`, getAuthHeaders());
    return data.data; 
  },

  createRestaurante: async (restaurante: CrearRestauranteDTO) => {
    const { data } = await axios.post(`${API_URL}/restaurantes`, restaurante, getAuthHeaders());
    return data.data;
  },

  deleteRestaurante: async (id: string) => {
    const { data } = await axios.delete(`${API_URL}/restaurantes/${id}`, getAuthHeaders());
    return data;
  },

  getSucursales: async (restauranteId?: string) => {
    const url = restauranteId 
      ? `${API_URL}/sucursales?restaurante_id=${restauranteId}`
      : `${API_URL}/sucursales`;
      
    const { data } = await axios.get(url, getAuthHeaders());
    return data.data; 
  },

  createSucursal: async (sucursal: CrearSucursalDTO) => {
    const { data } = await axios.post(`${API_URL}/sucursales`, sucursal, getAuthHeaders());
    return data.data;
  },

  deleteSucursal: async (id: string) => {
    const { data } = await axios.delete(`${API_URL}/sucursales/${id}`, getAuthHeaders());
    return data;
  },

  getMesas: async (sucursalId?: string) => {
    const url = sucursalId 
      ? `${API_URL}/mesas?sucursal_id=${sucursalId}`
      : `${API_URL}/mesas`; 
      
    const { data } = await axios.get(url, getAuthHeaders());
    return data.data;
  },

  createMesa: async (mesa: CrearMesaDTO) => {
    const { data } = await axios.post(`${API_URL}/mesas`, mesa, getAuthHeaders());
    return data.data;
  },

  deleteMesa: async (id: string) => {
    const { data } = await axios.delete(`${API_URL}/mesas/${id}`, getAuthHeaders());
    return data;
  },

  getHorarios: async (sucursalId: string) => {
    const { data } = await axios.get(`${API_URL}/horarios?sucursal_id=${sucursalId}`, getAuthHeaders());
    return data.data;
  },

  createHorario: async (horario: CrearHorarioDTO) => {
    const { data } = await axios.post(`${API_URL}/horarios`, horario, getAuthHeaders());
    return data.data;
  },

  deleteHorario: async (id: string) => {
    const { data } = await axios.delete(`${API_URL}/horarios/${id}`, getAuthHeaders());
    return data;
  },

  getPromociones: async (sucursalId: string) => {
    const { data } = await axios.get(`${API_URL}/promociones?sucursal_id=${sucursalId}`, getAuthHeaders());
    return data.data;
  },

  createPromocion: async (promocion: CrearPromocionDTO) => {
    const { data } = await axios.post(`${API_URL}/promociones`, promocion, getAuthHeaders());
    return data.data;
  },

  deletePromocion: async (id: string) => {
    const { data } = await axios.delete(`${API_URL}/promociones/${id}`, getAuthHeaders());
    return data;
  }
};
