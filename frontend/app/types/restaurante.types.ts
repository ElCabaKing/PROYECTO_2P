export interface Restaurante {
  id: string;
  name: string;
  legal_name?: string; 
  tax_id?: string;
  logo_url?: string;
  is_active: boolean;
  created_at?: string;
}

export interface CrearRestauranteDTO {
  name: string;
  legal_name?: string;
  tax_id?: string;
  logo_url?: string;
}