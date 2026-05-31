# Serveur MCP BinSearchLookup

**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

Le serveur officiel Model Context Protocol (MCP) pour [BinSearchLookup.com](https://www.binsearchlookup.com/). Ce serveur permet aux agents IA (comme Claude Desktop, Cursor et les LLM personnalisés) de s'interfacer de manière transparente et sécurisée avec l'API BinSearchLookup pour effectuer des recherches avancées de numéros d'identification bancaire (BIN), des analyses de fraude et des audits de cartes en masse.

## Fonctionnalités d'Entreprise
- **Diagnostics locaux hors ligne :** Identifie les réseaux et effectue des vérifications locales de l'algorithme de Luhn sur les PAN complets de 16 chiffres.
- **Découpage automatique et concurrence :** Soumettez des milliers de BIN à la fois.
- **Mise en cache LRU en mémoire :** Sauvegarde vos crédits API.
- **Désinfection stricte des entrées :** Supprime les tirets, lettres et espaces.
- **Résilience :** Backoff exponentiel intégré.
- **Déploiement sans installation :** Exécutez via un conteneur Docker.

For installation instructions, API tools, pricing, and configuration, please see the [English README](../README.md).