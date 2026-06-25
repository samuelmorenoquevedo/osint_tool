#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Configuración global del sistema OSINT Multi-Tool
"""

import os
from pathlib import Path

# ============================================
# CONFIGURACIÓN GENERAL
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
REPORTS_DIR = BASE_DIR / "reports"
CACHE_DIR = BASE_DIR / "cache"

# Crear directorios si no existen
for dir_path in [DATA_DIR, LOGS_DIR, REPORTS_DIR, CACHE_DIR]:
    dir_path.mkdir(exist_ok=True)

# ============================================
# API KEYS (llenar con tus propias claves)
# ============================================

API_KEYS = {
    "SHODAN": os.environ.get("SHODAN_API_KEY", ""),
    "GOOGLE_CSE": os.environ.get("GOOGLE_CSE_API_KEY", ""),
    "GOOGLE_CX": os.environ.get("GOOGLE_CX_ID", ""),
    "BING": os.environ.get("BING_API_KEY", ""),
    "HAVEIBEENPWNED": os.environ.get("HIBP_API_KEY", ""),
    "DEHASHED": os.environ.get("DEHASHED_API_KEY", ""),
    "VIRUSTOTAL": os.environ.get("VIRUSTOTAL_API_KEY", ""),
    "ABUSEIPDB": os.environ.get("ABUSEIPDB_API_KEY", ""),
    "GREYNOISE": os.environ.get("GREYNOISE_API_KEY", ""),
    "TWITTER_BEARER": os.environ.get("TWITTER_BEARER_TOKEN", ""),
    "FACEBOOK_ACCESS": os.environ.get("FACEBOOK_ACCESS_TOKEN", ""),
    "LINKEDIN": os.environ.get("LINKEDIN_API_KEY", ""),
    "IPINFO": os.environ.get("IPINFO_API_KEY", ""),
    "WHOISXML": os.environ.get("WHOISXML_API_KEY", ""),
}

# ============================================
# CONFIGURACIÓN DE BÚSQUEDA
# ============================================

SEARCH_CONFIG = {
    "GOOGLE": {
        "enabled": True,
        "max_results": 50,
        "language": "es",
        "safe_search": "off",
        "timeout": 10,
    },
    "BING": {
        "enabled": True,
        "max_results": 30,
        "language": "es-ES",
        "timeout": 10,
    },
    "SOCIAL_NETWORKS": {
        "enabled": True,
        "max_results": 20,
        "timeout": 15,
    },
    "DEEP_WEB": {
        "enabled": False,
        "timeout": 30,
    }
}

# ============================================
# CONFIGURACIÓN DE REDES SOCIALES
# ============================================

SOCIAL_MEDIA = {
    "twitter": {
        "enabled": True,
        "url": "https://twitter.com/",
        "search_url": "https://twitter.com/search?q=",
    },
    "facebook": {
        "enabled": True,
        "url": "https://www.facebook.com/",
        "search_url": "https://www.facebook.com/search/top/?q=",
    },
    "linkedin": {
        "enabled": True,
        "url": "https://www.linkedin.com/in/",
        "search_url": "https://www.linkedin.com/search/results/people/?keywords=",
    },
    "instagram": {
        "enabled": True,
        "url": "https://www.instagram.com/",
        "search_url": "https://www.instagram.com/",
    },
    "github": {
        "enabled": True,
        "url": "https://github.com/",
        "search_url": "https://github.com/search?q=",
    },
    "reddit": {
        "enabled": True,
        "url": "https://www.reddit.com/user/",
        "search_url": "https://www.reddit.com/search/?q=",
    },
}

# ============================================
# CONFIGURACIÓN DE SCRAPING
# ============================================

SCRAPING_CONFIG = {
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "delay": 1,
    "random_delay": True,
    "timeout": 15,
    "max_redirects": 5,
    "verify_ssl": True,
    "use_cache": True,
    "cache_expiry": 3600,
}

# ============================================
# CONFIGURACIÓN DE ANÁLISIS
# ============================================

ANALYSIS_CONFIG = {
    "sentiment": {
        "enabled": True,
        "language": "spanish",
        "model": "vader",
    },
    "ner": {
        "enabled": True,
        "entities": ["PERSON", "ORG", "LOC", "DATE", "EMAIL", "PHONE"],
    },
    "language_detection": {
        "enabled": True,
        "confidence_threshold": 0.8,
    },
    "text_processing": {
        "remove_stopwords": True,
        "stemming": True,
        "max_length": 5000,
    }
}

# ============================================
# CONFIGURACIÓN DE AUDITORÍA
# ============================================

AUDIT_CONFIG = {
    "check_dns": True,
    "check_whois": True,
    "check_subdomains": True,
    "check_ssl": True,
    "check_headers": True,
    "check_cookies": True,
    "check_shodan": True,
    "check_censys": False,
    "check_vulnerabilities": True,
    "scan_ports": {
        "enabled": False,
        "ports": [21, 22, 23, 25, 53, 80, 443, 3306, 3389, 8080, 8443],
        "timeout": 2,
    },
    "deep_scan": False,
}

# ============================================
# CONFIGURACIÓN DE LOGGING
# ============================================

LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "date_format": "%Y-%m-%d %H:%M:%S",
    "file": LOGS_DIR / "osint_tool.log",
    "max_size": 10 * 1024 * 1024,
    "backup_count": 5,
    "console": True,
}

# ============================================
# FUNCIÓN PARA VALIDAR CONFIGURACIÓN (silenciosa)
# ============================================

def validate_config():
    """Valida la configuración sin mostrar mensajes"""
    issues = []
    
    # Verificar API keys importantes
    if not API_KEYS["SHODAN"]:
        issues.append("SHODAN API key no configurada")
    
    if not API_KEYS["VIRUSTOTAL"]:
        issues.append("VIRUSTOTAL API key no configurada")
    
    return issues

# ============================================
# FUNCIÓN PARA OBTENER CONFIGURACIÓN
# ============================================

def get_api_key(service_name):
    """Obtiene una API key de forma segura"""
    return API_KEYS.get(service_name, "")

def is_service_enabled(service_name):
    """Verifica si un servicio está habilitado"""
    return SOCIAL_MEDIA.get(service_name, {}).get("enabled", False)
