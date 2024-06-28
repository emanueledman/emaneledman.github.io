from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Defina sua chave secreta para uso do flash

# Configurações de email para Flask-Mail (exemplo para Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'seu_email@gmail.com'  # Substitua com seu email
app.config['MAIL_PASSWORD'] = 'sua_senha'  # Substitua com sua senha
app.config['MAIL_DEFAULT_SENDER'] = 'seu_email@gmail.com'  # Substitua com seu email

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Enviar email para o endereço especificado
        try:
            send_email(email)
            flash('Presença marcada com sucesso! Um email foi enviado para confirmação.')
        except Exception as e:
            flash('Ocorreu um erro ao enviar o email. Por favor, tente novamente.')

        return redirect(url_for('index'))

    return render_template('attendance.html')

def send_email(email):
    msg = Message(subject='Confirmação de Presença',
                  recipients=['emanuelhedima@gmail.com'])  # Substitua com o seu endereço de email

    msg.body = f'Email do participante: {email}'

    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)
