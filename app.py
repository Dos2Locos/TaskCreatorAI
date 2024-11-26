import os
import json
from openai import OpenAI

from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from Task import Task
from datetime import datetime
from textwrap import dedent


# Load environment variables
load_dotenv()

# Configure OpenAI API
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
model = os.getenv('OPENAI_MODEL')

system_prompt = """
Eres un modelo de lenguaje especializado en convertir descripciones de tareas en JSON estructurados. Sigue estas reglas para cada tarea o nota:

1. **`title`**: Extrae el título principal. Obligatorio.
2. **`description`**: Incluye detalles adicionales o usa `""` si no hay.
3. **`is_completed`**: Por defecto `false`, salvo que se indique lo contrario.
4. **Fechas**:
   - **`due_date`**: Obligatorio si se menciona una fecha o recurrencia. Usa formato `YYYY-MM-DDTHH:MM:SSZ`. Ajusta horas según términos como:
     - "Por la mañana" → `09:00:00`.
     - "Por la noche" → `20:00:00`.
   - **`start_date`**, **`end_date`**: Solo si hay un rango de fechas.
5. **`assigned_to`**: Solo si se menciona a alguien.
6. **`subject`**: Solo si se menciona un sujeto relacionado.
7. **`location`**: Solo si se indica una ubicación.
8. **Recurrencia**:
   - **`is_recurring`**: `true` si es recurrente; incluye detalles en `recurrence` con:
     - `frequency`, `interval`, `days_of_week`, y `nth_weekday_of_month` (si aplica).
   - Si no es recurrente, usa `false` y omite `recurrence`.
9. **`emoji_icon`**: Obligatorio. Incluye un emoji representativo.

**Nota**: No incluyas campos sin valor. Siempre rellena `due_date` si hay una fecha mencionada. Sigue detenidamente las instrucciones anteriores y usa el formato correcto.
"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform_task():
    # Get the task description from the request
    task_description = request.json.get('task', '')

    if not task_description:
        return jsonify({"error": "No task description provided"}), 400

    # Add the current date and time to the system prompt
    current_system_prompt = f"{system_prompt}\nLa fecha y hora actual es {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    messages = [
        {
            "role": "system",
            "content": dedent(current_system_prompt)
        },
        {
            "role": "user",
            "content": task_description
        }
    ]

    try:
        # Call the OpenAI API
        completion = client.beta.chat.completions.parse(model=model,
        messages=messages,
        response_format=Task)

        event_response = completion.choices[0].message.parsed

        return jsonify(event_response.dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
