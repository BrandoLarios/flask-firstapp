from werkzeug import secure_filename
from flask import Flask, escape, request, render_template
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Retornamos el dataframe
    df = pd.read_csv('static/'+str(filename))
    return render_template('dataframe.html',titulos = df.columns.values, archivo = filename)

@app.route('/graphic', methods=['GET','POST'])
def graphic():
    filename = request.form.get('filename') 
    df = pd.read_csv('static/'+str(filename))
    dataframe = df[:10]
    column = request.form.get('column')
    graphic_type = request.form.get('graphic_type')
    title = request.form.get('title')
    if graphic_type == 'Linea':
        line_graphic(column, dataframe, title)
        return render_template('graphic.html', columna = column, grafica = graphic_type, titulo = title)
    elif graphic_type == 'Barras':
        bar_graphic(column, dataframe, title)
        return render_template('graphic.html', columna = column, grafica = graphic_type, titulo = title)
    elif graphic_type == 'Pastel':
        pie_graphic(column, dataframe, title)
        return render_template('graphic.html', columna = column, grafica = graphic_type, titulo = title)
    elif graphic_type == 'Puntos':
        point_graphic(column, dataframe, title)
        return render_template('graphic.html', columna = column, grafica = graphic_type, titulo = title)
    
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Pagina no encontrada</h1>"

def line_graphic(column, df, title): #Grafica de lineas
    s1 = df.loc[0:5, column]
    plt.plot(s1)
    plt.savefig('static/'+str(title)+'.png') 

def bar_graphic(column, df, title): #Grafica de barras
    plt.bar(df['Company'][0:5], df[column][0:5])
    plt.savefig('static/'+str(title)+'.png')

def pie_graphic(column, df, title): #Grafica de pastel
    plt.pie(df[column][0:10], labels=df['Company'][0:10], autopct='%0.1f%%')
    plt.savefig('static/'+str(title)+'.png')

def point_graphic(column, df, title): #Grafica de puntos
    s1 = df.loc[0:5, 'Revenue (in millions)']
    plt.plot(s1, '--b')
    plt.savefig('static/'+str(title)+'.png')

if __name__ == '__main__':
    app.run(debug=True)