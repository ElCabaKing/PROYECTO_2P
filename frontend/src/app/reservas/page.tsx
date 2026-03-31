'use client';
import { useState, useEffect } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css'; 
import { format } from 'date-fns';
import { es } from 'date-fns/locale';
import { adminService } from '@/services/admin.service'; 
import { reservasService } from '@/services/reservas.service';
import { Sucursal } from '@/types/sucursal.types';
import { MapPin, Users, Clock } from 'lucide-react';

export default function ReservasPage() {
  const [step, setStep] = useState(1);
  const [sucursales, setSucursales] = useState<Sucursal[]>([]);
  const [loading, setLoading] = useState(false);
  const [selectedSucursal, setSelectedSucursal] = useState('');
  const [date, setDate] = useState<Date>(new Date());
  const [time, setTime] = useState('');
  const [people, setPeople] = useState(2);
  const [clientData, setClientData] = useState({ name: '', email: '', phone: '' });
  const availableHours = ['12:00', '13:00', '14:00', '19:00', '20:00', '21:00'];

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await adminService.getSucursales(); 
        setSucursales(Array.isArray(data) ? data : []);
      } catch (e) { console.error(e); }
    };
    loadData();
  }, []);

  const handleReserve = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await reservasService.createReserva({
        sucursal_id: selectedSucursal,
        customer_name: clientData.name,
        customer_email: clientData.email,
        customer_phone: clientData.phone,
        reservation_date: format(date, 'yyyy-MM-dd'),
        reservation_time: time,
        number_of_people: people
      });
      alert('¡Reserva Confirmada con Éxito!');
      setStep(1); 
      setClientData({ name: '', email: '', phone: '' });
      setTime('');
    } catch (error) {
      console.error(error);
      alert('Hubo un problema al procesar tu reserva. Intenta nuevamente.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-base-200 p-4 md:p-10">
      <div className="max-w-4xl mx-auto bg-base-100 shadow-xl rounded-2xl overflow-hidden">
        
        {/* HEADER */}
        <div className="bg-primary p-6 text-primary-content text-center">
          <h1 className="text-3xl font-bold">Reserva tu Mesa</h1>
          <p className="opacity-80">Pasos para disfrutar de la mejor experiencia</p>
          
          <ul className="steps steps-horizontal mt-6 w-full text-primary-content">
            <li className={`step ${step >= 1 ? 'step-secondary' : ''}`}>Ubicación</li>
            <li className={`step ${step >= 2 ? 'step-secondary' : ''}`}>Fecha y Hora</li>
            <li className={`step ${step >= 3 ? 'step-secondary' : ''}`}>Confirmar</li>
          </ul>
        </div>

        <div className="p-8">
          {/* PASO 1 */}
          {step === 1 && (
            <div className="flex flex-col gap-6 animate-fade-in">
              <h2 className="text-2xl font-bold flex items-center gap-2">
                <MapPin /> ¿Dónde y Cuántos?
              </h2>
              <div className="form-control">
                <label className="label">Selecciona el Restaurante / Sucursal</label>
                <select 
                  className="select select-bordered w-full"
                  value={selectedSucursal}
                  onChange={(e) => setSelectedSucursal(e.target.value)}
                >
                  <option value="" disabled>-- Elige una opción --</option>
                  {sucursales.map(s => (
                    <option key={s.id} value={s.id}>{s.name} - {s.address}</option>
                  ))}
                </select>
              </div>
              <div className="form-control">
                <label className="label">Número de Personas</label>
                <div className="flex items-center gap-4">
                  <input 
                    type="range" min="1" max="10" value={people} 
                    className="range range-primary" 
                    onChange={(e) => setPeople(parseInt(e.target.value))}
                  />
                  <span className="font-bold text-xl w-10 text-center">{people}</span>
                  <Users />
                </div>
              </div>
              <button 
                className="btn btn-primary mt-4"
                disabled={!selectedSucursal}
                onClick={() => setStep(2)}
              >
                Siguiente
              </button>
            </div>
          )}

          {/* PASO 2 */}
          {step === 2 && (
            <div className="flex flex-col md:flex-row gap-8 animate-fade-in">
              <div className="flex-1">
                <h2 className="text-xl font-bold mb-4 flex gap-2"><Clock/> Elige la Fecha</h2>
                <div className="border rounded-lg p-4 flex justify-center bg-base-100">
                  <Calendar 
                    onChange={(val) => setDate(val as Date)} 
                    value={date}
                    locale="es-ES"
                    minDate={new Date()}
                  />
                </div>
              </div>
              <div className="flex-1">
                <h2 className="text-xl font-bold mb-4">Horas Disponibles para el {format(date, 'dd/MM')}</h2>
                <div className="grid grid-cols-3 gap-3">
                  {availableHours.map(h => (
                    <button 
                      key={h}
                      className={`btn ${time === h ? 'btn-primary' : 'btn-outline'}`}
                      onClick={() => setTime(h)}
                    >
                      {h}
                    </button>
                  ))}
                </div>
                <div className="flex gap-2 mt-8">
                  <button className="btn btn-ghost" onClick={() => setStep(1)}>Atrás</button>
                  <button 
                    className="btn btn-primary flex-1"
                    disabled={!time}
                    onClick={() => setStep(3)}
                  >
                    Siguiente
                  </button>
                </div>
              </div>
            </div>
          )}

          {/* PASO 3 */}
          {step === 3 && (
            <div className="animate-fade-in max-w-lg mx-auto">
              <h2 className="text-2xl font-bold mb-6 text-center">¡Ya casi está!</h2>
              <div className="bg-base-200 p-4 rounded-lg mb-6 text-sm">
                <p><strong>Lugar:</strong> {sucursales.find(s=>s.id===selectedSucursal)?.name}</p>
                <p><strong>Fecha:</strong> {format(date, 'dd MMMM yyyy', { locale: es })} a las {time}</p>
                <p><strong>Mesa para:</strong> {people} personas</p>
              </div>
              <form onSubmit={handleReserve} className="flex flex-col gap-4">
                <input 
                  type="text" placeholder="Tu Nombre Completo" className="input input-bordered" required
                  value={clientData.name} onChange={e => setClientData({...clientData, name: e.target.value})}
                />
                <input 
                  type="email" placeholder="Correo Electrónico" className="input input-bordered" required
                  value={clientData.email} onChange={e => setClientData({...clientData, email: e.target.value})}
                />
                <input 
                  type="tel" placeholder="Teléfono / Celular" className="input input-bordered" required
                  value={clientData.phone} onChange={e => setClientData({...clientData, phone: e.target.value})}
                />
                <div className="flex gap-2 mt-4">
                  <button type="button" className="btn btn-ghost" onClick={() => setStep(2)}>Atrás</button>
                  <button type="submit" className="btn btn-primary flex-1" disabled={loading}>
                    {loading ? <span className="loading loading-spinner"></span> : 'Confirmar Reserva'}
                  </button>
                </div>
              </form>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}