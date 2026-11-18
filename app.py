import os
import unicodedata

import gradio as gr
from groq import Groq


groq_key = os.getenv("GROQ_API_KEY")
if groq_key:
    groq_key = groq_key.strip().strip("'\"`")
client = Groq(api_key=groq_key) if groq_key else None


def encoder_texte_ascii(message: str) -> str:
    texte_normalise = unicodedata.normalize("NFKD", message)
    return texte_normalise.encode("ascii", "ignore").decode("ascii")


def repondre(message: str) -> str:
    if not groq_key:
        return "GROQ_API_KEY n'est pas définie dans le terminal."

    if not message.strip():
        return "Veuillez saisir un message RFP."

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
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


demo = gr.Interface(
    fn=repondre,
    inputs=gr.Textbox(label="Message RFP"),
    outputs=gr.Textbox(label="Réponse"),
    title="RFP Copilot",
)


if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
