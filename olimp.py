def chek_winners(scores, student_scores):
    scores_sorted = sorted(scores, reverse=True)
    winner = scores_sorted[:3]
    if student_scores in winner:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")

scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]
student_scores = int(input())
chek_winners(scores, student_scores)