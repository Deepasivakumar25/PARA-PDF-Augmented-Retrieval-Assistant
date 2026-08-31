while True:
    question = input("\nAsk a question (exit to quit): ")

    if question.lower() == "exit":
        break

    # Convert question into embedding
    question_embedding = embedding_model.encode([question])

    # Search similar chunk
    distance, index_number = index.search(
        np.array(question_embedding),
        k=1
    )

    # Retrieve best chunk
    best_chunk = chunks[index_number[0][0]]
    print("Best chunk:", best_chunk)

    # Create prompt
    prompt = f"""
You are a helpful assistant.

Use ONLY the context below.

If the answer is not present, reply exactly:

I couldn't find that information.

Context:

{best_chunk}

Question:

{question}

Give ONLY the final answer.

Do NOT generate another question.
"""

    # Generate answer
    response = chatbot(
        prompt,
        max_new_tokens=20,
        do_sample=False,
        return_full_text=False
    )

    # Print answer
    print("\nBot:\n")
    print(response[0]["generated_text"])
    answer = response[0]["generated_text"]

    if "Question:" in answer:
        answer = answer.split("Question:")[0]

    print(answer.strip())
