# 转换代码
def conver_code128b(inputData):
  checksum = 104
  for ii, char in enumerate(inputData):
   asciiStr = ord(char)
   if asciiStr >= 32:
    checksum += (asciiStr - 32) * (ii + 1)
   else:
    checksum += (asciiStr + 64) * (ii + 1)
  checksum = checksum % 103
  if checksum < 95:
   checksum += 32
  else:
   checksum += 100
  result = chr(204) + str(inputData) + chr(checksum) + chr(206)
  return result


# 源数据路径
source_dir = r'D:\data.txt'

# 转换后数据路径
new_dir = r'D:\new_data.txt'

with open(source_dir,'r')as file:
    all_lines = file.readlines()    # 读取数据
    all_lines = [line.strip() for line in all_lines]    # readlines() 读取文本后，会有换行符'\n'，影响条码生成，需要删除'\n'
    #print(all_lines)
    for num in range(len(all_lines)):   # 遍历读取到的数据
      conver = conver_code128b(all_lines[num])    # 转换
      conver = conver + '\n' # 刚刚删除了换行符，现在添加回去，不然保存文本时，不会自动换行
      new_file = open(new_dir,'a',encoding='utf-8-sig') # 打开要保持的文件，没有会自动生成
      new_file.write(conver) # 保存
      new_file.close() # 关闭
      #print(conver)

print('文件已保存在： ' +  new_dir)