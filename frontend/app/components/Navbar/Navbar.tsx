import Link from 'next/link';
import { LayoutDashboard, Store, MapPin, LogOut, UtensilsCrossed, Clock, Ticket, CalendarDays } from 'lucide-react';

export default function Sidebar() {
  return (
    <div className="drawer-side z-20">
      <label htmlFor="my-drawer-2" className="drawer-overlay"></label>
      
      <aside className="bg-base-200 w-80 min-h-screen flex flex-col text-base-content">
        {/* LOGO */}
        <div className="p-4 bg-primary text-primary-content font-bold text-2xl flex items-center gap-2">
          <UtensilsCrossed />
          <span>RestauAdmin</span>
        </div>

        {/* MENÚ DE NAVEGACIÓN */}
        <ul className="menu p-4 w-full gap-2 text-base flex-1">
          {/* Título de sección */}
          <li className="menu-title">Administración</li>
          
          <li>
            <Link href="/home" className="active:bg-primary/10">
              <LayoutDashboard size={20} />
              Resumen
            </Link>
          </li>
          <li>
            <Link href="/restaurantes">
              <Store size={20} />
              Restaurantes
            </Link>
          </li>
          <li>
            <Link href="/sucursales">
              <MapPin size={20} />
              Sucursales
            </Link>
          </li>
          <li>
            <Link href="/mesas">
              <UtensilsCrossed size={20} />
              Gestión de Mesas
            </Link>
          </li>
          <li>
            <Link href="/horarios">
              <Clock size={20} /> 
              Horarios
            </Link>
          </li>
          <li>
            <Link href="/promociones">
              <Ticket size={20} />
              Promociones
            </Link>
          </li>
          <li>
            <Link href="/gestion-reservas">
              <CalendarDays size={20} />  
              Gestión de Reservas
            </Link>
          </li>
        </ul>

        {/* BOTÓN SALIR */}
        <div className="p-4 border-t border-base-300">
          <button className="btn btn-outline btn-error w-full gap-2">
            <LogOut size={20} />
            Cerrar Sesión
          </button>
        </div>
      </aside>
    </div>
  );
}