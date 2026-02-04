import api from '@/lib/axios';
import { Reserva } from '@/types/reserva.types';

const BASE_ROUTE = '/reservations'; 

export const reservasService = {
  createReserva: async (reservaData: Reserva) => {
    try {
      const clientePayload = {
        nombre: reservaData.customer_name, 
        apellido: ".", 
        correo: reservaData.customer_email,
        telefono: reservaData.customer_phone
      };

      let clienteId;
      
      try {
        const resCliente = await api.post(`${BASE_ROUTE}/crear_cliente`, clientePayload);
        clienteId = resCliente.data.id || resCliente.data.data?.id; 
        if (!clienteId && resCliente.data.cliente_id) clienteId = resCliente.data.cliente_id;

      } catch (error) {
        console.warn("Error registrando cliente (puede que ya exista):", error);
        throw new Error("No se pudo registrar el cliente. Verifique si el correo ya está en uso.");
      }

      if (!clienteId) throw new Error("El sistema no pudo obtener el ID del cliente.");
      const reservaPayload = {
        fecha_reserva: reservaData.reservation_date, 
        hora_reserva: reservaData.reservation_time,  
        cantidad_personas: reservaData.number_of_people,
        cliente_id: clienteId,
        sucursal_id: parseInt(reservaData.sucursal_id), 
        mesa_id: null, 
        estado: "PENDING"
      };

      const { data } = await api.post(`${BASE_ROUTE}/crear_reserva`, reservaPayload);
      return data;

    } catch (error) {
      console.error("Error en flujo de reserva:", error);
      throw error;
    }
  },

  getAllReservas: async (sucursalId?: string, date?: string) => {
    try {
      const { data } = await api.get(`${BASE_ROUTE}/listar_reservas`);
      const listaReservas = Array.isArray(data) ? data : data.data || [];
      return listaReservas;
    } catch (error) {
      console.error("Error obteniendo reservas:", error);
      return [];
    }
  },

  checkAvailability: async (sucursalId: string, date: string, people: number) => {
    return { available: true }; 
  },

  updateStatus: async (id: string, status: string) => {
    const { data } = await api.patch(`${BASE_ROUTE}/reservas/${id}/status`, { status });
    return data;
  },

  getMyReservas: async (email: string) => {
    return []; 
  }
};