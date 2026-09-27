# Boreal Demo: catálogo de relojes para Meta

Tres productos ficticios para probar la importación de un archivo de datos en Commerce Manager y la conexión de un catálogo a una WABA propia.

## Archivos

- `catalogo-boreal-demo.csv`: feed para Meta con ID, título, descripción, disponibilidad, estado, precio, página, imagen, marca y categoría.
- `assets/*.png`: fotos originales de demostración (1254 × 1254 px, menos de 8 MB cada una).
- `index.html`, `products/*.html`, `style.css`: páginas públicas que respaldan los enlaces del CSV.
- `build_catalog.py`: vuelve a generar el CSV y las páginas si cambia el dominio público.

El CSV usa `https://gaonuk.github.io/boreal-demo-catalog` como dirección pública. Antes de subirlo a Meta, comprueba que los tres enlaces de productos y los tres de imágenes devuelvan HTTP 200. Si se usa otro host, ejecuta `BOREAL_CATALOG_BASE_URL=https://tu-dominio python3 build_catalog.py`.

## Carga en Meta

En la pantalla de Commerce Manager de la captura: `Archivo de datos` → `Siguiente` → `Subir desde la computadora` → seleccionar `catalogo-boreal-demo.csv`. Después revisa el informe de diagnósticos y el estado de aprobación de cada artículo. Conecta el catálogo a tu WABA en WhatsApp Manager → Herramientas de la cuenta → Catálogo.

Los productos, precios y marca son inventados; el sitio indica que no se aceptan compras. Este feed sirve para una prueba privada de integración, no para publicar una tienda o lanzar anuncios. `in stock` está elegido para probar la visibilidad de productos en WhatsApp; Meta puede rechazar artículos conceptuales durante su revisión. Si la prueba exige productos aprobados para venta real, reemplaza estos artículos por productos reales y páginas de compra válidas.
