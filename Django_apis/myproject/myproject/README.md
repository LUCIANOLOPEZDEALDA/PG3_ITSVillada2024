# Breweries List Project

Este proyecto es una aplicación web desarrollada con Django que permite buscar cervecerías utilizando la API de [Open Brewery DB](https://www.openbrewerydb.org/). Los usuarios pueden buscar cervecerías por nombre y cantidad, y seleccionar qué información se muestra en la tabla de resultados (ciudad, tipo o estado).

## API Utilizada

### Open Brewery DB

- **URL Base**: `https://api.openbrewerydb.org`
- **Endpoint utilizado**: `/breweries`
- **Documentación**: [Open Brewery DB API](https://www.openbrewerydb.org/documentation)

La API de Open Brewery DB proporciona datos sobre cervecerías en Estados Unidos. Para este proyecto, se utiliza el endpoint `/breweries` para obtener una lista de cervecerías. Se implementa la capacidad de búsqueda por nombre y cantidad, y se permite a los usuarios elegir qué columnas de información (ciudad, tipo o estado) mostrar en la tabla de resultados.

### Cómo se trabajó con la API

1. **Solicitud de Datos**: Se utilizan solicitudes HTTP GET para obtener datos de la API. La biblioteca `requests` de Python se usa para realizar estas solicitudes.
2. **Filtrado y Parámetros**: Los usuarios pueden ingresar un término de búsqueda y la cantidad de resultados deseados a través de un formulario. Estos parámetros se pasan a la API para filtrar los resultados.
3. **Renderización**: Los datos obtenidos de la API se pasan al contexto de la plantilla y se renderizan en una tabla HTML. Los usuarios pueden seleccionar qué columnas mostrar utilizando checkboxes.