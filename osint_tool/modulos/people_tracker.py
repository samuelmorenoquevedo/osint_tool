#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.social_media import buscar_perfiles
from utils.search_engines import buscar_en_google
from config.settings import SOCIAL_MEDIA, SEARCH_CONFIG

def buscar_persona(identificador):
    """Busca a una persona por teléfono o email"""
    print(f"\n👤 Buscando persona: {identificador['valor']}")
    print("-" * 50)
    
    resultados = {}
    
    # Buscar perfiles en redes sociales
    if identificador['tipo'] == 'telefono':
        print("📱 Buscando por número de teléfono...")
        perfiles = buscar_perfiles(identificador['valor'], tipo='telefono')
    else:
        print("📧 Buscando por email...")
        perfiles = buscar_perfiles(identificador['valor'], tipo='email')
    
    if perfiles:
        print("\n📋 PERFILES ENCONTRADOS:")
        for red, url in perfiles.items():
            print(f"   ✅ {red}: {url}")
            resultados[red] = url
    else:
        print("❌ No se encontraron perfiles públicos.")
    
    # Búsqueda avanzada en Google
    print("\n🔎 Realizando búsqueda en Google...")
    query = f'"{identificador["valor"]}"'
    resultados_google = buscar_en_google(query, num=SEARCH_CONFIG["GOOGLE"]["max_results"])
    
    if resultados_google:
        print(f"📊 Encontrados {len(resultados_google)} resultados en Google:")
        for i, resultado in enumerate(resultados_google[:5], 1):
            print(f"   {i}. {resultado}")
        if len(resultados_google) > 5:
            print(f"   ... y {len(resultados_google) - 5} resultados más")
    
    return resultados
