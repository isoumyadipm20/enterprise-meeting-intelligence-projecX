import re


ACTION_PATTERNS = [
    r"assigned .*? to .*?",
    r".*? should .*?",
    r".*? must .*?",
    r".*? needs to .*?",
    r".*? expected to .*?"
]


def extract_action_items(text: str):

    sentences = re.split(r'[.!?]', text)

    action_items = []

    for sentence in sentences:

        sentence = sentence.strip()

        for pattern in ACTION_PATTERNS:

            if re.search(
                pattern,
                sentence,
                re.IGNORECASE
            ):

                action_items.append(sentence)

                break

    return action_items