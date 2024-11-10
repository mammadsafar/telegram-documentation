from speechmatics.batch_client import BatchClient
import json
import os
import time
import logging
import json
import logging
import asyncio

def extract_transcription(data):
    print('entery')
    data = json.loads(data)
    print(type(data))

    transcription = ""
    for entry in data.get("results", []):
        entry_type = entry.get("type", "")
        if entry_type == "word":
            word = entry["alternatives"][0].get("content", "")
            transcription += word + " "
        elif entry_type == "punctuation":
            punctuation = entry["alternatives"][0].get("content", "")
            # حذف فاصله اضافی قبل از علائم نگارشی
            transcription = transcription.rstrip() + punctuation + " "

    return transcription.strip()

# تنظیمات لاگ‌گیری
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)
async def convert_speech_to_text(ogg_path):
    audio_path = ogg_path  # مسیر فایل صوتی

    # تنظیمات تبدیل گفتار به متن به صورت دیکشنری
    transcription_config = {
        "type": "transcription",
        "transcription_config": {
            "language": "fa",
            "diarization": "none",
        }
    }


    # بررسی وجود فایل صوتی
    if not os.path.isfile(audio_path):
        logging.error(f"Audio file not found at path: {audio_path}")
        raise FileNotFoundError(f"Audio file not found at path: {audio_path}")

    # کلید API شما
    api_key = "aiXpVpUovqOq3ZREMtE2crvjrrBrh8B9"

    try:
        with BatchClient(api_key) as client:
            jobs_list = client.list_jobs()
            if len(jobs_list)>=10:
                print('Deleting')
                job_ids= []
                for i in jobs_list:
                    if i['status'] == 'done':
                        job_ids.append(i['id'])
                if len(job_ids)>5:
                    counter = 0
                    for i in reversed(job_ids):
                        if counter<5:
                            print(i)
                            client.delete_job(i)
                            counter += 1
                        else:
                            break
                print('End of Deleting')

            # ارسال job و دریافت Job ID
            job_id = client.submit_job(
                audio=audio_path,
                transcription_config=transcription_config,
            )
            # job_id = 'ch6qg5tpch'
            logging.info(f"Job submitted successfully. Job ID: {job_id}")


            job_response = client.check_job_status(job_id)

            job_duration = job_response["job"]["duration"]
            # logging.info(f"Job Duration: {job_duration}")
            # print(job_duration)


            duration = job_duration
            if duration < 60:
                job_duration = 60
                duration = 20
            else:
                duration = int(duration / 5)
            timer = 0

            status = 'pending'
            logging.info(f"Sleep for {duration} Seconds.")

            flag = True
            while flag:
                print(timer)
                print(job_duration)
                if timer >= job_duration:                    
                    raise('error')
                jobs_list = client.list_jobs()
                print(jobs_list[0]["status"])
                if jobs_list[0]["status"] != 'done':
                    # برنامه یک دقیقه صبر میکند تا فایل آماده شود
                    time.sleep(duration)
                    timer += 20
                elif jobs_list[0]["status"] == 'done':
                    status = 'done'
                    flag = False


            transcript = client.get_job_result(f'{job_id}')
            text = extract_transcription(json.dumps(transcript, ensure_ascii=False, indent=2))
            # print(text)
            return text

    except Exception as e:
        if hasattr(e, 'response'):
            logging.error(f"HTTP Error: {e.response.status_code}")
            try:
                error_details = e.response.json()
                logging.error(f"Error Details: {json.dumps(error_details, indent=2, ensure_ascii=False)}")
            except json.JSONDecodeError:
                logging.error(f"Response Content: {e.response.text}")
        else:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # اجرای تابع async با استفاده از asyncio.run
    asyncio.run(convert_speech_to_text("./services/voice.ogg"))
