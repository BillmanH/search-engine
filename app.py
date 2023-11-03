import wikipedia as w
import os
import openai
from flask import *
from flask import request, render_template

app=Flask(__name__,static_folder="ico", template_folder=os.getcwd())

class OpenAiCon():
    def __init__(self):
        self.params = {"api_key":os.getenv('OPENAI_KEY'),
          "api_base":"https://exodestaiopen.openai.azure.com/",
          "api_type":"azure",
          "api_version":"2022-12-01"}

        self.openai = openai
        self.max_tokens = 100
        self.openai.api_key = self.params['api_key']
        self.openai.api_base =  self.params['api_base']
        self.openai.api_type = self.params['api_type']
        self.openai.api_version = self.params['api_version']
        self.deployment_name = 'exoplanetgpt'

    def request(self, prompt):
      self.response = self.openai.Completion.create(engine=self.deployment_name, 
                                    prompt=prompt, 
                                    max_tokens=self.max_tokens)
      textResponse = self.response.choices[0].text
      textResponse = textResponse.replace(". ",". \n")
      return textResponse

@app.route("/",methods=["POST","GET"])
def mn():
	if(request.method == "GET"):
		return render_template("index.html", info="")
	else:
		try:
			return render_template("index.html",info=w.summary(request.form["search"]))
		except:
			return render_template("index.html", info="Information not found")

if "__main__" == __name__:
	app.run()
