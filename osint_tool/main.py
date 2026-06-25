#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import importlib

# Importar módulos dinámicamente
threat_intel = importlib.import_module('modulos.threat_intel')
people_tracker = importlib.import_module('modulos.people_tracker')
reputation = importlib.import_module('modulos.reputation')
sociological = importlib.import_module('modulos.sociological')
privacy_audit = importlib.import_module('modulos.privacy_audit')
journalism = importlib.import_module('modulos.journalism')
detective = importlib.import_module('modulos.detective')
market_trends = importlib.import_module('modulos.market_trends')
marketing_analysis = importlib.import_module('modulos.marketing_analysis')

from utils.validators import validar_telefono, validar_email

def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones"""
    print("\n" + "="*60)
    print("🔍 OSINT MULTI-TOOL v2.0 - Framework de Análisis OSINT")
    print("="*60)
    print("""
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
    """)
    return input("Selecciona una opción (0-9): ").strip()

def submenu_busqueda_por_identificador():
    """Submenú común para búsquedas por teléfono o email"""
    print("\n" + "-"*40)
    print("🔎 BÚSQUEDA POR IDENTIFICADOR")
    print("-"*40)
    print("1. Buscar por número de teléfono")
    print("2. Buscar por correo electrónico")
    print("3. Volver al menú principal")
    opcion = input("Elige (1-3): ").strip()
    
    if opcion == "1":
        telefono = input("📞 Introduce el número (con código país, ej: +34600123456): ")
        if validar_telefono(telefono):
            return {"tipo": "telefono", "valor": telefono}
        else:
            print("❌ Número inválido.")
            return None
    elif opcion == "2":
        email = input("📧 Introduce el email: ")
        if validar_email(email):
            return {"tipo": "email", "valor": email}
        else:
            print("❌ Email inválido.")
            return None
    elif opcion == "3":
        return "volver"
    else:
        print("❌ Opción no válida.")
        return None

def main():
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "0":
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            sys.exit(0)
        elif opcion == "1":
            print("\n🛡️  MÓDULO DE IDENTIFICACIÓN DE AMENAZAS")
            identificador = submenu_busqueda_por_identificador()
            if identificador and identificador != "volver":
                threat_intel.analizar_amenaza(identificador)
            elif identificador == "volver":
                continue
        elif opcion == "2":
            print("\n👤 MÓDULO DE SEGUIMIENTO DE PERSONAS")
            identificador = submenu_busqueda_por_identificador()
            if identificador and identificador != "volver":
                people_tracker.buscar_persona(identificador)
            elif identificador == "volver":
                continue
        elif opcion == "3":
            print("\n⭐ MÓDULO DE REPUTACIÓN ONLINE")
            entidad = input("Introduce el nombre de la empresa o usuario: ")
            reputation.analizar_reputacion(entidad)
        elif opcion == "4":
            print("\n📊 MÓDULO DE ESTUDIOS SOCIALES")
            corpus = input("Introduce el texto o URL del corpus a analizar: ")
            sociological.analizar_corpus(corpus)
        elif opcion == "5":
            print("\n🔒 MÓDULO DE AUDITORÍA DE PRIVACIDAD")
            dominio = input("Introduce el dominio de la empresa (ej: ejemplo.com): ")
            privacy_audit.auditar_privacidad(dominio)
        elif opcion == "6":
            print("\n📰 MÓDULO DE RECOPILACIÓN PERIODÍSTICA")
            tema = input("Introduce el tema de investigación: ")
            journalism.recopilar_documentacion(tema)
        elif opcion == "7":
            print("\n🕵️ MÓDULO DE INVESTIGACIÓN DETECTIVESCA")
            criterio = input("Introduce el criterio de búsqueda (nombre, alias, etc.): ")
            detective.investigar(criterio)
        elif opcion == "8":
            print("\n📈 MÓDULO DE TENDENCIAS DE MERCADO")
            sector = input("Introduce el sector/industria: ")
            market_trends.evaluar_tendencias(sector)
        elif opcion == "9":
            print("\n🎯 MÓDULO DE ANÁLISIS PARA MARKETING")
            producto = input("Introduce el producto/servicio: ")
            marketing_analysis.analizar_mercado(producto)
        else:
            print("❌ Opción no válida. Intenta de nuevo.")
        
        input("\n⏎ Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
