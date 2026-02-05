'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Mesa } from '../../types/mesa.types';
import { Sucursal } from '../../types/sucursal.types';
import { Plus, Trash2, UtensilsCrossed, Users } from 'lucide-react';

export default function MesasPage() {
  const [mesas, setMesas] = useState<Mesa[]>([]);
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [selectedSucursal, setSelectedSucursal] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  

  const [formData, setFormData] = useState({
    sucursal_id: '',
    table_number: '',
    capacity_min: 1,
    capacity_max: 4,
    location: 'INTERIOR'
  });

  useEffect(() => {
    const cargarSucursales = async () => {
      try {
        const data = await adminService.getSucursales();
        setSucursales(Array.isArray(data) ? data : []);
        if (Array.isArray(data) && data.length > 0) {
          setSelectedSucursal(data[0].id);
        }
      } catch (error) {
        console.error("Error cargando sucursales", error);
      }
    };
    cargarSucursales();
  }, []);

 
  const cargarMesas = async () => {
    if (!selectedSucursal) return;
    setLoading(true);
    try {
      const data = await adminService.getMesas(selectedSucursal);
      setMesas(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
      setMesas([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarMesas();
  }, [selectedSucursal]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const payload = {
        ...formData,
        sucursal_id: formData.sucursal_id || selectedSucursal
      };
      
      await adminService.createMesa(payload);
      setModalOpen(false);
      cargarMesas(); 
      alert('Mesa creada con éxito');
    } catch (error) {
      console.error(error);
      alert('Error al crear mesa');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm('¿Eliminar esta mesa?')) {
      await adminService.deleteMesa(id);
      cargarMesas();
    }
  };

  return (
    <div className="p-6">
      <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        <h1 className="text-3xl font-bold flex items-center gap-2 text-primary">
          <UtensilsCrossed /> Gestión de Mesas
        </h1>
        
        {/* FILTRO DE SUCURSAL */}
        <div className="flex items-center gap-2">
          <span className="text-sm font-semibold">Ver sucursal:</span>
          <select 
            className="select select-bordered select-sm w-full max-w-xs"
            value={selectedSucursal}
            onChange={(e) => setSelectedSucursal(e.target.value)}
          >
            <option value="" disabled>Seleccione una sucursal</option>
            {sucursales.map(s => (
              <option key={s.id} value={s.id}>{s.name} ({s.restaurante_name})</option>
            ))}
          </select>
        </div>

        <button 
          className="btn btn-primary" 
          onClick={() => {
            setFormData({...formData, sucursal_id: selectedSucursal}); 
            setModalOpen(true);
          }}
          disabled={!selectedSucursal} 
        >
          <Plus size={20} /> Nueva Mesa
        </button>
      </div>

      {/* TABLA */}
      <div className="overflow-x-auto bg-base-100 shadow-xl rounded-box">
        <table className="table table-zebra w-full text-center">
          <thead>
            <tr className="bg-base-200">
              <th>Número</th>
              <th>Capacidad</th>
              <th>Ubicación</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={5} className="p-4">Cargando mesas...</td></tr>
            ) : mesas.length === 0 ? (
              <tr><td colSpan={5} className="p-4 text-gray-500">
                {!selectedSucursal ? "Selecciona una sucursal arriba 👆" : "Esta sucursal no tiene mesas creadas"}
              </td></tr>
            ) : (
              mesas.map((mesa) => (
                <tr key={mesa.id}>
                  <td className="font-bold text-lg">#{mesa.table_number}</td>
                  <td>
                    <div className="badge badge-outline gap-1">
                      <Users size={12}/> {mesa.capacity_min} - {mesa.capacity_max} p.
                    </div>
                  </td>
                  <td>{mesa.location || 'General'}</td>
                  <td>
                    <div className={`badge ${mesa.is_active ? 'badge-success text-white' : 'badge-ghost'}`}>
                      {mesa.is_active ? 'Activa' : 'Inactiva'}
                    </div>
                  </td>
                  <td>
                    <button onClick={() => handleDelete(mesa.id)} className="btn btn-ghost btn-xs text-error">
                      <Trash2 size={16} />
                    </button>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {/* MODAL */}
      {modalOpen && (
        <div className="modal modal-open">
          <div className="modal-box">
            <h3 className="font-bold text-lg mb-4">Nueva Mesa</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-3">
              
              <div className="form-control">
                <label className="label"><span className="label-text">Número de Mesa (Opcional)</span></label>
                <input 
                  type="text" placeholder="Ej: A-10"
                  className="input input-bordered"
                  value={formData.table_number}
                  onChange={(e) => setFormData({...formData, table_number: e.target.value})}
                />
                <span className="label-text-alt text-gray-500 mt-1">Si lo dejas vacío, se asignará automático.</span>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="form-control">
                  <label className="label"><span className="label-text">Mín. Personas</span></label>
                  <input 
                    type="number" min="1" className="input input-bordered"
                    value={formData.capacity_min}
                    onChange={(e) => setFormData({...formData, capacity_min: parseInt(e.target.value)})}
                  />
                </div>
                <div className="form-control">
                  <label className="label"><span className="label-text">Máx. Personas</span></label>
                  <input 
                    type="number" min="1" className="input input-bordered"
                    value={formData.capacity_max}
                    onChange={(e) => setFormData({...formData, capacity_max: parseInt(e.target.value)})}
                  />
                </div>
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Ubicación</span></label>
                <select 
                  className="select select-bordered"
                  value={formData.location}
                  onChange={(e) => setFormData({...formData, location: e.target.value})}
                >
                  <option value="INTERIOR">Interior</option>
                  <option value="EXTERIOR">Exterior</option>
                  <option value="TERRAZA">Terraza</option>
                  <option value="VIP">VIP</option>
                </select>
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