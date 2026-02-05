'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Restaurante } from '../../types/restaurante.types';
import { Plus, Trash2, Building2 } from 'lucide-react'; 

export default function RestaurantesPage() {
  const [restaurantes, setRestaurantes] = useState<Restaurante[]>([]);
  const [loading, setLoading] = useState(true);
  const [modalOpen, setModalOpen] = useState(false);
  const [formData, setFormData] = useState({ name: '', tax_id: '', legal_name: '' });

  const cargarDatos = async () => {
    try {
      setLoading(true);
      const data = await adminService.getRestaurantes();
      setRestaurantes(Array.isArray(data) ? data : []);
    } catch (error) {
      console.error("Error cargando restaurantes", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarDatos();
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await adminService.createRestaurante(formData);
      setModalOpen(false);
      setFormData({ name: '', tax_id: '', legal_name: '' }); 
      cargarDatos(); 
      alert('Restaurante creado con éxito');
    } catch (error) {
      console.error(error);
      alert('Error creando restaurante');
    }
  };

  const handleDelete = async (id: string) => {
    if (confirm('¿Estás seguro de eliminar este restaurante?')) {
      try {
        await adminService.deleteRestaurante(id);
        cargarDatos();
      } catch (error) {
        console.error(error);
        alert('Error eliminando');
      }
    }
  };

  return (
    <div className="p-6">
      {/* HEADER */}
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold flex items-center gap-2 text-primary">
          <Building2 /> Gestión de Restaurantes
        </h1>
        <button className="btn btn-primary" onClick={() => setModalOpen(true)}>
          <Plus size={20} /> Nuevo Restaurante
        </button>
      </div>

      {/* TABLA */}
      <div className="overflow-x-auto bg-base-100 shadow-xl rounded-box">
        <table className="table table-zebra w-full">
          <thead>
            <tr className="bg-base-200 text-base-content">
              <th>Nombre Comercial</th>
              <th>Razón Social</th>
              <th>RUC/NIT</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {loading ? (
              <tr><td colSpan={5} className="text-center p-4">Cargando datos...</td></tr>
            ) : restaurantes.length === 0 ? (
              <tr><td colSpan={5} className="text-center p-4 text-gray-500">No hay restaurantes registrados</td></tr>
            ) : (
              restaurantes.map((rest) => (
                <tr key={rest.id}>
                  <td className="font-bold">{rest.name}</td>
                  <td>{rest.legal_name || '-'}</td>
                  <td>{rest.tax_id || '-'}</td>
                  <td>
                    {rest.is_active ? 
                      <div className="badge badge-success gap-2 text-white">Activo</div> : 
                      <div className="badge badge-ghost gap-2">Inactivo</div>
                    }
                  </td>
                  <td>
                    <button 
                      onClick={() => handleDelete(rest.id)}
                      className="btn btn-ghost btn-xs text-error tooltip"
                      data-tip="Eliminar"
                    >
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
            <h3 className="font-bold text-lg mb-4">Registrar Nuevo Restaurante</h3>
            <form onSubmit={handleSubmit} className="flex flex-col gap-4">
              
              <div className="form-control">
                <label className="label"><span className="label-text">Nombre Comercial *</span></label>
                <input 
                  type="text" 
                  className="input input-bordered w-full" 
                  required
                  placeholder="Ej: Pizzería Don Pepe"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                />
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">Razón Social</span></label>
                <input 
                  type="text" 
                  className="input input-bordered w-full" 
                  placeholder="Ej: Inversiones Pepe S.A."
                  value={formData.legal_name}
                  onChange={(e) => setFormData({...formData, legal_name: e.target.value})}
                />
              </div>

              <div className="form-control">
                <label className="label"><span className="label-text">RUC / NIT</span></label>
                <input 
                  type="text" 
                  className="input input-bordered w-full" 
                  placeholder="Ej: 1720304050001"
                  value={formData.tax_id}
                  onChange={(e) => setFormData({...formData, tax_id: e.target.value})}
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