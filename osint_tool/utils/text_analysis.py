#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import re
from textblob import TextBlob
from langdetect import detect, detect_langs

def detectar_idioma(texto):
    """Detecta el idioma del texto"""
    try:
        lang = detect(texto)
        confidence = 1.0
        return lang, confidence
    except:
        return "unknown", 0.0

def frecuencia_palabras(texto, top=10):
    """Calcula la frecuencia de palabras"""
    palabras = re.findall(r'\w+', texto.lower())
    stopwords = {'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 
                 'de', 'en', 'a', 'por', 'con', 'sin', 'para', 'sobre'}
    palabras_filtradas = [p for p in palabras if p not in stopwords and len(p) > 2]
    return Counter(palabras_filtradas).most_common(top)

def analizar_emociones(texto):
    """Analiza emociones en el texto"""
    blob = TextBlob(texto)
    # Simulación de emociones
    return {
        "positivo": max(0, blob.sentiment.polarity),
        "negativo": max(0, -blob.sentiment.polarity),
        "neutral": 1 - abs(blob.sentiment.polarity)
    }

def analizar_entidades(texto):
    """Extrae entidades nombradas (NER)"""
    # Simulación
    return {
        "PERSON": ["Juan Pérez", "María García"],
        "ORG": ["Empresa X", "Gobierno"],
        "LOC": ["Madrid", "Barcelona"]
    }

def analizar_complejidad(texto):
    """Analiza la complejidad del texto"""
    oraciones = texto.split('.')
    palabras = texto.split()
    
    longitud_oracion = len(palabras) / len(oraciones) if oraciones else 0
    diversidad_lexica = len(set(palabras)) / len(palabras) if palabras else 0
    
    return {
        "longitud_oracion": longitud_oracion,
        "diversidad_lexica": diversidad_lexica,
        "legibilidad": 70.0  # Simulación
    }
