별까지의거리계산하기

##
#이프로그램은프록시마센토리까지빛이가는시간을계산한다. 
#
speed = 300000 .0 # 빛의속도
distance = 40000000000000.0 # 거리
secs = distance / speed # 걸리는시간, 단위는초
light_year= secs / (60.0*60.0*24.0*365.0) # 광년으로변환
print(light_year, "광년")

