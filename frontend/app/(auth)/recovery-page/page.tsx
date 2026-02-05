"use client"
import useRecovery from "./hook"


export default function RecoveryPage() {
  const { correo, setCorreo, errorMessage, recovery, alert,showAlert } = useRecovery()
  return (
    <div>
      
      {showAlert && (<div role="alert" className="alert alert-success max-w-2xs absolute">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 shrink-0 stroke-current" fill="none" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>{alert}</span>
      </div>)}
      <button onClick={() => window.location.href = "/"} className="btn"> Regresar al Login</button>
      <div className="flex min-h-screen items-center justify-center">
        <form onSubmit={(e) => { e.preventDefault(); recovery() }}>
          <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
            <p className="text-red-500 text-sm min-h-5">
              {errorMessage}
            </p>

            <label className="label">Correo Electronico</label>
            <input type="text" className="input"
              placeholder="Correo"
              onChange={(e) => setCorreo(e.target.value)}
              value={correo}
              required />

            <button className="btn w-64 rounded-full">Button</button>
          </fieldset>
        </form>
      </div>
    </div>
  )
}