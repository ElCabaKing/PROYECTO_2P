export interface Horario {
  id: string;
  sucursal_id: string;
  sucursal_name?: string;
  day_of_week: number; // 0=Domingo, 1=Lunes, ... 6=Sábado
  day_name?: string;   // El backend nos enviará "Lunes", "Martes", etc.
  opening_time: string; // Formato "HH:MM:SS"
  closing_time: string;
  is_active: boolean;
}

export interface CrearHorarioDTO {
  sucursal_id: string;
  day_of_week: number;
  opening_time: string;
  closing_time: string;
}

// Helper para usar en el formulario
export const DIAS_SEMANA = [
  { id: 1, nombre: 'Lunes' },
  { id: 2, nombre: 'Martes' },
  { id: 3, nombre: 'Miércoles' },
  { id: 4, nombre: 'Jueves' },
  { id: 5, nombre: 'Viernes' },
  { id: 6, nombre: 'Sábado' },
  { id: 0, nombre: 'Domingo' },
];