from flask import Flask, render_template, request, redirect, url_for, session
 
app = Flask(__name__)
 
app.secret_key = "minha_chave_secreta_super_dificil_de_adivinhar"
 
USUARIO_VALIDO = "admin"
SENHA_VALIDA = "1234"
 
 
@app.route("/")
def index():
    """Página inicial com mensagem de boas-vindas e link para login."""
    return render_template("index.html")
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    """Exibe o formulário de login e valida as credenciais."""
    erro = None
 
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "").strip()
 
        if usuario == USUARIO_VALIDO and senha == SENHA_VALIDA:
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválidos. Tente novamente."
 
    return render_template("login.html", erro=erro)
 
 
@app.route("/dashboard")
def dashboard():
    """Área restrita, só acessível se houver um usuário na sessão."""
    if "usuario" not in session:
        return redirect(url_for("login"))
 
    return render_template("dashboard.html", usuario=session["usuario"])
 
 
@app.route("/logout")
def logout():
    """Remove o usuário da sessão e volta para a página de login."""
    session.pop("usuario", None)
    return redirect(url_for("login"))
 
 
if __name__ == "__main__":
    app.run(debug=True)
 