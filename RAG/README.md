## What Is RAG 
 
RAG stands for Retrieval Augmented Generation 

The goal of RAG is to take information and pass it to an LLM so it can generate
outputs based on the information.

* Retrieval - Find the relevant information given the query. eg: "what are the macronutrients and what they do?" ->
retrieves the passages of text related to the macronutrients from the nutrition book.

*  Augmented - We want to take the relevant information and augment out input (prompt) to an LLM with that relevant information.

*  Generation - Take the first two steps and pass them to an LLM for generative outputs.
 ### Why RAG:
 The main goal of RAG is to improve the generation of the LLMs
 1* Prevent hallucination - LLMs  are incredibly good at generating good looking text, however this text doest't mean that it's factual.
 RAG can help LLMs generate information based on relevant passages that are factual.
 2* Work with custom data - Many base LLMs are traned with internet-scaled data. This means they hav a fairly goog understandig of language in general.
 However, it also does a lot of their response can generic in nature. RAG helps to create specific responses based on the specific documents. (eg: your own companie customer support doc)
## What can RAG be used for?
* Customer support Q&A chat - Treat your existing customer support documents as a resource and when a customer asks a question, you could have a retrieval system, retrieve relevant documentation snippets and then have an LLM craft those snippets into an answer. Think of this as a "chatbot for your documentation".
  * Email chain analysis - Let's say you're a large insurance company and you have chains and chains of emails of customer claims. You could use a RAG pipeline to find relevant information from those emails and then use an LLM to process that information into structured data.
  * * Company internal documentation chat
    * Textbook Q&A - Let's say you're a nutrition student and you've got a 1200 page textbook read, you could build a RAG pipeline to go through the textbook and find relevant passages to the questions you have.
## Why local?
Privacy , speed , cost.
* Privacy - If you have private documentation, maybe you don't want to send that to an API. You want to setup an LLM and run it on your own hardware.
*  Speed - Whenever you use an API, you have to send some kind of data across the internet. This takes time. Running locally means we don't have to wait for transfers of data.
*  Cost - If you own your hardware, the cost is paid. It may have a large cost to begin with. But overtime, you don't have to keep paying API fees.
*   No vendor lockin - If you run your own software/hardware. If OpenAI/another large internet company shut down tomorrow, you can still run your business.
  


 

    
