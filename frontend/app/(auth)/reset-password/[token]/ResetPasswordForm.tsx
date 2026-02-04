'use client'
import axios from "axios";
import { useState } from "react";
type Props = {
  token: string;
};



function ResetPasswordForm(Props: Props) {
  const { token } = Props;
  const [password, setPassword] = useState("")
  const [errorMessage, setErrorMessage] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")

  async function resetPassword() {
    try {
      const res = await axios.post("http://localhost:5003/auth/recovery",
        {
          new_password:password,
          confirm_password: confirmPassword,
          token
        })
      console.log(res.data)
      window.location.href = "/"
    }
    catch (e) {
      console.log(e)
    }
  }
  return (
    <div className="max-h-screen">
      <button onClick={() => window.location.href = "/"} className="btn"> Regresar al Login</button>
      <h1 className="text-xl font-bold">Restablecer contraseña</h1>
      <h2 className="text-sm ">Cambie su contraseña e intente de nuevo inisiar sesion</h2>
      <div className="flex  items-center justify-center">
        <form onSubmit={(e) => { e.preventDefault(); resetPassword() }}>
          <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
            <p className="text-red-500 text-sm min-h-5">
              {errorMessage}
            </p>

            <label className="label">Contrasena</label>
            <input type="password" className="input"
              placeholder="Contrasena"
              onChange={(e) => setPassword(e.target.value)}
              value={password}
              required />

            <label className="label">Confirmar Contrasena</label>
            <input type="password" className="input"
              placeholder="Confirmar Contrasena"
              onChange={(e) => setConfirmPassword(e.target.value)}
              value={confirmPassword}
              required />

            <button className="btn w-64 rounded-full">Button</button>
          </fieldset>
        </form>
      </div>
    </div>
  )
}

export default ResetPasswordForm