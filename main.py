
from  flask import Flask,render_template,request,redirect
import psycopg2

app = Flask(__name__)
app.secret_key='mysecretkey'

 
#main menu
@app.route('/')
def menu():
    return render_template('index.html')



@app.route('/add',methods=['POST'])
def agregado():
        nombre=request.form['names']
        fecha=request.form['dates']
        codgioPK=request.form['PK']
        
        #conexcion BDposter
        conn = psycopg2.connect(
            dbname="bncl0pg5ieghb03wu7gg",
            host="bncl0pg5ieghb03wu7gg-postgresql.services.clever-cloud.com",
            user="utag7moljob9r3vj2ajm",
            password="onJJ4M30LMVqlhU4Yg4T",
            port="5432"
        )
        
        #Navegador
        cursor = conn.cursor()
        
        #AGREGAR DATO
        #query
    
        query = '    INSERT INTO "Tabla3"(pk,nombre,fecha,comprobante) VALUES(%s,%s,%s,%s)   '
        cursor.execute(query,(codgioPK,nombre,fecha,True))
    
        conn.commit()
        conn.close()
        return redirect('/Tabla')

@app.route('/Tabla')
def Tabla():
        try:
            #conexcion BDposter
            conn = psycopg2.connect(
                dbname="bncl0pg5ieghb03wu7gg",
                host="bncl0pg5ieghb03wu7gg-postgresql.services.clever-cloud.com",
                user="utag7moljob9r3vj2ajm",
                password="onJJ4M30LMVqlhU4Yg4T",
                port="5432"
            )
        except:
            pass
        #Navegador
        cursor = conn.cursor()
        query = ' SELECT * FROM "Tabla3"'
        cursor.execute(query)
        #Recoger dato
        datos = cursor.fetchall()
        conn.commit()
        conn.close()

        return render_template("Tabla.html",datos=datos)


@app.route('/delete/<string:id>')
def delete(id):

    #conexcion BDposter
    conn = psycopg2.connect(
    dbname="bncl0pg5ieghb03wu7gg",
    host="bncl0pg5ieghb03wu7gg-postgresql.services.clever-cloud.com",
    user="utag7moljob9r3vj2ajm",
    password="onJJ4M30LMVqlhU4Yg4T",
    port="5432"
    )

    #Navegador
    cursor = conn.cursor()
    
    #AGREGAR DATO
    #query
    try:
        query = f'    DELETE FROM "Tabla3" WHERE id = {int(id)}'
        cursor.execute(query)
    except:
        pass
    conn.commit()
    conn.close()
    return redirect('/Tabla')

@app.route('/edit/<string:id>')
def menu_edit(id):

    try:
        #conexcion BDposter
        conn = psycopg2.connect(
            dbname="bncl0pg5ieghb03wu7gg",
            host="bncl0pg5ieghb03wu7gg-postgresql.services.clever-cloud.com",
            user="utag7moljob9r3vj2ajm",
            password="onJJ4M30LMVqlhU4Yg4T",
            port="5432"
        )
    except:
        pass

    cursor = conn.cursor()
    query = f' SELECT * FROM "Tabla3" WHERE id = {int(id)}'
    cursor.execute(query)
    #Recoger dato
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return render_template("modificar.html",datos=datos,id=id)


@app.route('/edit_/<id>',methods=['POST'])
def update(id):
    
    nombre=request.form['names']
    fecha=request.form['dates']
    codgioPK=request.form['PK']
    try:
        #conexcion BDposter
        conn = psycopg2.connect(
            dbname="bncl0pg5ieghb03wu7gg",
            host="bncl0pg5ieghb03wu7gg-postgresql.services.clever-cloud.com",
            user="utag7moljob9r3vj2ajm",
            password="onJJ4M30LMVqlhU4Yg4T",
            port="5432"
        )
    except:
        pass

    cursor = conn.cursor()
    query ='    UPDATE "Tabla3" SET pk=%s,nombre=%s,fecha=%s WHERE id = %s  '
    cursor.execute(query,(int(codgioPK),nombre,fecha,int(id)))
    #Recoger dato
    conn.commit()
    conn.close()
    return redirect('/Tabla')


#inicializador
if __name__ == "__main__":
    app.run(debug=True)
