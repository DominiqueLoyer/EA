import os

import gradio as gr
from groq import Groq


groq_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_key) if groq_key else None


def repondre(message: str) -> str:
    if not groq_key:
        return "GROQ_API_KEY n'est pas définie dans le terminal."

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Vous êtes un assistant spécialisé dans l'analyse de demandes de propositions (RFP).",
            },
            {"role": "user", "content": message},
        ],
        temperature=0.2,
    )
    return completion.choices[0].message.content


demo = gr.Interface(
    fn=repondre,
    inputs=gr.Textbox(label="Message RFP"),
    outputs=gr.Textbox(label="Réponse"),
    title="RFP Copilot",
)


if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860)
