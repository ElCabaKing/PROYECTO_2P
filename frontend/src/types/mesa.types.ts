export interface Mesa {
  id: string;
  sucursal_id: string;
  sucursal_name?: string; 
  table_number: string;
  capacity_min: number;
  capacity_max: number;
  location?: string; 
  is_active: boolean;
}

export interface CrearMesaDTO {
  sucursal_id: string;
  table_number?: string; 
  capacity_min: number;
  capacity_max: number;
  location?: string;
  description?: string;
}