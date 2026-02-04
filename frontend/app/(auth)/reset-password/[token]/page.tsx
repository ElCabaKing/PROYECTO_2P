import ResetPasswordForm from "./ResetPasswordForm";

type Props = {
  params: {
    token: string;
  };
};

export default async function page({ params }: Props) {
  const { token } = await params;

  return (
    <div >

      <ResetPasswordForm token={token} />

      {/* formulario de nueva contraseña aquí */}
    </div>
  );
}

