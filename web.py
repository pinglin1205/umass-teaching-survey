from flask import Flask, render_template,jsonify,url_for,request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/")
def first_web():
    return render_template('home.html')
  
# @app.route("/api/jobs")
# def list_jobs():
#   return jsonify(JOBS)
@app.route("/thank-you")
def thank_you():
    return render_template('thank-you.html')

@app.route("/word_count_result", methods=["POST"])
def word_count_result():
      input_text = request.form.get("input_text")

      # Count the words (assuming words are separated by spaces)
      word_count = len(input_text.split())

      return render_template('word_count_result.html', word_count=word_count)

@app.route("/ask-chatgpt", methods=["POST"])
def ask_chatgpt():
    user_input = request.form.get("user_input")

    try:
        # Make an API call to OpenAI
        response = openai.Completion.create(
            engine="davinci",  # Choose the GPT-3 engine
            prompt=user_input,
            max_tokens=100,  # Adjust the response length as needed
        )

        # Check if the API call was successful
        if response.choices and response.choices[0].text:
            chatgpt_response = response.choices[0].text
        else:
            chatgpt_response = "No response from the GPT-3 API."

    except Exception as e:
        # Handle API call errors
        chatgpt_response = "Error: " + str(e)

    return render_template('chatgpt_response.html', chatgpt_response=chatgpt_response)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)