import Sidebar from "../components/Navbar/Navbar";

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="drawer lg:drawer-open bg-base-100">
      {/* Control del Drawer para móviles */}
      <input id="my-drawer-2" type="checkbox" className="drawer-toggle" />
      
      {/* CONTENIDO PRINCIPAL (Lado derecho) */}
      <div className="drawer-content flex flex-col">
        {/* Barra superior solo para móvil (Hamburguesa) */}
        <div className="w-full navbar bg-base-100 lg:hidden border-b">
          <div className="flex-none">
            <label htmlFor="my-drawer-2" className="btn btn-square btn-ghost">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block w-6 h-6 stroke-current"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </label>
          </div>
          <div className="flex-1 px-2 mx-2 font-bold">Menú</div>
        </div>

        {/* AQUÍ SE CARGAN LAS PÁGINAS (Restaurantes, Sucursales, etc.) */}
        <main className="min-h-screen bg-base-200/50">
          {children}
        </main>
      </div>
      
      {/* BARRA LATERAL */}
      <Sidebar />
    </div>
  );
}