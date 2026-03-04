from src.query import answer_question

def main():
    print("AoN RAG — Ready.")
    print("Ask a question (or type 'exit'):\n")

    while True:
        q = input("> ").strip()
        if q.lower() == "exit":
            print("Goodbye.")
            break
        if not q:
            continue

        response = answer_question(q)
        print("\n" + response + "\n")

if __name__ == "__main__":
    main()
