import streamlit as st
import plotly.graph_objects as go
import time
from streamlit_lottie import st_lottie

def evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage):
    """
    Calcule le score d'exposition d'un métier à l'IA en fonction des critères donnés.
    """
    score = (task_automation * 3) + (data_usage * 2) - (creativity * 2) - (human_interaction * 3) - (critical_thinking * 3)
    
    if score > 8:
        return "Forte exposition : Votre métier est très exposé à l'IA. Une adaptation rapide est recommandée.", score
    elif score > 4:
        return "Moyenne exposition : Certaines tâches seront automatisées, mais la dimension humaine reste clé.", score
    else:
        return "Faible exposition : Votre métier repose sur des compétences difficilement remplaçables par l'IA.", score

def plot_radar_chart(scores):
    labels = ["Automatisation", "Créativité", "Interaction humaine", "Pensée critique", "Utilisation de données"]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],
        theta=labels + [labels[0]],
        fill='toself',
        line=dict(color='blue', width=2),
        name='Score'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# Configuration de l'interface
st.set_page_config(page_title="Impact IA", layout="wide")
st.title("🔍 Diagnostic interactif de l'impact de l'IA sur votre métier")

# Animation d'introduction
# Fonction pour charger une animation Lottie locale
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Charger l’animation localement
import os

def load_lottie_file():
    filepath = os.path.join(os.path.dirname(__file__), "animation.json")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

import os
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Fonction pour charger une animation Lottie locale
def load_lottie_file():
    dir_path = os.path.dirname(os.path.abspath(__file__))  # Récupère le bon chemin
    filepath = os.path.join(dir_path, "animation.json")  # Assure que le fichier est trouvé
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Charger l’animation
try:
    lottie_animation = load_lottie_file()
    st_lottie(lottie_animation, speed=1, width=600, height=300, key="intro_animation")
except FileNotFoundError:
    st.error("Erreur : Le fichier `animation.json` est introuvable. Vérifiez qu'il est bien uploadé sur GitHub.")
# Afficher l'animation
st.write("Découvrez à quel point votre métier est exposé à l'automatisation par l'IA.")

st.subheader("📊 Répondez aux questions pour voir l'impact en temps réel")

# Création des sliders avec mise à jour en temps réel
task_automation = st.slider("Automatisation des tâches (ex : saisie de données, traitement comptable)", 0, 10, 5)
creativity = st.slider("Créativité et innovation (ex : conception artistique, résolution de problèmes)", 0, 10, 5)
human_interaction = st.slider("Interaction humaine (ex : service client, éducation, thérapie)", 0, 10, 5)
critical_thinking = st.slider("Pensée critique et analyse (ex : décisions stratégiques, recherche)", 0, 10, 5)
data_usage = st.slider("Utilisation de données (ex : analyse de tendances, reporting)", 0, 10, 5)

# Mise à jour du diagnostic en temps réel
st.subheader("📌 Votre diagnostic en direct")

# Barre de progression dynamique
progress_bar = st.progress(0)
for percent_complete in range(0, 101, 20):
    time.sleep(0.1)
    progress_bar.progress(percent_complete)

# Affichage du résultat instantané
result, score = evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage)
st.success(result)

# Affichage du graphique radar interactif mis à jour en direct
plot_radar_chart([task_automation, creativity, human_interaction, critical_thinking, data_usage])

st.write("Ajustez les curseurs pour voir comment l'IA impacte votre métier.")
