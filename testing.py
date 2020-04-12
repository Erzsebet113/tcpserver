import logging


resultData = "0002 C1 01:13:02.877 00"

wrappedData = resultData.split(' ')

print(wrappedData)

showData = f"Спортсмен нагрудный номер {wrappedData[0]} прошел отсечку {wrappedData[1]} во время {wrappedData[2]}"

print(showData)

if wrappedData[3] == "00":
    wrappedShowData = f"Спортсмен нагрудный номер {wrappedData[0]} прошел отсечку {wrappedData[1]} во время {wrappedData[2][:-2]}"
    print(wrappedShowData)


logging.basicConfig(filename="data.log", level=logging.INFO)

logging.info(showData)