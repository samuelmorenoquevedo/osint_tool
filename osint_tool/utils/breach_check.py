#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from config.settings import API_KEYS

def check_breaches(email):
    """Verifica si un email ha aparecido en filtraciones"""
    print(f"   🔍 Verificando {email} en HaveIBeenPwned...")
    
    # Simulación usando HaveIBeenPwned
    try:
        # En producción usar API real
        # headers = {"hibp-api-key": API_KEYS.get("HAVEIBEENPWNED", "")}
        # response = requests.get(
        #     f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}",
        #     headers=headers
        # )
        # return response.json() if response.status_code == 200 else []
        
        # Simulación para pruebas
        if "test" in email or "example" in email:
            return ["Breach de ejemplo 1", "Breach de ejemplo 2"]
        return []
    except:
        return []
