export interface Reserva {
  id?: string;
  sucursal_id: string;
  table_id?: string; 
  customer_name: string;
  customer_email: string;
  customer_phone: string;
  reservation_date: string; 
  reservation_time: string; 
  number_of_people: number;
  status?: 'PENDING' | 'CONFIRMED' | 'CANCELLED';
}

export interface Disponibilidad {
  time: string; // "19:00"
  available_tables: number;
}