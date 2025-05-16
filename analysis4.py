import pandas as pd
import numpy as np

# وصف المشروع:
# هذا السكربت يقوم بتحميل وتحليل بيانات مرضى السكري من ملف CSV.
# يتم استكشاف البيانات مبدئيًا للتعرف على خصائصها، فحص وجود قيم مفقودة، 
# ثم حساب إحصائيات وصفية مثل المتوسط، الانحراف المعياري، والوسيط لكل عمود رقمي.
# كما يتم عرض توزيع حالات المرض (Outcome) والتحقق من وجود قيم صفرية في بعض الأعمدة المهمة.

# 1. تحميل البيانات من ملف CSV
people = pd.read_csv("diabetes.csv")

# 2. استكشاف مبدئي للبيانات
print(people.head())           # عرض أول 5 صفوف للاطلاع على شكل البيانات
print(people.info())           # معلومات عن الأعمدة وأنواع البيانات وعدد القيم غير الفارغة
print(people.describe())       # ملخص إحصائي للأعمدة الرقمية
print(people.isnull().sum())   # التحقق من وجود قيم مفقودة

# 3. توزيع حالات المرض
print(people["Outcome"].value_counts().sort_values(ascending=False))  # عدد المرضى المصابين وغير المصابين

# 4. حساب إحصائيات وصفية لكل عمود رقمي
for column in people.columns:
    print(f"the mean value for {column} is {round(people[column].mean())}")

for column in people.columns:
    print(f"the std for {column} is {round(people[column].std())}")

for column in people.columns:
    print(f"the median for {column} is {round(people[column].median())}")

# 5. عرض بيانات المرضى المصابين (Outcome=1) وغير المصابين (Outcome=0)
print(people.loc[people["Outcome"] == 1, :])
print(people.loc[people["Outcome"] == 0, :])

# 6. التحقق من وجود قيم صفرية في بعض الأعمدة المهمة
print((people["BMI"] == 0).any())            # هل يوجد قيم صفرية في عمود BMI؟
print((people["BloodPressure"] == 0).any())  # هل يوجد قيم صفرية في عمود BloodPressure؟
