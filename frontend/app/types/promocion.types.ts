export interface Promocion {
  id: string;
  sucursal_id: string;
  sucursal_name?: string;
  name: string;
  description?: string;
  discount_percentage: number; 
  start_date: string; 
  end_date: string;
  is_active: boolean;
}

export interface CrearPromocionDTO {
  sucursal_id: string;
  name: string;
  description?: string;
  discount_percentage: number;
  start_date: string;
  end_date: string;
}