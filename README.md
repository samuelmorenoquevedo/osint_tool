# 🔍 OSINT Multi-Tool

<div align="center">

![OSINT](https://img.shields.io/badge/OSINT-Tool-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-2.0-red)

**Framework modular de análisis OSINT con múltiples finalidades**

[Instalación](#-instalación) • [Uso](#-uso) • [Módulos](#-módulos) • [Configuración](#-configuración)

</div>

---

## 📋 Descripción

OSINT Multi-Tool es un framework modular para realizar análisis de inteligencia de fuentes abiertas (OSINT) con 9 módulos especializados:

1. 🛡️ Identificar y prevenir amenazas (Seguridad Nacional/Militar)
2. 👤 Buscar y seguir personas
3. ⭐ Reputación online (empresa/usuario)
4. 📊 Estudios sociológicos, psicológicos o lingüísticos
5. 🔒 Auditoría de privacidad y seguridad
6. 📰 Recopilación documental para periodismo
7. 🕵️ Investigación detectivesca
8. 📈 Evaluación de tendencias de mercado
9. 🎯 Análisis de mercado para marketing

> ⚠️ **Aviso Legal**: Esta herramienta es solo para fines educativos y autorizados. Asegúrate de cumplir con las leyes de protección de datos y obtener consentimiento cuando sea necesario.

---

## 🚀 Instalación

### Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/osint-tool.git
cd osint-tool
```
### Crear entorno virtual (recomendado)
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
### Instalar dependencias
```bash
pip install -r requirements.txt
```
### Verificar instalación
```bash
python main.py
```
---

## 📦 Dependencias
```bash
pip install requests beautifulsoup4 phonenumbers email-validator python-whois dnspython shodan tqdm textblob langdetect lxml
```
O instala todas de una vez con:
```bash
pip install -r requirements.txt
```
---

## ⚙️ Configuración

### 1. Configurar API Keys (opcional)

Edita el archivo `config/settings.py` o usa variables de entorno:
```bash
export SHODAN_API_KEY="tu_api_key_aqui"
export VIRUSTOTAL_API_KEY="tu_api_key_aqui"
export GOOGLE_CSE_API_KEY="tu_api_key_aqui"
export HIBP_API_KEY="tu_api_key_aqui"
```
### 2. Estructura de directorios
```bash
mkdir -p data logs reports cache

### 3. Verificar configuración
```bash
python -c "from config.settings import validate_config; print(validate_config())"
```
---

## 🎯 Uso

### Ejecutar la herramienta
```bash
python main.py
```
### Menú Principal

🔍 OSINT MULTI-TOOL v2.0 - Framework de Análisis OSINT

    1. 🛡️  Identificar y prevenir amenazas (Seguridad Nacional/Militar)
    2. 👤  Buscar y seguir personas
    3. ⭐  Reputación online (empresa/usuario)
    4. 📊  Estudios sociológicos, psicológicos o lingüísticos
    5. 🔒  Auditoría de privacidad y seguridad (empresas/organismos)
    6. 📰  Recopilación documental para periodismo
    7. 🕵️  Investigación detectivesca
    8. 📈  Evaluación de tendencias de mercado
    9. 🎯  Análisis de mercado para marketing
    0. 🚪  Salir

Selecciona una opción (0-9):

### Ejemplo de búsqueda por teléfono

`# Dentro de la herramienta, selecciona opción 1 o 2`
`# Introduce: +34600123456`

### Ejemplo de auditoría

`# Selecciona opción 5`
`# Introduce: ejemplo.com`

---

## 📁 Estructura del Proyecto

osint-tool/
├── main.py                 # Punto de entrada principal
├── modulos/                # Módulos OSINT
│   ├── threat_intel.py     # Análisis de amenazas
│   ├── people_tracker.py   # Seguimiento de personas
│   ├── reputation.py       # Reputación online
│   ├── sociological.py     # Estudios sociológicos
│   ├── privacy_audit.py    # Auditoría de privacidad
│   ├── journalism.py       # Recopilación periodística
│   ├── detective.py        # Investigación detectivesca
│   ├── market_trends.py    # Tendencias de mercado
│   └── marketing_analysis.py # Análisis de marketing
├── utils/                  # Utilidades
│   ├── validators.py       # Validadores (email, teléfono)
│   ├── search_engines.py   # Búsquedas en Google, Shodan, etc.
│   ├── social_media.py     # Búsqueda en redes sociales
│   ├── text_analysis.py    # Análisis de texto
│   ├── web.py              # Utilidades web
│   ├── sentiment.py        # Análisis de sentimiento
│   └── breach_check.py     # Verificación de filtraciones
├── config/
│   └── settings.py         # Configuración global
├── data/                   # Datos locales
├── logs/                   # Logs del sistema
├── reports/                # Reportes generados
└── requirements.txt        # Dependencias

---

## 🛠️ Módulos Disponibles

### 1. Threat Intelligence (threat_intel.py)

`from modulos import threat_intel`
`threat_intel.analizar_amenaza({"tipo": "email", "valor": "usuario@ejemplo.com"})`

**Funcionalidad:** Identifica posibles amenazas verificando filtraciones, spam y actividad sospechosa.

### 2. People Tracker (people_tracker.py)

`from modulos import people_tracker`
`people_tracker.buscar_persona({"tipo": "telefono", "valor": "+34600123456"})`

**Funcionalidad:** Busca perfiles en redes sociales y presencia online de una persona.

### 3. Reputation Analysis (reputation.py)

`from modulos import reputation`
`reputation.analizar_reputacion("Empresa XYZ")`

**Funcionalidad:** Analiza la reputación online mediante opiniones y noticias.

### 4. Sociological Studies (sociological.py)

`from modulos import sociological`
`sociological.analizar_corpus("https://ejemplo.com/articulo")`

**Funcionalidad:** Realiza análisis lingüístico, de emociones y complejidad textual.

### 5. Privacy Audit (privacy_audit.py)

`from modulos import privacy_audit`
`privacy_audit.auditar_privacidad("ejemplo.com")`

**Funcionalidad:** Audita WHOIS, subdominios, SSL y vulnerabilidades.

### 6. Journalism (journalism.py)

`from modulos import journalism`
`journalism.recopilar_documentacion("caso_corrupcion")`

**Funcionalidad:** Recopila documentación de prensa, oficial y redes sociales.

### 7. Detective (detective.py)

`from modulos import detective`
`detective.investigar("alias_sospechoso")`

**Funcionalidad:** Realiza investigación profunda en registros públicos y bases de datos.

### 8. Market Trends (market_trends.py)

`from modulos import market_trends`
`market_trends.evaluar_tendencias("tecnologia")`

**Funcionalidad:** Evalúa tendencias, crecimiento y competencia en un sector.

### 9. Marketing Analysis (marketing_analysis.py)

`from modulos import marketing_analysis`
`marketing_analysis.analizar_mercado("smartphone")`

**Funcionalidad:** Analiza público objetivo, competidores y estrategias de marketing.

---

## 🔧 Personalización

### Añadir nuevas fuentes de datos

Edita `utils/search_engines.py`:

`def buscar_en_mi_fuente(query):`
`    # Tu implementación aquí`
`    pass`

### Configurar límites legales

En `config/settings.py`:

`LEGAL_CONFIG = {`
`    "max_requests_per_minute": 30,`
`    "respect_robots_txt": True,`
`    "blocked_domains": [".gov", ".mil"],`
`    "require_authorization": False`
`}`

### Añadir nuevas redes sociales

En `config/settings.py`:

`SOCIAL_MEDIA = {`
`    "twitter": {`
`        "enabled": True,`
`        "url": "https://twitter.com/",`
`        "search_url": "https://twitter.com/search?q=",`
`    },`
`    # Añadir tu red social`
`    "tiktok": {`
`        "enabled": True,`
`        "url": "https://www.tiktok.com/@",`
`        "search_url": "https://www.tiktok.com/@",`
`    }`
`}`

---

## 📊 Ejemplos de Salida

### Búsqueda de persona

👤 Buscando persona: usuario@ejemplo.com

📋 PERFILES ENCONTRADOS:
   ✅ Twitter: https://twitter.com/usuario
   ✅ LinkedIn: https://linkedin.com/in/usuario
   ✅ GitHub: https://github.com/usuario
   ✅ Facebook: https://facebook.com/usuario

🔎 Realizando búsqueda en Google...
📊 Encontrados 50 resultados en Google:
   1. Resultado 1: https://ejemplo.com/resultado_1
   2. Resultado 2: https://ejemplo.com/resultado_2
   3. Resultado 3: https://ejemplo.com/resultado_3
   ... y 47 resultados más

### Auditoría de privacidad

🔒 Auditando privacidad de: ejemplo.com

📋 WHOIS:
   📛 Registrante: Privacidad activada
   ✉️  Email: privacidad@ejemplo.com
   📅 Creación: 2020-01-01
   ⏰ Expiración: 2025-01-01

🌐 SUBDOMINIOS DETECTADOS:
   ✅ www.ejemplo.com
   ✅ mail.ejemplo.com
   ✅ api.ejemplo.com

🔐 SSL/TLS:
   ✅ Certificado válido
   📅 Emitido para: ejemplo.com
   ⏰ Expira: 2025-12-31

📊 RESUMEN DE AUDITORÍA:
   - Subdominios encontrados: 3
   - Vulnerabilidades: 0
   ✅ SIN VULNERABILIDADES CRÍTICAS DETECTADAS

### Análisis sociológico

📊 Realizando análisis sociológico/lingüístico...

🌐 ANÁLISIS DE IDIOMA:
   ✅ Idioma detectado: es (confianza: 0.95)

📌 PALABRAS MÁS FRECUENTES:
   1. tecnología: 45 veces
   2. innovación: 32 veces
   3. futuro: 28 veces
   4. desarrollo: 25 veces
   5. inteligencia: 20 veces

😊 ANÁLISIS DE EMOCIONES:
   - positivo: 0.65
   - neutral: 0.25
   - negativo: 0.10

🏷️  ENTIDADES DETECTADAS:
   PERSON: Juan Pérez, María García
   ORG: Empresa X, Gobierno
   LOC: Madrid, Barcelona

📊 MÉTRICAS DE COMPLEJIDAD:
   - Longitud promedio de oración: 15.2 palabras
   - Diversidad léxica: 0.45
   - Índice de legibilidad: 65.3

---

## 🔐 Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

`# .env`
`SHODAN_API_KEY=tu_api_key`
`VIRUSTOTAL_API_KEY=tu_api_key`
`GOOGLE_CSE_API_KEY=tu_api_key`
`GOOGLE_CX_ID=tu_cx_id`
`HIBP_API_KEY=tu_api_key`
`BING_API_KEY=tu_api_key`
`ABUSEIPDB_API_KEY=tu_api_key`

Cargar variables de entorno:

`source .env`

---

## 🐛 Solución de Problemas

### Error: ModuleNotFoundError

`pip install nombre_del_modulo`

### Error: Permission denied

`sudo pip install -r requirements.txt`

### Error: SSL Certificate

`pip install --upgrade certifi`

### Error: API Key no configurada

`export SHODAN_API_KEY="tu_api_key"`

### Error: No se encuentran perfiles

`ping google.com`

---

## 🚀 Ejecutar en Modo Desarrollo

`python main.py --debug`
`python main.py --config mi_config.json`
`python -m modulos.threat_intel`

---

## 📝 Scripts Útiles

### Ejecutar todos los módulos automáticamente

`#!/bin/bash`
`# run_all.sh`
`python -c "from modulos import threat_intel; threat_intel.analizar_amenaza({'tipo': 'email', 'valor': 'test@example.com'})"`

### Limpiar archivos temporales

`#!/bin/bash`
`# clean.sh`
`rm -rf cache/*`
`rm -rf logs/*`
`rm -rf reports/*`

---

## 🔄 Actualización
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```
---

## 🗑️ Desinstalación
```bash
cd ..
rm -rf osint-tool
```
---

## 🤝 Contribuciones

1. Fork el repositorio
2. Crea tu rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit: `git commit -m 'Añadir nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

### Guía de Estilo

`def mi_funcion(parametro):`
`    """Descripción de la función."""`
`    pass`

---

## 📝 Licencia

MIT License - ver el archivo LICENSE para más detalles.

---

## ⚠️ Aviso Legal

**Esta herramienta es solo para fines educativos y de investigación.**

- ✅ Obtén consentimiento explícito antes de investigar personas
- ✅ Cumple con las leyes de protección de datos (GDPR, LOPD, etc.)
- ✅ No utilices para acoso, discriminación o actividades ilegales
- ✅ Respeta los términos de servicio de las plataformas

---

## 📚 Recursos Adicionales

- OSINT Framework - https://www.osintframework.com/
- Have I Been Pwned API - https://haveibeenpwned.com/API/v3
- Shodan Documentation - https://developer.shodan.io/api
- Google Custom Search API - https://developers.google.com/custom-search
- VirusTotal API - https://developers.virustotal.com/reference

---

