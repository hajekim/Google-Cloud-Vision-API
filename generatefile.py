from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
image = vision.types.Image()
# image.source.image_uri = 'gs://cloud-vision-codelab/otter_crossing.jpg'
image.source.image_uri = 'gs://oreobox/lastread.jpg'
resp = client.text_detection(image=image)
# A = print('\n'.join([d.description for d in resp.text_annotations]))

# print(resp.text_annotations)
# ocr.txt 라는 파일을 쓰기가 가능하도록 생성
f = open("dry-ocr.txt", 'w')
# 시작지점을 지정해줌
int = 0

# resp 를 for로 돌려서 d에 담아
for d in resp.text_annotations:
    # 제일 처음 디스크립션 내용만 출력하기 위해 int < 1 일 때만 출력한다
    if int < 1:
        # 추출된 텍스트가 디스크립션에 있기 때문에 디스크립션 부분만 출력
        # print(d.description)
        # 첫번째 디스크립션만 ocr.txt 에 기록해라
        f.write(d.description)
# 파일 기록 후 종료
f.close

# 파일 읽기 위해 로드함
f = open("dry-ocr.txt", "r")
# 파일의 Rows 값을 List로 하여 lineList에 저장
lineList = f.readlines()
# 파일 읽기 종료
f.close

# 리스트에서 마지막 값을 출력하기 위해 -1을 사용
# 리스트의 마지막은 마지막 Row
lastrow = lineList[-1]
wetstr = lastrow[0:10]

f = open("ocr.txt","w")
print(wetstr)
f.write(wetstr)
f.close