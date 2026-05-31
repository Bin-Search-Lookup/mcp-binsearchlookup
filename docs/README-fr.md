**Select Language:**
[English](../README.md) | [Français](README-fr.md) | [Español](README-es.md) | [Deutsch](README-de.md) | [Italiano](README-it.md) | [Português](README-pt.md) | [Русский](README-ru.md) | [中文](README-zh.md) | [日本語](README-ja.md) | [한국어](README-ko.md) | [العربية](README-ar.md)

---

# Serveur MCP BinSearchLookup

Le serveur officiel Model Context Protocol (MCP) pour [BinSearchLookup.com](https://www.binsearchlookup.com/).

Ce serveur permet aux agents IA (comme Claude Desktop, Cursor et les LLM personnalisés) de s'interfacer de manière transparente et sécurisée avec l'API BinSearchLookup pour effectuer des recherches avancées de numéros d'identification bancaire (BIN), des analyses de fraude et des audits de cartes en masse.

## Fonctionnalités d'Entreprise

- **Diagnostics Locaux Hors Ligne & Vérifications Préalables:** Identifie les réseaux (Visa, Mastercard, Amex, etc.) et effectue des vérifications locales de l'algorithme de Luhn sur des PAN complets de 16 chiffres. Les numéros invalides sont bloqués avant d'atteindre l'API, protégeant ainsi votre quota et sécurisant les PAN complets.
- **Découpage Automatique & Concurrence:** Soumettez des milliers de BIN à la fois. Le serveur déduplique automatiquement, les regroupe par lots de 50 et les traite simultanément tout en respectant les limites de débit.
- **Mise en cache LRU en mémoire:** Les requêtes IA dupliquées au sein d'une même session sont servies instantanément depuis la mémoire, économisant vos crédits API.
- **Désinfection Stricte des Entrées:** Supprime automatiquement les tirets, lettres et espaces des entrées LLM désordonnées.
- **Résilience:** Le backoff exponentiel intégré utilisant `tenacity` gère élégamment les interruptions de réseau et les erreurs `429 Rate Limit`.
- **Déploiement Sans Installation:** S'exécute entièrement dans un conteneur Docker léger.

## Installation & Utilisation

Vous pouvez exécuter ce serveur MCP de deux manières : via Docker (Recommandé) ou localement via Python.

### Option 1: Docker (Recommandé - Zéro Installation)

```json
{
  "mcpServers": {
    "binsearchlookup": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "BSL_API_KEY=bsl_votre_cle_api_ici",
        "-e", "BSL_USER_ID=votre_id_utilisateur_ici",
        "python:3.12-slim",
        "sh", "-c", "pip install mcp httpx pydantic tenacity python-dotenv cachetools -q && curl -s https://raw.githubusercontent.com/Bin-Search-Lookup/mcp-binsearchlookup/main/mcp_server.py | python -u"
      ]
    }
  }
}
```

### Option 2: Python Local

1. **Installer les prérequis:**
   `pip install httpx pydantic tenacity python-dotenv mcp cachetools`
2. **Configurer votre fichier `.env`:**
   Créez un fichier `.env` dans le même dossier que `mcp_server.py`:
   `BSL_API_KEY=bsl_votre_cle_api_ici`
   `BSL_USER_ID=votre_uuid_ici`
3. **Ajouter à votre configuration client MCP:**
   `"command": "python3", "args": ["/chemin/absolu/vers/mcp_server.py"]`

## Outils MCP Disponibles

- `local_card_diagnostics(number: str)`: Outil GRATUIT hors ligne pour identifier les réseaux et valider le Luhn.
- `lookup_bin(bin_number: str)`: Récupère les informations détaillées pour un seul BIN.
- `batch_lookup_bins(bins: List[str])`: Traite plusieurs recherches de BIN en une seule fois.
- `check_quota(public_user_id: str)`: Vérifie l'utilisation actuelle et les limites de l'API.
- `check_system_health()`: Outil de diagnostic pour vérifier l'état de l'API.

## Prompts IA Préconfigurés

- **`fraud_analysis`**: Demande au LLM d'exécuter d'abord un diagnostic hors ligne, d'extraire le BIN sécurisé, puis de générer une évaluation des risques.
- **`bulk_bin_audit`**: Exécute un audit en masse à partir d'une liste séparée par des virgules et génère un tableau markdown.

## Tarification & Limites

| Plan | Prix (Mensuel / Annuel) | Limite | Quota Mensuel | Clés API |
|---|---|---|---|---|
| **Free** | $0 | 20 req/min | 500 requêtes | 1 |
| **Starter** | $29 / $25 | 60 req/min | 10,000 requêtes | 3 |
| **Pro** | $199 / $175 | 280 req/min | 78,000 requêtes | 15 |
| **Enterprise** | $999 / $980 | 768 req/min | Requêtes illimitées | 190 |


---
*Built for the Model Context Protocol.*