import pyotp
import qrcode

def setup_2fa():
    """
    Configura autenticação de dois fatores e gera um código QR.
    """
    # Gera uma chave secreta
    secret = pyotp.random_base32()
    
    # Cria um URI para o código QR
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name="exemplo@empresa.com", issuer_name="MinhaEmpresa")
    
    # Gera o código QR
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(uri)
    qr.make(fit=True)
    
    # Cria uma imagem do código QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("2fa_qr.png")
    
    print("Chave secreta 2FA:", secret)
    print("Código QR salvo como '2fa_qr.png'")
    print("Escaneie o código QR com um aplicativo autenticador para configurar 2FA.")

if __name__ == "__main__":
    setup_2fa()