#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config.settings import SCRAPING_CONFIG

def descargar_texto(url):
    """Descarga el texto de una URL"""
    try:
        headers = {"User-Agent": SCRAPING_CONFIG["user_agent"]}
        response = requests.get(url, headers=headers, timeout=SCRAPING_CONFIG["timeout"])
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Eliminar scripts y estilos
        for script in soup(["script", "style"]):
            script.decompose()
        
        return soup.get_text()
    except Exception as e:
        print(f"Error al descargar: {e}")
        return None
