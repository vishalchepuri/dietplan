from flask import Flask, jsonify
import google.generativeai as genai # Your generative AI import
import os   

key = os.environ.get('API_KEY')


genai.configure(api_key=key)

app = Flask(__name__)

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

@app.route('/dietplan/<height>/<weight>')
def get_diet_plan(height, weight):
    prompt = f"""
    I'm {height} feet tall and weigh {weight} kilograms. Please calculate my Body Mass Index (BMI). Based on the results, I'd like a tailored diet plan to address my needs. Here's what I'm looking for:
    Goal: If my BMI is healthy, provide a balanced diet. If my BMI indicates I'm underweight, provide a weight gain diet. If I'm overweight, provide a weight loss diet.
    Nutritional Targets: Please specify the total protein, calories, and fiber in the diet plan.
    Indian Cuisine: I prefer Indian food options for both a vegetarian and non-vegetarian plan.
    Schedule: Outline a sample daily meal plan with suggestions for breakfast, lunch, and dinner.
    Drinkng water: no. of liters
    """
    response = get_gemini_response(prompt)
    return jsonify({'diet_plan': response})

if __name__ == '__main__':
    app.run(debug=True) 