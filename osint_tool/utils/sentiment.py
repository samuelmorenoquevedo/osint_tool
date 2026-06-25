#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from textblob import TextBlob
from config.settings import ANALYSIS_CONFIG

def analizar_sentimiento(texto):
    """Analiza el sentimiento de un texto"""
    if not texto:
        return "No hay texto para analizar"
    
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    
    if polaridad > 0.3:
        return "POSITIVO 😊"
    elif polaridad < -0.3:
        return "NEGATIVO 😞"
    else:
        return "NEUTRAL 😐"
