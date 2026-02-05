'use client';
import { useEffect, useState } from 'react';
import { adminService } from '../../services/admin.service';
import { Building2, Store, Users, TrendingUp, CalendarDays } from 'lucide-react';
import Link from 'next/link';

export default function DashboardHome() {
  const [stats, setStats] = useState({
    restaurantes: 0,
    sucursales: 0,
    reservasHoy: 12, 
    ocupacion: 45    
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const cargarDatos = async () => {
      try {
        const [rests, sucs] = await Promise.all([
          adminService.getRestaurantes().catch(() => []),
          adminService.getSucursales().catch(() => [])
        ]);

        setStats(prev => ({
          ...prev,
          restaurantes: Array.isArray(rests) ? rests.length : 0,
          sucursales: Array.isArray(sucs) ? sucs.length : 0
        }));
      } catch (error) {
        console.error("Error cargando dashboard", error);
      } finally {
        setLoading(false);
      }
    };
    cargarDatos();
  }, []);

  // Componente interno para el Skeleton de los números
  const StatSkeleton = () => <div className="h-8 w-16 bg-gray-200 animate-pulse rounded"></div>;

  return (
    <div className="p-6 space-y-8 animate-fade-in">
      {/* TÍTULO */}
      <div className="flex flex-col md:flex-row justify-between items-center gap-4">
        <div>
          <h1 className="text-3xl font-bold text-primary">Resumen General</h1>
          <p className="text-gray-500">Bienvenido al panel de administración de RestauAdmin.</p>
        </div>
        <div className="text-sm breadcrumbs">
          <ul>
            <li><a>Admin</a></li>
            <li>Dashboard</li>
          </ul>
        </div>
      </div>

      {/* TARJETAS DE ESTADÍSTICAS */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        
        {/* Card 1: Restaurantes */}
        <div className="stats shadow bg-base-100 border-l-4 border-primary">
          <div className="stat">
            <div className="stat-figure text-primary"><Building2 size={32} /></div>
            <div className="stat-title">Restaurantes</div>
            <div className="stat-value text-primary">
              {loading ? <StatSkeleton /> : stats.restaurantes}
            </div>
            <div className="stat-desc">Marcas registradas</div>
          </div>
        </div>

        {/* Card 2: Sucursales */}
        <div className="stats shadow bg-base-100 border-l-4 border-secondary">
          <div className="stat">
            <div className="stat-figure text-secondary"><Store size={32} /></div>
            <div className="stat-title">Sucursales</div>
            <div className="stat-value text-secondary">
              {loading ? <StatSkeleton /> : stats.sucursales}
            </div>
            <div className="stat-desc">Locales activos</div>
          </div>
        </div>

        {/* Card 3: Reservas */}
        <div className="stats shadow bg-base-100 border-l-4 border-accent">
          <div className="stat">
            <div className="stat-figure text-accent"><Users size={32} /></div>
            <div className="stat-title">Reservas Hoy</div>
            <div className="stat-value text-accent">
              {loading ? <StatSkeleton /> : stats.reservasHoy}
            </div>
            <div className="stat-desc">↗︎ 4 nuevas (Simulado)</div>
          </div>
        </div>

        {/* Card 4: Ocupación */}
        <div className="stats shadow bg-base-100 border-l-4 border-info">
          <div className="stat">
            <div className="stat-figure text-info"><TrendingUp size={32} /></div>
            <div className="stat-title">Ocupación</div>
            <div className="stat-value text-info">
              {loading ? <StatSkeleton /> : `${stats.ocupacion}%`}
            </div>
            <div className="stat-desc">Promedio actual</div>
          </div>
        </div>
      </div>

      {/* SECCIÓN INFERIOR */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Accesos Rápidos */}
        <div className="card bg-base-100 shadow-xl col-span-1">
          <div className="card-body">
            <h2 className="card-title mb-4">Accesos Rápidos</h2>
            <div className="grid grid-cols-2 gap-4">
              <Link href="/dashboard/restaurantes" className="btn btn-outline btn-primary h-24 flex-col gap-2">
                <Building2 size={24} /> Gestionar <br/> Restaurantes
              </Link>
              <Link href="/dashboard/mesas" className="btn btn-outline btn-secondary h-24 flex-col gap-2">
                <Users size={24} /> Configurar <br/> Mesas
              </Link>
              <Link href="/dashboard/promociones" className="btn btn-outline btn-accent h-24 flex-col gap-2">
                <TrendingUp size={24} /> Crear <br/> Promoción
              </Link>
              <Link href="/reservas" className="btn btn-outline btn-info h-24 flex-col gap-2">
                <CalendarDays size={24} /> Nueva <br/> Reserva
              </Link>
            </div>
          </div>
        </div>

        {/* Tabla Reciente */}
        <div className="card bg-base-100 shadow-xl lg:col-span-2">
          <div className="card-body">
            <div className="flex justify-between items-center mb-4">
              <h2 className="card-title">Próximas Reservas (Demo)</h2>
              <button className="btn btn-xs btn-ghost">Ver todas</button>
            </div>
            <div className="overflow-x-auto">
              <table className="table table-zebra">
                <thead>
                  <tr>
                    <th>Hora</th><th>Cliente</th><th>Mesa</th><th>Estado</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>19:00</td>
                    <td className="font-bold">Juan Pérez</td>
                    <td>Mesa 4 (Interior)</td>
                    <td><div className="badge badge-success text-white">Confirmada</div></td>
                  </tr>
                  <tr>
                    <td>20:30</td>
                    <td className="font-bold">María López</td>
                    <td>Mesa VIP 1</td>
                    <td><div className="badge badge-warning text-white">Pendiente</div></td>
                  </tr>
                  <tr>
                    <td>21:00</td>
                    <td className="font-bold">Carlos Ruiz</td>
                    <td>Mesa 2 (Terraza)</td>
                    <td><div className="badge badge-success text-white">Confirmada</div></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}