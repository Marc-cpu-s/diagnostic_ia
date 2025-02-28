import streamlit as st

def evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage):
    """
    Fonction qui évalue l'exposition d'un métier à l'IA en fonction des critères donnés.
    """
    score = (task_automation * 3) + (data_usage * 2) - (creativity * 2) - (human_interaction * 3) - (critical_thinking * 3)
    
    if score > 8:
        return "🌐 Forte exposition : Votre métier est très exposé à l'IA. Une adaptation rapide est recommandée."
    elif score > 4:
        return "📊 Moyenne exposition : Certaines tâches seront automatisées, mais la dimension humaine reste clé."
    else:
        return "🛠️ Faible exposition : Votre métier repose sur des compétences difficilement remplaçables par l'IA."

# Interface utilisateur avec Streamlit
st.title("🔍 Diagnostic d'impact de l'IA sur votre métier")

st.write("Répondez aux questions suivantes pour estimer à quel point votre métier est exposé à l'IA.")

st.subheader("Critères d'évaluation")

task_automation = st.slider("Automatisation des tâches : répétitivité, règles claires, structuration des données", 0, 10, 5)
creativity = st.slider("Créativité et innovation : originalité, prise de décisions non standardisées", 0, 10, 5)
human_interaction = st.slider("Interaction humaine : nécessité d’une présence physique, d’empathie ou de relations sociales", 0, 10, 5)
critical_thinking = st.slider("Analyse et pensée critique : résolution de problèmes complexes, jugement humain nécessaire", 0, 10, 5)
data_usage = st.slider("Utilisation de données : dépendance aux algorithmes et au traitement de grandes quantités d’informations", 0, 10, 5)

if st.button("🔎 Diagnostiquer"):
    result = evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage)
    st.subheader("Résultat :")
    st.write(result)
