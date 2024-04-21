from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)

def get_gemini_response(question):
    key = os.environ.get('API_KEY')
    genai.configure(api_key=key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

@app.route('/', methods=['GET'])
def diet_plan():
    height = request.args.get('height')
    weight = request.args.get('weight')
    gender =  request.args.get('gender')
    prompt = f"""
    I'm {height} feet tall and weigh {weight} kilograms and Gender {gender}. Please calculate my Body Mass Index (BMI). Based on the results, I'd like a tailored diet plan to address my needs. Here's what I'm looking for:
    Goal: If my BMI is healthy, provide a balanced diet. If my BMI indicates I'm underweight, provide a weight gain diet. If I'm overweight, provide a weight loss diet.
    Nutritional Targets: Please specify the total protein, calories, and fiber in the diet plan.
    Indian Cuisine: I prefer Indian food options for both a vegetarian and non-vegetarian plan.
    Schedule: Outline a sample daily meal plan with suggestions for breakfast, lunch, and dinner.
    Drinkng water: no. of liters
    note: In the output nothing should be bold
    """
    response = get_gemini_response(prompt)
    
    return render_template('result.html', diet_plan=response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
