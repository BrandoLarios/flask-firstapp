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
        plt.plot(df.loc[490:510, 'Year'])
        plt.title('Year')
        print('Barras 1')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Rank':
        plt.plot(df.loc[0:800, 'Rank'])
        print('Barras 2')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Company':
        #Definir la creacion de la grafica de lineas para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Revenue (in millions)':
        plt.plot(df.loc[490:550, 'Revenue (in millions)'])
        print('Barras 3')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Profit (in millions)':
        plt.plot(df.loc[490:510, 'Profit (in millions)'])
        print('Barras 4')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
        
def bar_graphic(column, df, title): #Grafica de barras
    if column == 'Year':
        ingresos = pd.DataFrame((df['Revenue (in millions)']).groupby(df['Company']).mean())
        lista_ingresos =ingresos.index
        lista_ingresos=lista_ingresos[0:5]
        ingresos=ingresos[0:5]
        plt.bar(lista_ingresos,ingresos['Revenue (in millions)'].values) 
        plt.title('Promedio de ingresos por compañia de 1955 a 2005')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Rank':
        frecuencia =  pd.DataFrame((df['Company']).groupby(df['Company']).count())
        lista = frecuencia.index
        lista = lista[0:5]
        frecuencia = frecuencia[0:5]
        plt.bar(lista,frecuencia['Company'].values) 
        plt.title('Aparicion en  el ranking por compañia') 
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Company':
        #Definir la creacion de la grafica de barras para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Revenue (in millions)':
        plt.bar(df.loc[0:5,'Company'],df.loc[0:5, column]) 
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Profit (in millions)':
        plt.bar(df.loc[0:5,'Company'],df.loc[0:5, column])   
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

def pie_graphic(column, df, title): #Grafica de pastel
    if column == 'Year':
        plt.pie(df['Year'][0:13], labels=df['Company'][0:13], autopct='%0.1f%%')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Rank':
        plt.pie(df['Rank'][0:9], labels=df['Company'][0:9], autopct='%0.1f%%')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Company':
        #Definir la creacion de la grafica de pastel para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Revenue (in millions)':
        plt.pie(df['Revenue (in millions)'][0:9], labels=df['Company'][0:9], autopct='%0.1f%%')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Profit (in millions)':
        plt.pie(df['Profit (in millions)'][0:5], labels=df['Company'][0:5], autopct='%0.1f%%')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
        
def point_graphic(column, df, title): #Grafica de puntos
    if column == 'Year':
        plt.plot(df.loc[490:510, 'Year'], '--b')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Rank':
        plt.plot(df.loc[0:800, 'Rank'], '--b')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Company':
        #Definir la creacion de la grafica de lineas para la columna Company
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Revenue (in millions)':
        plt.plot(df.loc[490:550, 'Revenue (in millions)'], '--b')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado

    elif column == 'Profit (in millions)':
        plt.plot(df.loc[490:510, 'Profit (in millions)'], '--b')
        plt.savefig('static/'+str(title)+'.png') #Guarda la grafica con el nombre dado
        
if __name__ == '__main__':
    app.run(debug=True)