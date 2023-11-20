from flask import Flask, request, jsonify

from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

mname = "facebook/blenderbot-1B-distill"
model = BlenderbotForConditionalGeneration.from_pretrained(mname)
tokenizer = BlenderbotTokenizer.from_pretrained(mname)






app = Flask(__name__)

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
      user_input = request.json['user_input']
      inputs = tokenizer([user_input], return_tensors="pt")
      reply_ids = model.generate(**inputs)
      bot_response = tokenizer.batch_decode(reply_ids)
      response =  bot_response[0].strip('<s>')
      final_response = response.strip('</')
        # Call your chatbot function with user_input
      return jsonify({'response': final_response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)







