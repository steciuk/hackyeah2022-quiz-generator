import torch
from transformers import (
    AutoModelForQuestionAnswering,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    pipeline,
)

from question_generator.questiongenerator import QuestionGenerator


def main() -> None:
    text = "In 1990, when the suspicions that the Soviet authorities also murdered prisoners from the camps in Starobelsk and Ostashkov were confirmed, the term began to denote a crime against Polish prisoners of war from three camps: in Kozelsk, Starobelsk and Ostaszków."

    ####

    q_tokenizer = AutoTokenizer.from_pretrained(
        "voidful/context-only-question-generator")
    q_model = AutoModelForSeq2SeqLM.from_pretrained(
        "voidful/context-only-question-generator")

    q_pipe = pipeline("text2text-generation",
                      model=q_model, tokenizer=q_tokenizer)
    q_result = q_pipe(text)

    ####

    # question_generator = QuestionGenerator(
    #     model_name_or_path='valhalla/t5-base-e2e-qg')
    # q_results = question_generator.generate(text)

    ####

    ####

    print(q_result)

    a_tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
    a_model = AutoModelForQuestionAnswering.from_pretrained(
        "deepset/roberta-base-squad2")

    a_pipe = pipeline("question-answering", model=a_model,
                      tokenizer=a_tokenizer)
    a_result = a_pipe(context=text, question=q_result[0]['generated_text'])
    print(a_result)


def generator():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    text = "In the middle of the third decade of April, the Polish forces in Upper Silesia were reorganised and split into three large tactical units: northern, eastern and southern. Their command staffs were also established. The largest and strongest Group “East”, commanded by Karol Grzesik, consisted of 9 regiments from Beuthen (Bytom), Gleiwitz (Gliwice), Katowice, Königshütte (Królewska Huta), Pleß (Pszczyna) and Hindenburg (Zabrze), made up of 34 battalions. It concentrated half the insurgent forces, and its headquarters were located in Bielschowitz (Bielszowice). Group “South”, commanded by Lt. Col. Bolesław Sikorsky consisted of 4 regiments from Rybnik, Ratibor (Racibórz), Loslau (Wodzisław) and Sohrau (Żory), made up of 12 battalions, with the headquarters in Loslau (Wodzisław). In turn, Group “North”, under the command of Capt. Alojzy Nowak, with its headquarters in Tworog (Tworóg), was made up of the forces from the Cosel (Koźle), Lublinitz (Lubliniec), Rosenberg (Olesno), Groß Strehlitz (Strzelce Opolskie) and Tarnowitz (Tarnowskie Góry) districts, numbering 16 batallions. In addition, in included a squadron of artillery and a squadron of cavalry. Thus, the operational groups consisted of 3 to 8 infantry regiments of 3–4 battalions and tactical groups in the strength of a regiment, consisting of 2–6 battalions, as well as rear and specialised units (sanitary columns, sappers, etc.). The operational groups were characterised by a high degree of independence and operated independently of each other. With time, they were reorganised. For example, the First Division of the Insurgent Army was formed from Group “East” and transformed into Group “Central” under the command of Capt. Maksymilian Żyła. Courts and field military police were attached to the operational groups. With the outbreak of the uprising, all these units were subordinated to the Civil High Command, led by Wojciech Korfanty, who proclaimed himself its dictator. He directed military operations with the help of the insurgent command with the Commander-in-Chief. Initially, until 31 May 1921, this function was performed by Lt. Col. Maciej “Nowina-Doliwa” Mielżyński from Greater Poland, and after his dismissal, from 3 June, by Kazimierz “Cietrzew” Zentkeller, also from Greater Poland. The insurgent troops numbered about 40,000, and during the course of the insurrection, as a result of an influx of volunteers, including from Poland, as well as compulsory conscription, they reached the number of 46,000 men by the end of May: 621 officers (including numerous Polish Army officers), 471 acting officers, 5,978 NCOs and 39,546 privates. The potential was thus half again greater than had been assumed in mid-March 1921. This speaks not only to the enormous mobilisation effort, but also to the organisational capabilities of the military conspiracy structures. The majority of the insurgents had not served in the recently ended world war. Many had no military experience until they joined the ranks of the insurgents. The average age of insurgents was about 23. Most of them were unmarried men with jobs in industry. They soon had to face experienced soldiers from German volunteer corps. A significant number of weapons used by the insurgents came from secret supplies organised by the Polish Army intelligence service and from the warehouses of the Association of Friends of Upper Silesia, located in borderland towns. The supply of weapons increased significantly in the third decade of May. The armament consisted of 26,474 rifles, 531 heavy machine guns and 136 light machine guns, 374 grenade launchers, 110 passenger cars and 52 transport cars, 60 motorcycles. Already during the operations, 50 cannons and armoured trains, of which there were 16 in total, including improvised ones, were smuggled from Poland. In addition, the insurgents had 3 armoured cars at their disposal. While the numbers did not look too bad, especially in comparison with previous uprisings, the diversity and provenance of armaments was a major problem. There were Austrian, Russian, German, French and British rifles, which caused technical problems. There was a shortage of parts and problems with obtaining suitable ammunition. Nevertheless, the insurgent army was a sizeable, well-organised and motivated force, which is evidenced by its successes, especially in the first stage of the uprising, and the accomplishment of its objective – the capture of the area up to the so-called Korfanty Line."

    generator = QuestionGenerator()
    result = generator.generate(
        article=text, answer_style="multiple_choice", num_questions=30)

    for obj in result:
        print(obj['question'])
        for answer in obj['answer']:
            ans = answer['answer']
            corr = answer['correct']
            print(f'{ans} - {corr}')

        print()


if __name__ == "__main__":
    generator()
