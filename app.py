import os
import unicodedata

import gradio as gr
from groq import Groq

try:
    import spaces
except ImportError:
    spaces = None


groq_key = os.getenv("GROQ_API_KEY")
if groq_key:
    groq_key = groq_key.strip().strip("'\"`")
client = Groq(api_key=groq_key) if groq_key else None


def encoder_texte_ascii(message: str) -> str:
    texte_normalise = unicodedata.normalize("NFKD", message)
    return texte_normalise.encode("ascii", "ignore").decode("ascii")


def obtenir_modele_disponible() -> str:
    modeles = client.models.list()
    identifiants = [modele.id for modele in modeles.data]

    preferences = [
        "openai/gpt-oss-20b",
        "openai/gpt-oss-120b",
        "qwen/qwen3-32b",
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
    ]
    for preference in preferences:
        if preference in identifiants:
            return preference

    for identifiant in identifiants:
        if "whisper" not in identifiant.lower() and "guard" not in identifiant.lower():
            return identifiant

    raise RuntimeError("Aucun modele de chat n'est disponible pour cette cle Groq.")


def repondre(message: str) -> str:
    if not groq_key:
        return "GROQ_API_KEY n'est pas définie dans le terminal."

    if not message.strip():
        return "Veuillez saisir un message RFP."

    try:
        completion = client.chat.completions.create(
            model=obtenir_modele_disponible(),
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant specialized in analyzing Request for Proposal documents.",
                },
                {"role": "user", "content": encoder_texte_ascii(message)},
            ],
            temperature=0.2,
        )
        return completion.choices[0].message.content
    except Exception as error:
        error_name = type(error).__name__
        return f"Erreur Groq ({error_name}) : {error}"


if spaces is not None and hasattr(spaces, "CPU"):
    repondre = spaces.CPU()(repondre)


demo = gr.Interface(
    fn=repondre,
    inputs=gr.Textbox(label="Message RFP"),
    outputs=gr.Textbox(label="Réponse"),
    title="RFP Copilot",
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
