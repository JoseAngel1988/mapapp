function initMap() {
    const miMapa = new google.maps.Map(document.getElementById("mapa"), {
      center: { lat: 4.15, lng: -74.08 }, // Coordenadas de Colombia
      zoom: 6,
      // Agrega más opciones según tus necesidades
    });
    // Puedes agregar marcadores, polígonos, etc., utilizando la API de Google Maps
  }
  
  // Asegúrate de que la función initMap esté disponible globalmente
  window.initMap = initMap;
