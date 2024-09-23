# --------------------------------------------
# repository
# https://github.com/xtekky/gpt4free
# --------------------------------------------
from g4f.client import Client


def gpt_run(text:str) -> str:
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
    )

    return response.choices[0].message.content   



if __name__ == "__main__":
   text = "Что такое система Антилаг на машинах?"
   answer = gpt_run(text)
   print(type(answer))
   print(answer)
   
