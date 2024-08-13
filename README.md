# Python Devloper
# Assignment:
API endpoint: https://devapi.beyondchats.com/api/get_message_with_sources

Above is a paginated GET API which returns an array of objects where each object contains a response text and a corresponding array of sources. 
source is a JSON array. Each object of the array consists of an id, context, and an optional link.

Your task is to develop a Python program that does the following:

      1.Fetch the data from the pages of the API above.
      2.Identify whether the response for each response-sources pair came from any of the sources
      3.List down the sources from which the response was formed. Returns an empty array if the response did not come from any source. The shortlisted sources will be called citations
      4.Return the citations for all objects coming from the API. 
      5. Extra points if you can present your solution through a user-friendly UI.


# Technologies to Use:
Feel free to use any tools or libraries in Python needed to accomplish this task. The use of LLMs, NLP, ML/AI is encouraged.
