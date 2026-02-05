'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Sucursal } from '../../types/sucursal.types';
import { Restaurante } from '../../types/restaurante.types';
import { Plus, Trash2, Store, MapPin } from 'lucide-react';

export default function SucursalesPage() {
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [restaurantes, setRestaurantes] = useState<Restaurante[]>([]); // Para el Select
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [formData, setFormData] = useState({
    restaurante_id: '',
    name: '',
    address: '',
    phone: '',
    tolerance_minutes: 15
  });

  const cargarDatos = async () => {
    try {
      setLoading(true);
      const [listaSucursales, listaRestaurantes] = await Promise.all([
        adminService.getSucursales(),
        adminService.getRestaurantes()
      ]);

      setSucursales(Array.isArray(listaSucursales) ? listaSucursales : []);
      setRestaurantes(Array.isArray(listaRestaurantes) ? listaRestaurantes : []);
    } catch (error) {
      console.error("Error cargando datos", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarDatos();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.restaurante_id) {
      alert("Debes seleccionar un restaurante");
      return;
    }
    try {
      await adminService.createSucursal(formData);
      setModalOpen(false);
      setFormData({ ...formData, name: '', address: '', phone: '' }); 
      cargarDatos();
      alert('Sucursal creada');
    } catch (error) {
      console.error(error);
      alert('Error al crear');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm('¿Eliminar sucursal?')) {
      try {
        await adminService.deleteSucursal(id);
        cargarDatos();
      } catch (e) { alert('Error al eliminar'); }
    }
  };

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold flex items-center gap-2 text-primary">
          <Store /> Sucursales
        </h1>
        <button className="btn btn-primary" onClick={() => setModalOpen(true)}>
          <Plus size={20} /> Nueva Sucursal
        </button>
      </div>

      {/* TABLA */}
      <div className="overflow-x-auto bg-base-100 shadow-xl rounded-box">
        <table className="table table-zebra w-full">
          <thead>
            <tr className="bg-base-200">
              <th>Restaurante</th>
              <th>Sucursal</th>
              <th>Dirección</th>
              <th>Teléfono</th>
              <th>Tolerancia (min)</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={6} className="text-center p-4">Cargando...</td></tr>
            ) : sucursales.length === 0 ? (
              <tr><td colSpan={6} className="text-center p-4 text-gray-500">No hay sucursales registradas</td></tr>
            ) : (
              sucursales.map((suc) => (
                <tr key={suc.id}>
                  <td className="font-bold text-primary">{suc.restaurante_name}</td>
                  <td>{suc.name}</td>
                  <td className="flex items-center gap-1"><MapPin size={14}/> {suc.address}</td>
                  <td>{suc.phone || '-'}</td>
                  <td>{suc.tolerance_minutes} min</td>
                  <td>
                    <button onClick={() => handleDelete(suc.id)} className="btn btn-ghost btn-xs text-error">
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
            <h3 className="font-bold text-lg mb-4">Nueva Sucursal</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-3">
              
              {/* SELECT DE RESTAURANTE */}
              <div className="form-control">
                <label className="label"><span className="label-text">Pertenece al Restaurante *</span></label>
                <select 
                  className="select select-bordered w-full"
                  value={formData.restaurante_id}
                  onChange={(e) => setFormData({...formData, restaurante_id: e.target.value})}
                  required
                >
                  <option value="">-- Seleccione --</option>
                  {restaurantes.map(r => (
                    <option key={r.id} value={r.id}>{r.name}</option>
                  ))}
                </select>
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Nombre de Sucursal *</span></label>
                <input 
                  type="text" placeholder="Ej: Matriz, Sucursal Norte..."
                  className="input input-bordered" required
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                />
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Dirección *</span></label>
                <input 
                  type="text" className="input input-bordered" required
                  value={formData.address}
                  onChange={(e) => setFormData({...formData, address: e.target.value})}
                />
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Teléfono</span></label>
                <input 
                  type="text" className="input input-bordered"
                  value={formData.phone}
                  onChange={(e) => setFormData({...formData, phone: e.target.value})}
                />
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