# services/documentation.py

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from utils.config import GPT_API_KEY

async def organize_text(text: str) -> str:
    print(text)
    
    # تعریف پیام سیستم
    system_message = SystemMessagePromptTemplate.from_template("شما یک دستیار هوشمند هستید.")
    
    # تعریف پیام کاربر با جایگذاری متن
    human_message = HumanMessagePromptTemplate.from_template(
        "متن زیر را به صورت سازمان‌یافته و مستندات قابل فهم دسته‌بندی کن:\n\n{text}"
    )
    
    # ایجاد قالب پیام چت
    prompt = ChatPromptTemplate.from_messages([system_message, human_message])
    
    # تنظیمات مدل GPT-4 با استفاده از LangChain
    llm = ChatOpenAI(
        openai_api_key=GPT_API_KEY,
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        max_tokens=1000,
    )
    
    # قالب‌بندی پیام با جایگذاری متن ورودی
    messages = prompt.format_messages(text=text)
    
    # ارسال درخواست به مدل و دریافت پاسخ
    response = llm(messages)
    
    # استخراج متن سازمان‌یافته از پاسخ
    organized_text = response.generations[0][0].text.strip()
    
    return organized_text
