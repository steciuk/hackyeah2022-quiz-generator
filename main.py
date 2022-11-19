from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


def main() -> None:
    text = "The conference brings together the most important cultural institutions of the Polish community abroad, including the Polish Library in Paris, the Polish Museum in Rapperswil, and similar establishments in London, Rome, Montreal and Buenos Aires. In the USA, it gathers associations such as the Polish Army Veterans' Association in America (SWAP), the Jozef Pilsudski Institute of America, the Kościuszko Foundation, the Polish Institute of Arts and Sciences of America, Archives, Library and Polish Museums in Orchard Lake and the Polish Museum in America based in Chicago. The aim of the conference is to strengthen cooperation between member institutions, exchange experiences, assist in collecting Polonica, conducting a joint information campaign and sharing the work of member institutions."
    tokenizer = AutoTokenizer.from_pretrained(
        "voidful/context-only-question-generator")
    model = AutoModelForSeq2SeqLM.from_pretrained(
        "voidful/context-only-question-generator")

    qa = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    result = qa(text)
    print(result)


if __name__ == "__main__":
    main()
