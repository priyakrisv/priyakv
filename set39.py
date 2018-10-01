SECONDS PER MINUTE=60
SECONDS PER HOUR=3600
SECONDS PER DAY=86400
seconds=int(input("enter number of seconds:"))
days=seconds / SECONDS PER DAY
seconds=seconds % SECONDS PER DAY
hours=seconds / SECONDS PER HOUR
seconds=seconds % SECONDS PER HOUR
minutes=seconds / SECONDS PER MINUTE 
seconds=seconds % SECONDS PER MINUTE
print("duration is:","%d:%02d:%02d:%02d%(days,hours,minutes,seconds)")

 
