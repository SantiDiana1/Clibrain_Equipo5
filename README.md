# Amelia Earhart

Este es el repositorio oficial del trabajo del equipo 5 formado por [Cayetano](https://www.linkedin.com/in/tamayoia), Ricardo, [Laura](https://www.linkedin.com/in/lauracuttier/) y [Santiago](https://www.linkedin.com/in/santi-diana-03b9a9206/), enmarcado en la primera hackathon organizada por el equipo de [Clibrain](https://www.clibrain.com/). Se presenta el proyecto **Amelia Earhart**, un servicio integrado dentro de la aerolínea **Vueling¨** para dar soporte al usuario en el proceso de compra de vuelo.

## Caso de uso

Amelia Earhart es un chat potenciado por Inteligencia Artificial que permite al usuario diversas funcionalidades mientras conversa con él, entre las cuales se encuentran:
- Compra automática de vuelos.
- Alquiler automático de coches u otros servicios.
- Recomendaciones personalizadas sobre todos los aspectos que desee el usuario relacionado con viajes (hoteles, planes...)
- Comparativa de ciudades personalizada dependiendo de las exigencias del usuario.

Y todas las que se le ocurran al usuario. Lo que Amelia Earhart proporciona es un chat inteligente del cual extraer consejos para que tu viaje sea el mejor posible.

## Arquitectura

Para la arquitectura de este modelo, ha sido utilizado el modelo preentrenado *databricks/dolly-v2-3b* proveniente de *Hugging Face*. Este LLM está entrenado con una cantidad de datos suficiente como para hacer recomendaciones mucho más personalizadas de lo que un conjunto de filtros podrían llegar a realizar. Se ha preparado una demo utilizando la herramienta **Streamlit**, en la que se pueden probar algunas de las funcionalidades que el proyecto propone.

## Implementación en la web de Vueling. 

Se ha realizado un prototipado de la implementación web de la solución utilizando la herramienta **Figma**. 
