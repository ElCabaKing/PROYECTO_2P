'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { authService } from '@/services/auth.service'; 

export default function LoginPage() {
  const router = useRouter();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const response = await authService.login(username, password);
      
      if (response && response.token) {
        localStorage.setItem('token', response.token);
        if (response.rol) localStorage.setItem('rol', response.rol);
        
        router.push('/dashboard');
      } else {
        setError('El servidor no devolvió un token válido.');
      }
    } catch (err:unknown) {
      console.error(err);
      setError('Credenciales incorrectas o error de conexión.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-base-200">
      {/* TARJETA CENTRADA */}
      <div className="card w-full max-w-sm shadow-2xl bg-base-100">
        <form onSubmit={handleLogin} className="card-body">
          <h2 className="card-title justify-center text-2xl mb-4 font-bold text-primary">
            Iniciar Sesión
          </h2>

          {/* MENSAJE DE ERROR */}
          {error && (
            <div role="alert" className="alert alert-error text-sm py-2">
              <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
              <span>{error}</span>
            </div>
          )}

          {/* INPUT USUARIO */}
          <div className="form-control">
            <label className="label">
              <span className="label-text">Usuario</span>
            </label>
            <input 
              type="text" 
              placeholder="Ej: admin" 
              className="input input-bordered" 
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required 
            />
          </div>

          {/* INPUT CONTRASEÑA */}
          <div className="form-control">
            <label className="label">
              <span className="label-text">Contraseña</span>
            </label>
            <input 
              type="password" 
              placeholder="******" 
              className="input input-bordered" 
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required 
            />
            <label className="label">
              <a href="#" className="label-text-alt link link-hover">¿Olvidaste tu contraseña?</a>
            </label>
          </div>

          {/* BOTÓN INGRESAR */}
          <div className="form-control mt-6">
            <button 
              className="btn btn-primary"
              disabled={loading}
            >
              {loading ? <span className="loading loading-spinner"></span> : 'Ingresar'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}