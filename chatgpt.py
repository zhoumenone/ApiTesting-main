# -*- coding: utf-8 -*-   

"""
@author: ZhouMen
@Time : 2023/4/23 16:14
"""
import openai  # Create the chatgpt model

model = openai.Completion.create(engine="text-davinci-002")

# Use the model to generate text

