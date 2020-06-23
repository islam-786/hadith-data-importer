import json

# import fireo

mypath = './bukhari'

onlyfiles = []

for n in range(1, 98):
    onlyfiles.append(str(n) + ".json")

for single_file in onlyfiles:

    file_location = mypath + "/" + single_file
    f = open(file_location, "r", encoding="utf8")

    # trans_batch = fireo.batch()
    count = 0

    data = json.load(f)

    for i in data: 
        print(i)
        break

    f.close()

    break

    # for line in f:
    
    #     if not line.strip():
    #         print('file end')
    #         break

    #     count += 1
    #     if(count >= 400):
    #         trans_batch.commit()
    #         count = 0

    # print('============Complete=============================')
    # trans_batch.commit()