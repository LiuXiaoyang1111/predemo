# import package
import streamlit as st

# set the title
st.title("海马体体积的初步计算")

# input the age first
st.write("🧓请在下方选择你目前的年龄")
col1, col2 = st.columns(2)
year, month = None, None
with col1:
    year_number = list(range(55, 70))
    for i in range(len(year_number)):
        year_number[i] = str(year_number[i])+"岁"
    year = st.selectbox("单位：年", year_number, index=None, placeholder="点击下拉选择")
with col2:
    month_number = list(range(12))
    for i in range(len(month_number)):
        month_number[i] = str(month_number[i])+"月"
    month = st.selectbox("单位：月", month_number, index=None, placeholder="点击下拉选择")

# input the gender and the education level
if year is not None and month is not None:
    st.write("你选择的年龄是"+year+month)
    gender = st.selectbox("请选择你的性别", ("男", "女"), index=None, placeholder="点击下拉选择")
    education = st.text_input("请选择你的受教育程度（8年至20年）", placeholder="例：11年")
    education_number = list(range(8, 21))
    for i in range(len(education_number)):
        education_number[i] = str(education_number[i])+"年"
    if education != "" and education not in education_number:
        st.write("你的输入不符合规范，请重新输入")

    #st.write("你的海马体体积是30")
