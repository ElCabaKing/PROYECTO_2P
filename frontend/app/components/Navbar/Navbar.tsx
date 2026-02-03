"use client"
import React, { useEffect, useState } from "react"
import axios from "axios"
import { LayoutData } from "../../types/types"
import { useRouter } from "next/navigation"
function Navbar() {
    const [navBarData, setNavBarData] = useState<LayoutData>({ user: null })
    const router = useRouter()
    const [openMenu, setOpenMenu] = useState(false)
    const menuRef = React.useRef<HTMLDivElement>(null)


    useEffect(() => {
        let mounted = true
        axios
            .get("http://localhost:5003/user/profile", { withCredentials: true })
            .then((res) => {
                if (mounted) setNavBarData(res.data)
            })
            .catch((err) => {
                console.log("Navbar fetch error:", err)
                if (mounted) {
                    setNavBarData({ user: null })
                    router.push("/ ")
                }
            })
        return () => {
            mounted = false
        }
    }, [])

    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
                setOpenMenu(false)
            }
        }

        document.addEventListener("mousedown", handleClickOutside)
        return () => {
            document.removeEventListener("mousedown", handleClickOutside)
        }
    }, [])



    const userName = navBarData.user ? `${navBarData.user.nombre} ${navBarData.user.apellido}` : null

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
                                {navBarData.user && navBarData.user.menus.map((menu) => (
                                    <li onClick={() => router.push(`${menu.path}`)} key={menu.id}><a>{menu.nombre}</a></li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="flex-1">
                    <a className="btn btn-ghost text-xl">Proyecto 2</a>
                    {userName && <span className="ml-4">Bienvenido  {userName}</span>}
                </div>
                <div className="flex-none relative" ref={menuRef}>
                    <button
                        className="btn btn-square btn-ghost"
                        onClick={() => setOpenMenu(o => !o)}
                    >
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                            viewBox="0 0 24 24"
                            className="inline-block h-5 w-5 stroke-current">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                d="M5 12h.01M12 12h.01M19 12h.01" />
                        </svg>
                    </button>
                    {openMenu && (
                        <ul className="absolute right-0 top-full mt-2 menu bg-base-100 rounded-box shadow w-52 z-50">
                            <li><a>Perfil</a></li>
                            <li><a>Configuración</a></li>
                            <li><a>Cerrar sesión</a></li>
                        </ul>
                    )}
                </div>

            </div>
        </div>
    )
}

export default Navbar