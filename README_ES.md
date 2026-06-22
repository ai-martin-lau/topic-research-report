<p align="center">
  <a href="README.md">简体中文</a> · <a href="README_EN.md">English</a> · <a href="README_JA.md">日本語</a> · <a href="README_KO.md">한국어</a> · <a href="README_ES.md">Español</a>
</p>

<p align="center">
  <img src="assets/cover.png" alt="Topic Research Report Skill" width="100%">
</p>

# Topic Research Report

> Introduce un solo tema. El skill investiga en línea por defecto y genera dos informes de investigación sin sabor genérico de IA: uno en chino y otro en inglés.
>
> One topic in, two evidence-based bilingual research reports out.

Este es un Skill para Claude Code / Codex. Hace una sola cosa: convertir un tema en un informe de investigación completo, listo para que otros sistemas lo transformen después en diapositivas, videos o contenido distribuible.

No genera guiones de voz, storyboards, estructuras de diapositivas, publicaciones sociales ni resúmenes de resultados de búsqueda. Los sistemas posteriores pueden adaptar el informe. Este skill se concentra en la investigación.

## Qué resuelve

Muchos "informes de investigación" parecen una mezcla de resultados de búsqueda, o un texto donde la IA explica cómo está escribiendo. Este skill fija varias reglas:

- **Investigación web por defecto**: salvo que el usuario pida trabajo offline o solo con fuentes dadas, el agente debe revisar fuentes reales primero.
- **Verificación de estado actual en temas sensibles al tiempo**: IPOs, salidas a bolsa, lanzamientos, financiación, cambios de política y productos no deben quedarse en lenguaje de anuncios antiguos.
- **Bilingüe sin traducción rígida**: los informes en chino e inglés comparten los mismos hechos, pero cada uno suena natural en su idioma.
- **Sin sabor de IA**: evita aperturas vagas, cierres mecánicos, tono de atención al cliente, lenguaje promocional y frases de validación interna.
- **Script de validación incluido**: revisa estructura, cantidad de fuentes, lenguaje prospectivo vencido, señales de escritura de IA y contenido de producción que no corresponde.

## Salida

Directorio de salida por defecto:

```text
skill output/topic-research-report/<timestamp>-<topic>/
├── 调研报告-中文.md
└── research-report-en.md
```

La estructura del informe incluye:

- Contexto y problema
- Hechos clave
- Línea de tiempo o mecanismo
- Análisis profundo
- Disputas e incertidumbres
- Implicaciones y puntos a observar
- Límites de evidencia
- Fuentes

## Inicio rápido

Crea el paquete de salida:

```bash
python3 scripts/create_topic_package.py "SpaceX IPO" --base "skill output/topic-research-report"
```

Después de investigar y completar ambos informes, valida la salida:

```bash
python3 scripts/check_topic_outputs.py "skill output/topic-research-report/<timestamp>-<topic>"
```

## Archivos

| Ruta | Función |
|---|---|
| `SKILL.md` | Instrucciones principales que lee primero el agente |
| `references/topic-research-framework.md` | Marco de investigación y reglas de fuentes |
| `references/human-writing-rules.md` | Reglas generales para quitar escritura con sabor de IA |
| `references/report-template.md` | Plantilla de informe bilingüe |
| `scripts/create_topic_package.py` | Crea el directorio de salida y los archivos de informe |
| `scripts/check_topic_outputs.py` | Valida la salida final |

## Para quién es

- Personas que necesitan buen material de investigación antes de crear diapositivas, videos o contenido
- Equipos que quieren que los sistemas posteriores adapten un informe, no que inventen la investigación
- Usuarios que no quieren resúmenes de búsqueda, ensayos con tono de IA o paquetes de material suelto
- Cualquiera que trabaje con temas sensibles al tiempo, como salidas a bolsa, políticas, lanzamientos de productos y cambios de industria

## Instalación

Colócalo en el directorio de skills de Claude Code:

```bash
~/.claude/skills/topic-research-report
```

O en el directorio de skills de Codex:

```bash
~/.codex/skills/topic-research-report
```

## License

MIT

## Historial de estrellas

[![Star History Chart](https://api.star-history.com/svg?repos=ai-martin-lau/topic-research-report&type=Date)](https://star-history.com/#ai-martin-lau/topic-research-report&Date)
