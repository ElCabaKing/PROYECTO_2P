export interface Sucursal {
  id: string;
  restaurante_id: string;
  restaurante_name?: string; 
  name: string;
  address: string;
  phone?: string;
  email?: string;
  tolerance_minutes: number;
  is_active: boolean;
}

export interface CrearSucursalDTO {
  restaurante_id: string; 
  name: string;
  address: string;
  phone?: string;
  email?: string;
  tolerance_minutes?: number;
}