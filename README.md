# pruebaCornerShop

Prueba de django para cornershop Esta prueba contiene 1 modelo con 3 clases Actividad, Shopper y Feedback.

Actividad: -Actividad permite registrar diferentes actividades bajo su descripcion. -Campo codigo lo coloque como un extra ya que es una buena practica.

Shopper: -Con campos nombre y nro_telefono. -Se puede registrar los Shoppers con que se trabaja. -Se pueden ir tambien agregando los shoppers nuevos.

Feedbacks: -Con campos feedback, fk_shopper, fk_actividad -Feedbacks posee dos foraneas que van indicar que shopper dio el feedback y bajo que actividad.

Ya se encuentra habilitado en el admin de django estos modelos para ser observados y manipulados.
