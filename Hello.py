# import package
import streamlit as st
import numpy as np

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
    education = st.text_input("请选择你的受教育程度（8年至20年）", placeholder="例：11")
    if education.isdigit():
        education = float(education)
        if education < 8 or education > 20:
            st.write("你的输入应位于[8,20]，请重新输入")
    elif education.isdigit() == False:
        st.write("你的输入不符合规范，请重新输入")
    diagnosis = st.selectbox("请选择你的诊断结果", ("NL","MCI","DEMEMTIA"), index=None, placeholder="点击下拉选择")
    apgen = st.selectbox("请选择你的apgen", ("2","3","4","5","6"), index=None, placeholder="点击下拉选择")
    CDORIENT = st.selectbox("请选择你的CDORIENT", ("0","0.5","1","2"), index=None, placeholder="点击下拉选择")
    GDMEMORY = st.selectbox("请选择你的GDMEMORY", ("0","1"), index=None, placeholder="点击下拉选择")
    GDTOTAL = st.selectbox("请选择你的GDTOTAL", list(range(8)), index=None, placeholder="点击下拉选择")
    Q1SCORE_number_1 = [temp for temp in list(range(1,9)) for i in range(3)]
    Q1SCORE_number_2 = [0, 0.33, 0.67]*8
    Q1SCORE_number = np.array(Q1SCORE_number_1)+np.array(Q1SCORE_number_2)
    Q1SCORE = st.selectbox("请选择你的Q1SCORE", Q1SCORE_number[:-2], index=None, placeholder="点击下拉选择")
    Q4SCORE = st.selectbox("请选择你的Q4SCORE", list(np.arange(0,11,1)), index=None, placeholder="点击下拉选择")
    Q8SCORE = st.selectbox("请选择你的Q8SCORE", list(np.arange(0,11,1)), index=None, placeholder="点击下拉选择")
    VISSPAT4 = st.selectbox("请选择你的VISSPAT4", ("1","2","3","4","9"), index=None, placeholder="点击下拉选择")
    LANG2 = st.selectbox("请选择你的LANG2", ("1","2","3","4","9"), index=None, placeholder="点击下拉选择")


