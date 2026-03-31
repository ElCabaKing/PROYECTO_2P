'use client';
import { useEffect, useState } from 'react';
import { reservasService } from '@/services/reservas.service';
import { adminService } from '@/services/admin.service'; 
import { Reserva } from '@/types/reserva.types';
import { Sucursal } from '@/types/sucursal.types';
import { CalendarDays, CheckCircle, XCircle, Clock, Filter } from 'lucide-react';

export default function GestionReservasPage() {
  const [reservas, setReservas] = useState<Reserva[]>([]);
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [loading, setLoading] = useState(true);
  

  const [selectedSucursal, setSelectedSucursal] = useState('');
  const [filterDate, setFilterDate] = useState(new Date().toISOString().split('T')[0]); 

  useEffect(() => {
    adminService.getSucursales().then(data => {
      setSucursales(Array.isArray(data) ? data : []);
      if (Array.isArray(data) && data.length > 0) setSelectedSucursal(data[0].id);
    });
  }, []);

  const cargarReservas = async () => {
    if (!selectedSucursal) return;
    setLoading(true);
    try {
      const data = await reservasService.getAllReservas(selectedSucursal, filterDate);
      setReservas(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
      setReservas([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarReservas();
  }, [selectedSucursal, filterDate]);


  const handleStatusChange = async (id: string, newStatus: 'CONFIRMED' | 'CANCELLED') => {
    if(!confirm(`¿Estás seguro de cambiar el estado a ${newStatus}?`)) return;
    try {
      await reservasService.updateStatus(id, newStatus);
      cargarReservas(); 
      alert('Estado actualizado');
    } catch (error) {
      alert('Error al actualizar');
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold flex items-center gap-2 mb-6 text-primary">
        <CalendarDays /> Control de Reservas
      </h1>

      {/* BARRA DE FILTROS */}
      <div className="bg-base-100 p-4 rounded-lg shadow mb-6 flex flex-wrap gap-4 items-end">
        
        <div className="form-control w-full max-w-xs">
          <label className="label"><span className="label-text flex gap-1"><Filter size={14}/> Sucursal</span></label>
          <select 
            className="select select-bordered"
            value={selectedSucursal}
            onChange={(e) => setSelectedSucursal(e.target.value)}
          >
            {sucursales.map(s => <option key={s.id} value={s.id}>{s.name}</option>)}
          </select>
        </div>

        <div className="form-control w-full max-w-xs">
          <label className="label"><span className="label-text">Fecha</span></label>
          <input 
            type="date" 
            className="input input-bordered"
            value={filterDate}
            onChange={(e) => setFilterDate(e.target.value)}
          />
        </div>

        <button className="btn btn-ghost" onClick={cargarReservas}>Refrescar</button>
      </div>

      {/* TABLA DE RESERVAS */}
      <div className="overflow-x-auto bg-base-100 shadow-xl rounded-box">
        <table className="table w-full">
          <thead>
            <tr className="bg-base-200">
              <th>Hora</th>
              <th>Cliente</th>
              <th>Contacto</th>
              <th>Personas</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={6} className="text-center p-8">Cargando reservas...</td></tr>
            ) : reservas.length === 0 ? (
              <tr><td colSpan={6} className="text-center p-8 text-gray-500">No hay reservas para esta fecha.</td></tr>
            ) : (
              reservas.map((res) => (
                <tr key={res.id}>
                  <td className="font-bold text-lg">{res.reservation_time}</td>
                  <td>
                    <div className="font-bold">{res.customer_name}</div>
                    <div className="text-xs opacity-50">Mesa sugerida: {res.table_id || 'Automática'}</div>
                  </td>
                  <td className="text-sm">
                    <div>{res.customer_email}</div>
                    <div>{res.customer_phone}</div>
                  </td>
                  <td>{res.number_of_people} pax</td>
                  <td>
                    {res.status === 'CONFIRMED' && <div className="badge badge-success text-white">Confirmada</div>}
                    {res.status === 'CANCELLED' && <div className="badge badge-error text-white">Cancelada</div>}
                    {(!res.status || res.status === 'PENDING') && <div className="badge badge-warning text-white">Pendiente</div>}
                  </td>
                  <td className="flex gap-2">
                    {/* Botones de acción */}
                    <button 
                      className="btn btn-square btn-sm btn-outline btn-success tooltip" 
                      data-tip="Confirmar"
                      onClick={() => res.id && handleStatusChange(res.id, 'CONFIRMED')}
                    >
                      <CheckCircle size={16} />
                    </button>
                    <button 
                      className="btn btn-square btn-sm btn-outline btn-error tooltip" 
                      data-tip="Cancelar"
                      onClick={() => res.id && handleStatusChange(res.id, 'CANCELLED')}
                    >
                      <XCircle size={16} />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}