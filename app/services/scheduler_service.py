import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.services.report_generator import generate_report
import uuid

scheduler = BackgroundScheduler()
scheduler.start()

def scheduled_report_job():
    input_file = os.path.join("uploads", "input.csv")
    reference_file = os.path.join("uploads", "reference.csv")
    if os.path.exists(input_file) and os.path.exists(reference_file):
        try:
            generate_report()
            print("Scheduled report generation succeeded.")
        except Exception as e:
            print(f"Scheduled report generation failed: {str(e)}")
    else:
        print("Scheduled job: Input or reference file missing.")



def add_schedule(cron_expr: str):
    try:
        trigger = CronTrigger.from_crontab(cron_expr)
    except Exception as e:
        raise ValueError(f"Invalid cron expression: {str(e)}")
    job_id = str(uuid.uuid4())
    job = scheduler.add_job(scheduled_report_job, trigger=trigger, id=job_id, replace_existing=True)
    return job

def list_schedules():
    jobs = scheduler.get_jobs()
    return [{"job_id": job.id, "next_run_time": str(job.next_run_time), "trigger": str(job.trigger)} for job in jobs]

def delete_schedule(job_id: str):
    scheduler.remove_job(job_id)
