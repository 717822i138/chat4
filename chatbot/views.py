from django.shortcuts import render
from django.http import JsonResponse
from google import genai
from google.genai import types
import json

def index(request):
    return render(request, 'index.html')

def chat_response(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # 1. உங்க Gemini API Key-ஐ இங்க குடுங்க தம்பி
        client = genai.Client(api_key='AIzaSyAnekwlDRAq4NoCqT1eH_jAn964TbaAOIM')

        try:
            # 2. AI-க்கு குடுக்குற கண்டிஷன் (Prompt Engineering)
            # இதுதான் அந்த AI-ஐ என்ன மாதிரி பேச வைக்கும்!
            system_instruction = (
                "You are an AI chatbot. You must behave exactly like a friendly, casual, and witty Tamil tech brother. "
                "Always reply in 'Tanglish' (Tamil words written in English script) or simple friendly Tamil. "
                "Use friendly slang like 'Makka', 'Dei thambi', 'Super da', 'Sollu thambi'. "
                "Be smart, helpful, adaptive, and have a great sense of humor just like Gemini!"
                "CRITICAL RULE: If the user asks about your name (e.g., 'your name', 'peru enna', 'பெயர் என்ன', 'who are you'), you must always reply that your name is 'Prabhu ' (e.g., 'I am Prabhu ' or 'En peru Prabhu '). "
            )

            # 3. Gemini மாடலை கூப்பிடுறோம்
            response = client.models.generate_content(
                model='gemini-2.5-flash', # லேட்டஸ்ட் அண்ட் ஃபாஸ்ட் மாடல்
                contents=user_message,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7, # கொஞ்சம் ஜாலியா பேச வைக்கிறதுக்கு
                ),
            )
            
            bot_reply = response.text
        except Exception as e:
            # எர்ரர் என்னனு VS Code டெர்மினல்ல பிரிண்ட் பண்ணி பார்க்குறதுக்கு
            print("உண்மையான எர்ரர் இதோ தம்பி:", e)
            bot_reply = "மக்கா, சின்ன நெட்வொர்க் பிராப்ளம்னு நினைக்கிறேன். மறுபடியும் கேளுங்க!"

        return JsonResponse({'reply': bot_reply})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)