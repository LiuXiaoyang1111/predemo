# 导入包
import streamlit as st
import matplotlib.pyplot as plt

# 历史病人数据
CA = [2322.69, 2150.578, 1671.45, 1396.486, 2587.49, 2697.97, 2779.24, 2037.37, 2451.48, 2166.75,
      1996.098, 2981.59, 2186.89, 2626.04, 1908.972, 2599.14, 2253.52, 2724.31, 2051.695, 2399.23, 1801.757,
      2705.69, 2608.04, 2575.68, 1640.32, 3736.13, 2482.0, 2417.91, 1952.821, 1535.645, 2810.23, 2569.77,
      1992.227, 2747.78, 2538.76, 2926.33, 2805.78, 2098.93, 2120.67, 2644.05, 2117.93, 1744.082, 1864.93,
      2206.12, 1733.939, 2700.5, 2330.41, 2379.15, 1864.013, 2009.279, 2069.09, 2318.11, 2939.76, 2004.399,
      2756.96, 2671.81, 1815.794, 2529.29, 2331.75, 2230.84, 1961.064, 2307.13, 2256.78, 2706.14, 2549.33,
      1986.389, 2446.29, 2934.87, 2270.51, 2654.11, 1954.952, 2763.06, 2647.71, 1449.586, 2580.87, 2097.17,
      2095.641, 2789.61, 2270.2, 2343.14, 1494.752, 1844.197, 2801.3, 2033.533, 2544.55, 2156.98, 2542.79,
      2687.07, 2431.03, 2579.05, 2629.7, 2781.98, 2813.72, 2106.01, 2380.77, 2018.131, 2674.56, 2700.21,
      2497.06, 3052.67, 2084.965, 2582.77, 1370.237, 2603.15, 2773.44, 1609.495, 2954.71, 3023.98, 2018.123,
      2850.04, 2131.36, 2409.36, 3429.87, 1169.544, 1728.519, 3176.58, 3335.88, 1676.023, 1278.685, 2585.75,
      2238.77, 2145.737, 2565.78, 1536.083, 2456.66, 1618.654, 2729.19, 1752.016, 2906.49, 2674.97, 1997.68,
      2038.27, 2697.14, 2682.49, 2790.22, 3014.84, 2737.73, 2782.28, 2134.1, 2128.9, 3250.42, 2639.47,
      2081.902, 1745.032, 1625.674, 3116.75, 2234.803, 2122.806, 2254.03, 2585.75, 2538.15, 2404.48, 3324.89,
      2518.92, 2414.55, 2048.04, 2297.37, 2701.16, 1635.742, 1744.077, 2800.29, 3075.12, 2268.85, 2573.55,
      2339.47, 2555.54, 2416.38, 2555.55, 1929.017, 1887.207, 2735.9, 2298.28, 3136.59, 2940.99, 3065.5,
      2475.28, 1606.141, 1962.729, 3114.01, 1804.195, 1549.375, 2131.337, 2825.63, 2971.79, 2244.87, 3222.2,
      1614.996, 2623.6, 2897.64, 2753.6, 1791.383, 2297.97, 2400.21, 2394.41, 1900.937, 1784.359, 1934.426,
      2087.71, 3003.84, 1465.759, 2255.87, 2829.36, 2339.37, 1851.197, 2087.709, 2612.62, 2006.805, 2578.13,
      2642.52, 2860.8, 1539.916, 2004.791, 1871.104, 2456.97, 3025.21, 2036.74, 2571.53, 2362.37, 1552.121,
      2819.83, 2241.517, 2860.72, 2372.44, 2644.35, 2486.57, 1788.319, 2307.13, 3099.97, 2439.66, 1739.196,
      3141.48, 2286.07, 2702.11, 2492.33, 2665.7, 2535.4, 2898.26, 2923.28, 2373.35, 2976.01, 2236.94,
      2294.92, 2586.98, 2808.22, 1850.897, 2349.86, 2317.2, 2714.85, 1972.657, 1800.231, 2448.28, 2769.17,
      2468.27, 2238.15, 2960.74, 2258.31, 1897.277, 1520.761, 1913.485, 2581.45, 2247.828, 2635.19, 2721.56,
      2411.81, 2241.22, 1038.512, 2627.26, 2743.83, 3229.69, 1665.646, 2044.07, 2643.13, 2770.39, 2735.6,
      2065.126, 2867.13, 2159.12, 2732.84, 2547.3, 2576.91, 2738.04, 2892.09, 2669.68, 2828.68, 1371.46,
      1850.887, 2250.67, 2026.969, 2701.72, 3009.52, 3296.51, 2703.55, 1678.772, 2203.375, 1246.947, 1145.324,
      2531.13, 2200.62, 2182.96, 2508.85, 2624.22, 2291.45, 2110.59, 2477.42, 2297.05, 2834.94, 2704.77,
      1863.097, 2547.49, 1674.5, 2710.27, 1897.583, 2119.138, 2037.054, 2197.73, 1664.734, 2140.5, 1831.672,
      2127.68, 1398.317, 2920.53, 2442.62, 3209.53, 2960.52, 2273.25, 1380.917, 2421.87, 2602.54, 2577.21,
      3264.77, 2138.98, 2123.716, 1454.775, 2178.12, 1819.762, 2855.83, 1806.335, 2546.99, 1621.092, 2731.02,
      3331.11, 1472.779, 1861.57, 2179.87, 2224.46, 2880.55, 2586.66, 1379.699, 2837.53, 1380.309, 2242.74,
      1965.941, 2415.47, 2150.573, 1402.281, 2285.77, 1731.268, 2622.07, 1063.842, 2501.52, 2410.89, 2761.23,
      1622.926, 2981.27, 2707.54, 1845.395, 2728.88, 2341.32, 1994.927, 1969.913, 2847.59, 3056.53, 595.092,
      2430.12, 2587.89, 2633.66, 2709.96, 1802.051, 2692.42, 1205.443, 2432.55, 2176.51, 2262.27, 1900.94,
      2417.93, 2247.63, 2747.18, 2070.0, 2645.58, 2102.21, 1568.07, 1498.409, 2665.71, 2925.11, 2677.32,
      3061.64, 2769.78, 1698.0, 2604.98, 1647.644, 2554.02, 2689.82, 1930.543, 1335.144, 2661.44, 2113.34,
      2441.72, 2265.319, 1975.405, 3080.75, 2191.47, 2611.58, 2530.82, 3131.38, 2091.365, 3716.49, 2052.2,
      2008.976, 2891.84, 2485.63, 3121.95, 2718.08, 1111.755, 1481.016, 2893.37, 2250.37, 2762.15, 2644.96,
      2672.78, 3109.13, 2852.17, 2697.76, 2494.2, 2900.98, 1682.74, 2711.69, 2203.13, 1922.302, 2439.41,
      2879.95, 2305.73, 1985.775, 2480.42, 3045.35, 2897.11, 1395.572, 2605.73, 2578.62, 2832.95, 2633.97,
      2612.91, 2930.61, 2442.42, 1804.543, 3215.44, 2630.31, 3098.45, 2303.33, 2700.2, 2544.86, 1894.831,
      2299.19, 2987.75, 3054.2, 2665.71, 1790.557, 2331.85, 2191.92, 2542.12, 2654.42, 2705.07, 2630.49,
      2313.23, 2776.49, 2441.09, 3099.67, 3238.84, 2088.76, 2805.48, 2527.47, 2422.49, 3042.29, 1008.91,
      2807.62, 3021.85, 3015.39, 2710.85, 2855.23, 2875.68, 1877.582, 2692.86, 3027.79, 3085.63, 3708.81,
      2036.089, 2294.92, 2781.37, 2294.62, 3327.33, 2259.21, 2806.52, 2427.06, 2900.39, 2499.69, 2792.05,
      3208.31, 2495.73, 2892.15, 2300.72, 3146.67, 1764.691, 2833.25, 2555.84, 2915.04, 2111.82, 3016.36,
      2436.33, 3441.47, 2352.9, 2825.62, 2166.29, 2904.06, 2752.53, 3060.36, 2387.89, 3020.76, 2742.61,
      2914.13, 2930.91, 3189.4, 2324.08, 2520.45, 2609.25, 2590.94, 2880.26, 2424.62, 2749.02, 2022.094, 2586.68,
      1586.002, 1727.337, 2861.02, 2174.38, 2701.76, 2867.47, 1513.368, 3333.14, 2279.71, 2408.14,
      3248.02, 2499.37, 2427.92, 2516.93, 2715.5, 1892.594, 2673.03, 1320.496, 1898.497, 2519.96, 2860.72,
      2735.9, 2770.13, 2740.75, 2633.05, 2669.68, 2394.4, 2771.3, 2883.92, 2257.63, 3107.3, 2573.14,
      2661.74, 2558.01, 2799.08, 2977.91, 2308.97, 2612.3, 2428.89, 2132.91, 1608.275, 2383.11, 2446.97,
      2904.66, 2486.28, 1788.022, 2568.36, 2432.86, 2111.48, 3154.86, 2535.49, 2346.8, 2318.11, 3458.56,
      2406.01, 2395.01, 2468.26, 2696.53, 2583.92, 3244.63, 2976.08, 2430.11, 3026.2, 2529.91, 3341.98,
      2557.8, 2651.37, 3028.26, 2645.87, 2421.606, 3177.49, 2412.0, 2745.66, 2729.58, 2556.76, 3112.8,
      2683.41, 2509.46, 2997.14, 1897.888, 1891.584, 3552.24, 2460.03, 2821.21, 2850.04, 3058.13, 2828.67,
      1555.559, 3024.6, 2257.15, 2856.74, 3268.21, 2619.64, 2621.77, 2215.534, 2794.71, 2580.47, 2641.8,
      2545.17, 2837.22, 2791.85, 2503.66, 2244.77, 2506.11, 3225.41, 2752.988, 2850.61, 3126.77, 2851.26,
      3319.09, 2054.136, 3110.35, 3118.67, 2510.58, 2982.63, 2385.06, 3108.51, 2941.28, 2716.37, 3004.85,
      2966.61, 2855.7, 2889.71, 2758.79, 2599.31, 3221.59, 2624.82, 3386.54, 3386.83, 3160.39, 2901.07,
      2405.7, 2385.47, 2810.97, 2933.05, 2684.15, 3091.74, 2492.38, 3026.74, 2550.46, 2734.69, 2910.02,
      3343.81, 2438.05, 2940.3, 2567.44, 2296.14, 2585.14, 3126.84, 2708.74, 2595.82, 2874.45, 1859.436,
      2611.08, 2593.14, 3357.24, 3036.5, 2430.72, 2633.77, 2336.93, 1430.969, 2732.55, 2209.77, 2934.57,
      2085.88, 2386.06, 2819.29, 1805.421, 2378.13, 2728.58, 3037.11, 2755.13, 3146.5, 2564.39, 2085.796,
      2694.4, 1658.933, 2800.59, 2604.98, 2353.64, 1610.415, 2093.5, 2591.85, 2657.78, 2774.04, 2459.41,
      2431.03, 2906.5, 2004.162, 2857.05, 3329.17, 3129.33, 2454.83, 3039.29, 1897.586, 3164.06, 2823.49,
      2742.27, 2802.06, 2990.81, 2713.32, 2602.54, 2573.86, 2868.82, 1835.632, 2903.9, 3494.26, 2714.85,
      1167.603, 3694.78, 1552.418, 2539.06, 2580.88, 1629.638, 2304.37, 2031.182, 2262.57, 2242.44, 2757.26,
      2210.85, 3619.38, 2829.29, 2285.62, 2470.4, 2969.36, 3116.14, 1954.984, 2208.24, 2843.02, 2467.69,
      2912.21, 2342.53, 2872.92, 3006.47, 2725.8, 2258.3, 2631.84, 1949.877, 1872.307, 2222.6, 1932.377,
      2216.48, 1776.427, 1572.263, 2632.51, 2342.61, 2879.95, 2243.55, 2765.1, 3110.36, 2432.52, 800.782,
      2317.38, 2277.89, 2339.48, 3370.53, 2535.09, 2440.79, 2838.75, 1694.254, 2575.67, 1482.056, 2231.14,
      1614.629, 2440.3, 2508.95, 2199.56, 2243.84, 1990.931, 2230.22, 1672.738, 1498.72, 2306.21, 2775.88,
      2055.35, 2731.94, 2470.68, 2312.52, 2188.42, 2601.01, 2763.67, 2794.2, 1861.269, 1553.103, 3061.52,
      2659.66, 2300.11, 2737.96, 1833.496, 2607.42, 1860.346, 2524.1, 2355.35, 2746.28, 2480.47, 2411.5,
      2658.08, 2411.57, 2466.48, 2265.32, 2684.32, 2860.41, 1946.107, 2251.59, 2264.7, 2327.04, 2492.67,
      2141.42, 2634.58, 1833.493, 1780.725, 1456.297, 2834.62, 2701.11]

# 设定标题
st.title("海马体体积的估算")

# 设定第一标题
st.subheader("请在下方选择你更关心的患者特征🏥‍")
selection = st.radio("⏰提醒：根据统计学意见，我们更推荐您选择受教育程度以估算患者的海马体体积", ("年龄", "受教育程度"),
                     index=None)

if selection == "年龄":
    # 首先输入年龄
    st.subheader("请在下方选择患者目前的年龄🧑")
    col1, col2 = st.columns(2)
    year, month = None, None
    with col1:
        year_number = list(range(55, 88))
        for i in range(len(year_number)):
            year_number[i] = str(year_number[i]) + "岁"
        year = st.selectbox("单位：年", year_number, index=None, placeholder="点击下拉选择")
    with col2:
        month_number = list(range(12))
        for i in range(len(month_number)):
            month_number[i] = str(month_number[i]) + "月"
        month = st.selectbox("单位：月", month_number, index=None, placeholder="点击下拉选择")

    # 根据不同导年龄段，进入不同的选项栏
    if year is not None and month is not None:
        # 第一阶段：55年0月-69年1月
        if int(year[:-1]) in list(range(55, 69)) or (int(year[:-1]) == 69 and int(month[:-1]) <= 1):
            AGE = int(year[:-1]) + float(month[:-1]) / 12
            st.write("⚠️请注意：上方选择的患者年龄是" + year + month)
            st.subheader("请填写下方相关信息📃")
            GENDER = st.selectbox("1️⃣请选择性别", ("男", "女"), index=None, placeholder="点击下拉选择")
            if GENDER == "男":
                GENDER = 1
            else:
                GENDER = 2
            EDUCATION = st.text_input("2️⃣请输入受教育程度（8年至20年）", placeholder="例：11")
            if EDUCATION.isdigit():
                EDUCATION = float(EDUCATION)
                if EDUCATION < 8 or EDUCATION > 20:
                    st.write("输入范围应位于[8,20]，请重新输入")
            elif EDUCATION.isascii() and EDUCATION != "":
                items = EDUCATION.split(("."))
                if len(items) == 2 and items[0].isdigit() and items[1].isdigit():
                    EDUCATION = float(EDUCATION)
                elif len(items) != 2:
                    st.write("输入不符合规范，请重新输入")
            elif EDUCATION.isdigit() == False and EDUCATION != "":
                st.write("输入不符合规范，请重新输入")
            DIAGNOSIS = st.selectbox("3️⃣请选择诊断结果", ("NL", "MCI", "DEMEMTIA"), index=None,
                                     placeholder="点击下拉选择")
            if DIAGNOSIS == "NL":
                DIAGNOSIS = 1
            elif DIAGNOSIS == "MCI":
                DIAGNOSIS = 2
            else:
                DIAGNOSIS = 3
            APGEN = st.selectbox("4️⃣请选择APGEN", (2, 3, 4, 5, 6), index=None, placeholder="点击下拉选择")
            CDORIENT = st.selectbox("5️⃣请选择CDORIENT", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
            GDMEMORY = st.selectbox("6️⃣请选择GDMEMORY", (0, 1), index=None, placeholder="点击下拉选择")
            GDTOTAL = st.selectbox("7️⃣请选择GDTOTAL", list(range(8)), index=None, placeholder="点击下拉选择")
            Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                              6.33,
                              6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
            Q1SCORE = st.selectbox("8️⃣请选择Q1SCORE", Q1SCORE_number, index=None, placeholder="点击下拉选择")
            Q4SCORE = st.selectbox("9️⃣请选择Q4SCORE", list(range(11)), index=None,
                                   placeholder="点击下拉选择")
            Q8SCORE = st.selectbox("1️⃣0️⃣请选择Q8SCORE", list(range(13)), index=None,
                                   placeholder="点击下拉选择")
            Q11SCORE = st.selectbox("1️⃣1️⃣请选择Q11SCORE", list(range(4)), index=None, placeholder="点击下拉选择")
            Q13SCORE = st.selectbox("1️⃣2️⃣请选择Q13SCORE", list(range(6)), index=None, placeholder="点击下拉选择")
            VISSPAT4 = st.selectbox("1️⃣3️⃣请选择VISSPAT4", (1, 2, 3, 4, 9), index=None,
                                    placeholder="点击下拉选择")
            MEMORY3 = st.selectbox("1️⃣4️⃣请选择MEMORY3", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            LANG2 = st.selectbox("1️⃣5️⃣请选择LANG2", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
            DIVATT1 = st.selectbox("1️⃣6️⃣请选择DIVATT1", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            DIVATT4 = st.selectbox("1️⃣7️⃣请选择DIVATT4", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            if GENDER != None and EDUCATION != None and DIAGNOSIS != None and APGEN != None and CDORIENT != None and GDMEMORY != None and GDTOTAL != None and Q1SCORE != None and Q4SCORE != None and Q8SCORE != None and Q11SCORE != None and Q13SCORE != None and VISSPAT4 != None and MEMORY3 != None and LANG2 != None and DIVATT1 != None and DIVATT4 != None:
                st.subheader("结果输出🖨️")
                INTERCEPT_coef = 3724.457
                AGE_coef = -14.796

                if GENDER == 2:
                    GENDER_coef = -265.635
                else:
                    GENDER_coef = 0
                EDUCATION_coef = -7.330

                if DIAGNOSIS == 2:
                    DIAGNOSIS_coef = -171.177
                elif DIAGNOSIS == 3:
                    DIAGNOSIS_coef = 340.242
                else:
                    DIAGNOSIS_coef = 0

                if APGEN == 3:
                    APGEN_coef = 188.120
                else:
                    APGEN_coef = 0

                if CDORIENT == 1:
                    CDORIENT_coef = -534.272
                else:
                    CDORIENT_coef = 0

                if GDMEMORY == 1:
                    GDMEMORY_coef = -254.921
                else:
                    GDMEMORY_coef = 0

                if GDTOTAL == 4:
                    GDTOTAL_coef = 404.145
                elif GDTOTAL == 3:
                    GDTOTAL_coef = 323.347
                elif GDTOTAL == 2:
                    GDTOTAL_coef = 205.479
                elif GDTOTAL == 1:
                    GDTOTAL_coef = 108.149
                else:
                    GDTOTAL_coef = 0

                if Q1SCORE == 5.33:
                    Q1SCORE_coef = 444.663
                elif Q1SCORE == 5:
                    Q1SCORE_coef = 146.203
                elif Q1SCORE == 3.33:
                    Q1SCORE_coef = 297.443
                elif Q1SCORE == 2.33:
                    Q1SCORE_coef = 192.840
                elif Q1SCORE == 5.67:
                    Q1SCORE_coef = -377.258
                elif Q1SCORE == 1.67:
                    Q1SCORE_coef = 313.529
                else:
                    Q1SCORE_coef = 0

                if Q4SCORE == 9:
                    Q4SCORE_coef = -855.968
                elif Q4SCORE == 10:
                    Q4SCORE_coef = -887.173
                else:
                    Q4SCORE_coef = 0

                if Q8SCORE == 4:
                    Q8SCORE_coef = -90.860
                elif Q8SCORE == 1:
                    Q8SCORE_coef = 163.155
                else:
                    Q8SCORE_coef = 0

                if Q11SCORE == 1:
                    Q11SCORE_coef = -342.146
                else:
                    Q11SCORE_coef = 0

                if Q13SCORE == 3:
                    Q13SCORE_coef = 456.490
                else:
                    Q13SCORE_coef = 0

                if VISSPAT4 == 2:
                    VISSPAT4_coef = 120.407
                else:
                    VISSPAT4_coef = 0

                if MEMORY3 == 4:
                    MEMORY3_coef = 169.713
                else:
                    MEMORY3_coef = 0

                if LANG2 == 9:
                    LANG2_coef = -201.520
                elif LANG2 == 4:
                    LANG2_coef = -381.351
                else:
                    LANG2_coef = 0

                if DIVATT1 == 4:
                    DIVATT1_coef = 98.634
                elif DIVATT1 == 2:
                    DIVATT1_coef = -121.042
                else:
                    DIVATT1_coef = 0

                if DIVATT4 == 9:
                    DIVATT4_coef = 405.506
                elif DIVATT4 == 2:
                    DIVATT4_coef = 200.565
                else:
                    DIVATT4_coef = 0

                y = INTERCEPT_coef + AGE_coef * AGE + GENDER_coef * GENDER + EDUCATION_coef * EDUCATION + DIAGNOSIS_coef * DIAGNOSIS + APGEN_coef * APGEN + CDORIENT_coef * CDORIENT + GDMEMORY_coef * GDMEMORY + GDTOTAL_coef * GDTOTAL + Q1SCORE_coef * Q1SCORE + Q4SCORE_coef * Q4SCORE + Q8SCORE_coef * Q8SCORE + Q11SCORE_coef * Q11SCORE + Q13SCORE_coef * Q13SCORE + VISSPAT4_coef * VISSPAT4 + MEMORY3_coef * MEMORY3 + LANG2_coef * LANG2 + DIVATT1_coef * DIVATT1 + DIVATT4_coef * DIVATT4
                if y <= 0:
                    st.write("很抱歉，无法估算患者的海马体体积")
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("基于上方填写的信息，该患者的海马体体积是")
                    with col2:
                        st.subheader("🧠" + str(y)[0:9])
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("该患者在所有受试者中，海马体体积的分位数为")
                    with col2:
                        yy_number = sum(item <= y for item in CA)
                        yy = yy_number / len(CA) * 100
                        st.subheader("👍" + str(yy)[:5] + "%")
                    fig = plt.figure()
                    plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                             label="Historical patient hippocampal volume")
                    plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                    plt.legend()
                    plt.savefig("result.jpg")
                    st.image("result.jpg")

        # 第二阶段：69年2月-76年1月
        if (int(year[:-1]) == 69 and int(month[:-1]) >= 2) or (int(year[:-1]) in list(range(70, 76))) or (
                int(year[:-1]) == 76 and int(month[:-1]) <= 1):
            AGE = int(year[:-1]) + float(month[:-1]) / 12
            st.write("⚠️请注意：上方选择的患者年龄是" + year + month)
            st.subheader("请填写下方相关信息📃")
            GENDER = st.selectbox("1️⃣请选择性别", ("男", "女"), index=None, placeholder="点击下拉选择")
            if GENDER == "男":
                GENDER = 1
            else:
                GENDER = 2
            EDUCATION = st.text_input("2️⃣请输入受教育程度（8年至20年）", placeholder="例：11")
            if EDUCATION.isdigit():
                EDUCATION = float(EDUCATION)
                if EDUCATION < 8 or EDUCATION > 20:
                    st.write("输入范围应位于[8,20]，请重新输入")
            elif EDUCATION.isascii() and EDUCATION != "":
                items = EDUCATION.split(("."))
                if len(items) == 2 and items[0].isdigit() and items[1].isdigit():
                    EDUCATION = float(EDUCATION)
                elif len(items) != 2:
                    st.write("输入不符合规范，请重新输入")
            elif EDUCATION.isdigit() == False and EDUCATION != "":
                st.write("输入不符合规范，请重新输入")
            M1 = st.text_input("3️⃣请输入M1（0.51-0.92）", placeholder="例：0.6333")
            if M1.isdigit():
                M1 = float(M1)
                if M1 < 0.51 or M1 > 0.92:
                    st.write("输入范围应位于[0.51,0.92]，请重新输入")
            elif M1.isascii() and M1 != "":
                items = M1.split(("."))
                if len(items) == 2 and items[0].isdigit() and items[1].isdigit():
                    M1 = float(M1)
                elif len(items) != 2:
                    st.write("输入不符合规范，请重新输入")
            elif M1.isdigit() == False and M1 != "":
                st.write("输入不符合规范，请重新输入")
            ORGAN3 = st.selectbox("4️⃣请选择ORGAN3", (1, 2, 3, 4, 9), index=None,
                                  placeholder="点击下拉选择")
            LANG9 = st.selectbox("5️⃣请选择LANG9", (1, 2, 3, 4, 9), index=None,
                                 placeholder="点击下拉选择")
            PHC_LAN = st.text_input("6️⃣请输入PHC_LAN（-1.16-2.59）", placeholder="例：2.33")
            try:
                PHC_LAN = float(PHC_LAN)
                if PHC_LAN < -1.16 or PHC_LAN > 2.59:
                    st.write("输入不在规定范围内，请重新输入！")
            except ValueError:
                if PHC_LAN != "":
                    st.write("输入不是一个数字，请重新输入！")
            VISSPAT1 = st.selectbox("7️⃣请选择VISSPAT1", (1, 2, 3, 4, 9), index=None,
                                    placeholder="点击下拉选择")
            VISSPAT7 = st.selectbox("8️⃣请选择VISSPAT7", (1, 2, 3, 9), index=None,
                                    placeholder="点击下拉选择")
            DIVATT4 = st.selectbox("9️⃣请选择DIVATT4", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            MEMORY7 = st.selectbox("1️⃣0️⃣请选择MEMORY7", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            MEMORY4 = st.selectbox("1️⃣1️⃣请选择MEMORY4", (1, 2, 3, 4), index=None,
                                   placeholder="点击下拉选择")
            ORGAN5 = st.selectbox("1️⃣2️⃣请选择ORGAN5", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")

            GDTOTAL = st.selectbox("1️⃣3️⃣请选择GDTOTAL", list(range(11)), index=None, placeholder="点击下拉选择")
            Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                              6.33, 6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
            Q1SCORE = st.selectbox("1️⃣4️⃣请选择Q1SCORE", Q1SCORE_number[:-2], index=None, placeholder="点击下拉选择")
            Q4SCORE = st.selectbox("1️⃣5️⃣请选择Q4SCORE", list(range(11)), index=None,
                                   placeholder="点击下拉选择")
            Q7SCORE = st.selectbox("1️⃣6️⃣请选择Q7SCORE", (0, 1, 2, 3, 4, 5, 7), index=None,
                                   placeholder="点击下拉选择")
            Q8SCORE = st.selectbox("1️⃣7️⃣请选择Q8SCORE", list(range(13)), index=None,
                                   placeholder="点击下拉选择")
            Q9SCORE = st.selectbox("1️⃣8️⃣请选择Q9SCORE", list(range(5)), index=None,
                                   placeholder="点击下拉选择")
            Q13SCORE = st.selectbox("1️⃣9️⃣请选择Q13SCORE", list(range(6)), index=None, placeholder="点击下拉选择")

            if GENDER != None and EDUCATION != None and M1 != None and ORGAN3 != None and LANG9 != None and PHC_LAN != None and VISSPAT1 != None and VISSPAT7 != None and DIVATT4 != None and MEMORY7 != None and MEMORY4 != None and ORGAN5 != None and GDTOTAL != None and Q1SCORE != None and Q4SCORE != None and Q7SCORE != None and Q8SCORE != None and Q9SCORE != None and Q13SCORE != None:
                st.subheader("结果输出🖨️")
                INTERCEPT_coef = 5890.306
                AGE_coef = -27.592

                if GENDER == 2:
                    GENDER_coef = -140.051
                else:
                    GENDER_coef = 0
                EDUCATION_coef = 15.568
                M1_coef = -1897.396

                if ORGAN3 == 2:
                    ORGAN3_coef = -140.426
                else:
                    ORGAN3_coef = 0

                if LANG9 == 9:
                    LANG9_coef = -1529.840
                else:
                    LANG9_coef = 0

                PHC_LAN_coef = 112.782

                if VISSPAT1 == 3:
                    VISSPAT1_coef = 385.341
                else:
                    VISSPAT1_coef = 0

                if VISSPAT7 == 2:
                    VISSPAT7_coef = -224.365
                else:
                    VISSPAT7_coef = 0

                if DIVATT4 == 9:
                    DIVATT4_coef = -562.555
                else:
                    DIVATT4_coef = 0

                if MEMORY7 == 4:
                    MEMORY7_coef = -361.477
                else:
                    MEMORY7_coef = 0

                if MEMORY4 == 3:
                    MEMORY4_coef = 158.445
                else:
                    MEMORY4_coef = 0

                if ORGAN5 == 2:
                    ORGAN5_coef = 90.572
                elif ORGAN5 == 3:
                    ORGAN5_coef = 125.491
                else:
                    ORGAN5_coef = 0

                if GDTOTAL == 1:
                    GDTOTAL_coef = -79.783
                elif GDTOTAL == 2:
                    GDTOTAL_coef = -140.542
                elif GDTOTAL == 3:
                    GDTOTAL_coef = -329.810
                elif GDTOTAL == 4:
                    GDTOTAL_coef = -414.621
                else:
                    GDTOTAL_coef = 0

                if Q1SCORE == 1:
                    Q1SCORE_coef = -91.354
                elif Q1SCORE == 4:
                    Q1SCORE_coef = -198.784
                elif Q1SCORE == 6:
                    Q1SCORE_coef = -399.927
                elif Q1SCORE == 5:
                    Q1SCORE_coef = -216.611
                elif Q1SCORE == 2.33:
                    Q1SCORE_coef = 325.379
                elif Q1SCORE == 0.67:
                    Q1SCORE_coef = 479.501
                else:
                    Q1SCORE_coef = 0

                if Q4SCORE == 8:
                    Q4SCORE_coef = -741.821
                elif Q4SCORE == 4:
                    Q4SCORE_coef = -108.199
                elif Q4SCORE == 9:
                    Q4SCORE_coef = -456.134
                else:
                    Q4SCORE_coef = 0

                if Q7SCORE == 1:
                    Q7SCORE_coef = -133.244
                elif Q7SCORE == 3:
                    Q7SCORE_coef = 560.618
                elif Q7SCORE == 4:
                    Q7SCORE_coef = 645.525
                else:
                    Q7SCORE_coef = 0

                if Q8SCORE == 6:
                    Q8SCORE_coef = -249.579
                elif Q8SCORE == 7:
                    Q8SCORE_coef = -301.252
                else:
                    Q8SCORE_coef = 0

                if Q9SCORE == 2:
                    Q9SCORE_coef = -1037.924
                else:
                    Q9SCORE_coef = 0

                if Q13SCORE == 2:
                    Q13SCORE_coef = -138.011
                elif Q13SCORE == 3:
                    Q13SCORE_coef = 523.437
                else:
                    Q13SCORE_coef = 0

                y = INTERCEPT_coef + AGE_coef * AGE + GENDER_coef * GENDER + EDUCATION_coef * EDUCATION + M1_coef * M1 + ORGAN3_coef * ORGAN3 + LANG9_coef * LANG9 + PHC_LAN_coef * PHC_LAN + VISSPAT1_coef * VISSPAT1 + VISSPAT7_coef * VISSPAT7 + DIVATT4_coef * DIVATT4 + MEMORY7_coef * MEMORY7 + MEMORY4_coef * MEMORY4 + ORGAN5_coef * ORGAN5 + GDTOTAL_coef * GDTOTAL + Q1SCORE_coef * Q1SCORE + Q4SCORE_coef * Q4SCORE + Q7SCORE_coef * Q7SCORE + Q8SCORE_coef * Q8SCORE + Q9SCORE_coef * Q9SCORE + Q13SCORE_coef * Q13SCORE
                if y <= 0:
                    st.write("很抱歉，无法估算患者的海马体体积")
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("基于你上方填写的信息，海马体体积是")
                    with col2:
                        st.subheader("🧠" + str(y)[0:9])
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("该患者在所有受试者中，海马体体积的分位数为")
                    with col2:
                        yy_number = sum(item <= y for item in CA)
                        yy = yy_number / len(CA) * 100
                        st.subheader("👍" + str(yy)[:5] + "%")
                    fig = plt.figure()
                    plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                             label="Historical patient hippocampal volume")
                    plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                    plt.legend()
                    plt.savefig("result.jpg")
                    st.image("result.jpg")

        # 第三阶段：76年2月-87年11月
        if (int(year[:-1]) == 76 and int(month[:-1]) >= 2) or (int(year[:-1]) in list(range(77, 87))) or (
                int(year[:-1]) == 87 and int(month[:-1]) <= 11):
            AGE = int(year[:-1]) + float(month[:-1]) / 12
            st.write("⚠️请注意：上方选择的患者年龄是" + year + month)
            st.subheader("请填写下方相关信息📃")
            GENDER = st.selectbox("1️⃣请选择性别", ("男", "女"), index=None, placeholder="点击下拉选择")
            if GENDER == "男":
                GENDER = 1
            else:
                GENDER = 2
            Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                              6.33, 6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
            Q1SCORE = st.selectbox("2️⃣请选择Q1SCORE", Q1SCORE_number[:-2], index=None, placeholder="点击下拉选择")
            Q4SCORE = st.selectbox("3️⃣请选择Q4SCORE", list(range(11)), index=None,
                                   placeholder="点击下拉选择")
            Q6SCORE = st.selectbox("4️⃣请选择Q6SCORE", list(range(5)), index=None,
                                   placeholder="点击下拉选择")
            Q7SCORE = st.selectbox("5️⃣请选择Q7SCORE", (0, 1, 2, 3, 4, 5, 7), index=None,
                                   placeholder="点击下拉选择")
            Q8SCORE = st.selectbox("6️⃣请选择Q8SCORE", list(range(13)), index=None,
                                   placeholder="点击下拉选择")
            Q13SCORE = st.selectbox("7️⃣请选择Q13SCORE", list(range(6)), index=None, placeholder="点击下拉选择")
            MEMORY2 = st.selectbox("8️⃣请选择MEMORY2", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            MEMORY5 = st.selectbox("9️⃣请选择MEMORY5", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            MEMORY8 = st.selectbox("1️⃣0️⃣请选择MEMORY8", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            LANG8 = st.selectbox("1️⃣1️⃣请选择LANG8", (1, 2, 3, 4, 9), index=None,
                                 placeholder="点击下拉选择")
            LANG9 = st.selectbox("1️⃣2️⃣请选择LANG9", (1, 2, 3, 4, 9), index=None,
                                 placeholder="点击下拉选择")
            DIVATT4 = st.selectbox("1️⃣3️⃣请选择DIVATT4", (1, 2, 3, 4, 9), index=None,
                                   placeholder="点击下拉选择")
            CDORIENT = st.selectbox("1️⃣4️⃣请选择CDORIENT", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
            CDGLOBAL = st.selectbox("1️⃣5️⃣请选择CDGLOBAL", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
            PTNOTRT = st.selectbox("1️⃣6️⃣请选择PTNOTRT", (0, 1, 2), index=None, placeholder="点击下拉选择")
            APGEN = st.selectbox("1️⃣7️⃣请选择APGEN", (1, 2, 3, 4, 5, 6), index=None, placeholder="点击下拉选择")
            ORGAN5 = st.selectbox("1️⃣8️⃣请选择ORGAN5", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
            if GENDER != None and Q1SCORE != None and Q4SCORE != None and Q6SCORE != None and Q7SCORE != None and Q8SCORE != None and Q13SCORE != None and MEMORY2 != None and MEMORY5 != None and MEMORY8 != None and LANG8 != None and LANG9 != None and DIVATT4 != None and CDORIENT != None and CDGLOBAL != None and PTNOTRT != None and APGEN != None and ORGAN5 != None:
                st.subheader("结果输出🖨️")
                INTERCEPT_coef = 2454.09

                if GENDER == 2:
                    GENDER_coef = -91.92
                else:
                    GENDER_coef = 0

                if Q1SCORE == 2:
                    Q1SCORE_coef = -151.23
                elif Q1SCORE == 2.67:
                    Q1SCORE_coef = -182.13
                elif Q1SCORE == 3.33:
                    Q1SCORE_coef = 250.45
                elif Q1SCORE == 4.33:
                    Q1SCORE_coef = 340.65
                elif Q1SCORE == 5:
                    Q1SCORE_coef = -125.53
                elif Q1SCORE == 6:
                    Q1SCORE_coef = 366.63
                elif Q1SCORE == 6.33:
                    Q1SCORE_coef = -137.72
                elif Q1SCORE == 6.67:
                    Q1SCORE_coef = 679.17
                else:
                    Q1SCORE_coef = 0

                if Q4SCORE == 8:
                    Q4SCORE_coef = -245.57
                elif Q4SCORE == 10:
                    Q4SCORE_coef = -409.3
                else:
                    Q4SCORE_coef = 0

                if Q6SCORE == 1:
                    Q6SCORE_coef = 258.94
                else:
                    Q6SCORE_coef = 0

                if Q7SCORE == 1:
                    Q7SCORE_coef = -153.37
                elif Q7SCORE == 2:
                    Q7SCORE_coef = -309.04
                elif Q7SCORE == 3:
                    Q7SCORE_coef = -307.37
                elif Q7SCORE == 4:
                    Q7SCORE_coef = -655.46
                else:
                    Q7SCORE_coef = 0

                if Q8SCORE == 6:
                    Q8SCORE_coef = -232.05
                elif Q8SCORE == 7:
                    Q8SCORE_coef = 163.64
                elif Q8SCORE == 9:
                    Q8SCORE_coef = -420.74
                else:
                    Q8SCORE_coef = 0

                if Q13SCORE == 1:
                    Q13SCORE_coef = -104.78
                else:
                    Q13SCORE_coef = 0

                if MEMORY2 == 2:
                    MEMORY2_coef = 121.99
                else:
                    MEMORY2_coef = 0

                if MEMORY5 == 4:
                    MEMORY5_coef = -312.63
                else:
                    MEMORY5_coef = 0

                if MEMORY8 == 9:
                    MEMORY8_coef = 711.99
                else:
                    MEMORY8_coef = 0

                if LANG8 == 3:
                    LANG8_coef = 209.39
                else:
                    LANG8_coef = 0

                if LANG9 == 2:
                    LANG9_coef = -99.77
                else:
                    LANG9_coef = 0

                if DIVATT4 == 2:
                    DIVATT4_coef = -148.21
                elif DIVATT4 == 9:
                    DIVATT4_coef = 651.39
                else:
                    DIVATT4_coef = 0

                if CDORIENT == 0.5:
                    CDORIENT_coef = -224.69
                else:
                    CDORIENT_coef = 0

                if CDGLOBAL == 0.5:
                    CDGLOBAL_coef = -207.1
                else:
                    CDGLOBAL_coef = 0

                if PTNOTRT == 1:
                    PTNOTRT_coef = 197
                else:
                    PTNOTRT_coef = 0

                if APGEN == 5:
                    APGEN_coef = 311.77
                else:
                    APGEN_coef = 0

                if ORGAN5 == 9:
                    ORGAN5_coef = -681.23
                else:
                    ORGAN5_coef = 0
                y = INTERCEPT_coef + Q1SCORE_coef * Q1SCORE + Q4SCORE_coef * Q4SCORE + Q6SCORE_coef * Q6SCORE + Q7SCORE_coef * Q7SCORE + Q8SCORE_coef * Q8SCORE + Q13SCORE_coef * Q13SCORE + MEMORY2_coef * MEMORY2 + MEMORY5_coef * MEMORY5 + MEMORY8_coef * MEMORY8 + LANG8_coef * LANG8 + LANG9_coef * LANG9 + DIVATT4_coef * DIVATT4 + CDORIENT_coef * CDORIENT + CDGLOBAL_coef * CDGLOBAL + PTNOTRT_coef * PTNOTRT + APGEN_coef * APGEN + ORGAN5_coef * ORGAN5
                if y <= 0:
                    st.write("很抱歉，无法估算患者的海马体体积")
                else:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("基于你上方填写的信息，海马体体积是")
                    with col2:
                        st.subheader("🧠" + str(y)[0:9])
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("该患者在所有受试者中，海马体体积的分位数为")
                    with col2:
                        yy_number = sum(item <= y for item in CA)
                        yy = yy_number / len(CA) * 100
                        st.subheader("👍" + str(yy)[:5] + "%")
                    fig = plt.figure()
                    plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                             label="Historical patient hippocampal volume")
                    plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                    plt.legend()
                    plt.savefig("result.jpg")
                    st.image("result.jpg")
elif selection == "受教育程度":
    st.subheader("请在下方选择患者的受教育程度🧑")
    EDUCATION = st.selectbox("单位：年", list(range(8, 21)), index=None, placeholder="点击下拉选择")
    # 第一阶段：8-14
    if EDUCATION in list(range(8, 15)):
        year, month = None, None
        year_number = list(range(55, 88))
        for i in range(len(year_number)):
            year_number[i] = str(year_number[i]) + "岁"
        year = st.selectbox("1️⃣请选择年龄（单位：年）", year_number, index=None, placeholder="点击下拉选择")
        month_number = list(range(12))
        for i in range(len(month_number)):
            month_number[i] = str(month_number[i]) + "月"
        month = st.selectbox("2️⃣请选择年龄（单位：月）", month_number, index=None, placeholder="点击下拉选择")
        if year is not None and month is not None:
            AGE = int(year[:-1]) + float(month[:-1]) / 12
        GENDER = st.selectbox("3️⃣请选择性别", ("男", "女"), index=None, placeholder="点击下拉选择")
        if GENDER == "男":
            GENDER = 1
        else:
            GENDER = 2
        DIAGNOSIS = st.selectbox("4️⃣请选择诊断结果", ("NL", "MCI", "DEMEMTIA"), index=None,
                                 placeholder="点击下拉选择")
        if DIAGNOSIS == "NL":
            DIAGNOSIS = 1
        elif DIAGNOSIS == "MCI":
            DIAGNOSIS = 2
        else:
            DIAGNOSIS = 3
        DIVATT4 = st.selectbox("5️⃣请选择DIVATT4", (1, 2, 3, 4, 9), index=None,
                               placeholder="点击下拉选择")
        VISSPAT7 = st.selectbox("6️⃣请选择VISSPAT7", (1, 2, 3, 9), index=None,
                                placeholder="点击下拉选择")
        R2 = st.text_input("7️⃣请输入R2（0.49-0.95）", placeholder="例：0.6333")
        try:
            R2 = float(R2)
            if R2 < 0.49 or R2 > 0.95:
                st.write("输入不在规定范围内，请重新输入！")
        except ValueError:
            if R2 != "":
                st.write("输入不是一个数字，请重新输入！")
        GDAFRAID = st.selectbox("8️⃣请选择GDAFRAID", (0, 1), index=None,
                                placeholder="点击下拉选择")
        APGEN = st.selectbox("9️⃣请选择APGEN", (2, 3, 4, 5, 6), index=None, placeholder="点击下拉选择")
        LANG7 = st.selectbox("1️⃣0️⃣请选择LANG7", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
        PLAN1 = st.selectbox("1️⃣1️⃣请选择PLAN1", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
        PHC_LAN = st.text_input("1️⃣2️⃣请输入PHC_LAN（-1.16-2.59）", placeholder="例：2.33")
        try:
            PHC_LAN = float(PHC_LAN)
            if PHC_LAN < -1.16 or PHC_LAN > 2.59:
                st.write("输入不在规定范围内，请重新输入！")
        except ValueError:
            if PHC_LAN != "":
                st.write("输入不是一个数字，请重新输入！")
        MEMORY7 = st.selectbox("1️⃣3️⃣请选择MEMORY7", (1, 2, 3, 4, 9), index=None,
                               placeholder="点击下拉选择")
        CDORIENT = st.selectbox("1️⃣4️⃣请选择CDORIENT", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
        Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                          6.33,
                          6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
        Q1SCORE = st.selectbox("1️⃣5️⃣请选择Q1SCORE", Q1SCORE_number, index=None, placeholder="点击下拉选择")
        Q4SCORE = st.selectbox("1️⃣6️⃣请选择Q4SCORE", list(range(11)), index=None,
                               placeholder="点击下拉选择")
        Q5SCORE = st.selectbox("1️⃣7️⃣请选择Q5SCORE", list(range(5)), index=None,
                               placeholder="点击下拉选择")
        Q7SCORE = st.selectbox("1️⃣8️⃣请选择Q7SCORE", (0, 1, 2, 3, 4, 5, 7), index=None,
                               placeholder="点击下拉选择")
        Q8SCORE = st.selectbox("1️⃣9️⃣请选择Q8SCORE", list(range(13)), index=None,
                               placeholder="点击下拉选择")
        Q9SCORE = st.selectbox("2️⃣0️⃣请选择Q9SCORE", list(range(5)), index=None,
                               placeholder="点击下拉选择")
        if year != None and month != None and GENDER != None and DIAGNOSIS != None and EDUCATION != None and DIVATT4 != None and VISSPAT7 != None and R2 != None and GDAFRAID != None and APGEN != None and LANG7 != None and PLAN1 != None and PHC_LAN != None and MEMORY7 != None and CDORIENT != None and Q1SCORE != None and Q4SCORE != None and Q5SCORE != None and Q7SCORE != None and Q8SCORE != None and Q9SCORE != None:
            st.subheader("结果输出🖨️")
            INTERCEPT_coef = 4624.319
            if GENDER == 2:
                GENDER_coef = -203.933
            else:
                GENDER_coef = 0
            AGE_coef = -17.639
            if DIAGNOSIS == 2:
                DIAGNOSIS_coef = -117.487
            elif DIAGNOSIS == 3:
                DIAGNOSIS_coef = -309.998
            else:
                DIAGNOSIS_coef = 0
            EDUCATION_coef = 8.879
            if DIVATT4 == 2:
                DIVATT4_coef = -141.114
            else:
                DIVATT4_coef = 0
            if VISSPAT7 == 2:
                VISSPAT7_coef = -264.548
            else:
                VISSPAT7_coef = 0
            R2_coef = -1272.685
            if GDAFRAID == 1:
                GDAFRAID_coef = -316.06
            else:
                GDAFRAID_coef = 0
            if APGEN == 5:
                APGEN_coef = 486.223
            else:
                APGEN_coef = 0
            if LANG7 == 3:
                LANG7_coef = 226.457
            elif LANG7 == 2:
                LANG7_coef = 307.873
            else:
                LANG7_coef = 0
            if PLAN1 == 3:
                PLAN1_coef = -291.899
            else:
                PLAN1_coef = 0
            PHC_LAN_coef = 173.937
            if MEMORY7 == 9:
                MEMORY7_coef = 519.589
            elif MEMORY7 == 2:
                MEMORY7_coef = 193.282
            elif MEMORY7 == 3:
                MEMORY7_coef = 174.722
            else:
                MEMORY7_coef = 0
            if CDORIENT == 1:
                CDORIENT_coef = 515.536
            else:
                CDORIENT_coef = 0
            if Q1SCORE == 2.33:
                Q1SCORE_coef = 243.639
            elif Q1SCORE == 5:
                Q1SCORE_coef = 103.453
            elif Q1SCORE == 5.33:
                Q1SCORE_coef = 303.74
            elif Q1SCORE == 1.67:
                Q1SCORE_coef = 513.99
            elif Q1SCORE == 6:
                Q1SCORE_coef = -376.009
            elif Q1SCORE == 3.33:
                Q1SCORE_coef = 300.93
            elif Q1SCORE == 3.67:
                Q1SCORE_coef = 300.388
            elif Q1SCORE == 2.67:
                Q1SCORE_coef = 373.122
            else:
                Q1SCORE_coef = 0
            if Q4SCORE == 1:
                Q4SCORE_coef = 59.952
            elif Q4SCORE == 7:
                Q4SCORE_coef = -318.806
            elif Q4SCORE == 10:
                Q4SCORE_coef = -543.63
            elif Q4SCORE == 8:
                Q4SCORE_coef = 86.084
            else:
                Q4SCORE_coef = 0
            if Q5SCORE == 1:
                Q5SCORE_coef = 174.125
            else:
                Q5SCORE_coef = 0
            if Q7SCORE == 1:
                Q7SCORE_coef = -190.784
            else:
                Q7SCORE_coef = 0
            if Q8SCORE == 3:
                Q8SCORE_coef = -196.315
            elif Q8SCORE == 4:
                Q8SCORE_coef = 140.385
            elif Q8SCORE == 12:
                Q8SCORE_coef = -534.431
            else:
                Q8SCORE_coef = 0
            if Q9SCORE == 2:
                Q9SCORE_coef = -644.434
            elif Q9SCORE == 3:
                Q9SCORE_coef = -155.288
            else:
                Q9SCORE_coef = 0
            y = INTERCEPT_coef + GENDER_coef * GENDER + AGE_coef * AGE + DIAGNOSIS_coef * DIAGNOSIS + EDUCATION_coef * EDUCATION + DIVATT4_coef * DIVATT4 + VISSPAT7_coef * VISSPAT7 + R2_coef * R2 + GDAFRAID_coef * GDAFRAID + APGEN_coef * APGEN + LANG7_coef * LANG7 + PLAN1_coef * PLAN1 + PHC_LAN_coef * PHC_LAN + MEMORY7_coef * MEMORY7 + CDORIENT_coef * CDORIENT + Q1SCORE_coef * Q1SCORE + Q4SCORE_coef * Q4SCORE + Q5SCORE_coef * Q5SCORE + Q7SCORE_coef * Q7SCORE + Q8SCORE_coef * Q8SCORE + Q9SCORE_coef * Q9SCORE
            if y <= 0:
                st.write("很抱歉，无法估算患者的海马体体积")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("基于你上方填写的信息，海马体体积是")
                with col2:
                    st.subheader("🧠" + str(y)[0:9])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("该患者在所有受试者中，海马体体积的分位数为")
                with col2:
                    yy_number = sum(item <= y for item in CA)
                    yy = yy_number / len(CA) * 100
                    st.subheader("👍" + str(yy)[:5] + "%")
                fig = plt.figure()
                plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                         label="Historical patient hippocampal volume")
                plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                plt.legend()
                plt.savefig("result.jpg")
                st.image("result.jpg")
    # 第二阶段：15-18
    if EDUCATION in list(range(15, 19)):
        year, month = None, None
        year_number = list(range(55, 88))
        for i in range(len(year_number)):
            year_number[i] = str(year_number[i]) + "岁"
        year = st.selectbox("1️⃣请选择年龄（单位：年） ", year_number, index=None, placeholder="点击下拉选择")
        month_number = list(range(12))
        for i in range(len(month_number)):
            month_number[i] = str(month_number[i]) + "月"
        month = st.selectbox("2️⃣请选择年龄（单位：月） ", month_number, index=None, placeholder="点击下拉选择")
        if year is not None and month is not None:
            AGE = int(year[:-1]) + float(month[:-1]) / 12
        GENDER = st.selectbox("3️⃣请选择性别 ", ("男", "女"), index=None, placeholder="点击下拉选择")
        if GENDER == "男":
            GENDER = 1
        else:
            GENDER = 2
        DIAGNOSIS = st.selectbox("4️⃣请选择诊断结果 ", ("NL", "MCI", "DEMEMTIA"), index=None,
                                 placeholder="点击下拉选择")
        if DIAGNOSIS == "NL":
            DIAGNOSIS = 1
        elif DIAGNOSIS == "MCI":
            DIAGNOSIS = 2
        else:
            DIAGNOSIS = 3
        Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                          6.33,
                          6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
        Q1SCORE = st.selectbox("5️⃣请选择Q1SCORE", Q1SCORE_number, index=None, placeholder="点击下拉选择")
        Q4SCORE = st.selectbox("6️⃣请选择Q4SCORE", list(range(11)), index=None,
                               placeholder="点击下拉选择")
        Q5SCORE = st.selectbox("7️⃣请选择Q5SCORE", list(range(5)), index=None,
                               placeholder="点击下拉选择")
        Q8SCORE = st.selectbox("8️⃣请选择Q8SCORE", list(range(13)), index=None,
                               placeholder="点击下拉选择")
        Q11SCORE = st.selectbox("9️⃣请选择Q11SCORE", list(range(5)), index=None,
                                placeholder="点击下拉选择")
        MEMORY5 = st.selectbox("1️⃣0️⃣请选择MEMORY5", (1, 2, 3, 4, 9), index=None,
                               placeholder="点击下拉选择")
        MEMORY7 = st.selectbox("1️⃣1️⃣请选择MEMORY7", (1, 2, 3, 4, 9), index=None,
                               placeholder="点击下拉选择")
        LANG2 = st.selectbox("1️⃣2️⃣请选择LANG2", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
        ORGAN3 = st.selectbox("1️⃣3️⃣请选择ORGAN3", (1, 2, 3, 4, 9), index=None,
                              placeholder="点击下拉选择")
        ORGAN5 = st.selectbox("1️⃣4️⃣请选择ORGAN5", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
        VISSPAT4 = st.selectbox("1️⃣5️⃣请选择VISSPAT4", (1, 2, 3, 4, 9), index=None,
                                placeholder="点击下拉选择")
        CDORIENT = st.selectbox("1️⃣6️⃣请选择CDORIENT", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
        CDCOMMUN = st.selectbox("1️⃣7️⃣请选择CDCOMMUN", (0, 0.5, 1, 2), index=None, placeholder="点击下拉选择")
        APGEN = st.selectbox("1️⃣8️⃣请选择APGEN", (2, 3, 4, 5, 6), index=None, placeholder="点击下拉选择")
        if year != None and month != None and GENDER != None and DIAGNOSIS != None and EDUCATION != None and Q1SCORE != None and Q4SCORE != None and Q5SCORE != None and Q8SCORE != None and Q11SCORE != None and MEMORY5 != None and MEMORY7 != None and LANG2 != None and ORGAN3 != None and ORGAN5 != None and VISSPAT4 != None and CDORIENT != None and CDCOMMUN != None and APGEN != None:
            st.subheader("结果输出🖨️")
            INTERCEPT_coef = 3571.618
            if GENDER == 2:
                GENDER_coef = -218.726
            else:
                GENDER_coef = 0
            AGE_coef = -16.222
            if DIAGNOSIS == 2:
                DIAGNOSIS_coef = -118.516
            elif DIAGNOSIS == 3:
                DIAGNOSIS_coef = -268.48
            else:
                DIAGNOSIS_coef = 0
            EDUCATION_coef = 20.074

            if Q1SCORE == 1.67:
                Q1SCORE_coef = 157.284
            elif Q1SCORE == 2.33:
                Q1SCORE_coef = 197.636
            elif Q1SCORE == 3.33:
                Q1SCORE_coef = 156.023
            elif Q1SCORE == 4.33:
                Q1SCORE_coef = 204.77
            elif Q1SCORE == 4.67:
                Q1SCORE_coef = 138.082
            elif Q1SCORE == 5.33:
                Q1SCORE_coef = 191.321
            elif Q1SCORE == 6:
                Q1SCORE_coef = 148.539
            elif Q1SCORE == 6.67:
                Q1SCORE_coef = 251.822
            else:
                Q1SCORE_coef = 0
            if Q4SCORE == 3:
                Q4SCORE_coef = 105.22
            elif Q4SCORE == 8:
                Q4SCORE_coef = -334.119
            elif Q4SCORE == 10:
                Q4SCORE_coef = -434.924
            elif Q4SCORE == 9:
                Q4SCORE_coef = -421.857
            else:
                Q4SCORE_coef = 0
            if Q5SCORE == 1:
                Q5SCORE_coef = -178.953
            else:
                Q5SCORE_coef = 0
            if Q8SCORE == 1:
                Q8SCORE_coef = 118.477
            elif Q8SCORE == 5:
                Q8SCORE_coef = -181.078
            elif Q8SCORE == 6:
                Q8SCORE_coef = -217.239
            else:
                Q8SCORE_coef = 0
            if Q11SCORE == 2:
                Q11SCORE_coef = 297.016
            else:
                Q11SCORE_coef = 0
            if MEMORY5 == 2:
                MEMORY5_coef = -64.35
            elif MEMORY5 == 4:
                MEMORY5_coef = -194.441
            else:
                MEMORY5_coef = 0
            if MEMORY7 == 4:
                MEMORY7_coef = -392.296
            elif MEMORY7 == 9:
                MEMORY7_coef = -226.238
            else:
                MEMORY7_coef = 0
            if LANG2 == 9:
                LANG2_coef = -1111.622
            else:
                LANG2_coef = 0
            if ORGAN3 == 3:
                ORGAN3_coef = 255.704
            elif ORGAN3 == 4:
                ORGAN3_coef = 377.343
            else:
                ORGAN3_coef = 0
            if ORGAN5 == 3:
                ORGAN5_coef = -73.164
            elif ORGAN5 == 9:
                ORGAN5_coef = -611.061
            else:
                ORGAN5_coef = 0
            if VISSPAT4 == 4:
                VISSPAT4_coef = 359.837
            elif VISSPAT4 == 9:
                VISSPAT4_coef = -273.306
            else:
                VISSPAT4_coef = 0
            if CDORIENT == 0.5:
                CDORIENT_coef = -131.88
            else:
                CDORIENT_coef = 0
            if CDCOMMUN == 1:
                CDCOMMUN_coef = 492.133
            else:
                CDCOMMUN_coef = 0
            if APGEN == 4:
                APGEN_coef = -70.005
            else:
                APGEN_coef = 0
            y = INTERCEPT_coef + GENDER_coef * GENDER + AGE_coef * AGE + DIAGNOSIS_coef * DIAGNOSIS + EDUCATION_coef * EDUCATION + Q1SCORE_coef * Q1SCORE + Q4SCORE_coef * Q4SCORE + Q5SCORE_coef * Q5SCORE + Q8SCORE_coef * Q8SCORE + Q11SCORE_coef * Q11SCORE + MEMORY5_coef * MEMORY5 + MEMORY7_coef * MEMORY7 + LANG2_coef * LANG2 + ORGAN3_coef * ORGAN3 + ORGAN5_coef * ORGAN5 + VISSPAT4_coef * VISSPAT4 + CDORIENT_coef * CDORIENT + CDCOMMUN_coef * CDCOMMUN + APGEN_coef * APGEN
            if y <= 0:
                st.write("很抱歉，无法估算患者的海马体体积")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("基于你上方填写的信息，海马体体积是")
                with col2:
                    st.subheader("🧠" + str(y)[0:9])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("该患者在所有受试者中，海马体体积的分位数为")
                with col2:
                    yy_number = sum(item <= y for item in CA)
                    yy = yy_number / len(CA) * 100
                    st.subheader("👍" + str(yy)[:5] + "%")
                fig = plt.figure()
                plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                         label="Historical patient hippocampal volume")
                plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                plt.legend()
                plt.savefig("result.jpg")
                st.image("result.jpg")
    # 第三阶段：19-20
    if EDUCATION in list(range(19, 21)):
        year, month = None, None
        year_number = list(range(55, 88))
        for i in range(len(year_number)):
            year_number[i] = str(year_number[i]) + "岁"
        year = st.selectbox("1️⃣请选择年龄（单位：年）  ", year_number, index=None, placeholder="点击下拉选择")
        month_number = list(range(12))
        for i in range(len(month_number)):
            month_number[i] = str(month_number[i]) + "月"
        month = st.selectbox("2️⃣请选择年龄（单位：月）  ", month_number, index=None, placeholder="点击下拉选择")
        if year is not None and month is not None:
            AGE = int(year[:-1]) + float(month[:-1]) / 12
        GENDER = st.selectbox("3️⃣请选择性别  ", ("男", "女"), index=None, placeholder="点击下拉选择")
        if GENDER == "男":
            GENDER = 1
        else:
            GENDER = 2
        DIAGNOSIS = st.selectbox("4️⃣请选择诊断结果  ", ("NL", "MCI", "DEMEMTIA"), index=None,
                                 placeholder="点击下拉选择")
        if DIAGNOSIS == "NL":
            DIAGNOSIS = 1
        elif DIAGNOSIS == "MCI":
            DIAGNOSIS = 2
        else:
            DIAGNOSIS = 3
        APGEN = st.selectbox("5️⃣请选择APGEN", (2, 3, 4, 5, 6), index=None, placeholder="点击下拉选择")
        R2 = st.text_input("6️⃣请输入R2（0.49-0.95）", placeholder="例：0.6333")
        try:
            R2 = float(R2)
            if R2 < 0.49 or R2 > 0.95:
                st.write("输入不在规定范围内，请重新输入！")
        except ValueError:
            if R2 != "":
                st.write("输入不是一个数字，请重新输入！")
        Q1SCORE_number = [0, 0.67, 1, 1.33, 1.67, 2, 2.33, 2.67, 3, 3.33, 3.67, 4, 4.33, 4.67, 5, 5.33, 5.67, 6,
                          6.33,
                          6.67, 7, 7.33, 7.67, 8, 8.33, 8.67, 9]
        Q1SCORE = st.selectbox("7️⃣请选择Q1SCORE", Q1SCORE_number, index=None, placeholder="点击下拉选择")
        Q3SCORE = st.selectbox("8️⃣请选择Q3SCORE", list(range(4)), index=None,
                               placeholder="点击下拉选择")
        Q4SCORE = st.selectbox("9️⃣请选择Q4SCORE", list(range(11)), index=None,
                               placeholder="点击下拉选择")
        Q5SCORE = st.selectbox("1️⃣0️⃣请选择Q5SCORE", list(range(5)), index=None,
                               placeholder="点击下拉选择")
        Q8SCORE = st.selectbox("1️⃣1️⃣请选择Q8SCORE", list(range(13)), index=None,
                               placeholder="点击下拉选择")
        Q10SCORE = st.selectbox("1️⃣2️⃣请选择Q10SCORE", list(range(4)), index=None,
                                placeholder="点击下拉选择")
        Q13SCORE = st.selectbox("1️⃣3️⃣请选择Q10SCORE", list(range(6)), index=None,
                                placeholder="点击下拉选择")
        ORGAN5 = st.selectbox("1️⃣4️⃣请选择ORGAN5 ", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")
        VISSPAT4 = st.selectbox("1️⃣5️⃣请选择VISSPAT4 ", (1, 2, 3, 4, 9), index=None,
                                placeholder="点击下拉选择")
        GDMEMORY = st.selectbox("1️⃣6️⃣请选择GDMEMORY", (0, 1), index=None, placeholder="点击下拉选择")
        LANG8 = st.selectbox("1️⃣7️⃣请选择LANG8", (1, 2, 3, 4, 9), index=None,
                             placeholder="点击下拉选择")
        LANG2 = st.selectbox("1️⃣8️⃣请选择LANG2", (1, 2, 3, 4, 9), index=None, placeholder="点击下拉选择")

        if year != None and month != None and GENDER != None and DIAGNOSIS != None and EDUCATION != None and R2 != None and Q1SCORE != None and Q3SCORE != None and Q4SCORE != None and Q5SCORE != None and Q8SCORE != None and Q10SCORE != None and Q13SCORE != None and ORGAN5 != None and VISSPAT4 != None and GDMEMORY != None and LANG8 != None and LANG2 != None:
            st.subheader("结果输出🖨️")
            INTERCEPT_coef = 4461.738
            if GENDER == 2:
                GENDER_coef = -79.97
            else:
                GENDER_coef = 0
            AGE_coef = -9.021
            if DIAGNOSIS == 2:
                DIAGNOSIS_coef = -127.205
            elif DIAGNOSIS == 3:
                DIAGNOSIS_coef = 46.467
            else:
                DIAGNOSIS_coef = 0
            EDUCATION_coef = -17.714
            if APGEN == 4:
                APGEN_coef = 238.945
            elif APGEN == 3:
                APGEN_coef = 203.608
            else:
                APGEN_coef = 0
            if Q1SCORE == 3.33:
                Q1SCORE_coef = 296.185
            elif Q1SCORE == 1:
                Q1SCORE_coef = -265.127
            else:
                Q1SCORE_coef = 0
            if Q3SCORE == 1:
                Q3SCORE_coef = 213.029
            else:
                Q3SCORE_coef = 0
            if Q13SCORE == 1:
                Q13SCORE_coef = -123.9
            else:
                Q13SCORE_coef = 0
            R2_coef = -1137.56
            if Q4SCORE == 4:
                Q4SCORE_coef = -51.388
            elif Q4SCORE == 8:
                Q4SCORE_coef = 198.361
            else:
                Q4SCORE_coef = 0
            if Q5SCORE == 1:
                Q5SCORE_coef = 177.165
            else:
                Q5SCORE_coef = 0
            if Q10SCORE == 1:
                Q10SCORE_coef = -709.985
            else:
                Q10SCORE_coef = 0
            if Q8SCORE == 10:
                Q8SCORE_coef = -618.838
            elif Q8SCORE == 6:
                Q8SCORE_coef = -557.584
            elif Q8SCORE == 9:
                Q8SCORE_coef = -696.84
            elif Q8SCORE == 2:
                Q8SCORE_coef = -187.374
            else:
                Q8SCORE_coef = 0
            if VISSPAT4 == 9:
                VISSPAT4_coef = -1177.229
            else:
                VISSPAT4_coef = 0
            if ORGAN5 == 3:
                ORGAN5_coef = 412.667
            else:
                ORGAN5_coef = 0
            if GDMEMORY == 1:
                GDMEMORY_coef = -278.751
            else:
                GDMEMORY_coef = 0
            if LANG8 == 3:
                LANG8_coef = -358.648
            elif LANG8 == 2:
                LANG8_coef = -226.218
            else:
                LANG8_coef = 0
            if LANG2 == 3:
                LANG2_coef = 389.737
            elif LANG2 == 2:
                LANG2_coef = 187.897
            elif LANG2 == 4:
                LANG2_coef = -433.608
            else:
                LANG2_coef = 0
            y = INTERCEPT_coef + GENDER_coef * GENDER + AGE_coef * AGE + DIAGNOSIS_coef * DIAGNOSIS + EDUCATION_coef * EDUCATION + APGEN_coef * APGEN + Q1SCORE_coef * Q1SCORE + Q3SCORE_coef * Q3SCORE + Q13SCORE_coef * Q13SCORE + R2_coef * R2 + Q4SCORE_coef * Q4SCORE + Q5SCORE_coef * Q5SCORE + Q10SCORE_coef * Q10SCORE + Q8SCORE_coef * Q8SCORE + ORGAN5_coef * ORGAN5 + VISSPAT4_coef * VISSPAT4 + GDMEMORY_coef * GDMEMORY + LANG8_coef * LANG8 + LANG2_coef * LANG2
            if y <= 0:
                st.write("很抱歉，无法估算患者的海马体体积")
            else:
                col1, col2 = st.columns(2)
                with col1:
                    st.write("基于你上方填写的信息，海马体体积是")
                with col2:
                    st.subheader("🧠" + str(y)[0:9])
                col1, col2 = st.columns(2)
                with col1:
                    st.write("该患者在所有受试者中，海马体体积的分位数为")
                with col2:
                    yy_number = sum(item <= y for item in CA)
                    yy = yy_number / len(CA) * 100
                    st.subheader("👍" + str(yy)[:5] + "%")
                fig = plt.figure()
                plt.hist(CA, bins=100, density=1, histtype="step", cumulative=1, color="b",
                         label="Historical patient hippocampal volume")
                plt.axvline(y, c="r", label="Current patient's hippocampal volume", alpha=0.6)
                plt.legend()
                plt.savefig("result.jpg")
                st.image("result.jpg")
