from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_ats_score(resume, job_desc):
    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job_desc, convert_to_tensor=True)

    score = util.pytorch_cos_sim(emb1, emb2)
    return round(float(score[0][0]) * 100, 2)