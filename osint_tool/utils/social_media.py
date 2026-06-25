#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config.settings import SOCIAL_MEDIA

def buscar_perfiles(identificador, tipo='email'):
    """Busca perfiles en redes sociales"""
    perfiles = {}
    
    # Redes sociales activas
    redes_activas = [red for red, config in SOCIAL_MEDIA.items() if config.get('enabled')]
    
    print(f"🔍 Buscando en {len(redes_activas)} redes sociales...")
    
    # Simulación: devolver algunos perfiles de ejemplo
    # En una implementación real, aquí se harían peticiones HTTP
    if tipo == 'email':
        perfiles = {
            "Twitter": f"https://twitter.com/search?q={identificador}",
            "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={identificador}",
            "GitHub": f"https://github.com/search?q={identificador}",
            "Facebook": f"https://www.facebook.com/search/top/?q={identificador}",
            "Instagram": f"https://www.instagram.com/explore/search/?q={identificador}"
        }
    else:  # teléfono
        perfiles = {
            "WhatsApp": f"https://wa.me/{identificador}",
            "Telegram": f"https://t.me/{identificador}",
            "Facebook": f"https://www.facebook.com/search/top/?q={identificador}",
            "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={identificador}"
        }
    
    return perfiles

def buscar_opiniones(entidad):
    """Busca opiniones sobre una entidad"""
    # Simulación
    opiniones_ejemplo = [
        "Excelente servicio, muy recomendable",
        "Producto de calidad, pero caro",
        "Atención al cliente mejorable",
        "Buena relación calidad-precio",
        "Muy profesional y eficiente"
    ]
    return opiniones_ejemplo

def buscar_en_redes(identificador, red_social=None):
    """Función genérica para buscar en redes (alias de buscar_perfiles)"""
    return buscar_perfiles(identificador)
