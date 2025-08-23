import streamlit as st

# ================================
# CONFIGURATION DE L'APPLICATION
# ================================
st.set_page_config(page_title="Espagnol B1 - Apprentissage", page_icon="🇪🇸", layout="centered")

st.title("🇪🇸 Apprendre l'espagnol - Niveau B1")
st.write("Exercice interactif avec vérification, traduction et prononciation.")

# Exemple de dialogue avec trou à remplir
dialogue = {
    "texte": "Hola, ¿cómo ____?",
    "solution": "estás",
    "traduction": "Bonjour, comment vas-tu ?"
}

# ================================
# 📝 Exercice à trous
# ================================
st.subheader("📝 Exercice à trous")
st.write(dialogue["texte"])
reponse = st.text_input("Tape ta réponse ici...")

if st.button("Vérifier"):
    if reponse.strip().lower() == dialogue["solution"].lower():
        st.success("✅ Bravo, c’est correct !")
    else:
        st.error(f"❌ Incorrect. La bonne réponse était : {dialogue['solution']}")

if st.button("Révéler la réponse"):
    st.info(f"La réponse est : {dialogue['solution']}")

# ================================
# 🎧 Leçon audio
# ================================
st.subheader("🎧 Écoute la phrase")
# Pour un vrai TTS, on pourra utiliser gTTS ou une API
st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav")

if st.checkbox("Afficher la traduction française"):
    st.write(f"👉 {dialogue['traduction']}")

# ================================
# 🎤 Prononciation
# ================================
st.subheader("🎤 Pratique la prononciation")
audio_file = st.file_uploader("Enregistre ta voix en espagnol", type=["wav", "mp3"])
if audio_file:
    st.audio(audio_file, format="audio/wav")
    st.info("🔎 (Étape suivante : ajouter une comparaison automatique avec la solution)")
