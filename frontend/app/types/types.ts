export interface Menu {
  id: number
  nombre: string
  descripcion: string
  path: string
  icono: string
}

export interface User {
  id: number
  nombre: string
  apellido: string
  cedula: string
  correo: string
  activo: boolean
  role_id: number
  restaurant_id: number
  sucursal_id: number | null
  menus: Menu[]
}

export interface LayoutData {
  user: User | null
}
