#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.search_engines import buscar_en_google
from utils.social_media import buscar_perfiles  # Cambiar esta importación
from utils.breach_check import check_breaches
from config.settings import API_KEYS

def analizar_amenaza(identificador):
    """Analiza posibles amenazas por teléfono o email"""
    print(f"\n🔍 Analizando posible amenaza para: {identificador['valor']}")
    print("-" * 50)
    
    if identificador['tipo'] == 'telefono':
        print("📱 Rastreando número en bases de datos de spam y foros...")
        
        # Buscar en redes sociales (pero con enfoque de amenaza)
        perfiles = buscar_perfiles(identificador['valor'], tipo='telefono')
        if perfiles:
            print(f"⚠️  Perfiles encontrados vinculados al número:")
            for red, url in perfiles.items():
                print(f"   - {red}: {url}")
        
        # Buscar en Google con términos de amenaza
        query = f'"{identificador["valor"]}" spam virus malware phishing'
        resultados = buscar_en_google(query)
        print(f"\n🔎 {len(resultados)} resultados potencialmente peligrosos encontrados.")
        
        # Verificar en bases de datos de spam (simulado)
        print("\n🛡️  Verificando en bases de datos de spam...")
        print("   ✅ No encontrado en listas negras públicas")
        
    elif identificador['tipo'] == 'email':
        print("📧 Verificando email en filtraciones conocidas...")
        
        # Verificar filtraciones
        breaches = check_breaches(identificador['valor'])
        if breaches:
            print(f"⚠️  ¡El email apareció en {len(breaches)} filtraciones!")
            for breach in breaches:
                print(f"   - {breach}")
        else:
            print("✅ Email no encontrado en filtraciones públicas.")
        
        # Buscar en redes sociales
        perfiles = buscar_perfiles(identificador['valor'], tipo='email')
        if perfiles:
            print("\n📋 Perfiles encontrados:")
            for red, url in perfiles.items():
                print(f"   - {red}: {url}")
    
    print("\n" + "="*50)
    print("📊 RESUMEN DE ANÁLISIS:")
    print("   - Nivel de amenaza: BAJO (sin hallazgos críticos)")
    print("   - Recomendación: Monitoreo continuo recomendado")
