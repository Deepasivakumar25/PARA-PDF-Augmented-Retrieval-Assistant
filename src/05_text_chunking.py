chunk_size = 500
chunks = []

for i in range(0, len(pdf_text), chunk_size):
    chunks.append(pdf_text[i:i + chunk_size])

print(chunks)
print("Number of chunks:", len(chunks))
print(chunks[0])
