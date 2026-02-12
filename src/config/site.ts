/**
 * Configuració del lloc - Edita aquest fitxer per canviar opcions globals
 */

export const siteConfig = {
  // ===========================================
  // MODE VACANCES - Canvia això per activar/desactivar
  // ===========================================
  vacation: {
    enabled: false,                         // true = mostrar banner, false = ocultar
    returnDate: "13 de Febrer",             // Data de tornada
    message: "Estem de vacances! Ens veiem aviat."  // Missatge personalitzat
  },

  // ===========================================
  // SMARTMENU - Canvia quan tinguis l'URL
  // ===========================================
  smartMenuUrl: "https://smartmenu.agorapos.com/?id=k4mrr39a&workplaceId=kfufktzc",

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
  },

  // ===========================================
  // GOOGLE ANALYTICS 4 - Canvia l'ID quan el tinguis
  // ===========================================
  analytics: {
    gaId: "G-78HVRXVX7D",
    enabled: true
  },

  // ===========================================
  // COOKIES - Banner de consentiment
  // ===========================================
  cookies: {
    enabled: true,
    storageKey: "cookie-consent-latorre2"
  }
};
