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
        f = request.files['archivo']
        filename = secure_filename(f.filename)

        if filename != "":
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            df = pd.read_csv('static/'+str(filename))
            df = df.head(20)
            return render_template('dataframe.html', tables=[df.to_html(classes='data')], titulos = df.columns.values, archivo = filename)
        else:
            return render_template('index.html')

@app.route('/graphic', methods=['GET','POST'])
def graphic():

    filename = request.form.get('filename') 
    column = request.form.get('column')
    graphic_type = request.form.get('graphic_type')
    title = request.form.get('title')

    df = pd.read_csv('static/'+str(filename))
    dataframe = df.head(100)

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
    if column == 'Year':
        #Definir la creacion de la grafica de lineas para la columna Year
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Rank':
        #Definir la creacion de la grafica de lineas para la columna Rank
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Company':
        #Definir la creacion de la grafica de lineas para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Revenue (in millions)':
        #Definir la creacion de la grafica de lineas para la columna Revenue (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Profit (in millions)':
        #Definir la creacion de la grafica de lineas para la columna Profit (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

def bar_graphic(column, df, title): #Grafica de barras
    if column == 'Year':
            #Definir la creacion de la grafica de barras para la columna Year
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Rank':
        #Definir la creacion de la grafica de barras para la columna Rank
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Company':
        #Definir la creacion de la grafica de barras para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Revenue (in millions)':
        #Definir la creacion de la grafica de barras para la columna Revenue (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Profit (in millions)':
        #Definir la creacion de la grafica de barras para la columna Profit (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

def pie_graphic(column, df, title): #Grafica de pastel
    if column == 'Year':
            #Definir la creacion de la grafica de pastel para la columna Year
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Rank':
        #Definir la creacion de la grafica de pastel para la columna Rank
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Company':
        #Definir la creacion de la grafica de pastel para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Revenue (in millions)':
        #Definir la creacion de la grafica de pastel para la columna Revenue (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Profit (in millions)':
        #Definir la creacion de la grafica de pastel para la columna Profit (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

def point_graphic(column, df, title): #Grafica de puntos
    if column == 'Year':
            #Definir la creacion de la grafica de puntos para la columna Year
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Rank':
        #Definir la creacion de la grafica de puntos para la columna Rank
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Company':
        #Definir la creacion de la grafica de puntos para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Revenue (in millions)':
        #Definir la creacion de la grafica de puntos para la columna Revenue (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
    elif column == 'Profit (in millions)':
        #Definir la creacion de la grafica de puntos para la columna Profit (in millions)
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

if __name__ == '__main__':
    app.run(debug=True)