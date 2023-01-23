import math

#accuracy and purity is 100% for milestons 1,2,3,5,6

#my assumption for fourth milestone is that may be the two polygons combine together to form another polygon

#calculate the distances of polygon poi and sources
def distances(poi,source):
    lengths_poi = [] #distsnce in coordinates of poi is stored in list of list
    p = []
    for i in range(len(poi)):
        if poi[i] == 'boundary\n' and 'xy' in poi[i+3]:
            poi_xy = poi[i+3].split(" ")
            poi_xy = [ele for ele in poi_xy if ele.strip()]
            y = 0
            a1 = []
            while 2 + y < 2 * int(poi_xy[1]) - 1:
                u1 = (int(poi_xy[2 + y]) - int(poi_xy[4 + y])) * (int(poi_xy[2 + y]) - int(poi_xy[4 + y]))
                v1 = (int(poi_xy[3 + y]) - int(poi_xy[5 + y])) * (int(poi_xy[3 + y]) - int(poi_xy[5 + y]))
                a1 += [math.sqrt(u1 + v1)]
                y += 2
            a1.sort()
            lengths_poi.append(a1)

    for j in range(len(source)):
        a = []
        if source[j] == 'boundary\n' and 'xy' in source[j+3]:
            source_xy = source[j+3].split(" ")
            source_xy = [ele for ele in source_xy if ele.strip()]
            z = 0
            while 2+z < 2*int(source_xy[1])-1:
                u = (int(source_xy[2+z])-int(source_xy[4+z]))*(int(source_xy[2+z])-int(source_xy[4+z]))
                v = (int(source_xy[3+z])-int(source_xy[5+z]))*(int(source_xy[3+z])-int(source_xy[5+z]))
                a += [math.sqrt(u+v)]
                z += 2
            a.sort()
            #checking the ratio of the lengths are equal
            for t in range(len(lengths_poi)):
                if len(a) == len(lengths_poi[0]):
                    temp = lengths_poi[0][0]/a[0]
                    f = 1
                    for s in range(len(a)):
                        if lengths_poi[t][s]/a[s] == temp:
                            pass
                        else:
                            f = 0
                    if f == 1:
                        p.append(source[j]+source[j+1]+source[j+2]+source[j+3]+source[j+4])
    return p

#milestone1 - verifying the input file  and writing in the output file
def output_verification(k):
    output1 = open("output1.txt", "w")
    for i in range(len(k)):
         if k[i] == 'boundary\n':
             if 'layer' in k[i+1] and 'datatype' in k[i+2] and 'xy' in k[i+3] and 'endel' in k[i+4]:
                 output1.write(k[i])
                 output1.write(k[i+1])
                 output1.write(k[i+2])
                 output1.write(k[i+3])
                 output1.write(k[i+4])


if __name__ == '__main__':
    input1 = open("Format_Source.txt", "r")
    #milestone1
    k = input1.readlines()
    output_verification(k) #milestone1 output stored here

    #milestone2-milestone3-milestone4-milestone5
    input2 = open("POI.txt","r")
    input3 = open("Source.txt","r")
    poi = input2.readlines()
    source = input3.readlines()
    p = distances(poi, source)
    print(len(source))
    print(len(p))
    print(poi)
    #lengths_poi,lengths_source = distances(poi,source)
    #area(poi,source)
    #p = matching_pairs(lengths_poi,lengths_source)

    output2 = open("output2.txt", "w") #milestone 2,3,4,5,6,7 are stored here according to their respective inputs
    for i in range(len(p)):
        output2.write(p[i])











