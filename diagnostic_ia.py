import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage):
    """
    Fonction qui évalue l'exposition d'un métier à l'IA en fonction des critères donnés.
    """
    score = (task_automation * 3) + (data_usage * 2) - (creativity * 2) - (human_interaction * 3) - (critical_thinking * 3)
    
    if score > 8:
        return "🌐 Forte exposition : Votre métier est très exposé à l'IA. Une adaptation rapide est recommandée.", score
    elif score > 4:
        return "📊 Moyenne exposition : Certaines tâches seront automatisées, mais la dimension humaine reste clé.", score
    else:
        return "🛠️ Faible exposition : Votre métier repose sur des compétences difficilement remplaçables par l'IA.", score

def plot_chart(scores):
    labels = ["Automatisation des tâches", "Créativité", "Interaction humaine", "Pensée critique", "Utilisation de données"]
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    scores += scores[:1]  # Boucler le graphique
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"projection": "polar"})
    ax.fill(angles, scores, color='blue', alpha=0.25)
    ax.plot(angles, scores, color='blue', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    st.pyplot(fig)

# Interface utilisateur avec Streamlit
st.title("🔍 Diagnostic d'impact de l'IA sur votre métier")

st.write("Répondez aux questions suivantes pour estimer à quel point votre métier est exposé à l'IA.")

st.subheader("Critères d'évaluation")

task_automation = st.slider("Automatisation des tâches : répétitivité, règles claires, structuration des données", 0, 10, 5)
task_automation_ex1 = st.text_input("Exemple 1 (Automatisation des tâches)")
task_automation_ex2 = st.text_input("Exemple 2 (Automatisation des tâches)")

creativity = st.slider("Créativité et innovation : originalité, prise de décisions non standardisées", 0, 10, 5)
creativity_ex1 = st.text_input("Exemple 1 (Créativité)")
creativity_ex2 = st.text_input("Exemple 2 (Créativité)")

human_interaction = st.slider("Interaction humaine : nécessité d’une présence physique, d’empathie ou de relations sociales", 0, 10, 5)
human_interaction_ex1 = st.text_input("Exemple 1 (Interaction humaine)")
human_interaction_ex2 = st.text_input("Exemple 2 (Interaction humaine)")

critical_thinking = st.slider("Analyse et pensée critique : résolution de problèmes complexes, jugement humain nécessaire", 0, 10, 5)
critical_thinking_ex1 = st.text_input("Exemple 1 (Pensée critique)")
critical_thinking_ex2 = st.text_input("Exemple 2 (Pensée critique)")

data_usage = st.slider("Utilisation de données : dépendance aux algorithmes et au traitement de grandes quantités d’informations", 0, 10, 5)
data_usage_ex1 = st.text_input("Exemple 1 (Utilisation de données)")
data_usage_ex2 = st.text_input("Exemple 2 (Utilisation de données)")

if st.button("🔎 Diagnostiquer"):
    result, score = evaluate_impact(task_automation, creativity, human_interaction, critical_thinking, data_usage)
    st.subheader("Résultat :")
    st.write(result)
    
    # Afficher les exemples fournis
    st.subheader("Vos exemples")
    st.write(f"**Automatisation des tâches** : {task_automation_ex1}, {task_automation_ex2}")
    st.write(f"**Créativité** : {creativity_ex1}, {creativity_ex2}")
    st.write(f"**Interaction humaine** : {human_interaction_ex1}, {human_interaction_ex2}")
    st.write(f"**Pensée critique** : {critical_thinking_ex1}, {critical_thinking_ex2}")
    st.write(f"**Utilisation de données** : {data_usage_ex1}, {data_usage_ex2}")
    
    # Afficher un graphique radar
    plot_chart([task_automation, creativity, human_interaction, critical_thinking, data_usage])
