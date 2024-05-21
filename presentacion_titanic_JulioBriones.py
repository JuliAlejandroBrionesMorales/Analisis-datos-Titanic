# --------------------LIBRERÍAS----------------------------#
# Importamos las librerias necesarias para poder llevar a cabo el proyecto
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import streamlit as st

# --------------------CONFIGURACIÓN DE LA PÁGINA----------------------------#
# layout="centered" or "wide".
st.set_page_config(page_title='Proyecto 1: Titanic', layout='wide', page_icon='⛴️')
logo = 'img/imagen_titanic_2.jpeg'



# --------------------COLUMNAS----------------------------#

col1, col2, col3 = st.columns(3)
with col1 :
    st.image(logo, use_column_width=True)
with col2 :
    st.write('') 
with col3 :
    st.write('By Julio Briones')
st.title('LA TRAVESIA DEL TITANIC')
    


# --------------------SIDEBAR----------------------------#
st.sidebar.image(logo, width=100)
st.sidebar.title('CURIOSIDADES')
# Imagen 1: Curiosidad 1
st.sidebar.image('img/imagen_titanic_3.jpg', caption='Presupuesto de Titanic')

# Texto relacionado con la curiosidad 1
st.sidebar.write('La película fue dirigida por James Cameron y fue más costosa más dinero que construir el barco original (200 millones $)')

# Imagen 2: Curiosidad 2
st.sidebar.image('img/imagen_titanic_4.jpg', caption='Ubicacion actual')

# Texto relacionado con la curiosidad 2
st.sidebar.write('Actualmente el Titanic se encuentra a 4000 metros de profundidad en el Oceáno Atlántico.')

# Imagen 3: Curiosidad 3
st.sidebar.image('img/imagen_titanic_5.jpg', caption='Botes Salvavidas')

# Texto relacionado con la curiosidad 3
st.sidebar.write('Originalmente iba a contar con 64 salvavidas, pero finalmente solo conto con 20 botes.')

# Imagen 4: Curiosidad 4
st.sidebar.image('img/imagen_titanic_6.jpg', caption='Número de muertes')

# Texto relacionado con la curiosidad 3
st.sidebar.write('Según los registros, 1496 personas murieron en el hundimiento del Titanic. De los 2,208 pasajeros a bordo, solo 712 pudieron escapar en los botes salvavidas (32.2%).')



# --------------------COSAS QUE VAMOS A USAR EN TODA LA APP----------------------------#
df = pd.read_csv(r'data/titanic.csv')
if "Unnamed: 0" in df:
    df = df.drop(columns=["Unnamed: 0"])  # Eliminamos la columna Unnamed: 0
else:
    pass
    
    
# --------------------TABS----------------------------#
tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
    [
        "INTRODUCCION",
        "BASE DE DATOS",
        "VALORES NULOS",
        "PUERTOS DE EMBARQUE",
        "PRECIO DE EMBARQUE",
        "EDADES DE PERSONAS A BORDO",
        "SOBREVIVIENTES",
        "CONCLUSION",
    ]
)


# --------------------TAB 0 ----------------------------#
with tab0:
    st.title('INTRODUCCIÓN')
    # Especificamos el tamaño de la imagen
    width = 500

    col1, col2 = st.columns(2)
    with col1:
        st.write('1)')
        st.image('img/imagen_titanic_8.jpg',width=width)
        st.write('Contruido en Irlanda del Norte')
    with col2:
        st.write('2)')
        st.image('img/imagen_titanic_9.jpg',width=width)
        st.write('Southampton - 10 de abril de 1912')

    col1, col2 = st.columns(2)
    with col1:
        st.write('3)')
        st.image('img/imagen_titanic_10.jpg',width=width)
        st.write('J.Bruce Ismay - White Star Line')
        
    with col2:
        st.write('4)')
        st.image('img/imagen_titanic_11.jpg',width=width)
        st.write('20 botes salvavidas')



# --------------------TAB 1 ----------------------------#
with tab1:
    st.write('REPRESENTACIÓN DE LA BASE DE DATOS')
    st.dataframe(df)
    col1, col2, col3, col4 = st.columns(4)
    with col1 :
        st.write('SibSp: número de hermanos/conyujes abordo del Titanic')
    with col2 :
        st.write('Parch: número de padres / hijos a bordo del Titanic.') 
    with col3 :
        st.write('Fare: tarifa pagada por el pasajero') 
    with col4:
        st.write('') 


# --------------------TAB 2 ----------------------------#
with tab2:
        st.title('REPRESENTACIÓN VALORES NULOS')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('NÚMERO VALORES NULOS')
            valores_nulos = df.isnull().sum().reset_index()
            valores_nulos.columns=['Columna','Nº valores nulos']
            valores_nulos_con_numeros = valores_nulos[valores_nulos['Nº valores nulos']>0]
            valores_nulos_con_numeros
        with col2:
            st.write('PORCENTAJE DE VALORES NULOS')
            porcentaje_nulos = (df.isnull().sum()/len(df)*100).reset_index()
            porcentaje_nulos.columns =['Columna','Porcentaje de valores nulos']
            porcentaje_nulos_filtrado = porcentaje_nulos[porcentaje_nulos['Porcentaje de valores nulos']>0]
            porcentaje_nulos_filtrado
        with col3: 
            st.write('')
            
        col1, col2 = st.columns(2)
        with col1:
            # MOSTRAMOS VALORES NULOS SIN REPARAR DE MANERA GRAFICA
            st.write('GRÁFICO DE VALORES NULOS- SIN REPARAR')
            fig, ax = plt.subplots(figsize=(7,5))
            sns.heatmap(df.isnull(), cbar=True, cmap='viridis')
            st.pyplot(fig) 
        with col2:
            # AHORA REPARAMOS VALORES NULOS
            # 1. REPARAMOS COLUMNA AGE (sustituimos por media)
            media_age = df['Age'].median()
            df.fillna({'Age':media_age}, inplace=True) 
            # 2. ELIMINAMOS COLUMNA CABIN (tiene muchos valores nulos / no reparamos)
            df.drop('Cabin', axis=1, inplace=True) 
            # 3. REPARAMOS COLUMNA EMBARKED (sustituimos por moda)
            moda_embarked = df['Embarked'].mode()[0]
            df.fillna({'Embarked':moda_embarked}, inplace=True) 
            st.write('GRÁFICO DE VALORES NULOS - REPARADOS')
            fig,ax = plt.subplots(figsize=(7,5))
            sns.heatmap(df.isnull(), cbar=True, cmap='viridis')
            st.pyplot(fig)


# --------------------TAB 3 ----------------------------#
with tab3:
    st.title("REPRESENTACION NUMÉRICA DE LOS PUERTOS DE EMBARQUE")
    # COLUMAS CON FOTOS DE LOS PUERTOS
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('S -> "Southampton"')
        st.image ('img/puerto_southampon_14.jpg')
    with col2:
        st.write('C -> "Cherbour"')
        st.image ('img/puerto_cherbourg_12.jpg')
    with col3:
        st.write('Q -> "Queenstown"')
        st.image ('img/puerto_Queenstow_Cobh_13.jpg')
    st.write('')
    
    # COLUMNAS CON NUMEROS Y PORCENTAJES DE EMBARQUES POR PUERTOS
    col1, col2, col3 = st.columns (3)
    with col1:
        st.write('Nº de embarques por puerto')
        ciudad_embarcadas = df['Embarked'].value_counts().reset_index()
        ciudad_embarcadas.columns = ['Ciudad', 'Cantidad de Pasajeros']
        ciudad_embarcadas ['Ciudad']= ciudad_embarcadas ['Ciudad'].map({'S': 'Southampton', 'C': 'Cherbour', 'Q' :'Queenstown' })# Asignamos etiquetas a los valores de Embarked
        ciudad_embarcadas
    with col2:
        st.write('% de embarques por puerto')
        porcentajes_embarcados_ciudad = df['Embarked'].value_counts()/len(df)*100
        porcentajes_embarcados_ciudad = porcentajes_embarcados_ciudad.reset_index()
        porcentajes_embarcados_ciudad.columns = ['Ciudad', 'Porcentaje']
        porcentajes_embarcados_ciudad ['Ciudad']= porcentajes_embarcados_ciudad ['Ciudad'].map({'S': 'Southampton', 'C': 'Cherbour', 'Q' :'Queenstown' })# Asignamos etiquetas a los valores de Embarked
        porcentajes_embarcados_ciudad
    with col3:
        st.write('')
    
    # PRESENTAMOS GRAFICAMENTE EL NÚMERO DE EMBARQUES
    col1, col2 = st.columns(2)
    with col1:
        # GRAFICO DE BARRARS CON PERSONAS EMBARCAS POR PUERTOS
        # Fijamos unos colores para los puertos 
        colors = ['#FF9999','#79B8FF', '#99FFCC']
        # Creamos el gráfico de barras con Plotly Express
        fig = px.bar(ciudad_embarcadas, x='Ciudad', y='Cantidad de Pasajeros', 
                    color='Ciudad', template='plotly', 
                    title='CANTIDAD DE PASAJEROS EMBARCADOS POR CIUDAD', color_discrete_sequence=colors, width=600, height=500)
        # Actualizamos el nombre del título de nuestros ejes
        fig.update_layout(xaxis_title='Ciudad de embarque', yaxis_title='Cantidad de pasajeros')
        # Mostramos el gráfico
        st.plotly_chart(fig)
    with col2:
        # GRAFICO PASTEL CON PORCENTAJES DE PERSONAS EMBARCADAS POR PUERTOS
        # Fijamos unos colores para los puertos 
        colors = ['#FF9999','#79B8FF', '#99FFCC']
        fig = px.pie(porcentajes_embarcados_ciudad, names='Ciudad', values='Porcentaje', 
                    title='PORCENTAJE DE PASAJERO EMBARCADOS POR CIUDAD', color_discrete_sequence=colors, width=600, height=500)
        # Mostramos nuestro gráfico
        st.plotly_chart(fig)


# --------------------TAB 4 ----------------------------#
with tab4:
    st.title('REPRESENTACION PRECIO DE EMBARQUE')
    col1, col2, col3 = st.columns(3) # mostramos los precios max, min, media, mediana
    with col1:
        st.write('Precio máximo')
        edad_máxima = df['Fare'].max()
        edad_máxima
        st.write('Mediana de precios')
        mediana_edades = df['Fare'].median().__round__(2)
        mediana_edades
        st.write('Precio mínimo')
        edad_mínima = df['Fare'].min()
        edad_mínima
        st.write('Precio medio')
        media_edad = df['Fare'].mean().__round__(2)
        media_edad
    with col2:
        fig=px.scatter(df, x='Fare', y='Embarked', color='Fare', template='plotly',
               width=900, height=700, size= 'Fare', size_max=50,
               title='PRECIO DEL BILLETE EN FUNCION DEL PUERTO DE EMBARQUE Y CLASE DEL BILLETE',
               facet_col='Pclass', facet_col_wrap=1) 
        st.plotly_chart(fig)
        
    with col3:
        st.write('')
    


# --------------------TAB 5 ----------------------------#
with tab5:
    st.title('REPRESENTACIÓN DE EDADES')
    col1, col2, col3 = st.columns(3) # calculamos la edad media, max, min y mediana
    with col1:
        st.write('EDAD MÁXIMA')
        edad_máxima = df['Age'].max()
        edad_máxima
        st.write('MEDIANA DE EDADES')
        mediana_edades = df['Age'].median().__round__(2)
        mediana_edades
        st.write('EDAD MÍNIMA')
        edad_mínima = df['Age'].min()
        edad_mínima
        st.write('EDAD MEDIA')
        media_edad = df['Age'].mean().__round__(2)
        media_edad
    with col2:
        # REALIZAMOS GRAFICO DE BIGOTES CON LAS EDADES 
        fig = px.box(df, y='Age', title='DIAGRAMA DE EDADES', width=800, height=800, template='plotly')
        st.plotly_chart(fig)   
    with col3:
        st.write('')



# --------------------TAB 6----------------------------#
with tab6:
    st.title('REPRESENTACION DE SOBREVIVIENTES')
    col1, col2,col3 = st.columns(3)
    with col1:
        # Calculamos el número de número de hombres y mujeres embarcados
        sexos_embarcados = df['Sex'].value_counts().reset_index()
        sexos_embarcados.columns = ['Sexo','Cantidad de pasajeros']
        
        # Fijamos un color para la gráfica
        colors = ['#ff7f0e', '#6dafe3']

        # GRAFICA DE BARRAS CON LA CANTIDAD DE MUJERES Y HOMBRES A BORDO
        fig = px.bar (sexos_embarcados, x='Sexo', y='Cantidad de pasajeros', 
                    color='Sexo', template='plotly',
                    title='NÚMERO DE MUJERES Y HOMBRES EMBARCADOS', color_discrete_sequence=colors,
                    width=700, height=500)
        # Actualizamos el nombres del título del nuestros ejes
        fig.update_layout(xaxis_title='Tipo de Sexo', yaxis_title='Cantidad de pasajeros')
        # Mostramos el gráfico
        st.plotly_chart(fig)
        personas = df['Sex'].value_counts().sum()
        personas
        
    with col2:
        # Calculamos el porcentaje hombres y mujeres embarcados
        porcentaje_sexos = df['Sex'].value_counts()/len(df)*100
        porcentaje_sexos = porcentaje_sexos.reset_index()
        porcentaje_sexos.columns = ['Sexos', 'Porcentaje']

        # Creamos el gráfico de pastel con Plotly Express
        fig = px.pie (porcentaje_sexos, names='Sexos', values='Porcentaje', title='Porcentaje de sexos embarcados',color_discrete_sequence=colors, 
                      width=700, height=500)
        # Mostramos el gráfico
        st.plotly_chart(fig)
    with col3: 
        st.write ('')
    
    col1, col2 = st.columns(2)
    with col1:
        # Calculamos los valores de sobrevivientes de nuestro dataframe
        porcentaje_sobrevivientes = df['Survived'].value_counts()/len(df)*100
        porcentaje_sobrevivientes = porcentaje_sobrevivientes.reset_index()
        porcentaje_sobrevivientes.columns = ['Sobrevivió', 'Porcentaje']
        # Asignamos etiquetas a los valores de Sobrevivió
        porcentaje_sobrevivientes ['Sobrevivió'] = porcentaje_sobrevivientes ['Sobrevivió'].map({0: 'No Sobrevivió', 1: 'Sobrevivió'})
        # Fijamos un color para la gráfica
        colors = ['#ff6666', '#66ff99']
            
        # GRAFICO PASTEL DE LOS PORCENTAJES DE LAS PERSONAS QUE SOBREVIVIERON
        fig = px.pie(porcentaje_sobrevivientes, names = 'Sobrevivió', values='Porcentaje', title= 'PORCENTAJE DE SOBREVIVIENTES',
                        color_discrete_sequence= colors, width=700, height=500)
        st.plotly_chart(fig)
    
    with col2:
        numero_sobrevivientes = df['Survived'].value_counts()
        numero_sobrevivientes
    
        
    # Ahora vamos a crear 3 graficos, con los sobrevivientes en función del sexo y la clase
    col1, col2, col3 = st.columns(3)
    with col1:
        # Calculamos el porcentaje de hombres que sobrevivieron
        porcentaje_hombres = df[df['Sex']=='male']['Survived'].value_counts(normalize=True)*100
        
        # Creamos un dataFrame con los porcentajes de sobrevivientes de las hombres
        df_hombres = pd.DataFrame({'Sobrevivió': porcentaje_hombres.index, 'Porcentaje':porcentaje_hombres.values})
        
        # Asignamos etiquetas a los valores de Sobrevivió
        df_hombres['Sobrevivió'] = df_hombres['Sobrevivió'].map({0: 'No Sobrevivió', 1: 'Sobrevivió'})
        
        # Fijamos un color para la gráfica
        colors = ['#ff6666', '#66ff99'] 
        
        # CREAMOS LA GRAFICA PASTEL DE LOS HOMBRES QUE SOBREVIVIERON
        fig_hombres = px.pie(df_hombres, names='Sobrevivió', values='Porcentaje', 
                     title='HOMBRES QUE SOBREVIVIERON',
                     color_discrete_sequence=colors, width=600, height=400)
        st.plotly_chart(fig_hombres)
        
        # Calculamos el número de sobrevivientes hombres
        sobrevivientes_hombres = df[df['Sex']=='male']['Survived'].sum()
        sobrevivientes_hombres
    with col2:
        # Calculamos el porcentaje de mujeres que sobrevivieron
        porcentaje_mujeres = df[df['Sex']=='female']['Survived'].value_counts(normalize=True)*100
        
        # Creamos un dataFrame con los porcentajes de sobrevivientes de las mujeres
        df_mujeres = pd.DataFrame({'Sobrevivió': porcentaje_mujeres.index, 'Porcentaje':porcentaje_mujeres.values})
        
        # Asignamos etiquetas a los valores de Sobrevivió
        df_mujeres ['Sobrevivió'] = df_mujeres['Sobrevivió'].map({0: 'No Sobrevivió', 1: 'Sobrevivió'})
        
        # Fijamos un color para la gráfica
        colors = ['#66ff99','#ff6666'] 
        
        # CREAMOS LA GRAFICA PASTEL DE LOS MUJERES SOBREVIVIENTES
        fig_mujeres = px.pie(df_mujeres, names='Sobrevivió', values='Porcentaje', 
                            title='MUJERES QUE SOBREVIVIERON',
                            color_discrete_sequence=colors, width=600, height=400)
        st.plotly_chart(fig_mujeres)
        
        # Calculamos el número de muejeres que sobrevivieron
        sobrevivientes_mujeres = df[df['Sex'] == 'female']['Survived'].sum()
        sobrevivientes_mujeres
    with col3: 
        # Calculamos el porcentaje de sobrevivientes por clase
        porcentaje_sobrevivientes = df.groupby('Pclass')['Survived'].mean() * 100
        # Creamos un diccionario para mapear los nombres de las clases
        clase_labels = {1: '1ºClase', 2: '2ºClase', 3: '3ºClase'}
        # Mapeamos los nombres de las clases
        labels = [clase_labels[clase] for clase in porcentaje_sobrevivientes.index]
        
        # Fijamos colores para la gráfica
        colors = colors = ['#66ff99','#ff6666','#6dafe3']
        
        # CREAMOS EL GRAFICO DE BARRAS DE LA PROBABILIDAD DE SOBREVIVIR EN FUNCIÓN DE LA CLASE
        fig = px.pie(names=labels, values=porcentaje_sobrevivientes.values, 
            title='PORCENTAJE DE SOBREVIVIENTES POR CLASE',
            color=porcentaje_sobrevivientes.index,
            color_discrete_sequence=colors, width=600, height=400)
        # Mostramos el gráfico
        st.plotly_chart(fig)  
        

    # CALCULAMOS LOS PORCENTAJES DE SUPERVIVENCIA POR EDAD Y SEXO
    sobrevivir_edad = df.groupby(['Age', 'Sex', 'Pclass', 'Survived'])['Pclass'].count().reset_index(name='count')
    sobrevivir_edad['Porcentaje'] = sobrevivir_edad.groupby(['Age', 'Sex', 'Pclass'])['count'].transform(lambda x: x / x.sum() * 100)


    # Fijamos un color para la gráfica
    colors = ['#ff7f0e', '#6dafe3']

    # Creamos un gráfico de dispersión (scatter plot)
    fig = px.scatter(sobrevivir_edad, 
                    x='Age', 
                    y='Porcentaje', 
                    color='Sex',
                    facet_col='Survived',
                    title='PORCENTAJE DE SUPERVIVENCIA POR EDAD Y SEXO',
                    labels={'Age': 'Edad', 'Porcentaje': 'Porcentaje de supervivencia'},
                    color_discrete_sequence=colors, width=1200,
                    height=750, size='Age', size_max=15,
                    hover_data={'Age': True, 'Sex': True, 'Survived': True, 'Pclass': True})

    # Mostrar el gráfico
    st.plotly_chart(fig)

        



# --------------------TAB 7 ----------------------------#
with tab7:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.title('CONCLUSIONES')
    with col3:
        st.write('')
    st.write('')
    st.write('1. Es importante determinar los valores nulos y ver si se pueden reparar o no.')
    st.write('')
    
    st.write('')
    st.write('2. Al analizar las edades de las personas pudimos observar una persona de 80 años, lo cual es algo sorprendente por la longetividad.')
    st.write('')
    
    st.write('')
    st.write('3. Resaltar la diferencia de probabilidad de sobrevivir en función del sexo y también de la clase.')
    st.write('')
    
