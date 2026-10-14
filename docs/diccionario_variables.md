# Diccionario de Variables — Base de Datos Dengue Bucaramanga (SIVIGILA)

**Fuente:** Sistema Nacional de Vigilancia en Salud Pública (SIVIGILA) — INS Colombia  
**Período:** 2015–2023 | **Municipio:** Bucaramanga, Santander

---

## Variables de identificación

| Variable | Descripción | Tipo | Valores |
|----------|-------------|------|---------|
| `ORDEN` | Número de registro único | Entero | ID único |
| `COD_EVE` | Código del evento SIVIGILA | Entero | 210=dengue, 220=grave, 580=mortalidad |
| `NOM_EVE` | Nombre del evento | Texto | — |
| `VERSION` | Versión del formulario | Entero | — |

## Variables temporales

| Variable | Descripción | Tipo | Valores |
|----------|-------------|------|---------|
| `FEC_NOT` | Fecha de notificación | Fecha (string) | YYYY-MM-DD |
| `SEMANA` | Semana epidemiológica | Entero | 1–53 |
| `AÑO` | Año epidemiológico | Entero | 2015–2023 |
| `FEC_CON_` | Fecha de consulta | Fecha (string) | — |
| `INI_SIN_` | Fecha de inicio de síntomas | Fecha (string) | — |
| `FEC_HOS_` | Fecha de hospitalización | Fecha (string) | NaN si no hospitalizado |
| `FEC_DEF_` | Fecha de defunción | Fecha (string) | 1900-01-01 = sin defunción (centinela) |

## Variables demográficas y socioeconómicas

| Variable | Descripción | Tipo | Valores |
|----------|-------------|------|---------|
| `SEXO_` | Sexo del paciente | Categórica | 1=Masculino, 2=Femenino |
| `GRUPO_ETARIO` | Grupo etario SIVIGILA | Categórica | — |
| `DEF_CLAS_EDAD` | Clasificación etaria definida | Categórica | — |
| `OCUPACION_` | Ocupación | Categórica | Códigos INS |
| `TIP_SS_` | Tipo de seguridad social | Categórica | 1=Contributivo, 2=Subsidiado, 3=Vinculado, 4=Excepción, 5=Especial, 6=No asegurado |
| `ESTRATO_` | Estrato socioeconómico | Ordinal | 1–6 |
| `PER_ETN_` | Pertenencia étnica | Categórica | Códigos INS |

## Variables de grupos poblacionales especiales

| Variable | Descripción | Valores |
|----------|-------------|---------|
| `GP_DISCAPA` | Discapacidad | 1=Sí, 2=No |
| `GP_DESPLAZ` | Desplazado | 1=Sí, 2=No |
| `GP_MIGRANT` | Migrante | 1=Sí, 2=No |
| `GP_GESTAN` | Gestante | 1=Sí, 2=No |
| `GP_INDIGEN` | Indígena | 1=Sí, 2=No |
| `GP_VIC_VIO` | Víctima de violencia | 1=Sí, 2=No |

## Síntomas generales (fase febril del dengue)

> Codificación SIVIGILA: **1 = Sí (presente)**, **2 = No (ausente)**

| Variable | Descripción clínica |
|----------|---------------------|
| `FIEBRE` | Fiebre (T° > 38°C). Presente en >95% de casos. Altamente colineal con otros síntomas (VIF ~8). |
| `CEFALEA` | Cefalea intensa. Uno de los síntomas más reportados. |
| `DOLRRETROO` | Dolor retroocular (retro-orbital). Característico del dengue clásico. |
| `MALGIAS` | Mialgias (dolores musculares). Contribuye al síndrome "rompe-huesos". |
| `ARTRALGIA` | Artralgias (dolores articulares). |
| `ERUPCIONR` | Erupción cutánea (rash). Aparece tardíamente en la fase febril. |

## Signos de alarma (criterios OMS 2009 / INS Colombia)

> Los signos de alarma predicen progresión hacia dengue grave.  
> Codificación: **1 = Sí (presente)**, **2 = No (ausente)**

| Variable | Signo de alarma OMS | Relevancia clínica |
|----------|--------------------|---------------------|
| `DOLOR_ABDO` | Dolor abdominal intenso y continuo | Alto OR ajustado con hospitalización (~2.5) |
| `VOMITO` | Vómito persistente (≥3 episodios/día) | Indicador de pérdida de fluidos |
| `DIARREA` | Diarrea | Contribuye a desequilibrio hidroelectrolítico |
| `SOMNOLENCI` | Somnolencia / irritabilidad | Indicador neurológico de compromiso sistémico |
| `HIPOTENSIO` | Hipotensión postural | Signo de choque compensado |
| `HEPATOMEG` | Hepatomegalia (hígado palpable >2cm) | Compromiso hepático |
| `HEM_MUCOSA` | Hemorragia de mucosas | Alto OR ajustado (~2.3–2.4) |
| `HIPOTERMIA` | Hipotermia | Signo de choque descompensado |
| `AUM_HEMATO` | Aumento del hematocrito | Indicador de hemoconcentración (extravasación de plasma) |
| `CAIDA_PLAQ` | Caída rápida de plaquetas | Mayor OR ajustado en todos los modelos (~2.7–5.8) |
| `ACUM_LIQUI` | Acumulación de líquidos (ascitis, derrame) | Indicador de fuga capilar |

## Variables de dengue grave

| Variable | Descripción |
|----------|-------------|
| `EXTRAVASAC` | Extravasación grave de plasma |
| `HEMORR_HEM` | Hemorragia grave |
| `CHOQUE` | Choque por dengue |
| `DAÑO_ORGAN` | Daño grave de órganos |

## Variables de desenlace

| Variable | Descripción | Valores |
|----------|-------------|---------|
| `PAC_HOS_` | ¿El paciente fue hospitalizado? | 1=Sí, 2=No |
| `FEC_HOS_` | Fecha de hospitalización | NaN si no hospitalizado |
| `CON_FIN_` | Condición final | Vivo, Muerto |
| `CONDUCTA` | Conducta médica adoptada | Hospitalización piso, UCI, Ambulatorio, etc. |
| `CLASFINAL` | Clasificación final del dengue | DENGUE SIN SIGNOS, CON SIGNOS, GRAVE, MORTALIDAD |
| `TARGET_HOSPITALIZACION_ORIGINAL` | Variable objetivo binaria (construida) | 1=Hospitalizado, 0=No hospitalizado |

---

## Notas de calidad de datos

1. **Valor centinela 1900-01-01:** En `FEC_DEF_` indica ausencia de defunción (no una fecha real).
2. **Período 2017–2020:** Ruptura estructural en la distribución de `CLASFINAL`. Evaluar sensibilidad.
3. **CLASFINAL vs COD_EVE:** Algunos registros con `COD_EVE=580` (mortalidad) no estaban clasificados en `CLASFINAL`. Corregidos en notebook 01.
4. **Inconsistencias PAC_HOS_:** 2 registros con `PAC_HOS_=2` (no hospitalizado) pero con fecha de hospitalización y conducta intrahospitalaria. Corregidos a 1.
