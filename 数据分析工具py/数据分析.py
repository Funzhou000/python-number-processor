figure_list=[]
while True:
    
     figure=input("请输入数字：")
     if figure =="quit":
          break
     elif figure=="analyze":
          print("analyzing")
          for num in figure_list:
                        # --- 把这段代码放入 for 循环 ---

            # 1. 创建 odd_even_status 变量
            odd_even_status = "偶数" if num % 2 == 0 else "奇数"

            # 2. 创建 sign_status 变量
            sign_status = "正数" if num > 0 else "负数" if num < 0 else "零"

            # 3. 组合成最终的打印语句
            print(f"数字 {num}: 是{odd_even_status}, 是{sign_status}")

            # --- 结束 ---          
     else:     
         try:
             figure_int=int(figure)
             figure_list.append(figure_int)
         except ValueError:
           print(f"'{figure}' 不是一个有效的整数。")
    
          
          