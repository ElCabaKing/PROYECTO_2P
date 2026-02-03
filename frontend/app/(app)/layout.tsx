

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <div>
            <div className="navbar bg-base-100 shadow-sm">
                <div className="flex-none">
                    <div className="drawer">
                        <input id="my-drawer-1" type="checkbox" className="drawer-toggle" />
                        <div className="drawer-content">
                            <label htmlFor="my-drawer-1" className="btn drawer-button">

                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block h-5 w-5 stroke-current"> <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h16"></path> </svg>

                            </label>
                        </div>
                        <div className="drawer-side">
                            <label htmlFor="my-drawer-1" aria-label="close sidebar" className="drawer-overlay"></label>
                            <ul className="menu bg-base-200 min-h-full w-80 p-4">
                                {/* Sidebar content here */}
                                <li><a>Sidebar Item 1</a></li>
                                <li><a>Sidebar Item 2</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="flex-1">
                    <a className="btn btn-ghost text-xl">daisyUI</a>
                </div>
                <div className="flex-none">
                    <button className="btn btn-square btn-ghost">
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" className="inline-block h-5 w-5 stroke-current"> <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path> </svg>
                    </button>
                    <ul className="absolute right-0 top-full mt-2 menu bg-base-100 rounded-box shadow w-52 z-50">
                        <li><a>Perfil</a></li>
                        <li><a>Configuración</a></li>
                        <li><a>Cerrar sesión</a></li>
                    </ul>

                </div>

            </div>
            {children}
        </div>
    )
}
