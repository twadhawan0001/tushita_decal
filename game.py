from animations import animation_functions, animation_descriptions, obesity_animation, adipokine_animation, inflammation_animation, insulin_animation, ir_animation, hyperglycemia_animation, pancreas_animation, beta_animation, t2d_animation
stages = [
    {"hint": "First stage of metabolic disorder", "answer": "obesity"},
    {"hint": "Beneficial cytokines released by adipose tissue", "answer": "adipokine"},
    {"hint": "Immune system's response to increasing obesity and pro-inflammatory cytokines", "answer": "inflammation"},
    {"hint": "Hormone released to regulate increased blood glucose levels", "answer": "insulin"},
    {"hint": "Inability of tissues to respond to insulin", "answer": "insulin resistance"},
    {"hint": "Excessive amount of glucose in bloodstream", "answer": "hyperglycemia"},
    {"hint": "Organ that produces insulin", "answer": "pancreas"},
    {"hint": "Type of cells that produce insulin", "answer": "beta"},
    {"hint": "Most common metabolic disease in the US due to obesity", "answer": "type 2 diabetes"}
]

for stage_num, stage in enumerate(stages, start=1):
    print(f"\nStage {stage_num}:")
    print("Hint:", stage["hint"])
    print("Word:", " ".join(["_" for _ in stage["answer"]]))

    attempts = 3
    guessed = False

    while attempts > 0:
        guess = input(f"You have {attempts} attempts. Your guess: ").strip().lower()
        if guess == stage["answer"]:
            guessed = True
            break
        else:
            print("Incorrect! Try Again!")
            attempts -= 1
            
    if guessed:
        print(f"✅ Correct! The word was {stage['answer'].upper()}")
    else:
        print(f"❌ Out of attempts! The correct word was {stage['answer'].upper()}")
    
    answer = stage["answer"]
    # Print animation description
    print(animation_descriptions.get(answer, "\n🎬 Starting animation..."))
    # Run the corresponding animation
    animation_func = animation_functions.get(answer)
    if animation_func:
        animation_func()
    else:
        print("⚠️ No animation available for this stage.")
    