#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import whois
import dns.resolver
import ssl
import socket
from datetime import datetime
from utils.search_engines import buscar_en_shodan
from config.settings import AUDIT_CONFIG, API_KEYS

def auditar_privacidad(dominio):
    """Audita la privacidad y seguridad de un dominio/empresa"""
    print(f"\n🔒 Auditando privacidad de: {dominio}")
    print("=" * 60)
    
    resultados = {
        "dominio": dominio,
        "fecha": datetime.now().isoformat(),
        "whois": {},
        "dns": {},
        "ssl": {},
        "subdominios": [],
        "vulnerabilidades": []
    }
    
    # 1. WHOIS
    if AUDIT_CONFIG["check_whois"]:
        print("\n📋 WHOIS:")
        try:
            w = whois.whois(dominio)
            resultados["whois"] = {
                "registrante": w.name if w.name else "Privacidad activada",
                "email": w.email if w.email else "Privacidad activada",
                "creacion": w.creation_date,
                "expiracion": w.expiration_date,
                "servidor": w.whois_server
            }
            print(f"   📛 Registrante: {resultados['whois']['registrante']}")
            print(f"   ✉️  Email: {resultados['whois']['email']}")
            print(f"   📅 Creación: {resultados['whois']['creacion']}")
            print(f"   ⏰ Expiración: {resultados['whois']['expiracion']}")
        except Exception as e:
            print(f"   ⚠️  Error obteniendo WHOIS: {str(e)}")
    
    # 2. DNS y subdominios
    if AUDIT_CONFIG["check_subdomains"]:
        print("\n🌐 SUBDOMINIOS DETECTADOS:")
        subdominios_comunes = [
            "www", "mail", "ftp", "admin", "dev", "api", 
            "test", "blog", "shop", "secure", "portal",
            "webmail", "cpanel", "whm", "mysql", "db"
        ]
        
        for sub in subdominios_comunes:
            try:
                dns.resolver.resolve(f"{sub}.{dominio}", "A")
                print(f"   ✅ {sub}.{dominio}")
                resultados["subdominios"].append(f"{sub}.{dominio}")
            except:
                pass
    
    # 3. SSL/TLS
    if AUDIT_CONFIG["check_ssl"]:
        print("\n🔐 SSL/TLS:")
        try:
            ctx = ssl.create_default_context()
            with ctx.wrap_socket(socket.socket(), server_hostname=dominio) as s:
                s.connect((dominio, 443))
                cert = s.getpeercert()
                print(f"   ✅ Certificado válido")
                print(f"   📅 Emitido para: {cert.get('subject', [])[0][0][1] if cert.get('subject') else 'Desconocido'}")
                print(f"   ⏰ Expira: {cert.get('notAfter', 'No disponible')}")
        except Exception as e:
            print(f"   ❌ Error SSL: {str(e)}")
    
    # 4. Shodan (si API key disponible)
    if AUDIT_CONFIG["check_shodan"] and API_KEYS.get("SHODAN"):
        print("\n🛡️  SHODAN:")
        try:
            resultados_shodan = buscar_en_shodan(dominio)
            if resultados_shodan:
                print(f"   🔓 {len(resultados_shodan)} servicios expuestos encontrados:")
                for servicio in resultados_shodan[:3]:
                    print(f"      - Puerto {servicio.get('port')}: {servicio.get('service')}")
                    if servicio.get('vulns'):
                        print(f"        ⚠️  Vulnerabilidades: {len(servicio['vulns'])}")
                        resultados["vulnerabilidades"].extend(servicio['vulns'])
            else:
                print("   ✅ No se encontraron servicios expuestos")
        except Exception as e:
            print(f"   ⚠️  Error en Shodan: {str(e)}")
    
    # Resumen
    print("\n" + "="*60)
    print("📊 RESUMEN DE AUDITORÍA:")
    print(f"   - Subdominios encontrados: {len(resultados['subdominios'])}")
    print(f"   - Vulnerabilidades: {len(resultados['vulnerabilidades'])}")
    if resultados["vulnerabilidades"]:
        print("   ⚠️  SE RECOMIENDA REVISIÓN DE SEGURIDAD")
    else:
        print("   ✅ SIN VULNERABILIDADES CRÍTICAS DETECTADAS")
    
    return resultados
