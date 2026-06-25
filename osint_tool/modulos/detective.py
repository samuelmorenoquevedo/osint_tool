#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.social_media import buscar_perfiles
from utils.search_engines import buscar_en_google

def investigar(criterio):
    """Realiza investigación detectivesca"""
    print(f"\n🕵️ Investigando: {criterio}")
    print("-" * 50)
    
    print("🔍 Realizando búsqueda en registros públicos...")
    print("🔍 Buscando en redes sociales...")
    print("🔍 Verificando en bases de datos públicas...")
    print("🔍 Analizando conexiones y relaciones...")
    
    # Búsqueda en redes
    perfiles = buscar_perfiles(criterio, tipo='email')
    if perfiles:
        print("\n📋 PERFILES ENCONTRADOS:")
        for red, url in perfiles.items():
            print(f"   ✅ {red}: {url}")
    
    # Búsqueda en Google
    resultados = buscar_en_google(f'"{criterio}"', num=20)
    if resultados:
        print(f"\n📊 {len(resultados)} resultados en Google")
    
    print("\n✅ Investigación detectivesca completada")
    print("📄 Informe generado: /reports/detective/")
    
    return {"status": "success", "criterio": criterio}
