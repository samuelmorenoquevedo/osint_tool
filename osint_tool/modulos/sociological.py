#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.text_analysis import (
    frecuencia_palabras, 
    analizar_emociones, 
    detectar_idioma,
    analizar_entidades,
    analizar_complejidad
)
from utils.web import descargar_texto
from config.settings import ANALYSIS_CONFIG

def analizar_corpus(corpus):
    """Realiza análisis sociológico/lingüístico de un texto"""
    print("\n📊 Realizando análisis sociológico/lingüístico...")
    print("-" * 50)
    
    # Obtener texto (si es URL, descargar)
    if corpus.startswith("http"):
        print("🌐 Descargando contenido desde URL...")
        texto = descargar_texto(corpus)
        if not texto:
            print("❌ Error al descargar el contenido")
            return
    else:
        texto = corpus
    
    if len(texto.strip()) < 10:
        print("❌ El texto es demasiado corto para analizar")
        return
    
    print(f"📄 Longitud del texto: {len(texto)} caracteres")
    print("-" * 50)
    
    # 1. Detección de idioma
    if ANALYSIS_CONFIG["language_detection"]["enabled"]:
        print("\n🌐 ANÁLISIS DE IDIOMA:")
        idioma, confianza = detectar_idioma(texto)
        if confianza >= ANALYSIS_CONFIG["language_detection"]["confidence_threshold"]:
            print(f"   ✅ Idioma detectado: {idioma} (confianza: {confianza:.2f})")
        else:
            print(f"   ⚠️  Idioma dudoso: {idioma} (confianza baja: {confianza:.2f})")
    
    # 2. Frecuencia de palabras
    print("\n📌 PALABRAS MÁS FRECUENTES:")
    frecuencias = frecuencia_palabras(texto, top=10)
    for i, (palabra, count) in enumerate(frecuencias, 1):
        print(f"   {i}. {palabra}: {count} veces")
    
    # 3. Análisis de emociones
    if ANALYSIS_CONFIG["sentiment"]["enabled"]:
        print("\n😊 ANÁLISIS DE EMOCIONES:")
        emociones = analizar_emociones(texto)
        for emocion, puntuacion in emociones.items():
            if puntuacion > 0.1:  # Mostrar solo emociones significativas
                print(f"   - {emocion}: {puntuacion:.2f}")
    
    # 4. Entidades nombradas (NER)
    if ANALYSIS_CONFIG["ner"]["enabled"]:
        print("\n🏷️  ENTIDADES DETECTADAS:")
        entidades = analizar_entidades(texto)
        for tipo, lista in entidades.items():
            if lista:
                print(f"   {tipo}: {', '.join(lista[:5])}")
    
    # 5. Complejidad del texto
    print("\n📊 MÉTRICAS DE COMPLEJIDAD:")
    metricas = analizar_complejidad(texto)
    print(f"   - Longitud promedio de oración: {metricas['longitud_oracion']:.1f} palabras")
    print(f"   - Diversidad léxica: {metricas['diversidad_lexica']:.2f}")
    print(f"   - Índice de legibilidad: {metricas['legibilidad']:.1f}")
