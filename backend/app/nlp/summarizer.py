from transformers import pipeline


summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


def generate_summary(text: str):

    text = "summarize: " + text

    result = summarizer(
        text,
        max_length=60,
        min_length=15,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["summary_text"]