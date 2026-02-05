'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Promocion } from '../../types/promocion.types';
import { Sucursal } from '../../types/sucursal.types';
import { Plus, Trash2, Ticket, Percent } from 'lucide-react';

export default function PromocionesPage() {
  const [promociones, setPromociones] = useState<Promocion[]>([]);
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [selectedSucursal, setSelectedSucursal] = useState<string>('');
  
  const [loading, setLoading] = useState(false);
  const [modalOpen, setModalOpen] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    discount_percentage: 0,
    start_date: '',
    end_date: ''
  });

  // Cargar Sucursales
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

  //  Cargar Promociones
  const cargarPromociones = async () => {
    if (!selectedSucursal) return;
    setLoading(true);
    try {
      const data = await adminService.getPromociones(selectedSucursal);
      setPromociones(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error(error);
      setPromociones([]);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarPromociones();
  }, [selectedSucursal]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await adminService.createPromocion({
        sucursal_id: selectedSucursal,
        ...formData
      });
      setModalOpen(false);
      setFormData({ name: '', description: '', discount_percentage: 0, start_date: '', end_date: '' });
      cargarPromociones();
      alert('Promoción creada');
    } catch (error) {
      alert('Error al crear promoción');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm('¿Eliminar esta promoción?')) {
      await adminService.deletePromocion(id);
      cargarPromociones();
    }
  };

  return (
    <div className="p-6">
      <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        <h1 className="text-3xl font-bold flex items-center gap-2 text-primary">
          <Ticket /> Promociones
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
          <Plus size={20} /> Nueva Promo
        </button>
      </div>

      {/* TABLA */}
      <div className="overflow-x-auto bg-base-100 shadow-xl rounded-box">
        <table className="table table-zebra w-full">
          <thead>
            <tr className="bg-base-200">
              <th>Nombre</th>
              <th>Descuento</th>
              <th>Vigencia</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={5} className="text-center p-4">Cargando...</td></tr>
            ) : promociones.length === 0 ? (
              <tr><td colSpan={5} className="text-center p-4 text-gray-500">No hay promociones activas</td></tr>
            ) : (
              promociones.map((promo) => (
                <tr key={promo.id}>
                  <td className="font-bold">
                    {promo.name}
                    <div className="text-xs font-normal text-gray-500">{promo.description}</div>
                  </td>
                  <td>
                    <div className="badge badge-accent text-white gap-1 font-bold">
                      <Percent size={12}/> {promo.discount_percentage}%
                    </div>
                  </td>
                  <td className="text-sm">
                    {promo.start_date} <span className="text-gray-400">hasta</span> {promo.end_date}
                  </td>
                  <td>
                    {promo.is_active ? 
                      <div className="badge badge-success text-white">Activa</div> : 
                      <div className="badge badge-ghost">Inactiva</div>
                    }
                  </td>
                  <td>
                    <button onClick={() => handleDelete(promo.id)} className="btn btn-ghost btn-xs text-error">
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
            <h3 className="font-bold text-lg mb-4">Nueva Promoción</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-3">
              
              <div className="form-control">
                <label className="label"><span className="label-text">Nombre de la Promo *</span></label>
                <input 
                  type="text" placeholder="Ej: Descuento Verano" className="input input-bordered" required
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                />
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Descripción</span></label>
                <textarea 
                  className="textarea textarea-bordered" placeholder="Detalles de la promo..."
                  value={formData.description}
                  onChange={(e) => setFormData({...formData, description: e.target.value})}
                ></textarea>
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Porcentaje de Descuento (%) *</span></label>
                <input 
                  type="number" min="1" max="100" className="input input-bordered" required
                  value={formData.discount_percentage}
                  onChange={(e) => setFormData({...formData, discount_percentage: parseFloat(e.target.value)})}
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="form-control">
                  <label className="label"><span className="label-text">Fecha Inicio *</span></label>
                  <input 
                    type="date" className="input input-bordered" required
                    value={formData.start_date}
                    onChange={(e) => setFormData({...formData, start_date: e.target.value})}
                  />
                </div>
                <div className="form-control">
                  <label className="label"><span className="label-text">Fecha Fin *</span></label>
                  <input 
                    type="date" className="input input-bordered" required
                    value={formData.end_date}
                    onChange={(e) => setFormData({...formData, end_date: e.target.value})}
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