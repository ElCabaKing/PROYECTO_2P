'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Horario, DIAS_SEMANA } from '../../types/horario.types';
import { Sucursal } from '../../types/sucursal.types';
import { Plus, Trash2, Clock, Calendar } from 'lucide-react';

export default function HorariosPage() {
  const [horarios, setHorarios] = useState<Horario[]>([]);
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [selectedSucursal, setSelectedSucursal] = useState<string>('');
  
  const [loading, setLoading] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  
  const [formData, setFormData] = useState({
    day_of_week: 1, // Lunes por defecto
    opening_time: '09:00',
    closing_time: '18:00'
  });

  useEffect(() => {
    const cargarSucursales = async () => {
      try {
        const data = await adminService.getSucursales();
        setSucursales(Array.isArray(data) ? data : []);
        if (Array.isArray(data) && data.length > 0) setSelectedSucursal(data[0].id);
      } catch (error) { console.error(error); }
    };
    cargarSucursales();
  }, []);

  const cargarHorarios = async () => {
    if (!selectedSucursal) return;
    setLoading(true);
    try {
      const data = await adminService.getHorarios(selectedSucursal);
      const ordenados = (Array.isArray(data) ? data : []).sort((a, b) => {
          const diaA = a.day_of_week === 0 ? 7 : a.day_of_week;
          const diaB = b.day_of_week === 0 ? 7 : b.day_of_week;
          return diaA - diaB;
      });
      setHorarios(ordenados);
    } catch (error) {
      console.error(error);
      setHorarios([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarHorarios();
  }, [selectedSucursal]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await adminService.createHorario({
        sucursal_id: selectedSucursal,
        ...formData
      });
      setModalOpen(false);
      cargarHorarios();
      alert('Horario agregado');
    } catch (error) {
      alert('Error: Es posible que ya exista un horario para ese día.');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm('¿Eliminar este horario?')) {
      await adminService.deleteHorario(id);
      cargarHorarios();
    }
  };

  return (
    <div className="p-6">
      <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        <h1 className="text-3xl font-bold flex items-center gap-2 text-primary">
          <Clock /> Gestión de Horarios
        </h1>
        
        {/* FILTRO SUCURSAL */}
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold">Sucursal:</span>
          <select 
            className="select select-bordered select-sm"
            value={selectedSucursal}
            onChange={(e) => setSelectedSucursal(e.target.value)}
          >
            <option value="" disabled>-- Seleccione --</option>
            {sucursales.map(s => (
              <option key={s.id} value={s.id}>{s.name}</option>
            ))}
          </select>
        </div>

        <button 
          className="btn btn-primary" 
          onClick={() => setModalOpen(true)}
          disabled={!selectedSucursal}
        >
          <Plus size={20} /> Agregar Horario
        </button>
      </div>

      {/* TABLA */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {loading ? <p>Cargando horarios...</p> : horarios.length === 0 ? (
          <div className="col-span-3 text-center p-10 bg-base-100 rounded-box shadow">
            <Calendar className="mx-auto h-12 w-12 text-gray-400 mb-2"/>
            <p>No hay horarios configurados para esta sucursal.</p>
          </div>
        ) : (
          horarios.map((horario) => (
            <div key={horario.id} className="card bg-base-100 shadow-lg border-l-4 border-primary">
              <div className="card-body p-4 flex-row justify-between items-center">
                <div>
                  <h3 className="card-title text-lg">{horario.day_name || DIAS_SEMANA.find(d => d.id === horario.day_of_week)?.nombre}</h3>
                  <div className="badge badge-ghost gap-2 mt-1">
                    <Clock size={14}/> {horario.opening_time.slice(0,5)} - {horario.closing_time.slice(0,5)}
                  </div>
                </div>
                <button onClick={() => handleDelete(horario.id)} className="btn btn-ghost btn-sm text-error">
                  <Trash2 size={18} />
                </button>
              </div>
            </div>
          ))
        )}
      </div>

      {/* MODAL */}
      {modalOpen && (
        <div className="modal modal-open">
          <div className="modal-box">
            <h3 className="font-bold text-lg mb-4">Nuevo Horario de Atención</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
              
              <div className="form-control">
                <label className="label"><span className="label-text">Día de la Semana</span></label>
                <select 
                  className="select select-bordered"
                  value={formData.day_of_week}
                  onChange={(e) => setFormData({...formData, day_of_week: parseInt(e.target.value)})}
                >
                  {DIAS_SEMANA.map(d => (
                    <option key={d.id} value={d.id}>{d.nombre}</option>
                  ))}
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="form-control">
                  <label className="label"><span className="label-text">Apertura</span></label>
                  <input 
                    type="time" className="input input-bordered" required
                    value={formData.opening_time}
                    onChange={(e) => setFormData({...formData, opening_time: e.target.value})}
                  />
                </div>
                <div className="form-control">
                  <label className="label"><span className="label-text">Cierre</span></label>
                  <input 
                    type="time" className="input input-bordered" required
                    value={formData.closing_time}
                    onChange={(e) => setFormData({...formData, closing_time: e.target.value})}
                  />
                </div>
              </div>

              <div className="modal-action">
                <button type="button" className="btn" onClick={() => setModalOpen(false)}>Cancelar</button>
                <button type="submit" className="btn btn-primary">Guardar</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}