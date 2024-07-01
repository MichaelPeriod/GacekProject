from django.shortcuts import render
import openai

#My API keys don't work since I don't have any tokens but this should otherwise work. Replace with yours to test
openai.api_key = "sk-####"
# openai.organization = "org-yLGw7p9b6HQYPUIQ8lxBAa5B"

messages = []
history = []

# Create your views here.
def chat(request):
  if request.method == 'POST':
    message = request.POST["inp"]
    history.append("You: " + message)
    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    
    #Tested by forcing reply to something static
    
    #Handle response
    history.append("GPT: " + reply)

  return render(request, 'gpt/chat.html', {'chat': history})