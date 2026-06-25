#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.social_media import buscar_opiniones
from utils.search_engines import buscar_en_google, buscar_en_news
from utils.sentiment import analizar_sentimiento
from config.settings import ANALYSIS_CONFIG

def analizar_reputacion(entidad):
    """Analiza la reputación online de una empresa o usuario"""
    print(f"\n⭐ Analizando reputación de: {entidad}")
    print("-" * 50)
    
    # Opiniones en redes sociales
    print("📱 Buscando opiniones en redes sociales...")
    opiniones = buscar_opiniones(entidad)
    if opiniones:
        print(f"📊 {len(opiniones)} opiniones encontradas")
    else:
        print("⚠️  No se encontraron opiniones")
    
    # Noticias recientes
    print("\n📰 Buscando noticias relacionadas...")
    noticias = buscar_en_news(entidad)
    print(f"📊 {len(noticias)} noticias encontradas")
    
    # Análisis de sentimiento
    if ANALYSIS_CONFIG["sentiment"]["enabled"]:
        print("\n💬 Analizando sentimiento general...")
        texto_completo = " ".join(opiniones + noticias)
        if texto_completo:
            sentimiento = analizar_sentimiento(texto_completo)
            print(f"📊 Sentimiento general: {sentimiento}")
        else:
            print("⚠️  No hay suficiente texto para analizar sentimiento")
    
    # Resumen
    print("\n" + "="*50)
    print("📊 RESUMEN DE REPUTACIÓN:")
    print(f"   - Opiniones: {len(opiniones)}")
    print(f"   - Noticias: {len(noticias)}")
    if opiniones or noticias:
        print("   - Estado: ANÁLISIS COMPLETADO")
    else:
        print("   - Estado: SIN INFORMACIÓN SUFICIENTE")
