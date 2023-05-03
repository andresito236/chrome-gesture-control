
# Control de Google Chrome a través de gestos
A continuación se enlistan los gestos habilitados para controlar el navegador, junto con la acción que cada uno ejecuta.
| Gesto | Nombre dado | Comando que realiza |
| --- | :---: | :---: |
| ![Image_1683041133 146112](https://user-images.githubusercontent.com/93633761/236046393-eb56b18c-c169-43b0-b105-e3e4e32bc71a.jpg) | tijera | Presiona Alt, accediendo a la barra superior |
| ![Image_1683041724 304473](https://user-images.githubusercontent.com/93633761/236042752-9548decc-b172-417f-a02a-d54495e0f6dc.jpg) | rock-sin-pulgar | Selecciona un elemento mediante Tab |
| ![Image_1683038413 7871797](https://user-images.githubusercontent.com/93633761/236042951-1e95c7ef-b46a-4d52-aeef-56b79bb3693e.jpg) | rock | Selecciona el elemento anterior mediante Shift + Tab |
| ![Image_1683038043 0113523](https://user-images.githubusercontent.com/93633761/236043168-ca0aee57-bc94-4134-924e-9e4d1eacf67d.jpg) | indice-arriba | Presiona flecha arriba |
| ![Image_1683038277 799484](https://user-images.githubusercontent.com/93633761/236043356-569e1385-abbe-4d59-8a77-21e2236af1ad.jpg) | puno-cerrado | Presiona flecha abajo |
| ![Image_1683038560 5777776](https://user-images.githubusercontent.com/93633761/236043588-b9c52f75-aaef-4638-8c46-e6890e91a065.jpg) | grande-vertical | Presiona flecha izquierda |
| ![Image_1683041881 9164958](https://user-images.githubusercontent.com/93633761/236043747-8d84569b-c709-460d-adff-6127ac8471ac.jpg) | promesa-L | Presiona flecha derecha |
| ![Image_1683038948 2105362](https://user-images.githubusercontent.com/93633761/236044071-ba5594cd-4fe5-4474-be2d-a5bdced2ecb5.jpg) | pulgar-arriba | Subir en la página con Re Pág |
| ![Image_1683039085 871405](https://user-images.githubusercontent.com/93633761/236044230-335e3a98-b7b7-49b6-b32d-7aa4a2be2e38.jpg) | pulgar-abajo | Bajar en la página con Av Pág |
| ![Image_1683041408 8222876](https://user-images.githubusercontent.com/93633761/236044452-6874a51d-d364-42b8-b423-1fdaa4377f10.jpg) | cuatro-lado | Cambiar a pestaña a la izquierda con Ctrl + Re Pág |
| ![Image_1683041484 5584738](https://user-images.githubusercontent.com/93633761/236044735-705923bc-2b7a-4c06-9304-1d8a10ce1f32.jpg) | cinco-lado | Cambiar a pestaña a la derecha con Ctrl + Av Pág |
| ![Image_1683038670 9754667](https://user-images.githubusercontent.com/93633761/236045101-e11e1480-9704-4754-a713-2a240e7d058e.jpg) | telefono | Abrir nueva pestaña con Ctrl + w |
| ![Image_1683042202 868675](https://user-images.githubusercontent.com/93633761/236045220-892e2c1f-f2ac-4f39-99c8-9bb10c004747.jpg) | rock-lado | Aceptar / Entrar con Enter|
| ![Image_1683037947 2656171](https://user-images.githubusercontent.com/93633761/236045361-1c9c5011-61a4-4c74-933e-2c073858d472.jpg) | dos-dedos | Salir / Escapar con Esc |
| ![Image_1683042380 321436](https://user-images.githubusercontent.com/93633761/236045501-1eeb3759-484d-4b7e-9fcb-a57544d94a99.jpg) | poquito | Volver a la página anterior con Alt + Flecha izquierda |
| ![Image_1683042579 90073](https://user-images.githubusercontent.com/93633761/236045719-43d60e2d-c41d-4ed7-aca1-6c948f018ace.jpg) | dame | Volver a la página siguiente con Alt + Flecha derecha |
| ![Image_1683042066 6705244](https://user-images.githubusercontent.com/93633761/236045988-82e82475-f8c6-46f8-a519-f20e21131dd3.jpg) | acercate | Refrescar la página con Ctrl + r |
| ![Image_1683038154 961358](https://user-images.githubusercontent.com/93633761/236046303-bf81ce7e-4d4c-4555-b0ad-b44c383f1a41.jpg) | pistolita | Cerrar la pestaña actual con Ctrl + w, salir del programa si Chrome no fue abierto. |
| ![Image_1683042722 0223873](https://user-images.githubusercontent.com/93633761/236039924-a56ffd1d-5f48-4a01-8e43-25f75a169e33.jpg)| iglu  | Cierra la ventana a través de Alt + F4, y cierra el programa si no Chrome fue cerrado |

## Correr el programa
Para correr el programa, simplemente hay que correr a través de un intérprete de Python el script **control-chrome-gestos.py**

Sin embargo, para que automáticamente abrá Chrome, este deberá estar anclado a la barra de herramientas de acceso rápido, o el ícono deberá estar visible en la pantalla de manera que solo sea necesario darle **un** click para activarlo. Esto se debe a la forma en que fue creado a través de las librerías *pyautogui* y *pygetwindow*.
## Recomendaciones para su uso
1. La primera recomendación es asegurarse de estar en un entorno iluminado, ya que el modelo puede confundir los gestos si estos no están iluminados correctamente. También puede influir el fondo sobre el cual se realizan los gestos.
2. No acercar los gestos a la cámara, al hacerlo, el modelo no podrá recortar la imágen captada de la mano al tamaño correcto necesario para su interpretación. Aleje la mano de la cámara para una interpretación más fácil.
3. Para mayor confiabilidad, realizar los gestos con la mano derecha.
