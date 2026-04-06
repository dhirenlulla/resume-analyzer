def resume_score_breakdown(ats, skills_count, experience):
    score = 0
    score += ats * 0.5
    score += min(skills_count * 5, 25)
    score += min(experience * 5, 25)
    return round(score, 2)