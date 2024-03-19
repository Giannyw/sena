from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# Crear instancia
app = Flask(__name__)
app.secret_key='12345678'
# Configurar la conexión
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda2024"
)

cursor = db.cursor()

@app.route('/password/<passwordencrip>')
def encriptarpassword (passwordencrip):
    #generar un hash de la contraseña
    # encriptar= bcrypt.hashpw(Passwordencrip.encode('utf-8'), bcrypt.gestsalt())
    encriptar = generate_password_hash(passwordencrip)
    valor= check_password_hash(encriptar, passwordencrip)
   # return "Encriptado: {0} | coincide:{1}".format(encriptar, valor)
    return valor


@app.route('/lista')  # Crear ruta
def lista():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM personas")
    usuario = cursor.fetchall()
       
    return render_template('index.html', usuario=usuario)

@app.route('/Registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
       Nombres = request.form.get('nombre')
       Apellidos = request.form.get('apellido')
       email = request.form.get('email')
       Direccion = request.form.get('direccion')
       Telefono = request.form.get('telefono')
       Usuario = request.form.get('usuario')
       Password = request.form.get('password')
       Roles = request.form.get('txtrol')
       
       Passwordencrip= generate_password_hash(Password)
    
        # Insertar datos a la tabla de mysql
       cursor.execute("INSERT INTO personas(nombrep, apellidop, emailp, dirp, telp, usup, passp, roles) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Nombres, Apellidos, email, Direccion, Telefono, Usuario, Passwordencrip,Roles))
       db.commit()

       print ("Usuario no registrado")     
       return redirect(url_for('login'))  # Redirigir a la página principal
   
    return render_template("Registrar.html")




@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_canciones():
    if request.method == 'POST':
       Codigo = request.form.get('id_canciones')
       Titulo = request.form.get('titulo')
       Artista = request.form.get('artista')
       Genero = request.form.get('genero')
       Precio = request.form.get('precio')
       Duración = request.form.get('duracion')
       Lanzamiento = request.form.get('lanzamiento')
    
        # Insertar datos a la tabla de mysql
       sql= "UPDATE canciones set titulo=%s,codigo=%s,artista=%s,genenero=%s,precio=%s,duracion=%s,lanzamiento=%s"
       cursor.execute(sql,(Titulo,Codigo,Artista,Genero,Precio,Duración,Lanzamiento))
       db.commit()

    else: 
        cursor = db.cursor()
        cursor.execute("SELECT * FROM canciones WHERE polper=%s" ,(id,))
        data = cursor.fetchall()

    return render_template('actcanciones.html', personas=data[0])


@app.route('/Canciones')  # Crear ruta
def mostrar_canciones():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM canciones")
    usuario = cursor.fetchall()
       
    return render_template('index.html', usuario=usuario)

@app.route('/canciones', methods=['GET', 'POST'])
def registro_canciones():
    if request.method == 'POST':
       Titulo = request.form.get('titulo')
       Artista = request.form.get('artista')
       Genero = request.form.get('genero')
       Precio = request.form.get('precio')
       Duración = request.form.get('duracion')
       Lanzamiento = request.form.get('lanzamiento')
       Imagen= request.form.get('img')
       

        # Insertar datos a la tabla de mysql
       cursor.execute("INSERT INTO canciones(id_canciones,titulo,artista,genero,precio,duracion,lanzamiento,img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (Titulo,Artista,Genero,Precio,Duración,Lanzamiento,Imagen))
       db.commit()

            
       return redirect(url_for('login'))  # Redirigir a la página principal
    return render_template("Registro.html")




@app.route('/Ingresar', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #VERIFICAR LAS CREDENCIALES DEL USUARIO
        username = request.form.get('username')
        password = request.form.get('password')
        
        cursor = db.cursor(dictionary=True)
        sql="SELECT usup, passp, roles from personas WHERE usup= %s"
        cursor.execute(sql,(username,))
        resultado = cursor.fetchone()
        
        if resultado and check_password_hash(resultado['passp'], password): 
                session['usuario'] = resultado['usup']
                session['rol']= resultado['roles']
                
                #de acuerdo al rol asignamnos las url 
                if resultado['roles'] == 'administrador':
                    return redirect(url_for('lista'))
                else:  
            
                    return redirect(url_for('mostrar_canciones'))
        
        else:
            print ('Credenciales invalidas. Por favor intente de nuevo')
            return render_template('Ingresar.html')
    else:
        print('Usuario no encontrado') 
        return render_template('Ingresar.html')

    return render_template('Ingresar.html')

@app.route('/logout')
def logout():
    #eliminar el usuario de la sesion
    session.pop('usuario',None)
    print("Sesion Finalizada")
    return redirect(url_for('login'))

        
@app.route('/Editar/<int:id>',methods=['GET', 'POST'])
def editar_usuario(id):
    cursor = db.cursor()
    if request.method == 'POST':
        nombreper = request.form.get('nombreper')
        apellidoper = request.form.get('apellidoper')
        emailper = request.form.get('emailper')
        dirper = request.form.get('dirper')
        telper = request.form.get('telper')
        usuper = request.form.get('usuper')
        passper = request.form.get('passper')

        sql = "UPDATE personas SET nombrep=%s, apellidop=%s, emailp=%s, dirp=%s, telp=%s, usup=%s, passp=%s WHERE polper=%s"
        cursor.execute(sql,(nombreper,apellidoper,emailper, dirper,telper,usuper,passper,id,))
        db.commit()
        return redirect(url_for('lista'))
    
    else: 
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personas WHERE polper=%s" ,(id,))
        data = cursor.fetchall()

        return render_template('Editar.html', personas=data[0])

@app.route("/eliminar/<int:id>", methods=['GET'])
def eliminar_usuario(id):
    cursor = db.cursor()
    if request.method == 'POST':
        nombreper = request.form.get('nombreper')
        apellidoper = request.form.get('apellidoper')
        emailper = request.form.get('emailper')
        dirper = request.form.get('dirper')
        telper = request.form.get('telper')
        usuper = request.form.get('usuper')
        passper = request.form.get('passper')
    
    cursor.execute('DELETE FROM personas WHERE polper=%s', (id,))
    db.commit()
    return redirect(url_for('lista'))
# Ejecutar app
if __name__ == '__main__':
    app.add_url_rule('/',view_func=lista)
    app.run(debug=True, port=5005) 
    # Debug para que salgan los errores en consola