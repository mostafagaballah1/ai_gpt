import json
import openai
import numpy as np



# add OpenAI key
openai.api_key = "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"

# add training data
training_data = [{
    "prompt": "Where is the billing ->",
    "completion": " You find the billing in the left-hand side menu.\n"
}, {
    "prompt": "How do I upgrade my account ->",
    "completion": "Visit you user settings in the left-hand side menu, then click 'upgrade account' button at the "
                  "top.\n "
},
    {
        "prompt": "What is BusNaa ->",
        "completion": " Its a Bus School tracking system.\n"},
    {
        "prompt": "BusNaa ->",
        "completion": " Its a Bus School tracking system.\n"},
    {
        "prompt": "BusNaa ->",
        "completion": " Its a Bus School tracking system.\n"}

]

# create training data file and check its format to be jsonl
file_name = "training_data_5_5_prepared_new.jsonl"
# with open(file_name, "w") as output_file:
#  for entry in training_data:
#   json.dump(entry, output_file)
#   output_file.write("\n")

# important
# get the training file and check if its training data is  correct or not:
# use the command: openai tools fine_tunes.prepare_data -f training_data.jsonl


# # upload the training file
# upload_response = openai.File.create(
#   file=open(file_name, "rb"),
#   purpose='fine-tune'
# )
# file_id = upload_response.id
# print(upload_response)


# #create fine tune model and get its response
# fine_tune_response = openai.FineTune.create(training_file="file-SV3xvFpmAD6m7YygMOWRrakG", model="davinci")
# print("\n Fine Tune Model Response \n")
# print(fine_tune_response)


# ------------------------------------Now we will check the models status and access it-------------------------------

# #Check fine-tuning progress
# #Option 1: List events
# fine_tune_events = openai.FineTune.list_events("ft-U3hsb3aEPxkunsgJatkKkfTh")
# print("\n Fine Tune Events Response \n")
# print(fine_tune_events)

# # Option 2: Retrieve fine-tuning job
# retrieve_response = openai.FineTune.retrieve("ft-KXWuFeJfhFTDxPvRUKsj9zYd")
# print("\n Fine Tune Job Response \n")
# print(retrieve_response)

# #Get the Fine Tune Model
# retrieve_response = openai.FineTune.retrieve("ft-KXWuFeJfhFTDxPvRUKsj9zYd")
# fine_tuned_model = retrieve_response.fine_tuned_model
# print("\n Fine Tune Model  \n")
# print(fine_tuned_model)


# #Test the prompt
# new_prompt = "How to use BusNaa? ->"
# answer = openai.Completion.create(
#   model="curie:ft-personal-2023-05-04-21-21-19",
#   prompt=new_prompt,
#   max_tokens=100,
#   temperature=0
# )
# print(answer)

#Test Embidding
answer2 = openai.Embedding.create(
  model="text-embedding-ada-002",
  input="The food was delicious and the waiter...",
  max_tokens=100,
  temperature=0
)
print(answer2)

# print(answer['choices'][0]['text'])


# #Get all Fine Tune models
# print(openai.FineTune.list())

# #Get all Uploaded files
# print(openai.File.list())

# #Delete Model
# openai.Model.delete("davinci:ft-personal-2023-04-24-18-50-44")
