/**
 * Configuració del lloc - Edita aquest fitxer per canviar opcions globals
 */

export const siteConfig = {
  // ===========================================
  // MODE VACANCES - Canvia això per activar/desactivar
  // ===========================================
  vacation: {
    enabled: true,                          // true = mostrar banner, false = ocultar
    returnDate: "13 de Febrer",             // Data de tornada
    message: "Estem de vacances! Ens veiem aviat."  // Missatge personalitzat
  },

  // ===========================================
  // SMARTMENU - Canvia quan tinguis l'URL
  // ===========================================
  smartMenuUrl: "#",  // Canvia "#" per l'URL real de SmartMenu

  // ===========================================
  // DADES DEL RESTAURANT
  // ===========================================
  restaurant: {
    name: "La Torre 2 Frankfurt",
    phone: "+34687985175",
    phoneDisplay: "687 985 175",
    email: "latorre2frankfurt@gmail.com",
    address: "Plaça Estació, 1",
    city: "Pineda de Mar",
    postalCode: "08397",
    hours: "18:00 - 23:00",
    hoursNote: "Obert cada dia"
  }
};
