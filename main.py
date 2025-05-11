from fastapi import FastAPI

from app.db import engine
from app.models import user, education, experience, forget_password, job_application, job_post_tag, job_post, resume, saved_job, session, skill
# from app.routers

user.Base.metadata.create_all(bind=engine)
job_post.Base.metadata.create_all(bind=engine)
resume.Base.metadata.create_all(bind=engine)
job_application.Base.metadata.create_all(bind=engine)
saved_job.Base.metadata.create_all(bind=engine)
session.Base.metadata.create_all(bind=engine)
skill.Base.metadata.create_all(bind=engine)
experience.Base.metadata.create_all(bind=engine)
education.Base.metadata.create_all(bind=engine)
forget_password.Base.metadata.create_all(bind=engine)
job_post_tag.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "App is running"}
