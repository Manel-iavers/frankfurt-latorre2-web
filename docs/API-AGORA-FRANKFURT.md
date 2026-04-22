# API Àgora TPV — Frankfurt La Torre 2

**Data verificacio:** 9 abril 2026
**Estat:** Connexio activa, endpoint `export-master` funcional

---

## 1. Connexio

### Credencials

| Camp | Valor |
|------|-------|
| **URL base** | `http://frankfurtlatorre2.dyndns.org:8984` |
| **IP directa** | `93.176.162.104` |
| **Port** | `8984` |
| **Token** | `LaTorre2-2026` |
| **Header autenticacio** | `Api-Token: LaTorre2-2026` |
| **Workplace ID** | `kfufktzc` |
| **Proveidor TPV** | pcSystem, S.C.P. (CIF: J63839435, Barcelona) |

### SmartMenu (comandes online)

```
https://smartmenu.agorapos.com/?id=k4mrr39a&workplaceId=kfufktzc
```

Configurat a `src/config/site.ts:18` de la web.

### Test rapid de connexio

```bash
curl -H "Api-Token: LaTorre2-2026" \
  "http://frankfurtlatorre2.dyndns.org:8984/api/export-master/?filter=Series"
```

Resposta esperada: JSON amb series de facturacio.

---

## 2. Endpoints Disponibles

### Funcional

| Endpoint | Metode | Estat |
|----------|--------|-------|
| `/api/export-master/` | GET | **200 OK** |
| `/api/export-master/?filter=X` | GET | **200 OK** |

### No disponibles (HTTP 404)

| Endpoint | Funcio esperada | Motiu probable |
|----------|----------------|----------------|
| `/api/export-sales/` | Exportar vendes/tiquets | Modul no activat |
| `/api/import-master/` | Importar dades mestres | Modul no activat |
| `/api/import-sales/` | Importar vendes | Modul no activat |
| `/api/export-closings/` | Tancaments de caixa | Modul no activat |
| `/api/export-employee-clockings/` | Fitxatge empleats | Modul no activat |
| `/api/import-employee-clockings/` | Introduir fitxatge | Modul no activat |
| `/api/export-stock/` | Moviments d'estoc | Modul no activat |

> **IMPORTANT:** Nomes `export-master` funciona. Per activar la resta,
> cal demanar a **pcSystem** que activi els moduls complets de l'API HTTP a l'Administracio d'Agora.

---

## 3. Dades Mestres (export-master)

### Filtres disponibles

```bash
# Tots els filtres a la vegada (resposta gran)
curl -H "Api-Token: LaTorre2-2026" \
  "http://frankfurtlatorre2.dyndns.org:8984/api/export-master/"

# Filtre individual
curl -H "Api-Token: LaTorre2-2026" \
  "http://frankfurtlatorre2.dyndns.org:8984/api/export-master/?filter=Products"
```

| Filtre | Elements | Descripcio |
|--------|----------|------------|
| `Products` | 60 | Carta completa amb preus, suplements, IVA |
| `Families` | 5 | Entrepans, Tapes, Begudes, Varis, Suplements |
| `Customers` | 732 | Clients registrats (nom fiscal, CIF, adreca) |
| `Users` | 13 | Empleats del sistema |
| `Series` | 6 | Series de facturacio |
| `PriceLists` | 2 | Salo, Terrassa |
| `Vats` | 4 | Tipus d'IVA |
| `SaleCenters` | 3 | Salo, Terrassa, Comanda (TakeAway) |
| `Warehouses` | 1 | Magatzem General |
| `PreparationTypes` | 3 | Tipus de preparacio |
| `PreparationOrders` | 4 | Ordres de preparacio |
| `PredefinedNotes` | 27 | Notes predefinides (poc fet, molt fet, sense salsa...) |
| `PaymentMethods` | 1 | Metodes de pagament |
| `WorkplacesSummary` | 1 | Info del local (TPV + Tablet) |

---

## 4. Estructura de Dades

### Producte (exemple: FRANKFURT)

```json
{
  "Id": 1,
  "Name": "FRANKFURT",
  "FamilyId": 1,
  "VatId": 3,
  "CostPrice": 0.0,
  "Prices": [
    { "PriceListId": 1, "MainPrice": 4.00 },
    { "PriceListId": 2, "MainPrice": 4.25 }
  ],
  "Addins": [
    { "AddinSaleFormatId": 51 },
    { "AddinSaleFormatId": 53 }
  ],
  "StorageOptions": [
    { "WarehouseId": 1, "MinStock": 0.0, "MaxStock": 0.0 }
  ]
}
```

- `PriceListId 1` = Salo
- `PriceListId 2` = Terrassa (normalment +0,25€)
- `Addins` = Suplements disponibles (formatge, baco, ceba, ou, tomaquet...)

### Families

| Id | Nom | Visible al TPV |
|----|-----|----------------|
| 1 | ENTREPANS | Si |
| 2 | TAPES | Si |
| 3 | BEGUDES | Si |
| 4 | VARIS | No |
| 5 | SUPLEMENTS | No |

### Centres de Venda (SaleCenters)

| Id | Nom | Llista preus | Taules |
|----|-----|-------------|--------|
| 1 | Salo | Salo | BARRA, 1-7 (amb Bis) |
| 2 | Terrassa | Terrassa | T1-T22 |
| 3 | Comanda | Salo | TAKE, EMP.1-16 |

### Empleats (Users)

| Id | Nom |
|----|-----|
| 1 | admin |
| 2 | pcsystem |
| 3 | PEDRO |
| 4 | MANEL |
| 5 | MARC |
| 6 | LAIA |
| 7 | ALEIX |
| 8 | ALGU |
| 9 | PAPE |
| 10 | AMIN |
| 11 | EMPLE. 10 |
| 12 | EMPLE. 11 |
| 13 | DAVID |

### Series de Facturacio

| Serie | Ultim numero | Tipus |
|-------|-------------|-------|
| T | 27.168 | Tiquet simplificat (BasicInvoice) |
| F | 13 | Factura completa (StandardInvoice) |
| TD | 284 | Devolucion (BasicRefund) |
| FD | 0 | Devolucion factura (StandardRefund) |
| A | 7 | Albara (DeliveryNote) |
| P | 985 | Comanda (SalesOrder) |

### Carta Completa (60 productes)

**Entrepans:** Frankfurt, Bratwurst, Hamburguesa, Petxuga, Llom, Cervela, Pikanwurst, Xistorra, Malaguenya, Baco, Pinxo, Bikini, Truita, Formatge amb Ceba

**Tapes:** Braves, 1/2 Braves, Fritas, 1/2 Fritas, Nuggets, Croquetes, Calamars, Morrillo, Aletes Pollastre

**Begudes:** Estrella Damm, Voll Damm, Free-Damm, Free-Lemon, Torrada Damm, Turia (mitjanes), Copa cervesa, Copa 1/2L, Shandy, Tinto de Verano, Copa vi negre/blanc, Ampolla vi negre/blanc, Coca Cola, Coca Cola Zero, Fanta Taronja/Llimona, Aigua, Aigua amb gas, Aquarius Taronja/Llimona, Nestea, Sprite

**Suplements:** Formatge, Baco, Ceba, Ou, Tomaquet, Pa amb Tomaquet, Pot Salsa

---

## 5. Que es pot fer AMB el que tenim (export-master)

### 5.1 Sincronitzar carta web amb TPV
**Complexitat:** Baixa
**Com:** Llegir productes + preus de l'API i actualitzar la web automaticament.
No caldria mantenir la carta manualment.

### 5.2 Validar coherencia preus web vs TPV
**Complexitat:** Baixa
**Com:** Script periodic que compara preus de la web amb els de l'API.
Alerta si hi ha discrepancies.

### 5.3 Directori d'empleats
**Complexitat:** Baixa
**Com:** Llistat d'empleats actius. Util per a control intern.

---

## 6. Moduls d'Agora — Que cal activar

Segons la documentacio oficial d'Agora (agorapos.com), el TPV te **moduls addicionals** que es poden
activar des de `Eines → Activar Moduls Addicionals` a l'Administracio d'Agora.
Cada modul pot requerir llicencia addicional — pcSystem ho ha de consultar amb Agora/IGT.

### Moduls rellevants per nosaltres

| Modul Agora | Estat actual | Que ens aporta |
|-------------|-------------|----------------|
| **Servicios de Integración** | ACTIU (parcial) | API HTTP — ara nomes export-master. Cal que obrin export-sales, import, clockings |
| **Fichajes** | DESCONEGUT | Registre jornada laboral. Si s'activa, l'API pot exportar/importar fitxatges |
| **Compras y Stock** | DESCONEGUT | Control compres i inventari. Si s'activa, l'API pot exportar estoc |
| **My Ágora** | DESCONEGUT | Consulta estat del local des del mobil (my.agorapos.com) — pot ser util directament |
| **Programación de Tarifas** | DESCONEGUT | Canvis de preu automatics per horari/dia (happy hour, etc.) |

### El que necessitem de l'API (Servicios de Integración)

#### export-sales (PRIORITAT ALTA)
**Per a que serveix:** Exportar tiquets de venda amb detall (productes, quantitats, preus, hora, empleat, metode pagament).

**Que podrem fer:**
- Informe nocturn de vendes → WhatsApp/Telegram (23:45h)
- Dashboard de vendes en temps real
- Comparativa vendes per dia/setmana/mes
- Ranking de productes mes venuts
- Analisi d'hores punta
- Facturacio per empleat

#### export-employee-clockings (PRIORITAT ALTA)
**Per a que serveix:** Exportar fitxatge d'empleats (entrada/sortida). Requereix el modul **Fichajes** actiu.

**Que podrem fer:**
- Consultar fitxatge de qualsevol empleat
- Generar full de fitxatge mensual (PDF)
- Calcular hores treballades per empleat
- Detectar anomalies (faltes, retards)
- Compliment legal fitxatge (obligatori des de 2019)

#### import-employee-clockings (PRIORITAT MITJANA)
**Per a que serveix:** Introduir fitxatge des de fora del TPV.

**Que podrem fer:**
- App de fitxatge per mobil (els empleats fichen des del telefon)
- Correccions de fitxatge sense tocar el TPV
- Fitxatge remot per a repartidors

#### export-stock / import-stock (PRIORITAT MITJANA)
**Per a que serveix:** Veure moviments d'estoc i nivells actuals. Requereix el modul **Compras y Stock** actiu.

**Que podrem fer:**
- Alertes d'estoc baix per WhatsApp
- Historial de moviments
- Prediccio de necessitats de compra

> **Nota sobre estoc:** Per a que funcioni, cal que el Frankfurt tingui
> introduit l'estoc inicial i el vagi actualitzant. Si no ho fan manualment,
> es podria fer via import-master o amb lectura d'albarans (veure seccio 7).

#### import-master (PRIORITAT BAIXA)
**Per a que serveix:** Importar/actualitzar productes, preus, clients al TPV.

**Que podrem fer:**
- Actualitzar preus massivament des d'un Excel
- Afegir productes nous sense tocar el TPV
- Gestionar clients des d'una app externa

### Funcionalitats d'Agora que NO passen per l'API

| Funcionalitat | Com funciona | Notes |
|---------------|-------------|-------|
| **Copies de seguretat** | Fitxers locals al PC del TPV | Cal acces a la carpeta (xarxa, SSH, FTP) — no hi ha endpoint API |
| **My Agora** | App mobil directa (my.agorapos.com) | No cal desenvolupament, nomes activar |
| **SmartMenu** | Ja configurat i funcionant | Comandes online directes al TPV |

---

## 7. Ideas Avancades (futures)

### 7.1 Pujar compres des d'imatge d'albara
**Viabilitat:** Possible pero complexa
**Com funcionaria:**
1. El Frankfurt fa foto de l'albara del proveidor
2. IA (Claude Vision / GPT-4o) extreu productes, quantitats, preus
3. Es crea un moviment d'estoc via `import-master` o `import-stock`
4. L'estoc s'actualitza automaticament al TPV

**Requisits:**
- Que pcSystem activi `import-master` o `import-stock`
- Desenvolupar l'extractor d'albarans (OCR + IA)
- Mappejar productes albara → productes Agora

### 7.2 Copies de seguretat automatitzades
**Viabilitat:** No via API (no hi ha endpoint de backup)
**Alternativa:** pcSystem va oferir donar acces a la carpeta de copies.
- Si es per xarxa local (SMB/NFS): script que copia cada nit
- Si es per SSH/SFTP: cron job que descarrega
- Cal preguntar a pcSystem el path exacte i com accedir-hi

### 7.3 Full de fitxatge PDF
**Viabilitat:** Possible un cop tinguem `export-employee-clockings`
**Format:** PDF mensual per empleat amb:
- Dies treballats
- Hora entrada / sortida
- Total hores dia
- Total hores mes
- Signatura digital (opcio)

---

## 8. Accions Pendents

### Per demanar a pcSystem

```
Hola,

Sobre l'API HTTP del TPV Agora de Frankfurt La Torre 2:

1. Podries activar els seguents moduls de l'API?
   - export-sales (vendes/tiquets)
   - export-employee-clockings (fitxatge)
   - import-employee-clockings (introduir fitxatge)
   - export-stock (estoc)
   - import-master (importar productes/preus)

2. Sobre les copies de seguretat:
   - A quina carpeta estan les copies?
   - Com hi podem accedir remotament? (xarxa local, SSH, FTP?)
   - Amb quina frequencia es fan?

Gracies!
```

---

## 9. Arquitectura Tecnica

```
[Frankfurt La Torre 2]
        |
        |  TPV Agora (PC local)
        |  Port 8984 → obert a Internet via router
        |  DynDNS: frankfurtlatorre2.dyndns.org
        |
        v
[Internet]
        |
        +--→ SmartMenu (agorapos.com) → Comandes online → TPV
        |
        +--→ API HTTP (:8984) → export-master → Dades mestres
        |    (export-sales, clockings, stock → PENDENTS d'activar)
        |
        +--→ Web Frankfurt (Astro/Vercel) → Landing + link SmartMenu
        |
        +--→ n8n (automatitzacions futures)
             - Informe vendes nocturn
             - Alertes estoc
             - Full fitxatge
```

---

*Document generat: 9 abril 2026*
*Ultima connexio verificada: 9 abril 2026 — export-master OK*
